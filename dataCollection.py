import requests
from bs4 import BeautifulSoup
import time

import pandas as pd

# FUNCTION FOR WEB SCRAPING

import time
def get_recipe_data(url, nutrient_df, ingredient_df):
    """
    Scrape allrecipes.com for information on the nutrient content and ingredients of each recipe
    Based on the url, ingredients and nutrient content are extracted separately from the website.
    
    IN: url: URL of the specific recipe as a string
    OUT: nutrient and ingredient dataframes with the information for the given recipe
    """
    
    #nutrition information
    url_nutrition = url + 'fullrecipenutrition'
    
    r1 = requests.get(url_nutrition)
    time.sleep(1)
    soup1 = BeautifulSoup(r1.text, 'html.parser')
    
    #this is the div containing all the nutrition information
    nutrition_info = soup1.find_all('div', class_='nutrition-row')
    
    nutrient_list = []
    
    recipe = soup1.find('h2')
    if recipe is not None:
        recipe = recipe.text
        for n in nutrition_info:
            name = n.find(class_ = 'nutrient-name').text
            amount = n.find(class_ = 'nutrient-value').text
            name = name[:name.index(':')]
            nutrient_list.append({'nutrient': name, 'amount': amount, 'recipe': recipe, 'URL': url})

    nutrients = pd.DataFrame(nutrient_list)
    nutrient_df = nutrient_df.append(nutrients, sort=True)
    
    #ingredients
    r2 = requests.get(url)
    time.sleep(1)
    soup2 = BeautifulSoup(r2.text, 'html.parser')
    ingredient_info = soup2.find_all(class_='recipe-container-outer')
    
    ingredient_list = []
    for i in ingredient_info:
        ingredient = i.find_all('span', {'itemprop':'recipeIngredient'}, class_ = 'recipe-ingred_txt added')
        for x in ingredient:
            ingredient_list.append({'ingredient': x.text, 'URL':url})

    ingredients = pd.DataFrame(ingredient_list)
    ingredient_df = ingredient_df.append(ingredients, sort=True)
    
    return nutrient_df, ingredient_df

brunch_url_df = pd.read_csv('data/recipeLists/breakfast_brunch_url.csv')
#The last row is "Nan" so we decided to drop it
brunch_url_df = brunch_url_df.dropna()

brunch_url_df.columns = ["originGridUrl", "recipeName", "recipeURL"]
#pd.options.display.max_colwidth = 200
#display(dinner_url_df['recipeURL'].head())

#dinner_url_df['recipeURL'] = dinner_url_df['recipeURL'].split("?")[0]
brunch_url_df['recipeURL'] = brunch_url_df['recipeURL'].astype(str).apply(lambda x: x.split("?")[0])
#dinner_url_df['recipeURLPrime'] = str(dinner_url_df['recipeURL']).split("?")[0]
pd.set_option('display.max_rows', None,'display.max_columns', None)
#display(dinner_url_df.head())

brunchURLList = brunch_url_df.recipeURL.tolist()

nutrient_columns = ['URL', 'amount', 'nutrient', 'recipe']
ingredient_columns = ['URL', 'ingredient']
brunch_nutrient_df = pd.DataFrame(columns=nutrient_columns)
brunch_ingredient_df = pd.DataFrame(columns=ingredient_columns)

brunchURLList = brunchURLList[525:]
brunch_length=str(len(brunchURLList))
for url in range(len(brunchURLList)):
    brunch_nutrient_df, brunch_ingredient_df = get_recipe_data(brunchURLList[url], brunch_nutrient_df, brunch_ingredient_df)
    print(str(url+1) + "/" + brunch_length)

brunch_nutrient_df.to_csv("brunch_nutrient_525-.csv")
brunch_ingredient_df.to_csv("brunch_ingredient_525-.csv")
