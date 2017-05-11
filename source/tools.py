import numpy

def fourier_coefficient(k_val, y_vals, x_vals):
    basis = numpy.sin(k_val*numpy.pi*x_vals)
    return 2*numpy.dot(basis, y_vals)/(len(x_vals))

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

def data_loader():
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
    return numpy.array(x_vals)/x_vals[-1], numpy.array(temperature_vals)


def recompose(coefficients, x_vals):
    model = numpy.zeros(len(x_vals))
    for index in range(len(coefficients)):
        model += coefficients[index]*numpy.sin(numpy.pi*(index+1)*x_vals)
    return model

def error_measure(coefficients, y_vals, x_vals):
    model = recompose(coefficients, x_vals)
    absolute_error = numpy.absolute(model-y_vals)
    return numpy.sum(absolute_error)
