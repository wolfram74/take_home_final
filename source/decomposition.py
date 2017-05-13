import numpy
import tools
from matplotlib import pyplot

def main():
    x_vals, temperature_vals = tools.data_loader()
    temperature_left = temperature_vals[0]
    stable_gradient = (temperature_vals[-1]-temperature_vals[0])/x_vals[-1]
    stable_temperature = temperature_left + stable_gradient*x_vals
    transient_temperatures = temperature_vals-stable_temperature
    fourier_coefficients = []
    normalized_error =[]
    for i in range(1,101):
        fourier_coefficients.append(tools.fourier_coefficient(i, transient_temperatures, x_vals))
    model = tools.recompose(fourier_coefficients, x_vals)
    residues = transient_temperatures-model
    pyplot.plot(x_vals, transient_temperatures)
    pyplot.plot(x_vals, model)
    pyplot.title('transient temperature vs recomposition')
    pyplot.savefig('comparison.png')
    pyplot.clf()
    pyplot.plot(x_vals, numpy.log(numpy.absolute(residues)))
    pyplot.ylabel('log(abs(residue))')
    pyplot.savefig('log_residues.png' )
    pyplot.clf()
    pyplot.bar(range(1,101), fourier_coefficients)
    pyplot.savefig('bar_spectra.png' )
    pyplot.clf()
    return

if __name__ == "__main__":
    main()
