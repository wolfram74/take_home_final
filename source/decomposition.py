import numpy
import tools
from matplotlib import pyplot

def main():
    x_vals, temperature_vals = tools.data_loader()
    temperature_left = temperature_vals[0]
    stable_gradient = (temperature_vals[-1]-temperature_vals[0])/x_vals[-1]
    print(temperature_left, stable_gradient)
    stable_temperature = temperature_left + stable_gradient*x_vals
    print(stable_temperature[0], stable_temperature[-1])
    print(x_vals[0], x_vals[-1])
    transient_temperatures = temperature_vals-stable_temperature
    fourier_coefficients = []
    normalized_error =[]
    for i in range(1,51):
        fourier_coefficients.append(tools.fourier_coefficient(i, transient_temperatures, x_vals))
    model = tools.recompose(fourier_coefficients, x_vals)
    residues = transient_temperatures-model
    pyplot.plot(x_vals, transient_temperatures)
    pyplot.plot(x_vals, model)
    pyplot.plot(x_vals, numpy.absolute(residues))
    pyplot.show()
    # pyplot.plot(range(1,101), fourier_coefficients)
    # pyplot.show()
    # pyplot.plot(range(1,101), numpy.absolute(fourier_coefficients))
    # pyplot.show()
    return

if __name__ == "__main__":
    main()
