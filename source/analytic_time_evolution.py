import numpy
import tools
from matplotlib import pyplot
import time

params = {
    'kappa': 1.0,
    'steps': 10000,
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
    fourier_coefficients = numpy.array(fourier_coefficients)
    decay_rates = numpy.exp(-numpy.pi**2*indices**2*params['kappa']*del_t)
    print(indices[0:5], decay_rates[0:5])
    evolution = numpy.array([tools.recompose(fourier_coefficients, x_vals)])
    times = numpy.linspace(0, params['steps']*del_t, params['steps'])
    print(params['steps']/100)
    start = time.time()
    for i in range(1, params['steps']/100):
        fourier_coefficients *= decay_rates
        evolution = numpy.append(evolution, [tools.recompose(fourier_coefficients, x_vals)], axis=0)
        if i%100==0:
            print i
    end = time.time()
    print(end-start)
    # mesh_x, mesh_y = numpy.meshgrid(x_vals, times)
    # print(evolution.shape, mesh_x.shape)
    # pyplot.figure()
    # contour = pyplot.contour(mesh_x, mesh_y, evolution)
    # pyplot.clabel(contour, inline=1, fontize=10)
    # pyplot.title('heat evolution')
    # pyplot.show()
    return

if __name__ == "__main__":
    main()
