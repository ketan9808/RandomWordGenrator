
# coding: utf-8

# In[1]:


from itertools import permutations
from nltk.corpus import names
from nltk.corpus import words


# In[2]:


def toupper(obj):
    upper_list = []

    for word in obj:
        upper_list.append(word.upper())
    
    return upper_list


# In[3]:


def data_preprocessing(char_list,req_len):
    words_obj = words.words()
    All_names = names.words()
    All_words = toupper(words.words())
    
    # number of characters = len(list)
    
    perm = permutations(char_list,req_len)
    perm_list = []
    # prepairing all set of words that
    for Set in perm:
        perm_list.append(''.join(list(Set)))
    
    possible_combination = []
    
    for Words in perm_list:
        if Words in All_words and Words not in All_names:
            possible_combination.append(Words)
    
    return possible_combination


# In[4]:


char_list = list(input('Enter any word forming from characters given: '))

req_len = int(input('Enter length of resultant word: '))

print(data_preprocessing(toupper(char_list),req_len))

