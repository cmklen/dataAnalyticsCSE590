# Part A
The text used is the Princess and the Goblin. It is a children's story and fiarly short, making the execution time for this project quick.
# Part B
For part a, there are two helper functions to aid in the creation of the list and future parts. `filterUnwantedCharacters` takes out all special characters froma word using regular expressions. `addWordOnly` calls that helper function and additionally filters out `--` which can't simply be removed since it joins two words; the funciton splits these up and adds them to the list

# Part C
`df` is the variable used for the data frame for part c. To convert the list to a dataframe, an intermediate step of converting to a dictionary is used. This method was presented in class for counting the words, and a dictionary is very simple to convert to a dataframe.

# Part D
`dfStopWordsSorted` contains the desired output for part d. We make sure to copy this dataframe from the df in part C as we don't want to edit that variable. The stop words are included as a list and then passed as the paramter for the .drop function. The `sort_values` function does exactly what is need to the dataframe, and sorts the remaining data.

# Part E
`chapterDfList` contains the list of dataframes counting the words for each chapter. This part is a compilation of the methods used in parts B-D. There could have defintely been some simplicfication by reusing code in the form of more functions, but at the same time it was fairly consise code to copy over. Instead of reusing old lists, a new one is created to manipulate, converted into a dict to count the words, then sorted and trimmed of the stop words. This process is looped through each chapter, which is initially split using `.split()` on each instance of the CHAPTER heading.