#!/usr/bin/env python

"""
A text based plotter
Takes two lists/tuples x & y and prints a sequence of stars on the terminal screen

Args
x- list/tuple
y- list/tuple

Default behaviour on executing the file from terminal is to print sin(x). The terminal size is not changed.

Functions provided:

make_list(lower,upper,size): Returns a list of length=size by discretizing all values between upper and lower

make_sin_list(): Creates 2 lists a,b for domain and range of sin x. Return the two as lists

terminal_size(): Returns the number of rows and columns on the terminal screen as integers

plot(x,y,r,c): Takes 2 lists/tuples and prints the corresponding plot on the terminal with x along the x axis and y along the y axis. Takes optional input of rows and columns to resize the screen(ie the terminal window)which is otherwise set to a default value of 24 rows and 80 columns.

"""

import os
import sys
import math

class InputListLengthError(Exception):
     #Throws an error if both lists are not of the same length
     pass

class IntervalLengthError(Exception):
     #Throws an error if upper and lower limit of make_list have the same value
     pass

class TextScatterPlot(object):
     """
        Functions provided with this class:
  
           terminal_resize(r,c): Resizes the terminal based on given input value of rows and columns

           read_terminal_size(): Returns the number of rows and columns in the current terminal. Returns 2 strings
  
           rescale(n, size): Scales each value of the list n to an integer value corresponding to a value on the terminal screen

           plot_print(x,y,r): Prints a star in column x, row y and takes the number of rows on the terminal screen as a parameter
  
           convert_to_list(p): Converts the input to a list in case it is a tuple and leaves it unchanged if it is a list.Else returns an error


     """

     def convert_to_list(self,p):
          if type(p)==list:
              return p
          if type(p)==tuple:
              z=[]
              for i in p:
                 z.append(i)
              return z
          else:
              raise TypeError
     
     def rescale(self,n,size):
          if type(size)!=int and type(size)!= long:
             raise TypeError
          if size<=0:
             raise ValueError
          if type(n)!=list:
             raise TypeError
          minima=min(n)
          maxima=max(n)
          l=maxima-minima
          m=[]
          if l==0:  #If the list contains constant elements then show a line in the centre of the screen
              for i in range(len(n)):
                  m.append(size/2) 
              return m         
          for i in range(len(n)):
              m.append(int(round((n[i]-minima)*float(size)/l)))
          return m

     def plot_print(self,x1,y1,r):
          if type(r)!=int and type(r)!= long:
              raise TypeError
          if x1==0:
              x1=1
          if y1==r:
              y1=r-1
          #Changing zero co-ordinate to 1 in order to print to screen
          print("\033["+str(y1)+";"+str(x1)+"H*")

     def terminal_resize(self,r,c):
          if type(r)!=int or type(c)!=int:
             raise TypeError
          if r<0 or c<0:
             raise ValueError
          sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=r, cols=c)) # C command to resize terminal

     def read_terminal_size(self):
          rows, columns = os.popen('stty size', 'r').read().split()
          return rows, columns
          
     
def plot(x,y,r=24,c=80):
     plotter=TextScatterPlot()
     x=plotter.convert_to_list(x)
     y=plotter.convert_to_list(y)
     if len(x)!=len(y):
         msg="The lengths of the input arrays len(x)=%d and len(y)=%d don't match"%(len(x),len(y))
         raise InputListLengthError(msg)
     
     x=plotter.rescale(x,c)
     y=plotter.rescale(y,r)
     plotter.terminal_resize(r,c)
     os.system('clear') # Clears the screen before printing
     for i in range(len(x)):
         plotter.plot_print(x[i],r-y[i],r)

def make_list(lower,upper,size): # Essentially performs the role of linspace in matplotlib
     if type(size)!=int and type(size)!= long:
        raise TypeError
     if type(upper)!=int and type(upper)!=long and type(upper)!=float:
        raise TypeError
     if type(lower)!=int and type(lower)!=long and type(lower)!=float:
        raise TypeError   
     if size<0:
        raise ValueError     
     if upper<lower:
         upper,lower=lower,upper
     if upper==lower:
         raise IntervalLengthError("The interval length is zero")
     indep_var=[lower]
     delta=(upper-lower)/(float(size)-1)
     for i in range(1,size):
          indep_var.append(indep_var[i-1]+delta)
     return indep_var

def terminal_size():
     plotter=TextScatterPlot()
     r,c=plotter.read_terminal_size()
     r=int(r)
     c=int(c)
     return r,c
     
def make_sin_list():
     r,c=terminal_size()
     a=make_list(0,2*math.pi,c)
     b=[]
     for i in a:
        b.append(math.sin(i))
     return a,b
     
def main():
     r,c=terminal_size()
     plotter=TextScatterPlot()
     indep_var,dep_var = make_sin_list()
     indep_var= plotter.rescale(indep_var,c)
     dep_var= plotter.rescale(dep_var,r)
     plot(indep_var,dep_var,r,c)

if __name__=='__main__': #Prints the sine function to the screen when called from the terminal
     main()
