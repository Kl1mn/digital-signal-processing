import numpy as np
import csv
import matplotlib.pyplot as plt


def read_my_csv(data, filename):
    with open(filename, "r") as f:
        reader = csv.DictReader(f, delimiter=',')
        for line in reader:
            k = {}
            k["t"] = float(line["t"])
            k["U"] = float(line["U"])
            data.append(k)
    return data

freq1 = np.fft.fftfreq(10000, 0.00001)

for i in range(len(freq1)):
    if freq1[i] == 25630:
        print(f"Номер отсчета, соответствующий положительной частоте заданного сигнала для 10000 отсчетов: {i}")
        a1 = i
    if freq1[i] == -25630:
        print(f"Номер отсчета, соответствующий отрицательной частоте заданного сигнала для 10000 отсчетов: {i}")
        b1 = i

data_signal = []
data_noise = []
data_mix1 = []

data_signal = np.fft.fft(list([(i["U"]) for i in read_my_csv(data_signal, "../1/12_signal.csv")]))
data_noise = np.fft.fft(list([(i["U"]) for i in read_my_csv(data_noise, "../2/12_noise.csv")]))
data_mix1 = np.fft.fft(list([(i["U"]) for i in read_my_csv(data_mix1, "../3/12_sn.csv")]))


power_signal1 = np.abs(data_mix1[a1]) ** 2 + np.abs(data_mix1[a1+1]) ** 2 + np.abs(data_mix1[b1]) ** 2 + np.abs(data_mix1[b1-1]) ** 2
power_noise1 = sum([i ** 2 for i in np.abs(data_mix1)]) - power_signal1
snr1 = 10*np.log10(power_signal1 / power_noise1)
print(f"Практическое отношение SNR1: {snr1}")




freq2 = np.fft.fftfreq(8192, 0.00001)

for i in range(len(freq2)):
    if round(freq2[i]) == 25635:
        print(f"Номер отсчета, соответствующий положительной частоте заданного сигнала для 8192 отсчетов: {i}")
        a2 = i
    if round(freq2[i]) == -25635:
        print(f"Номер отсчета, соответствующий отрицательной частоте заданного сигнала для 8192 отсчетов: {i}")
        b2 = i

data_mix2 = []
data_mix2 = [(i["U"]) for i in read_my_csv(data_mix2, "../3/12_sn.csv")]
data_mix2 = np.fft.fft(data_mix2[:8192])

power_signal2 = np.abs(data_mix2[a2]) ** 2 +  np.abs(data_mix2[b2]) ** 2
power_noise2 = sum([i ** 2 for i in np.abs(data_mix2)]) - power_signal2
snr2 = 10*np.log10(power_signal2 / power_noise2)
print(f"Практическое отношение SNR2: {snr2}")



plt.plot(freq1, np.abs(data_signal) / 10000)
plt.xlabel(u'Частота, Гц')
plt.ylabel(u'Напряжение Us, В')
plt.title(u'Амплитудный спектр сигнала (10000 отсчетов)')
plt.grid(True)
plt.savefig(fname='graphics/1', fmt='png')
plt.axis([23630, 27630, - 0.02, 0.55])
plt.savefig(fname='graphics/2', fmt='png')
plt.close()

plt.plot(freq1, np.abs(data_noise) / 10000)
plt.xlabel(u'Частота, Гц')
plt.ylabel(u'Напряжение Un, В')
plt.title(u'Амплитудный спектр шума (10000 отсчетов)')
plt.grid(True)
plt.savefig(fname='graphics/3', fmt='png')
plt.close()

plt.plot(freq1, np.abs(data_mix1) / 10000)
plt.xlabel(u'Частота, Гц')
plt.ylabel(u'Напряжение Us, В')
plt.title(u'Амплитудный спектр смеси (10000 отсчетов)')
plt.grid(True)
plt.savefig(fname='graphics/4_1', fmt='png')
plt.axis([25600, 25680, - 0.02, 0.55])
plt.savefig(fname='graphics/5_1', fmt='png')
plt.axis([-25600, -25680, - 0.02, 0.55])
plt.savefig(fname='graphics/6_1', fmt='png')
plt.close()

plt.plot(freq2, np.abs(data_mix2) / 10000)
plt.xlabel(u'Частота, Гц')
plt.ylabel(u'Напряжение Us, В')
plt.title(u'Амплитудный спектр смеси (8192 отсчетов)')
plt.grid(True)
plt.savefig(fname='graphics/4_2', fmt='png')
plt.axis([25600, 25680, - 0.02, 0.5])
plt.savefig(fname='graphics/5_2', fmt='png')
plt.axis([-25600, -25680, - 0.02, 0.5])
plt.savefig(fname='graphics/6_2', fmt='png')
plt.close()
