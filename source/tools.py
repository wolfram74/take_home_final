import numpy
from functools import reduce

def fourier_coefficient(k_val, y_vals, x_vals):
    del_x = x_vals[1]
    indices = numpy.arange(0, len(x_vals))
    #result of integrating over narrow band discussed in section 2
    basis = (
        numpy.cos(k_val*numpy.pi*indices*del_x)
        -numpy.cos(k_val*numpy.pi*(indices+1)*del_x)
        )/(k_val*numpy.pi)
    return 2*numpy.dot(basis, y_vals)

def spectrum(y_vals, x_vals, order):
    coefficients = []
    for i in range(1,order+1):
        coefficients.append(fourier_coefficient(i, y_vals, x_vals))
    return numpy.array(coefficients)

def recompose(coefficients, x_vals):
    model = numpy.zeros(len(x_vals))
    indices = numpy.arange(0, len(x_vals))
    for index in range(len(coefficients)):
        #index+1 because python is 0 indexed
        model += coefficients[index]*numpy.sin(numpy.pi*(index+1)*x_vals)
    return model


def du_fort_frankel(y_vals, previous_y_vals, kappa, del_t, del_x):
    scale = kappa*del_t/(del_x**2)
    denom = (1+scale)
    numer = y_vals+scale*(
        numpy.roll(y_vals,1)
        + numpy.roll(y_vals,-1)
        - previous_y_vals
        )
    next_y_vals = numer/denom
    next_y_vals[0] = y_vals[0]
    next_y_vals[-1] = y_vals[-1]
    return next_y_vals

def data_loader(scale = 1.0):
    x_file = open('../data_set_peter_final_x.txt', 'r')
    x_vals = []
    for line in x_file:
        x_vals.append(float(line))
    print(len(x_vals))
    temperature_file = open('../data_set_peter_final_t.txt', 'r')
    temperature_vals = []
    for line in temperature_file:
        temperature_vals.append(float(line))
    print(len(temperature_vals))
    # pass
    # if normalized:

    return numpy.array(x_vals)*(scale/x_vals[-1]), numpy.array(temperature_vals)
    # return numpy.array(x_vals), numpy.array(temperature_vals)



def error_measure(coefficients, y_vals, x_vals):
    model = recompose(coefficients, x_vals)
    absolute_error = numpy.absolute(model-y_vals)
    return numpy.sum(absolute_error)
