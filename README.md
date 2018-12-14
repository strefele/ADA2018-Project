
# Are vegetarian meals truly healthier?

## Abstract

We all know that overeating is a big issue. However, with more and more people going on diets or becoming vegetarian, we decided to investigate how this type of meal compares, in terms of nutrient profile, to meals containing meat, poultry, or fish. We will use data from cooking recipes to get a realistic idea of what is eaten. Macromolecule profiles will be compared to recommended values as percentages of total caloric intake. For other nutrients, we will look at how values compare across meal types. As differences appear, we will try to determine what sort of ingredients may be responsible.

## Research questions

* How can we scrape and use html data?
* How can we efficiently sort through data to get the desired subset of information?
* Are there common nutient deficiencies or overdoses across multiple meal types?
* How, in terms of nutrition, do vegetarian meals compare with those containing fish, meat, or poultry?


## Dataset

First we thought of using the dataset recipePages on the cluster, and described as Cooking Recipes in the excel document. However, we learned that the perl scripts created by Robert West do not extract all the nutritional information that we need. Therefore, we use web scraping to get the necessary data from allrecipes.com. Desserts are ignored since there are so many they would skew the nutrient profiles towards high fat and sugar content in vegetarian meal types. We noticed farther into data analysis that we were missing calories for each recipe. We decided for reasons of time contstraint that we would calculate the calories for each recipe rather than scraping everything again. With more time, we would scrape again, and add more cooking websites to our repertoire.

First is data collection. BeautifulSoup is be used to parse html data. The html code from allrecipes.com is examined to find the tags corresponding to the desired information, about both ingredients and nutrition. This information is then extracted into pandas dataframes. This method requires the URL for each recipe, and ParseHub is be used to obtain these with a semi-interactive interface.

The data must be processed to separate values such as a nutrient name and amount. Ingredients, nutrients, and general data about the recipes are put into separate datasets and are cleaned. We merge data collected from allrecipes.com under different tags to create a large general dataset for each of these categories. Handmade text documents containing words specific to fish, meat, and poultry respectively are created. These are used to create datasets specifically for different meal types.

Caloric content for each recipe is calculated, as well as the percentage to which each of the macromolecules (fat, carbohydrates, and protein) contribute. These percentages are compared with those recommended by the National Institute of Health, as well as between meal types. Histogram profiles for vitamins and minerals are also compared between meal types to identify differences. In this last case, we cannot compare with recommended values since they are given daily but the information we have is per serving.


## A list of internal milestones

* Scrape ingredient and nutrient data from allrecipes.com
* Create datasets for different meal types
* Compare macromolecules (as percentage of total calories) with recommended values as well as between meal types
* Examine histogram distributions and statistics of key nutrient amounts
* Identify ingredient types responsible for differences between the nutrient profiles


## Contributions of group members

**Jérémy Alexandre**
Data collection, calorie conversions, nutrient histograms, part of the report, planning the poster

**Abigail Strefeler**
Project idea and plan of implementation, data collection function, creating meal type datasets, calorie conversions, part of the report

**Léo Sumi**
Data cleaning, poster
