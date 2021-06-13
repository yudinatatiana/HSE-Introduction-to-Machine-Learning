#!/usr/bin/env python
# coding: utf-8

# # Task 1
# 
# Use the Tree data structure below; write code to build the tree from figure 1.2 in Daumé.

# In[1]:


class Tree:
    '''Create a binary tree; keyword-only arguments `data`, `left`, `right`.
    Examples:
    l1 = Tree.leaf("leaf1")
    l2 = Tree.leaf("leaf2")
    tree = Tree(data="root", left=l1, right=Tree(right=l2))
    '''

    def leaf(data):
        '''Create a leaf tree
        '''
        return Tree(data=data)

    # pretty-print trees
    def __repr__(self):
        if self.is_leaf():
            return "Leaf(%r)" % self.data
        else:
            return "Tree(%r) { left = %r, right = %r }" % (self.data, self.left, self.right)

    # all arguments after `*` are *keyword-only*!
    def __init__(self, *, data = None, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

    def is_leaf(self):
        '''Check if this tree is a leaf tree
        '''
        return self.left == None and self.right == None

    def children(self):
        '''List of child subtrees
        '''
        return [x for x in [self.left, self.right] if x]

    def depth(self):
        '''Compute the depth of a tree
        A leaf is depth-1, and a child is one deeper than the parent.
        '''
        return max([x.depth() for x in self.children()], default=0) + 1


# In[34]:


leaf_nah = Tree.leaf('nah')
leaf_like = Tree.leaf('like')
Tree1 = Tree(data = 'likedOtherSys?', left = leaf_nah, right = leaf_like)
Tree2 = Tree(data = 'morning?', left = leaf_like, right = leaf_nah)
Tree3 = Tree(data = 'takenOtherSys?', left = Tree2, right = Tree1)
Tree4 = Tree(data = 'isSystems?', left = leaf_like, right = Tree3)
print(Tree4)


# # Task 2
# 
# In your python code, load the following dataset and add a boolean "ok" column, where "True" means the rating is non-negative and "False" means the rating is negative.

# In[4]:


import pandas as pd


# In[35]:


data = '''rating,easy,ai,systems,theory,morning
 2,True,True,False,True,False
 2,True,True,False,True,False
 2,False,True,False,False,False
 2,False,False,False,True,False
 2,False,True,True,False,True
 1,True,True,False,False,False
 1,True,True,False,True,False
 1,False,True,False,True,False
 0,False,False,False,False,True
 0,True,False,False,True,True
 0,False,True,False,True,False
 0,True,True,True,True,True
-1,True,True,True,False,True
-1,False,False,True,True,False
-1,False,False,True,False,True
-1,True,False,True,False,True
-2,False,False,True,True,False
-2,False,True,True,False,True
-2,True,False,True,False,False
-2,True,False,True,False,True'''

with open('./data.csv', 'w') as f:
    f.write(data)
  

df = pd.read_csv('./data.csv')
df['ok'] = df.rating >= 0 
print(df)


# # Task 3
# 
# Write a function which takes a feature and computes the performance of the corresponding single-feature classifier:

# In[7]:


from functools import partial
import numpy as np


# In[8]:


def single_feature_score(data, goal, feature):
    true = data[data[feature] == True][goal]
    false = data[data[feature] == False][goal]
    
    true_matches = 0
    false_matches = 0
    if len(true) != 0:
        true_most_common = true.value_counts()[:1].index.tolist()[0]
        true_matches = true.value_counts()[true_most_common]        
    
    if len(false) != 0:
        false_most_common = false.value_counts()[:1].index.tolist()[0]
        false_matches = false.value_counts()[false_most_common]      
    
    return (true_matches + false_matches) / len(data)


# Use this to find the best feature:

# In[9]:


# Use this to find the best feature:
def best_feature(data, goal, features):
    # optional: avoid the lambda using `functools.partial`
    scorer = partial(single_feature_score, data, goal)
    return max(features, key=scorer)

def worst_feature(data, goal, features):
    # optional: avoid the lambda using `functools.partial`
    scorer = partial(single_feature_score, data, goal)
    return min(features, key=scorer)


# Which feature is best? Which feature is worst?

# In[10]:


features = df.columns.tolist()[1:-1]
bf =  best_feature(df, 'ok', features)
wf = worst_feature(df, 'ok', features)
print('Best feature is', bf, 'with score', single_feature_score(df, 'ok', bf))
print('Worst feature is', wf, 'with score', single_feature_score(df, 'ok', wf))


# # Task 4
# 
# Implement the DecisionTreeTrain and DecisionTreeTest algorithms from Daumé, returning Trees. (Note: our dataset and his are different; we won't get the same tree.)
# How does the performance compare to the single-feature classifiers?

# In[36]:


def DecisionTreeTrain(data, goal, features):
    guess = data[goal].value_counts()[:1].index.tolist()[0]
    if len(features) == 0 or len(set(data[goal])) == 1:
        return Tree.leaf(guess)
    else:
        bf = best_feature(data, goal, features)
        remaining_features = features.copy()
        remaining_features.remove(bf)        
        true = data[data[bf] == True]
        false = data[data[bf] == False]
        
        if len(true) != 0:
            right = DecisionTreeTrain(true, goal, remaining_features)
        else:
            right = Tree.leaf(guess)
        
        if len(false) != 0:
            left = DecisionTreeTrain(false, goal, remaining_features)
        else:
            left = Tree.leaf(guess)         
        
        return Tree(data=bf, left=left, right=right)
    
def DecisionTreeTest(tree, data_point):
    if tree.is_leaf():
        return tree.data
    else:
        feature_name = tree.data
        if not data_point[feature_name]:
            return DecisionTreeTest(tree.left, data_point)
        else:
            return DecisionTreeTest(tree.right, data_point)


# In[37]:


tree = DecisionTreeTrain(df, 'ok', features)
print(tree)


# # Task 5
# 
# Add an optional maxdepth parameter to DecisionTreeTrain, which limits the depth of the tree produced. Plot performance against maxdepth.

# In[22]:


def DecisionTreeTrain_2(data, goal, features, max_depth):
    guess = data[goal].value_counts()[:1].index.tolist()[0]
    if len(features) == 0 or len(set(data[goal])) == 1 or max_depth == 0:
        return Tree.leaf(guess)
    else:
        bf = best_feature(data, goal, features)
        remaining_features = features.copy()
        remaining_features.remove(bf)        
        true = data[data[bf] == True]
        false = data[data[bf] == False]
        
        if len(true) != 0:
            right = DecisionTreeTrain_2(true, goal, remaining_features, max_depth-1)
        else:
            right = Tree.leaf(guess)
        
        if len(false) != 0:
            left = DecisionTreeTrain_2(false, goal, remaining_features, max_depth-1)
        else:
            left = Tree.leaf(guess)          
        
        return Tree(data=bf, left=left, right=right)


# In[38]:


tree_2 = DecisionTreeTrain_2(df, 'ok', features, max_depth=2)
print(tree_2)


# In[39]:


def performance(tree, goal, data):
    data_points = data.to_dict(orient='records')
    y_pred = [DecisionTreeTest(tree, point) for point in data_points]
    y_true = [point[goal] for point in data_points]    
    count = 0
    for i in range(len(data)):
        if y_pred[i] == y_true[i]:
            count += 1
    return count / len(data)

max_depths = [i for i in range(10)]
scores = list()
for i in max_depths:
    tree = DecisionTreeTrain_2(df, 'ok', features, max_depth=i)
    scores.append(performance(tree, 'ok', df))


# In[40]:


import matplotlib.pyplot as plt

plt.grid(True)
plt.xlabel('Max Depth')
plt.ylabel('Accuracy')
plt.plot(max_depths, scores)
plt.savefig('plot.png')

