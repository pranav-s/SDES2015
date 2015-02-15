#!/usr/bin/env python

"""
A text based plotter
Takes two lists x & y and prints a sequence of stars on the terminal screen

Args
x- list
y- list

Functions:

terminal_resize(r,c): Resizes the terminal based on given input value of rows and columns

read_terminal_size(): Returns the number of rows and columns in the current terminal. Returns 2 strings

find_min(z): Finds and returns the smallest element in a list z

find_max(z): Finds and returns the largest element in a list z

make_list(lower,upper,size): Returns a list of length=size by discretizing all values between upper and lower

make_sin_list(): Create 2 lists a,b for domain and range of sin x, return the two as lists

rescale(n, size): scales each value of the list to an integer value corresponding to a value on the terminal screen(row or column). Returns a different list from the one provided to it

sort(x,y): sort list x and then swap y accordingly to take care of the possibility that x may not be a sorted list

plot_print(x,y): print a star in row x, column y

plot(x,y): Takes 2 lists and prints the corresponding plot on the terminal

"""

import os
import sys
import math

def plot(x,y):
     x=convert_to_list(x)
     y=convert_to_list(y)
     if len(x)!=len(y):
         print 'Incorrect Input data'
         return
     sort(x,y)
     r,c=read_terminal_size()
     r=int(r)
     c=int(c)
     x=rescale(x,c)
     y=rescale(y,r)
     os.system('clear') # Clears the screen before printing
     for i in range(len(x)):
         plot_print(x[i],r-y[i],r)

def sort(x,y):
     if len(x)!=len(y):
         return
     for i in range(len(x)-1):
         min=x[i]
         index=i
         for j in range(i+1,len(x)):
             
             if(x[j]<min):
                   min=x[j]
                   index=j
         
         if index!=i:
             x[i],x[index]=x[index],x[i]
             y[i],y[index]=y[index],y[i]

def convert_to_list(p):
     if type(p)==list:
         return p
     if type(p)==tuple:
         z=[]
         for i in p:
            z.append(i)
         return z
     else:
         raise TypeError

def rescale(n,size):
     if type(size)!=int and type(size)!= long:
        raise TypeError
     if size<0:
        raise ValueError
     minima=find_min(n)
     maxima=find_max(n)
     m=[]
     for i in range(len(n)):
         m.append(int(round((n[i]-minima)*size/maxima)))
     return m


def find_min(z):
     minimum=z[0]
     for i in z:
        if i<minimum:
          minimum=i
     return minimum 

def find_max(z):
     maximum=z[0]
     for i in z:
        if i>maximum:
          maximum=i
     return maximum 

def plot_print(x1,y1,r):
     if type(r)!=int and type(r)!= long:
        raise TypeError
     if x1==0:
        x1=1
     if y1==r:
        y1=r-1
     #Changing zero co-ordinate to 1 in order to print to screen
     print("\033["+str(y1)+";"+str(x1)+"H*")


def terminal_resize(r,c):
     if type(r)!=int and type(r)!= long:
        raise TypeError
     if type(c)!=int and type(c)!= long:
        raise TypeError
     if r<0 or c<0:
        raise ValueError

     sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=r, cols=c)) # C command to resize terminal

def read_terminal_size():
     rows, columns = os.popen('stty size', 'r').read().split()
     return rows, columns

def make_list(lower,upper,size):
     if type(size)!=int and type(size)!= long:
        raise TypeError
     if size<0:
        raise ValueError
     
     if upper<lower:
         upper,lower=lower,upper
     if upper==lower:
         return
     indep_var=[lower]
     delta=(upper-lower)/(size-1)
     for i in range(1,size):
          indep_var.append(indep_var[i-1]+delta)
     return indep_var

def make_sin_list():
     r,c=read_terminal_size()
     r=int(r)
     c=int(c)
     a=make_list(0,2*math.pi,c)
     b=[]
     for i in a:
        b.append(math.sin(i))
     return a,b

if __name__=='__main__': #Prints the sine function to the screen when called from the terminal
     r,c=read_terminal_size()
     r=int(r)
     c=int(c)
     indep_var,dep_var = make_sin_list()
     indep_var= rescale(indep_var, c)
     dep_var= rescale(dep_var, r)
     plot(indep_var,dep_var)
