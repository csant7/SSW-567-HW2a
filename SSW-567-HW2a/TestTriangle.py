# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')
        self.assertEqual(classifyTriangle(5,3,4),'Not Right','Should Fail')
        self.asserEqual(classifyTriangle(9, 12, 15), 'Right', '9, 12, 15 is a Right triangle')
    
    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')
        self.assertEqual(classifyTriangle(3,3,3),'Equilateral','3,3,3 should be Equilateral')
        self.assertEqual(classifyTriangle(4,4,5),'Not Equilateral','Should Fail')

    def testIsoscelesTriangles(self):
        self.assertEqual(classifyTriangle(2,2,4),'Isosceles','2,2,4 should be Isosceles')
        self.assertEqual(classifyTriangle(5,5,8),'Isosceles','5,5,8 should be Isosceles')
        self.assertEqual(classifyTriangle(1,2,5),'Not Isosceles','Should Fail')
         
    def testScaleneTriangles(self):
        self.assertEqual(classifyTriangle(1,2,3),'Scalene','1,1,1 should be Scalene')
        self.assertEqual(classifyTriangle(5,7,12),'Scalene','5,7,12 should be Scalene')
        self.assertEqual(classifyTriangle(4,4,6),'Not Scalene','Should Fail')
        

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

