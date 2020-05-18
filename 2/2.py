import numpy as np
import csv
import matplotlib.pyplot as plt

sample_freq = 100000
model_time = 0.1

data2 = []

np.random.seed(1002012012)


def noise_sample_data(data):
    t = 1 / sample_freq
    while t <= model_time:
        k = {}
        k["t"] = "%.5f" % t
        k["U"] = "%.8f" % np.random.normal()
        data.append(k)
        t += 1 / sample_freq
    return data


def avarage_noise(data):
    value = 0.0
    for i in data:
        value += float(i["U"])
    return value / len(data)


def disp(data):
    a = avarage_noise(data)
    b = 0.0
    for i in data:
        b += (float(i["U"]) - a) ** 2
    return b / (len(data) - 1)


def graph2():
    x1 = []
    x2 = []
    for i in data2:
        if float(i["t"]) >= 0.05000 and float(i["t"]) <= 0.055:
            x1.append(float(i["t"]))
            x2.append(float(i["U"]))
    plt.scatter(x1, x2)
    # plt.axis([0.034992, 0.04005, -3.55, 3.55])
    plt.title('Part of noise')
    plt.xlabel('t, c')
    plt.ylabel('U, В')
    plt.grid(True)
    plt.savefig(fname='graphics/1', fmt='png')
    plt.close()


if __name__ == "__main__":
    with open("12_noise.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["t", "U"])
        writer.writeheader()
        writer.writerows(noise_sample_data(data2))

    graph2()

    print(f'Среднее значение шума по выборке {"%.6f" % avarage_noise(data2)}, В')
    print(f'Дисперсия шума по выборке  {"%.6f" % disp(data2)}')
