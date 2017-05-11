import unittest
import numpy
import tools
import copy

pi = numpy.pi

class TestTools(unittest.TestCase):
    def test_fourier_coefficients(self):
        x_vals = numpy.linspace(0, 1, 100001)
        true_k3 = 5.0
        true_k7 = 0.2
        y_vals = true_k3*numpy.sin(3*pi*x_vals)+true_k7*numpy.sin(7*pi*x_vals)
        k3 = tools.fourier_coefficient(3, y_vals, x_vals)
        k7 = tools.fourier_coefficient(7, y_vals, x_vals)
        print(k3, k7)
        self.assertLess(abs(true_k3-k3),(10**-4))
        self.assertLess(abs(true_k7-k7),(10**-4))
        return

    def test_du_fort_frankel(self):
        x_vals = numpy.linspace(0,1, 7)
        y_vals = numpy.array([2.0, 4.0, 3.5, 2.1, 9.1, 5.3, 4.0])
        previous_y_vals = copy.copy(y_vals)
        del_t = 0.01
        del_x = 1.0/7.0
        steps = 1000
        kappa = 0.1
        for step in range(steps):
            next_y_vals = tools.du_fort_frankel(
                y_vals, previous_y_vals,
                kappa, del_t, del_x
                )
            previous_y_vals = y_vals
            y_vals = next_y_vals
        self.assertLess(abs(next_y_vals[3]-3.0),10**-4)
        return
