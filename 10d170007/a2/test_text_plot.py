#!/usr/bin/env python

from text_plot import find_min,find_max, rescale, terminal_resize, read_terminal_size, make_list, convert_to_list


def test_rescale():
     pass

def test_sort():
     pass

def test_convert_to_list():
     assert convert_to_list((1,2,2,3,5))==[1,2,2,3,5]
     assert convert_to_list([1,2,2,3,7])==[1,2,2,3,7]

def test_find_min():
    assert find_min([1,7,6,4,9,2,123])==1
    assert find_min([23,54,35,546,123,1])==1
    assert find_min([34,54,127,56,1232,43])==34


def test_find_max():
    assert find_max([1,7,6,4,9,2,123])==123
    assert find_max([23,54,35,546,123,1])==546
    assert find_max([34,54,127,56,1232,43])==1232

def test_errors():
     try :
        a=[]
        rescale(a,-2)
     except ValueError:
        assert True
     else:
        assert False

     try :
        a=[]
        rescale(a,2.3)
     except TypeError:
        assert True
     else:
        assert False

     try :
          make_list(2,5,-2)
     except ValueError:
        assert True
     else:
        assert False
     
     try :
          terminal_resize(20,-53)
     except ValueError:
        assert True
     else:
        assert False
     
     try :
          terminal_resize(43.5,53)
     except TypeError:
        assert True
     else:
        assert False
          
     try :
          convert_to_list('dft')
     except TypeError:
        assert True
     else:
        assert False
