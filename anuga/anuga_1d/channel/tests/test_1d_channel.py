import unittest

from math import pi, sqrt, pow

import tempfile
import numpy
from pprint import pprint

from anuga.anuga_1d.config import g, epsilon
from anuga.anuga_1d.base.generic_mesh import uniform_mesh
from anuga.anuga_1d.channel.channel_domain import Domain

# Get gateway to C implementation of flux function for direct testing
from anuga.anuga_1d.channel.channel_domain_ext import compute_fluxes_channel_ext as flux_function

# Define functions for initial quantities
def initial_area(x):
    return 1.4691*width(x)

def width(x):
    x1=(x/1000)*(x/1000)
    x2=x1*(x/1000)
    x3=x2*(x/1000)
    return 10-64*(x1-2*x2+x3)

def bed(x):
    y = numpy.ones(len(x),numpy.float)

    return numpy.where( (x<525) & (x>475),y,0.0)
    
def initial_discharge(x):
    return 20

class Test_1d_Channel(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_init(self):
        N = 200
        domain = Domain(*uniform_mesh(N))

        domain.check_integrity()

        keys = ['area', 'discharge', 'elevation', 'height', 'velocity','width','stage','friction']
        self.assertEqual(set(keys), set(domain.quantities.keys()))

if __name__ == "__main__":
    suite = unittest.makeSuite(Test_1d_Channel, 'test_')
    runner = unittest.TextTestRunner(verbosity=1)
    runner.run(suite)
