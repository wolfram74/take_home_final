import numpy
import tools
from matplotlib import pyplot

params = {
    'kappa': 1.0,
    'steps': 100000,
    'foldings': 5.0,
    'modes':100
}

def main():
    del_t = (params['foldings'])/(params['kappa']*params['steps']*numpy.pi**2)
    print('del_t %f' % del_t )
    x_vals, temperature_vals = tools.data_loader()
    temperature_left = temperature_vals[0]
    stable_gradient = (temperature_vals[-1]-temperature_vals[0])/x_vals[-1]
    stable_temperature = temperature_left + stable_gradient*x_vals

    transient_temperatures = temperature_vals-stable_temperature
    fourier_coefficients = []
    indices = numpy.arange(1, params['modes']+1)
    for i in range(1,params['modes']+1):
        fourier_coefficients.append(tools.fourier_coefficient(i, transient_temperatures, x_vals))
    decay_rates = numpy.exp(-numpy.pi**2*indices**2*params['kappa']*del_t)
    print(indices[0:5], decay_rates[0:5])
    return

if __name__ == "__main__":
    main()
