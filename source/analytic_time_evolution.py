import numpy
import tools
from matplotlib import pyplot
import time

params = {
    'kappa': 1.0,
    'steps': 10000,
    'foldings': 0.02,
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

    evolution = numpy.array([tools.recompose(fourier_coefficients, x_vals)])
    times = numpy.array([0])

    # fig = pyplot.plot(x_vals, evolution[-1])
    # axes = pyplot.gca()
    # axes.set_ylim([-40,30])
    # pyplot.savefig('step_%05d.png' % 0)
    # pyplot.clf()

    start = time.time()
    for i in range(1, params['steps']+1):
        fourier_coefficients *= decay_rates
        if i%100==0:
            evolution = numpy.append(evolution, [tools.recompose(fourier_coefficients, x_vals)], axis=0)
            # fig = pyplot.plot(x_vals, evolution[-1])
            # axes = pyplot.gca()
            # axes.set_ylim([-40,30])
            # pyplot.savefig('step_%05d_t%f.png' % (i, i*del_t))
            # pyplot.clf()
            times = numpy.append(times, i*del_t)

    end = time.time()
    print(end-start)

    mesh_x, mesh_y = numpy.meshgrid(x_vals, times)
    pyplot.figure()
    contour = pyplot.contour(mesh_x, mesh_y, evolution)
    pyplot.clabel(contour, inline=1, fontize=10)
    pyplot.title('heat evolution till %0.3f e-foldings' % params['foldings'])
    pyplot.savefig('analytic_contour.png' )
    pyplot.clf()
    return

if __name__ == "__main__":
    main()
