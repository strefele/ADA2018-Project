
# Is a vegetarian diet truly healthier?

## Abstract

*A 150 word description of the project idea, goals, dataset used. What story you would like to tell and why? What's the motivation behind your project?*

We all know that overeating is a big issue. However, with more and more people going on diets or becoming vegetarian, we decided to investigate whether these people are still getting the recommended dietary intake of key nutrients. We will use data from cooking recipes to get a realistic idea of what they are eating. As deficiencies appear, compared to recommended intake, we will investigate what ingredients could be used to combat these cases. Finally, we will compare the nutrient deficiencies of vegetarian versus omnivorous diets to find common trends and identify large differences.

## Research questions

*A list of research questions you would like to address during the project.*

* How can we scrape and use html data?
* How can we efficiently sort through data to get the desired subset of information?
* Are there common nutient deficiencies in vegetarian diets?
* What (vegetarian) ingredients can help combat these deficiencies?
* How does a vegetarian diet compare with an omnivorous one, in terms of nutrition?

## Dataset

*List the dataset(s) you want to use, and some ideas on how do you expect to get, manage, process and enrich it/them. Show us you've read the docs and some examples, and you've a clear idea on what to expect. Discuss data size and format if relevant.*

First we thought of using the dataset recipePages on the cluster, and described as Cooking Recipes in the excel document. However, we learned that the perl scripts created by Robert West do not extract all the nutritional information that we need. Therefore, we will use web scraping to get the necessary data from allrecipes.com. If time permits, we will add more cooking websites to our repertoire, but since we are unfamiliar with web scraping we will start with just one.

First is data collection. BeautifulSoup will be used to parse html data. The html code from allrecipes.com will be examined to find the tags corresponding to the desired information, about both ingredients and nutrition. This information will then be extracted into pandas dataframes. This method requires the URL for each recipe, and ParseHub will be used to obtain these.

The data must be processed to separate values such as a nutrient name and amount. The next step in processing will be to remove all meat and fish dishes. We will create a document with a list of corresponding words to exclude. Care will have to be taken with cases such as chicken broth that can easily be replaced with vegetable broth.

Once we have a vegetarian dataset, we will examine key nutrient levels throughout the recipes, and compare these levels to the recommended dietary intake, taking care that we look consistently per serving and with the same units. Recommended dietary intakes will be taken manually from the FDA recommendations on dietary values and kept in a separate document. If feasible (depending on the number of recipes concerned), we can look at recipes where a common deficiency is not present and try to identify the ingredient(s) responsible.

Finally, we will compare the vegetarian dataset to the original one, supposed to be representative of an omnivorous diet. In this case we will see if there are trends of nutrient deficiencies common to both, or clear differences. Once again this comparison is based on the FDA recommended dietary values.

## A list of internal milestones up until project milestone 2

*Add here a sketch of your planning for the next project milestone.*

* Scrape ingredient and nutrient data from allrecipes.com
* Exclude meat and fish recipes from the data
* Examine histogram distributions and statistics of key nutrient amounts
* Compare nutrient quantities (mode or median) with recommended dietary intake
* For consistently low nutrient levels, compare the ingredients in recipes that have higher levels of these nutrients to identify what ingredient may be rescuing the deficiency
* Determine if its feasible to include these more into the diet (is increasing the quantity of the ingredient reasonable; we can check if high quantities are used)
* Compare vegetarian and omnivorous diets by looking at median/mode of nutrient quantities and histograms

## Questions for TAs

*Add here some questions you have for us, in general or project-specific.*

