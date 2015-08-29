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

class Test_1d_Channel(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_init(self):
        N = 10
        domain = Domain(*uniform_mesh(N))

        domain.check_integrity()

        expectedkeys = ['area', 'discharge', 'elevation', 'height', 'velocity','width','stage','friction']
        expected_conserved_quantities = [0, 0]

        self.assertItemsEqual(expectedkeys, domain.quantities.keys())

        self.assertItemsEqual(domain.get_conserved_quantities(0), expected_conserved_quantities)

if __name__ == "__main__":
    suite = unittest.makeSuite(Test_1d_Channel, 'test_')
    runner = unittest.TextTestRunner(verbosity=1)
    runner.run(suite)
