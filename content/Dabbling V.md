Title: CS109 lecture four
Date: 2014-05-31 13:42
Category: data science
Tags: harvard, python, cs109
Author: jacksongs
Summary: CS109 rolls into data munging and scraping.

*Never stop learning is a motto of mine. [Here](/dabbling-in-data-science.html) it's data science, and [Harvard's CS109 data science course](http://cs109.org/).*

**Summary:** This lecture was mostly basic html scraping, but then it got really awesome really quickly when Chris Beaumont started looking at data exploration.

The key takeaways were some of the data exploration methods, especially the small multiples code, which I will have to borrow (thanks Chris) from [here](http://www.google.com/url?q=http%3A%2F%2Fnbviewer.ipython.org%2Furls%2Fraw.github.com%2Fcs109%2Fcontent%2Fmaster%2Flec_04_wrangling.ipynb&sa=D&sntz=1&usg=AFQjCNFBcyzq-zO_dFqZPeWkoq1U-bNsMg).

![Awesome small multiples from Chris Beaumont](https://www.evernote.com/shard/s162/sh/a96b4116-ddca-418f-9458-f110ad2d1e5c/82c6f3f9f8640d759ef88dd54d3fead2/res/153c4182-4ec9-48c0-be27-97a7b1e9de54/skitch.png?resizeSmall&width=832)

Lecture four notes - [video link](http://cm.dce.harvard.edu/2014/01/14328/L04/index_H264SingleHighBandwidth-16x9.shtml)
=======================

Getting data from the web
-------------------------

Check out the resources page on the course site for lots of data sources.

Talking about web basics...

Scraping demo
-------------

Very basic scraping example...

Wrangling demo
--------------

Starts ~55:00

Data cleaning patterns

1) Build a dataframe

2) Clean:

-	Row - Object... each row describes a single object
-	Column - Describe... each column describes a property of that object
-	Column - Numeric... columns are numeric wherever possible
-	Column - Atomic... columns contain atomic properties that cannot be further decomposed

3) Explore global properties:

-	histograms
-	scatter plots
-	aggregation

4) Group properties:

-	use groupby and small multiples to explore subsets.

Computing indicator variables
-----------------------------

These are useful when you want to split a field with a list of indicators out across different columns each with a boolean value.

~1:02:30

When collecting the unique values, use set()... this doesn't add a value twice.

Then create another loop... code at 1:05:00

Exploratory data analysis
-------------------------

Note questions and findings as you go.

Awesome small multiples code in the demo notebook.
