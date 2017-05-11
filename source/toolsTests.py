import unittest
import numpy
import tools

pi = numpy.pi

class TestTools(unittest.TestCase):
    def test_fourier_coefficients(self):
        x_vals = numpy.linspace(0, 1, 100001)
        true_k3 = 5.0
        true_k7 = 0.2
        y_vals = true_k3*numpy.sin(3*pi*x_vals)+true_k7*numpy.sin(7*pi*x_vals)
        k3 = tools.fourier_coefficient(3, y_vals)
        k7 = tools.fourier_coefficient(7, y_vals)

        self.assertLess(abs(true_k3-k3),(10**-6))
        self.assertLess(abs(true_k7-k7),(10**-6))
        return

    def test_du_fort_frankel(self):
        self.assertEqual(0,0)
        return
