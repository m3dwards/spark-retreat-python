## Using Olympics.csv data:

1: Which country scored the most medals?

2: For “United States”, find the year in which it scored  most medals?

3: List the years when  “United States” scored less than 200 medals?

4: Which player has medals in more than one sport?


## Inverted Indices
Build Inverted indices from given text  
Given the following input,  
 1: if you prick us do we not bleed  
 2: if you tickle us do we not laugh  
 3: if you poison us do we not die and  
 4: if you wrong us shall we not revenge  

The inverted index, we want to build looks like,  
and     : 1 : (3, 1)  
bleed   : 1 : (1, 1)  
die     : 1 : (3, 1)  
do      : 3 : (1, 1), (2, 1), (3, 1)  
if      : 4 : (1, 1), (2, 1), (3, 1), (4, 1)  
laugh   : 1 : (2, 1)  
not     : 4 : (1, 1), (2, 1), (3, 1), (4, 1)  
poison  : 1 : (3, 1)  
prick   : 1 : (1, 1)  
revenge : 1 : (4, 1)  
shall   : 1 : (4, 1)  
tickle  : 1 : (2, 1)  
us      : 4 : (1, 1), (2, 1), (3, 1), (4, 1)  
we      : 4 : (1, 1), (2, 1), (3, 1), (4, 1)  
wrong   : 1 : (4, 1)  
you     : 4 : (1, 1), (2, 1), (3, 1), (4, 1)  

Note - The data set we have is just a text file, without line numbers, to get line numbers, you need can get that by calling “zipWithIndex”  

Questions to answer  

In which line can you find the term "starcross'd".  
In how many lines does "gold" appear once, twice, three times.  
