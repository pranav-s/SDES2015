#!/usr/bin/env python

def gcd(a,b) :
      """
        Returns the Greatest Common Divisor of the two integers passed as arguments
        Args:
        a-int
        b-int

      """
      if a<0 or b<0:
          raise ValueError
      if type(a)!=int and type(a)!=long :
          raise TypeError
      if type(b)!=int and type(b)!=long :
          raise TypeError

      while b!=0:
          a,b=b,a%b

      return a

