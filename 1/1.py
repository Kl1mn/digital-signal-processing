import numpy as np
import matplotlib.pyplot as plt
import csv
import math

ampl = 1.2
offs = -0.5
freq = 25634.76563
init_phase = 110
sample_freq = 100000
model_time = 0.1
data1 = []

init_phase = (init_phase / 180) * math.pi


def func(t, ampl, offs, freq, init_phase):
    return (ampl * np.cos(2 * math.pi * freq * t + init_phase) + offs)


def signal_sample_data(data, model_time, sample_freq):
    t = 1 / sample_freq
    while t <= model_time:
        k = {}
        k["t"] = "%.5f" % t
        k["U"] = "%.8f" % func(t, ampl, offs, freq, init_phase)
        data.append(k)
        t += 1 / sample_freq
    return data


def avarage_count(data):
    value = 0.0
    for i in data:
        value += float(i["U"])
    return value / len(data)


def graph1():
    x1 = np.arange(0, 0.1, 0.0000001)
    x2 = np.arange(0.050, 0.051, 0.0000001)

    plt.plot(x1, func(x1, ampl, offs, freq, init_phase))
    plt.xlabel('t, c')
    plt.ylabel('U, В')
    plt.grid(True)
    plt.title('Full signal')
    plt.savefig(fname='graphics/1', fmt='png')
    plt.close()

    plt.plot(x2, func(x2, ampl, offs, freq, init_phase))
    plt.xlabel('t, c')
    plt.ylabel('U, В')
    plt.grid(True)
    plt.title('Part of signal')
    plt.savefig(fname='graphics/2', fmt='png')
    plt.close()



if __name__ == "__main__":
    with open("12_signal.csv", 'w', newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["t", "U"])
        writer.writeheader()
        writer.writerows(signal_sample_data(data1, model_time, sample_freq))

    graph1()

    print(f'Начальная фаза {"%.6f" % init_phase}, рад')
    print(f'Количество отсчетов для моделирования {len(data1)}')
    print(f'Среднее значений сигнала {"%.6f" % avarage_count(data1)}, В')
    print(f'Частота сигнала с учетом частоты дискретизации {"%.6f" % (freq / sample_freq)}')