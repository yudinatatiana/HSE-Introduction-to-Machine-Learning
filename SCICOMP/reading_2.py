#!/usr/bin/env python
# coding: utf-8

# Exercise: use python to check this:

# In[1]:


from decimal import Decimal

print(repr(Decimal(0.1)))


# Exercise: what is the best approximation of 0.01?

# In[2]:


print(repr(Decimal(0.01)))


# Exercise: implement the Caesar cipher in python, which advances each letter of 'M' by 'SEC = n': enc(1, "a") = "b", etc.

# In[1]:


def caesar_cipher(text, step, alphabets):

    def shift(alphabet):
        return alphabet[step:] + alphabet[:step]

    shifted_alphabets = tuple(map(shift, alphabets))
    joined_aphabets = ''.join(alphabets)
    joined_shifted_alphabets = ''.join(shifted_alphabets)
    table = str.maketrans(joined_aphabets, joined_shifted_alphabets)
    return text.translate(table)


# In[4]:


import string
alphabets = (string.ascii_lowercase, string.ascii_uppercase, string.digits)
caesar_cipher('hello', step=13, alphabets=alphabets)


# In[ ]:




