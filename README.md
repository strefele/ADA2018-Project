# Are you getting enough to eat?

## Abstract

*A 150 word description of the project idea, goals, dataset used. What story you would like to tell and why? What's the motivation behind your project?*

We all know that overeating is a big issue. However, with more and more people going on diets or becoming vegetarian, we decided to investigate whether these people are still getting the recommended dietary intake of key nutrients. We will use data from cooking recipes to get a realistic idea of what they are eating. As deficiencies appear, we will investigate what ingredients could be used to combat these cases. Finally, we will look into different types of cuisine to see if one is more conductive to eating vegetarian while remaining healthy.

## Research questions

*A list of research questions you would like to address during the project.*

* How can we use html data?
* How can we take advantage of the cluster to use larger datasets and to perform calculations?
* How can we efficiently sort through data to get the desired subset of information?
* Are there common nutient deficiencies in vegetarian diets?
* What (vegetarian) ingredients can help combat these deficiencies?
* Are certain types of cuisine better suited to a healthy vegetarian diet?

## Dataset

*List the dataset(s) you want to use, and some ideas on how do you expect to get, manage, process and enrich it/them. Show us you've read the docs and some examples, and you've a clear idea on what to expect. Discuss data size and format if relevant.*

We will use the dataset called recipePages on the cluster, and described as Cooking Recipes in the excel document. We will use the [perl scripts][from cookies to cooks] that already exist, created by Robert West, to extract from these html files lists of ingredients and nutrients per serving.

The first step in processing the data will be to remove all meat and fish dishes. We will create a document with a list of corresponding words to exclude. Care will have to be taken with cases such as chicken broth that can easily be replaced with vegetable broth.

Once we have a vegetarian dataset, we will examine key nutrient levels throughout the recipes, and compare these levels to the recommended dietary intake, taking care that we look consistently per serving. Recommended dietary intakes will be taken manually from the FDA website and kept in a separate document. If feasible (depending on the number of recipes concerned), we can look at recipes where a common deficiency is not present and try to identify the ingredient(s) responsible. We further plan on dividing the vegetarian recipes based on type of cuisine, and creating general nutrient profiles for each.

## A list of internal milestones up until project milestone 2

*Add here a sketch of your planning for the next project milestone.*

* Get ingredient and nutrient data from the html files
* Exclude meat and fish recipes from the data
* Examine distributions and modes of key nutrient amounts and compare with recommended dietary intake
* For consistently low nutrient levels, compare the recipes with higher levels of these nutrients to identify corresponding ingredients
* Common-sense determination if its feasible to include these more into the diet
* Create general nutrient profiles for different types of cuisine

## Questions for TAs

*Add here some questions you have for us, in general or project-specific.*

We are still very unsure of how the cluster is used in relation to the jupyter notebook where the code will be. If we understood correctly, calculations are performed on the cluster, but the results will need to be in the notebook; how do we make this link?

[from cookies to cooks]: http://infolab.stanford.edu/~west1/from-cookies-to-cooks/
