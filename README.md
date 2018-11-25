
# Is a vegetarian diet truly healthier?

## Abstract

We all know that overeating is a big issue. However, with more and more people going on diets or becoming vegetarian, we decided to investigate whether these people are still getting the recommended dietary intake of key nutrients. We will use data from cooking recipes to get a realistic idea of what they are eating. As deficiencies appear, compared to recommended intake, we will investigate what ingredients could be used to combat these cases. Finally, we will compare the nutrient deficiencies of vegetarian versus omnivorous diets to find common trends and identify large differences.

## Research questions

* How can we scrape and use html data?
* How can we efficiently sort through data to get the desired subset of information?
* Are there common nutient deficiencies in vegetarian diets?
* What (vegetarian) ingredients can help combat these deficiencies?
* How does a vegetarian diet compare with an omnivorous one, in terms of nutrition?


## Dataset

First we thought of using the dataset recipePages on the cluster, and described as Cooking Recipes in the excel document. However, we learned that the perl scripts created by Robert West do not extract all the nutritional information that we need. Therefore, we use web scraping to get the necessary data from allrecipes.com. If time permits, we will add more cooking websites to our repertoire, but since we are unfamiliar with web scraping we will start with just one recipe website.

First is data collection. BeautifulSoup is be used to parse html data. The html code from allrecipes.com is be examined to find the tags corresponding to the desired information, about both ingredients and nutrition. This information is then extracted into pandas dataframes. This method requires the URL for each recipe, and ParseHub is be used to obtain these.

The data must be processed to separate values such as a nutrient name and amount. The next step in processing is to create a vegetarian dataste. We originally thought to remove all meat and fish dishes from dinner recipes. To do this, we created text documents containing words referring to meat and fish that were supposed to be excluded. However, we discovered that almost every recipe from the section "dinner" contains meat or fish. From the roughly 1000 recipes extracted, less than ten did not contain any meat or fish. Therefore we extracted recipes from the "vegetarian" category on the website. We plan on merging the vegetarian dataset with the more varied one, since most people eat a mix of vegetarian and meat dishes.

Once we have a vegetarian dataset, we examine key nutrient levels throughout the recipes, and compare these levels to the recommended dietary intake, taking care that we look consistently per serving and with the same units. Recommended dietary intakes is taken manually from the FDA recommendations on dietary values and kept in a separate document. If feasible (depending on the number of recipes concerned), we can look at recipes where a common deficiency is not present and try to identify the ingredient(s) responsible.

Finally, we will compare the vegetarian dataset to the original one, supposed to be representative of an omnivorous diet. In this case we will see if there are trends of nutrient deficiencies common to both, or clear differences. Once again this comparison is based on the FDA recommended dietary values.

More recipes will be scraped as we need for the comparison analysis.

## A list of internal milestones


* Scrape ingredient and nutrient data from allrecipes.com
* Create a vegetarian dataset
* Examine histogram distributions and statistics of key nutrient amounts
* Compare nutrient quantities (mode or median) with recommended dietary intake
* For consistently low nutrient levels, compare the ingredients in recipes that have higher levels of these nutrients to identify what ingredient may be rescuing the deficiency
* Determine if its feasible to include these more into the diet (is increasing the quantity of the ingredient reasonable? To do this we can check if high quantities are used)
* Compare vegetarian and omnivorous diets by looking at median/mode of nutrient quantities and by comparing histogram distributions

## Questions for TAs

*Add here some questions you have for us, in general or project-specific.*

