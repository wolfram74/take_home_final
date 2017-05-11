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
    # pyplot.plot(x_vals, temperature_vals)
    # pyplot.plot(x_vals, transient_temperatures)
    # pyplot.show()
    fourier_coefficients = []
    for i in range(1,100):
        fourier_coefficients.append(tools.fourier_coefficient(i, transient_temperatures, x_vals))
    model = tools.recompose(fourier_coefficients, x_vals)
    # print(i)
    print(tools.error_measure(fourier_coefficients, transient_temperatures,x_vals))
    print(tools.error_measure(fourier_coefficients, transient_temperatures,x_vals)/len(x_vals))
    pyplot.plot(x_vals, transient_temperatures)
    pyplot.plot(x_vals, model)
    pyplot.show()


    return

if __name__ == "__main__":
    main()
