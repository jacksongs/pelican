Title: CS109 lecture three
Date: 2014-05-27 19:42
Category: data science
Tags: harvard, python, cs109
Author: jacksongs
Summary: Moving into week two of the CS109 data science course at Harvard.

*Never stop learning is a motto of mine. [Here](/dabbling-in-data-science.html) it's data science, and [Harvard's CS109 data science course](http://cs109.org/).*

The [first lab](http://cm.dce.harvard.edu/2014/01/14328/S01/index_H264SingleHighBandwidth-16x9.shtml) was pretty basic Python, and didn't include much of the array-based computing techniques I'm looking for. 

The readings for week one were also fairly preliminary and were mostly covered in the lectures.

So onward it is to the second week...

Lecture three notes - [video link](http://cm.dce.harvard.edu/2014/01/14328/L03/index_H264SingleHighBandwidth-16x9.shtml)
=======================

15:25 - Edward Tufte.

16:10 - Key principle of Tufte:

*	Graphical integrity, spatial distortions, ie bar graphs always start at zero. (reference to How to Lie with Statistics). For line graphs, scale distortions are more acceptable, though reader should be alerted.
*	Show context, ie don't be selective with data. But need to be a little bit selective. 
*	Avoid lie factor, based on size of effect in graphic/size of effect in data.
*	Data ink ratio maximised, ie data ink/total ink used in graphic.
*	Avoid chartjunk, but matplotlib defaults are awful! Check out IPython notebook in reading.

32:30 - Chart types. Start by asking:

Comparisons?
------------

Bar chart, look at Chris' notebook

For long labels, rotate bars 90 degrees

Trends over time?
-----------------

Line charts are reliable

Important that x-axis is continuous variable

But! Bars vs lines: lines imply continuous data points.

Consider aspect ratio. Look at average slope... we are tuned for comparing lines at about 45 degrees.

Correlations?
-------------

Consider light grey border for plotting dots in crowded scatter plots.

Overplotting problems, try grey borders and muted colours. Or try opacity changes.

Add a trend line for scatter plots along with confidence intervals.

Compositions?
-------------

Pie chart is used most often here, even though people hate them.

Some advantages. Ie showing how two categories add up - bar chart is less effective.

Labelling and order by size is important.

But consider bar unless there is good reason.

Donut charts lost the middle piece, the angle, which helps with comparisons.

What about stacked bar graph? Or 100% bar graph. These are pretty good, arguably better than pie charts.

But, the problem is when you want to compare segments that aren't lined up on the x-axis.

Small multiples are also very handy.

Stacked area chart/100% stacked area chart.

But - combined line chart is usually better.

Distributions?
--------------

Histogram - play with the bin size.

Density plots - you could also show the raw data in dots along the axis.

Heat maps - 2d version of heatmap.

Box and whisker plots. Red line - median. Box - 25/75 percentile. Whiskers - max/min or 5/95 percentile.

Colour
------

Sometimes required - eg maps with quantitative info, if you already have used 2 spatial dimensions use colour for 3rd dimension, categories in line charts or bar charts.

3 dimensions:

*	lightness
*	hue
*	saturation

Nominal data or categories suits colours well.

Ordinal data suits the lightness spectrum.

For quantitative data, don't use colour map!

Why? Hard to order. But also chroma channel has lower resolution than lightness channel. And also it is perceptually non-uniform: ie for a uniform change, changes in colour look like there are small jumps.

Instead, use Brewer scales. See ColorBrewer website. And see Chris' IPython notebook for examples in Python.

