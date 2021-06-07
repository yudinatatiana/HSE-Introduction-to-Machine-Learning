#!/usr/bin/env python
# coding: utf-8

# # Task 1
# 
# Read the documentation for scipy.optimize.minimize, paying special attention to the Jacobian argument jac. Who computes the gradient, the minimize function itself, or the developer using it?
# 
# 
# **Answer:** The gradient is calculated by the developer, if a function for calculating the gradient is specified in the jac-parameter, otherwise the gradient is calculated by the minimization function itself.
# 
# Run the following two examples; which performs better?

# In[1]:


import scipy.optimize, numpy.random


# In[2]:


def f(x):
  return x**2
def df(x):
  return 2*x


# In[3]:


get_ipython().run_cell_magic('time', '', 'print(scipy.optimize.minimize(f, numpy.random.randint(-1000, 1000), jac=df))')


# In[4]:


get_ipython().run_cell_magic('time', '', 'print(scipy.optimize.minimize(f, numpy.random.randint(-1000, 1000), jac=False))')


# **Answer:** The first example (with gradient vector) works faster both in time (5.11 < 7.35) and in the number of iterations (3 < 4). Also, in the first case, the value of the objective function turned out to be equal to 0, and in the second case, it is greater than 0 (5.72).

# # Task 2
# 
# Write in python the loss function for support vector machines from equation (7.48) of Daumé. You can use the following hinge loss surrogate:

# In[5]:


import numpy as np


# In[6]:


def hinge_loss_surrogate(y_gold, y_pred):
    return max(0, 1 - y_gold * y_pred)

def svm_loss(w_b, C, D): 
    w, b = w_b[:-1], w_b[-1]
    small_slack = 0
    for pair in D:        
        small_slack += hinge_loss_surrogate(pair[1], np.dot(w, pair[0]) + b)    
    return 0.5 * np.dot(w, w) + C * small_slack


# # Task 3
# 
# Use scipy.optimize.minimize with jac=False to implement support vector machines.

# In[7]:


def svm(D, C=1):
    w = np.zeros(len(D[0][0]))
    b = np.array([0])
    fun = lambda w_b: svm_loss(w_b, C=C, D=D)
    result = scipy.optimize.minimize(fun, x0=np.concatenate([w, b]), jac=False).x
    w, b = result[:-1], result[-1]
    return w, b    


# # Task 4
# 
# Implement the gradient of svm_loss, and add an optional flag to svm to use it:

# In[8]:


def gradient_hinge_loss_surrogate(y_gold, y_pred):
    if hinge_loss_surrogate(y_gold, y_pred) == 0:
        return 0
    else:
        return -y_gold

def gradient_svm_loss(w_b, C, D): 
    w, b = w_b[:-1], w_b[-1]
    d_w = w + C * sum(pair[0] * gradient_hinge_loss_surrogate(pair[1], np.dot(w, pair[0]) + b) for pair in D)
    d_b = C * sum(gradient_hinge_loss_surrogate(pair[1], np.dot(w, pair[0]) + b) for pair in D)
    return np.hstack([d_w, d_b])

def svm(D, C=1, use_gradient=False):
    w = np.random.randint(100, size=len(D[0][0]))
    b = np.random.rand(1)    
    fun = lambda w_b: svm_loss(w_b, C=C, D=D)
    if use_gradient is False:
        result = scipy.optimize.minimize(fun, x0=np.concatenate([w, b]), jac=False).x
    else:
        jac_f  = lambda w_b: gradient_svm_loss(w_b, C=C, D=D)
        result = scipy.optimize.minimize(fun, x0=np.concatenate([w, b]), jac=jac_f).x
    w, b = result[:-1], result[-1]
    return w, b 


# # Task 5
# 
# Use numpy.random.normal to generate two isolated clusters of points in 2 dimensions, one x_plus and one x_minus, and graph the three hyperplanes found by training:
# - an averaged perceptron
# - support vector machine without gradient
# - support vector machine with gradient.
# 
# How do they compare?

# In[9]:


import matplotlib.pyplot as plt


# In[23]:


x_plus = np.random.normal(loc=[-1,-1], scale=0.5, size=(20,2))
x_minus = np.random.normal(loc=[1,1], scale=0.5, size=(20,2))

D = list()

for x in x_plus:
    D.append((x, 1))
    
for x in x_minus:
    D.append((x, -1))


# In[24]:


def AveragedPerceptronTrain(D, maxiter = 1000):
    w = np.zeros(len(D[0][0]))
    b = np.zeros(1)
    u = np.zeros(len(D[0][0]))
    beta = 0
    c = 1
    for i in range(maxiter):
        for x, y in D:
            a = np.dot(x, w) + b
            if np.sign(y * a) <= 0: 
                w += y * x
                b += y
                u += y * c * x
                beta += y * c
            c += 1
    return w - (1/c) * u, b - beta * (1/c)


# In[25]:


w_perc, b_perc = AveragedPerceptronTrain(D)
w_svm, b_svm = svm(D)
w_svm_grad, b_svm_grad = svm(D, use_gradient=True)


# In[26]:


def hyperplane(w, b, color, label):
    """
    https://stackoverflow.com/questions/46511017/plot-hyperplane-linear-svm-python
    """
    a = -w[0] / w[1]
    xx = np.linspace(-2, 2)
    yy = a * xx - (b) / w[1]
    return plt.plot(xx, yy, color=color, label=label)


# In[27]:


plt.scatter(x_plus[:,0], x_plus[:,1], marker='+', color='b')
plt.scatter(x_minus[:,0], x_minus[:,1], marker='x', color='r')
hyperplane(w_perc, b_perc, color='c', label='Averaged perceptron')
hyperplane(w_svm, b_svm, color='m', label='SVM without gradient')
hyperplane(w_svm_grad, b_svm_grad, color='y', label='SVM with gradient')
plt.legend(loc='lower right')
plt.savefig("svm-svm-perceptron.pdf") 
plt.show()


# **Answer:** All three models split the data correctly. It seems that SVMs perform better because they are not as close to the red class as the perceptron.
