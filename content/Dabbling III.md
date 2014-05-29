Title: CS109 lecture two
Date: 2014-05-25 20:42
Category: data science
Tags: harvard, python, cs109
Author: jacksongs
Summary: More riveting notes and reflections from the second lecture of CS109.

*Never stop learning is a motto of mine. [Here](/dabbling-in-data-science.html) it's data science, and [Harvard's CS109 data science course](http://cs109.org/).*

Week 1, lecture 2 notes - [video link](http://cm.dce.harvard.edu/2014/01/14328/L02/index_H264SingleHighBandwidth-16x9.shtml)
=======================

Here are some notes from the second lecture video in week one.

Outline:
--------

*Process and process books
*Effective visualisations
*Data sources and cleanup

11:20 - AGEMC! Ask, get, explore, model, communicate. Plus loops between them.

12:20 - 'What do analysts do paper?' - This is part of the readings, should be good reading.

13:50 - Most of time spent? Prepping the data!

14:50 - Process of data science not yet codified in these companies. Interesting... Repeatability, documentation, process are all critical.

16:20 - Data cleanup and knowing your data is very important. John Tukey: exploratory data analysis. Look at the data visually before you formulate hypotheses.

17:35 - Anscombe's Quartet: artificial datasets that have same mean, variance, correlation and linear regression line.

18:30 - Antibiotic example. Will Burtin, 1951. Data and questions. Talking data types: strings, floats, booleans.

29:30 - Bacteria comparison example. Key learning: think of more interesting questions, for example consider categories.

31:15 - "That's funny..." is a cue to pursue more and better informed questions.

32:00 - Process book! Suits the static blog very well with IPython notebooks.

35:30 - IPython notebook demonstrations.

41:40 - Good coding practices: commenting, modularity, array-oriented computing, using assert statements and tests, version control. Array-oriented computing will need some work! (No more for/while loops.) 

Data types
----------

Starts 46:54

Ben Shneiderman, 1996, different types:

*	sequences (1D)
*	temporal
*	2d (maps)
*	3d (shaped)
*	nD (relational) - ie table
*	trees (hierarchical)
*	networks (graphs)
*	others?

Tamara Munzner, 2013, simpler:

*	tables
*	networks
*	text/logs

Semantics (meaning) vs types (interpretation in terms of scale of measurement)

1946, Stevens paper:

*	nominal (a thing, equal or not equal, but little else)
*	ordinal (obey size relationships)
*	quantitative (can be interval or ratio)

Operations therefore:

*	nominal: =
*	ordinal: =,>
*	interval: =,>,+ (distance)
*	ratio: =,>,+,x (proportions)

Row = item
Column = attribute or feature

Nominal/Ordinal = Dimensions
Quantitative = Measures

Data dimensions
---------------

*	Univariate - lots of chart options
*	Bivariate - scatter only really (not 3D! Use size/colour instead)
*	Multivariate - tables of many columns (consider small multiples, but this is a big challenge in data visualisation)

So focus on data reduction...

*Filtering - select of interest
*Aggregation - ave, min, max

Mapping data to images
----------------------

Jacques Bertin, French Cartographer, 'Semiology of Graphics' 1967 provided a basic vocabulary of marks:

*	Points
*	Lines
*	Zones

Along with channels:

*	Position
*	Size
*	Greyscale
*	Texture
*	Colour
*	Orientation
*	Shape

William Playfair came up with most types of chart in the late 18th century.

So what channels/marks are most effective for what data types?

Colour hue is not perceived as ordered, though brightness and saturation do.

Bertin set out how well each channel works with data.

Cleveland/McGill, 1984 and Mackinlay, 1986 carried out studies to check how well people could judge quantities.

Scale of efficiency:

*	position
*	length
*	slope or angle
*	area
*	intensity
*	colour or shape (but good for nominal types/categories)

