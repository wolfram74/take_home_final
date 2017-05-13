import numpy
import tools
from matplotlib import pyplot
import time

params = {
    'kappa': 1.0,
    'steps': 100000,
    'foldings': 1.0,
    'modes':100
}

def main():
    del_t = (params['foldings'])/(
        params['kappa']*params['steps']*numpy.pi**2
        )
    x_vals, temperature_vals = tools.data_loader( scale=1)
    print('del_t %f' % del_t )
    print(params['kappa'], del_t, (x_vals[1]**2))
    print(params['kappa']*del_t/(x_vals[1]**2))
    print('scale %f' % (params['kappa']*del_t/(x_vals[1]**2)))
    temperature_left = temperature_vals[0]
    stable_gradient = (temperature_vals[-1]-temperature_vals[0])/x_vals[-1]
    stable_temperature = temperature_left + stable_gradient*x_vals

    transient_temperatures = temperature_vals-stable_temperature
    # transient_temperatures = temperature_vals#-stable_temperature
    time_slices = [transient_temperatures, transient_temperatures]
    start = time.time()
    record = open(
        'steps_%d_foldings_%f_kappa_%f.txt'%(
            params['steps'],
            params['foldings'],
            params['kappa']),
        'w')
    for time_i in range(1, params['steps']+1):
        time_slices.append(tools.du_fort_frankel(
            time_slices[1],time_slices[0],
            params['kappa'], del_t, x_vals[1]
            ))
        time_slices.pop(0)
        if time_i % 500 == 0:
            components = tools.spectrum(time_slices[0], x_vals, 100)
            record.write("%f:%s\n" % (time_i*del_t, ','.join(map(str, components))) )
            print(time_i)
            # fig = pyplot.plot(x_vals, time_slices[0])
            # axes = pyplot.gca()
            # axes.set_ylim([-40,30]) #transients only
            # # axes.set_ylim([40,110]) #original values
            # pyplot.savefig('step_%d_t_%f.png' % (time_i, time_i*del_t))
            # pyplot.clf()
    end = time.time()
    print(end-start)
    # pyplot.plot(x_vals, time_slices[0])
    # # pyplot.plot(x_vals, time_slices[10])
    # pyplot.plot(x_vals, time_slices[params['steps']/4])
    # pyplot.plot(x_vals, time_slices[params['steps']/2])
    # pyplot.plot(x_vals, time_slices[-1])
    # pyplot.show()
    return

if __name__ == "__main__":
    main()
