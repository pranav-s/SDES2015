#!/usr/bin/env python

import text_plot
import unittest

class TestTextPlotter(unittest.TestCase):

     def setUp(self):
         self.plotter=text_plot.TextScatterPlot()

     def test_rescale(self):
         self.assertEqual(self.plotter.rescale([1,3,5,7,9],5),[0,1,3,4,5])
         self.assertEqual(self.plotter.rescale([10,10,10,10,10],8),[4,4,4,4,4])

     def test_convert_to_list(self):
         self.assertEqual(self.plotter.convert_to_list((1,2,2,3,5)),[1,2,2,3,5])
         self.assertEqual(self.plotter.convert_to_list([1,2,2,3,7]),[1,2,2,3,7])
         
     def test_make_list(self):
         self.assertEqual(text_plot.make_list(1,5,5),[1,2.0,3.0,4.0,5.0])
         self.assertEqual(text_plot.make_list(5,1,3),[1,3.0,5.0])       

     def test_class_function_errors(self):
         a=[1,2,3]
         self.assertRaises(TypeError,self.plotter.rescale,(a,-2))
         self.assertRaises(TypeError,self.plotter.rescale,(a,2.3))
         self.assertRaises(ValueError,lambda: self.plotter.terminal_resize(-24,80))
         self.assertRaises(TypeError,lambda: self.plotter.terminal_resize(53,43.5))
         self.assertRaises(TypeError,self.plotter.convert_to_list,('dft'))
         self.assertRaises(TypeError,self.plotter.convert_to_list,(2))
         
     def test_sine_printing_function_errors(self):
         self.assertRaises(TypeError,lambda: text_plot.make_list(2,5,2.3))
         self.assertRaises(ValueError,lambda: text_plot.make_list(2,5,-2))
         self.assertRaises(TypeError,text_plot.make_list,(2,5,'s'))
         self.assertRaises(text_plot.IntervalLengthError,lambda: text_plot.make_list(5,5,2))
         
     def tearDown(self):
         del self.plotter
          
if __name__=='__main__':
     unittest.main()
