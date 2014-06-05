Title: SA government contract analysis
Date: 2014-06-05 19:55
Category: work
Tags: data science, python, south australia
Author: jacksongs
Summary: A few charts that help make sense of the SA government's procurement data. 

I've been researching historical SA government procurement contract data. The agencies haven't been particularly helpful as yet, but I'm able to look at some archived data held on the [www.tenders.sa.gov.au](http://www.tenders.sa.gov.au).

It's not complete, and is very messy. But with nearly 10,000 contracts there is plenty of truth in what it shows. [This scraper](/a-humble-scraper.html) is how I collected the data.

This is the first part of analysis. Expect more in future.

Hit me up on Twitter if you have any suggestions: [@jacksongs](http://www.twitter.com/jacksongs).

*Update: I should mention that there is a $500,000 threshold under which contracts for goods and services do not have to be disclosed (though contracts with consultants still do). The effect of this threshold is pretty obvious in this data, as you can see...*

{% notebook aContractAnalyser.ipynb %}
