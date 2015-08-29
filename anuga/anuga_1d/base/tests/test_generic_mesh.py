import unittest

from math import pi, sqrt, pow

import numpy

from anuga.anuga_1d.config import g, epsilon
from anuga.anuga_1d.base.generic_mesh import uniform_mesh

class Test_Uniform_Mesh(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_init_defaults(self):
        N = 4
        expected_points =  [0.0, 0.25, 0.5, 0.75, 1.0]
        expected_bdry = {(0, 0): 'left', (N-1, 1): 'right'}

        points, bdry = uniform_mesh(N)

        numpy.testing.assert_array_equal(points, expected_points)
        self.assertEqual(bdry, expected_bdry)

    def test_init_leftdefault(self):
        N = 4
        x1 = 4.0
        expected_points =  [0.0, 1.0, 2.0, 3.0, 4.0]
        expected_bdry = {(0, 0): 'left', (N-1, 1): 'right'}

        points, bdry = uniform_mesh(N, x_1=x1)

        numpy.testing.assert_array_equal(points, expected_points)
        self.assertEqual(bdry, expected_bdry)

    def test_init_rightdefault(self):
        N = 4
        x0 = -3.0
        expected_points =  [-3.0, -2.0, -1.0, 0.0, 1.0]
        expected_bdry = {(0, 0): 'left', (N-1, 1): 'right'}

        points, bdry = uniform_mesh(N, x_0=x0)

        numpy.testing.assert_array_equal(points, expected_points)
        self.assertEqual(bdry, expected_bdry)

    def test_init_nodefaults(self):
        N = 4
        x0 = 1.0
        x1 = 5.0
        expected_points =  [1.0, 2.0, 3.0, 4.0, 5.0]
        expected_bdry = {(0, 0): 'left', (N-1, 1): 'right'}

        points, bdry = uniform_mesh(N, x0, x1)

        numpy.testing.assert_array_equal(points, expected_points)
        self.assertEqual(bdry, expected_bdry)
        
    def test_init_positivelen(self):
        N = -1

        with self.assertRaises(ValueError):
            uniform_mesh(N)        

if __name__ == "__main__":
    suite = unittest.makeSuite(Test_Uniform_Mesh, 'test_')
    runner = unittest.TextTestRunner(verbosity=1)
    runner.run(suite)
