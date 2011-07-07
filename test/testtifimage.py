#!/usr/bin/env python
# -*- coding: utf8 -*-
"""
# Tiff Unit tests

#built on testedfimage
"""

import unittest
import os
import logging
import sys
import gzip, bz2

for idx, opts in enumerate(sys.argv[:]):
    if opts in ["-d", "--debug"]:
        logging.basicConfig(level=logging.DEBUG)
        sys.argv.pop(idx)
try:
    logging.debug("tests loaded from file: %s" % __file__)
except:
    __file__ = os.getcwd()

from utilstest import UtilsTest
from fabio.openimage import openimage


class testtifimage(unittest.TestCase):
    def setUp(self):
        UtilsTest.getimage("pilatus2M.tif.bz2")
        UtilsTest.getimage("pilatus2M.edf.bz2")

        self.tif = os.path.join("testimages",
                                   "pilatus2M.tif")
        self.edf = os.path.join("testimages",
                                     "pilatus2M.edf")
        assert os.path.exists(self.tif)
        assert os.path.exists(self.edf)

    def test1(self):
        """
        Testing pilatus tif bug
        """
        o1 = openimage(self.tif).data
        o2 = openimage(self.edf).data
        self.assertEqual(abs(o1 - o2).max(), 0.0)




def test_suite_all_tiffimage():
    testSuite = unittest.TestSuite()
    testSuite.addTest(testtifimage("test1"))
    return testSuite

if __name__ == '__main__':
    mysuite = test_suite_all_tiffimage()
    runner = unittest.TextTestRunner()
    runner.run(mysuite)
