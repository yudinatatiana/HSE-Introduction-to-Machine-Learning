# Task 1

Read the documentation for scipy.optimize.minimize, paying special attention to the Jacobian argument jac. Who computes the gradient, the minimize function itself, or the developer using it?


**Answer:** The gradient is calculated by the developer, if a function for calculating the gradient is specified in the jac-parameter, otherwise the gradient is calculated by the minimization function itself.

Run the following two examples; which performs better?

![Task 1](/SVM/task_1.PNG)

**Answer:** The first example (with gradient vector) works faster both in time (5.11 < 7.35) and in the number of iterations (3 < 4). Also, in the first case, the value of the objective function turned out to be equal to 0, and in the second case, it is greater than 0 (5.72).
