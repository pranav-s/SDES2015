#!/usr/bin/env python

from gcd import gcd

def test_coprime():
     assert gcd(10,27)==1
     assert gcd(12,85)==1
     assert gcd(1234,9)==1


def test_multiples():
     assert gcd(27, 54)==27
     assert gcd(100,200)==100
     assert gcd(1234,2468)==1234
     assert gcd(4443,8886)==4443
     assert gcd(18,90)==18


def test_prime():
     assert gcd(17,71)==1
     assert gcd(93, 7)==1
     assert gcd(17,43)==1

def test_random_cases():
     assert gcd(9,21)==3
     assert gcd(12,16)==4
     assert gcd(15,40)==5
     assert gcd(22,99)==11
     assert gcd(123432,78654)==6
     assert gcd(764896, 749784)==8

def test_errors():
     try:
        gcd(5,-3)
     except ValueError:
        assert True
     else :
         assert False  

     try:
        gcd(-5,3)
     except ValueError:
        assert True
     else :
         assert False  

     try:
        gcd(7,'rty')
     except TypeError:
        assert True
     else :
         assert False  

     try:
        gcd('rty',10)
     except TypeError:
        assert True
     else :
         assert False  

     try:
        gcd(7,2.3)
     except TypeError:
        assert True
     else :
         assert False  

     try:
        gcd(2.5,10)
     except TypeError:
        assert True
     else :
         assert False  



