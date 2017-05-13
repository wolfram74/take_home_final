import numpy
import tools
from matplotlib import pyplot
import time

def load_spectra():
    output = {}
    saved_spectra = open('steps_100000_foldings_1.000000_kappa_1.000000.txt', 'r')
    for line in saved_spectra:
        time_stamp = float(line.split(':')[0])
        string_spectra = line.split(':')[1]
        spectra = [ float(mode) for mode in string_spectra.split(',')]
        output[time_stamp] = spectra
    return output

def mode_curve_extractor(times, spectra_series, mode):
    output = []
    for time in times:
        output.append(spectra_series[time][mode-1])
    return output

def main():
    estimated_spectra = load_spectra()

    x_vals, temperature_vals = tools.data_loader()
    temperature_left = temperature_vals[0]
    stable_gradient = (temperature_vals[-1]-temperature_vals[0])/x_vals[-1]
    stable_temperature = temperature_left + stable_gradient*x_vals
    transient_temperatures = temperature_vals-stable_temperature
    estimated_spectra[0.0] = tools.spectrum(transient_temperatures,x_vals, 100)
    times = sorted(estimated_spectra.keys())
    for i in range(1, 100):
        mode = mode_curve_extractor(times, estimated_spectra, i)
        pyplot.plot(times, mode)
        pyplot.savefig('mode_%d.png'% i )
        pyplot.clf()
    return

if __name__ == "__main__":
    main()
