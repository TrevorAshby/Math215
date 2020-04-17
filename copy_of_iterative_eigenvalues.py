# -*- coding: utf-8 -*-
"""Copy of Iterative_eigenvalues.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1W76mznlW2y56sUShtRCIYsqHuRymsjiw

#**Lab 9 - Iterative eigenvalues and Markov chains**

Enter your code in the spaces provided. Do not change any of the variable names or function names that are already provided for you. In places where we specify the name of the return value, make sure that your code produces the a value with the correct name.
"""

# Do not edit this cell.

LabID="Lab9"

try:
  from graderHelp import ISGRADEPLOT
except ImportError:
  ISGRADEPLOT = True

"""**Enter your name, section number, and BYU NetID**"""

# Enter your first and last names in between the quotation marks.

first_name="Trevor"

last_name="Ashby"

# Enter your Math 215 section number in between the quotation marks. 

section_number="003"  

# Enter your BYU NetID in between the quotation marks.  NOT YOUR BYU ID NUMBER! 

BYUNetID="trashby"

"""**Import NumPy**"""

import numpy as np

"""**Problem 1**"""

# This function approximates the dominant eigenvector of our matrix A.

def evect_approx1(x_0,k):
  A= np.array([[1,1],[2,0]])
  x_k= np.matmul(np.linalg.matrix_power(A,k),x_0) # Put your code here.
  return x_k # Put your return value here.

"""**Problem 2**"""

# This function approximates the dominant eigenvalue of our matrix A.

def eval_approx1(x_0,k):
  A= np.array([[1,1],[2,0]])
  Lk0= evect_approx1(x_0,k)
  Lk1= evect_approx1(x_0,k+1)

  result= Lk1[0]/Lk0[0]
  # Put your code here.
  return result # Put your return value here.

"""**Problem 3**"""

# This function approximates the dominant eigenvalue and eigenvector of our matrix A using the normalized iterative process.

def norm_evect_approx1(x_0,k):
  A= np.array([[1,1],[2,0]])
  w_j= x_0
  for j in range(1,k):
    w_j= np.matmul(A,w_j)
    x_j= w_j/np.linalg.norm(w_j)
  w_k= np.matmul(A,w_j)
  x_k= w_k/np.linalg.norm(w_k)
  # Put your code here.
  return x_k, w_k[0]/w_j[0] # Put your return value here.

"""**Problem 4**"""

# This function approximates the dominant eigenvalue and eigenvector of an arbitrary matrix using the process described in Problem 4.

def norm_approx_gen(M,x_0,k):
  for j in range(k):
    w_j= np.matmul(M,x_0)
    eigen = w_j[0]/x_0[0]
    x_0= w_j/(np.max(np.abs(w_j)))
  #w_k= np.matmul(M,w_j)
  #x_k= w_k/np.linalg.norm(w_k)
  # Put your code here.
  return x_0, eigen # Put your return value here.

"""**Problem 5**"""

# This function approximates the dominant eigenvalue and eigenvector of an arbitrary matrix using the Rayleigh quotiend as described in Problem 5.

def ray_quotient(M,x_0,k):
  # Put your code here.
  x_k,eigen= norm_approx_gen(M,x_0,k)
  v= np.matmul(M,x_k)
  ray= np.dot(v,x_k)/np.dot(x_k,x_k) 
  return ray #Put your return value here.

ray_quotient(np.array([[2,4,6],[4,8,0],[1,2,9]]),np.array([1,5,-1]),10)

"""**Problem 6**"""

# Replace all of the 0 values with the vectors requested in Problem 6.
M= np.array([[3,2,-2],[-1,1,4],[3,2,-5]])
x_0= np.array([1,1,1])
#print(norm_approx_gen(M,x_0,3))
#print(norm_approx_gen(M,x_0,4))

x_vect_3=norm_approx_gen(M,x_0,3)[0]

x_vect_4=norm_approx_gen(M,x_0,4)[0]

"""**Problem 7**"""

# This function returns the number of subscribers to the different streaming services after month k.

def subscriber_vals(x_0,k):
  # Put your code here.
  P = np.array([[0.7,0.2],[0.3,0.8]])
  for i in range(k):
    x_0 = np.matmul(P,x_0)
  return x_0# Put your return value here.

"""**Problem 8**"""

# Replace all of the 0 values with the value requested in Problem 8.
netflix_subs6= subscriber_vals(np.array([0.6,0.4]),6)[1]

"""**Problem 9**"""

# Replace all of the 0 values with the matrix/vector/value requested in Problem 9.
A= np.array([.8,.5,.3,.2])
B= np.array([.05,.2,.1,.1])
C= np.array([.1,.1,.3,.1])
D= np.array([.05,.2,.3,.6])
trans_matrix= np.array([A,B,C,D])

"""**STOP!  BEFORE YOU SUBMIT THIS LAB:**  Go to the "Runtime" menu at the top of this page, and select "Restart and run all".  If any of the cells produce error messages, you will either need to fix the error(s) or delete the code that is causing the error(s).  Then use "Restart and run all" again to see if there are any new errors.  Repeat this until no new error messages show up.

**You are not ready to submit until you are able to select "Restart and run all" without any new error messages showing up.  Your code will not be able to be graded if there are any error messages.**

To submit your lab for grading you must first download it to your compute as .py file.  In the "File" menu select "Download .py".  The resulting file can then be uploaded to http://www.math.byu.edu:30000/ for grading.
"""