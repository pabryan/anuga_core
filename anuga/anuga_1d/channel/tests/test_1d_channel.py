#!/usr/bin/env python

import unittest, os, time
import os.path
from math import pi, sqrt, pow
import tempfile
import numpy
from pprint import pprint

from anuga.anuga_1d.channel.channel_domain import *
from anuga.anuga_1d.config import g, epsilon
from anuga.anuga_1d.base.generic_mesh import uniform_mesh
from anuga.anuga_1d.channel.channel_domain import Domain

from anuga.utilities.system_tools import get_pathname_from_package

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

    def test_channel_domain(self):
        # Set final time and yield time for simulation
        finaltime = 50.0
        yieldstep = 10.0

        # Length of channel (m)
        L = 1000.0   
        # Define the number of cells
        N = 200

        # Create domain with centroid points as defined above
        domain = Domain(*uniform_mesh(N))

        # Set initial values of quantities - default to zero
        domain.set_quantity('area', initial_area)
        domain.set_quantity('width',width)
        domain.set_quantity('elevation',bed)
        domain.set_quantity('discharge',initial_discharge)

        # Set boundry type, order, timestepping method and limiter
        Bd = Dirichlet_boundary([14,20,0,1.4,20/14,9,1.4])
        domain.set_boundary({'left': Bd , 'right' : Bd })

        domain.order = 2
        domain.set_timestepping_method('rk2')
        domain.set_CFL(1.0)
        domain.set_limiter("vanleer")

        for t in domain.evolve(yieldstep = yieldstep, finaltime = finaltime):
            domain.write_time()


if __name__ == "__main__":
    suite = unittest.makeSuite(Test_1d_Channel, 'test_')
    runner = unittest.TextTestRunner(verbosity=1)
    runner.run(suite)
