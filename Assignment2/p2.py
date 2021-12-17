#Answers Question 2 of Assignment 2

import numpy as np

#Current state
I = np.matrix([[0.5, 0.3,0.2,0.0]])
#Transition Matrix
T = np.matrix([[0.2, 0.5, 0.2, 0.1],
               [0.3, 0.4, 0.2, 0.1],
               [0.1, 0.3, 0.4, 0.2],
               [0.1, 0.1, 0.3, 0.5]])
# Step 1
T1 = I * T
# Step 2
T2 = T1 * T
# Step 3
T3 = T2 * T
# Step 4
T4 = T3 * T
print (T4)

print("At the end of 4 steps, the probability that exactly 3 phonelines are occupied is 0.20484")
print("At the end of 4 steps one line beign busy has the highest probability")
