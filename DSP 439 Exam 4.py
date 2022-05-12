#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Chris Kerfoot
# DSP 439
# Exam 4
# May 11, 2022


# In[30]:


#Imports
import pandas as pd
import sys


#  Define a function to count possible kmers of size k from a string, where k and the string are
#  specified as arguments.

def possible_kmers(string, k): # function for counting possbile kmers with string and k as the arguments
    return (min(len(string)-k+1,4**k))

# Example
output = possible_kmers("ATTTGGATT", 1)
print(output)


# In[42]:


#Define a function to count observed kmers of size k from a string, where k and the string are specified as arguments.
def observed_kmers(string, k): # function for counting possbile kmers with string and k as the arguments
  #''' Takes in a string and kmer of size k and outputs observed kmers '''
    counts = []
    duplicates = []
    for i in range( len(string)-k+1):   
        kmer = string[i:i+k]
#         if kmer not in counts:
#             counts[kmer] = 0
#             counts[kmer] = counts[kmer] + 1
        counts.append(kmer)
    # Removes all possible substrings of not length k
    for i in range(len(counts)):
        if (len(counts[i]) != k ):
            counts.popback()
    # Compares two lists if the duplicates are not in other list and we append it, otherwise we don't
    for i in counts:
        if i not in duplicates:
            duplicates.append(i)
        
    return len(duplicates)    


#Examples
output = observed_kmers("ATATATATATATA", 2)
print(output)

output2 = observed_kmers("ATTTGGATT",3)
print(output2)





# In[62]:


# Define a function to create a pandas data frame containing all possible k and the associated
# number of observed and expected kmers (see above table).
def dataframe(k, observed_kmers, possible_kmers, string):
    observed = observed_kmers(string,k)
    possible = possible_kmers(string,k)

# dictionary with values of the dataframe
    dict = {'k': k,'Observed Kmers' : observed_kmers, "Possible kmers": possible_kmers}
    df = pd.DataFrame(dict)
    return (df)


# In[52]:


# Define a function to calculate linguistic complexity
def linguistic_complexity(string,k):
    numerator = 0
    denominator = 0
    
    for i in range (0,k):
        output = possible_kmers(string,i)
        output_2 = observed_kmers(string,i)
        numerator += output_2
        denominator += output
    complexity = numerator/denominator
    return complexity

linguistic_complexity("ATTTGGATT",9)

