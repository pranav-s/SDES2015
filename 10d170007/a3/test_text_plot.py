#!/usr/bin/env python

import text_plot
import unittest

class TestTextPlotter(unittest.TestCase):

     def setUp(self):
         plotter=text_plot.TextScatterPlot()
         a=[1,2,3]

     def test_rescale(self):
         plotter=text_plot.TextScatterPlot()
         self.assertEqual(plotter.rescale([1,3,5,7,9],5),[0,1,2,3,5])
         self.assertEqual(plotter.rescale([10,10,10,10,10],8),[4,4,4,4,4])

     def test_convert_to_list(self):
         plotter=text_plot.TextScatterPlot()
         self.assertEqual(plotter.convert_to_list((1,2,2,3,5)),[1,2,2,3,5])
         self.assertEqual(plotter.convert_to_list([1,2,2,3,7]),[1,2,2,3,7])

     def test_errors(self):
         plotter=text_plot.TextScatterPlot()
         a=[1,2,3]
         self.assertRaises(TypeError,plotter.rescale,(a,-2))
         self.assertRaises(TypeError,plotter.rescale,(a,2.3))
         self.assertRaises(ValueError,plotter.terminal_resize,(plotter,20,-53))
         self.assertRaises(ValueError,plotter.terminal_resize,(plotter,43.5,53))
         self.assertRaises(TypeError,plotter.convert_to_list,(plotter, 'dft'))
         self.assertRaises(TypeError,plotter.convert_to_list,(2))
         self.assertRaises(ValueError,text_plot.make_list,(2 , 5 , 2.3))
         self.assertRaises(ValueError,text_plot.make_list,(2,5,-2))
         self.assertRaises(ValueError,text_plot.make_list,(2,5,'s'))
         self.assertRaises(IntervalLengthError,text_plot.make_list,(5,5,2))
    
     #def tearDown(self):
      #    del plotter
          
if __name__=='__main__':
     unittest.main()
