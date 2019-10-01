# -*- coding: utf-8 -*-
"""Copy of Iterative_methods.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ySNOMRVIe5A6aexzSAwUSYzFTn36vAVI

#**Lab 4 - Iterative methods for solving systems of linear equations**

Enter your code in the spaces provided. Do not change any of the variable names or function names that are already provided for you. In places where we specify the name of the return value, make sure that your code produces the a value with the correct name.
"""

# Do not edit this cell.

LabID="Lab4"

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

"""**Problem 1**"""

# Replace the values of 0 with the values you solved for in Problem 1.

x_val=1    

y_val=1

"""**Problem 2**"""

# Performs one iteration of the Jacobi method for system (1) applied to the point (x,y).

def jacobi1_iteration(x,y): 
    new_x = (1/7)*(6 + y)
    new_y = (1/5)*(x + 4)# Put your code here.
    return [new_x,new_y] # Your return statement should return a list of the form [new_x,new_y]

"""**Problem 3**"""

# Performs n iterations of the Jacobi method on system (1) with starting estimate (0,0).

def jacobi1_method(n):
    x_n=0
    y_n=0
    for i in range(n): # Put your code here.
      [x_n,y_n] = jacobi1_iteration(x_n,y_n)
      x_n = x_n
      y_n = y_n
    return [x_n,y_n] # Your return statement should return a list of the form [x_n,y_n]

"""**Problem 4**"""

# Replace the values of 0 with the values you solved for in Problem 4.

n_var1=2    

n_var2=6

"""**Problem 5**"""

# Performs one iteration of the Gauss-Seidel method for system (1) applied to the point (x,y).

def gs1_iteration(x,y): 
    new_x = (1/7)*(6 + y)
    new_y = (1/5)*(new_x + 4) # Put your code here.
    return [new_x, new_y] # Your return statement should return a list of the form [new_x,new_y]

"""**Problem 6**"""

# Performs n iterations of the Gauss-Seidel method on system (1) with starting estimate (0,0).

def gs1_method(n): 
    x_n=0
    y_n=0
    for i in range(n):
      [x_n,y_n] = gs1_iteration(x_n,y_n) # Put your code here.
    return [x_n,y_n] # Your return statement should return a list of the form [x_n,y_n]

"""**Problem 7**"""

# Replace the values of 0 with the values you solved for in Problem 7.

n_var3=2    

n_var4=4

"""**Problem 8**"""

import numpy as np

# Finds the error of the nth approximation of the solution to system (1) using the Gauss-Seidel method.

def gs1_error(n): 
    x_n = 0
    y_n = 0
    for i in range(n):
        [x_n,y_n] = gs1_iteration(x_n,y_n)
    estimate = [x_n,y_n]
    approx = np.linalg.norm(np.array([1,1])-np.array(estimate)) # Put your code here.
    return approx # Put your return statement here.

# The following code will construct your plot of gs1_error for you.  You don't need to change anything in this cell, simply execute it. Consider this one a freebie.

# Note that you must have a function defined called gs1_error from the previous problem in order for the plot to be created.  We first import matplotlib.pyplot:

import matplotlib.pyplot as plt



# This command uses the function gs1_error to create a new function vect_gs1_error which will accept NumPy arrays of various sizes as input, instead of just a single number.

vect_gs1_error=np.vectorize(gs1_error)  



# This creates a NumPy array of values of the form [0,1,2,...,48,49], similar to the np.linspace command.  The 1 in the function tells NumPy to count up by ones.

n_vals=np.arange(0,50,1)



# This creates the plot, and labels the axes.  See if you can determine what each command is doing.

plt.title('Error of the Gauss-Seidel Method Applied to System 1')
plt.xlabel('Number of iterations')
plt.ylabel('Error')
plt.plot(n_vals,vect_gs1_error(n_vals),'ro')
plt.show()

"""**Problem 9**"""

# Gives one iteration of the Gauss-Seidel method for system (4) applied to the point (x,y).

def gs2_iteration(x,y): 
    new_x = 1 + y
    new_y = 5 - (2*new_x) # Put your code here.
    return [new_x,new_y] # Your return statement should return a list of the form [new_x,new_y]
  

  
  
# Performs n iterations of the Gauss-Seidel method on system (4) with starting estimate (0,0).

def gs2_method(n): 
    x_n=0
    y_n=0
    for i in range(n):
        [x_n,y_n] = gs2_iteration(x_n,y_n) # Put your code here.
    return [x_n,y_n] # Your return statement should return a list of the form [x_n,y_n]
  
  
  
  
# Finds the error of the nth approximation of the solution to system (4) using the Gauss-Seidel method.

def gs2_error(n): 
    x_n = 0
    y_n = 0
    for i in range(n):
        [x_n,y_n] = gs2_iteration(x_n,y_n)
    estimate2 = [x_n,y_n] # Put your code here.
    approx = np.linalg.norm(np.array([2,1])-np.array(estimate2))
    return approx # Put your return statement here.

# The following code will construct your plot of gs2_error for you.  You don't need to change anything in this cell, simply execute it. Consider this one another freebie.

# Note again that you must have a function defined called gs2_error from the previous problem in order for the plot to be created.

vect_gs2_error=np.vectorize(gs2_error)  

n_vals=np.arange(0,50,1)

plt.title('Error of the Gauss-Seidel Method Applied to System 4')
plt.xlabel('Number of iterations')
plt.ylabel('Error')
plt.plot(n_vals,vect_gs2_error(n_vals),'ro')
plt.show()

"""**Problem 10**"""

# Gives one iteration of the Gauss-Seidel method for the final system, applied to the point (x,y,z).

def gs3_iteration(x,y,z): 
    new_x = ((2/5)*y) - ((3/5)*z) - (8/5)
    new_y = -(new_x/4) + z + (102/4)
    new_z = ((1/2)*new_x) + ((1/2)*new_y) - (90/4) # Put your code here.
    return [new_x, new_y, new_z] # Your return statement should return a list of the form [new_x,new_y,new_z]
  

  
  
# Performs n iterations of the Gauss-Seidel method on the final system with starting estimate (0,0,0).

def gs3_method(n): 
    x_n=0
    y_n=0
    z_n=0
    for i in range(n):
        [x_n,y_n,z_n] = gs3_iteration(x_n,y_n,z_n) # Put your code here.
    return [x_n,y_n,z_n] # Your return statement should return a list of the form [x_n,y_n,z_n]

"""**STOP!  BEFORE YOU SUBMIT THIS LAB:**  Go to the "Runtime" menu at the top of this page, and select "Restart and run all".  If any of the cells produce error messages, you will either need to fix the error(s) or delete the code that is causing the error(s).  Then use "Restart and run all" again to see if there are any new errors.  Repeat this until no new error messages show up.

**You are not ready to submit until you are able to select "Restart and run all" without any new error messages showing up.  Your code will not be able to be graded if there are any error messages.**

To submit your lab for grading you must first download it to your compute as .py file.  In the "File" menu select "Download .py".  The resulting file can then be uploaded to https://linearalgebra.byu.edu for grading.
"""