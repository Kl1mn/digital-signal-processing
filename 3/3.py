import csv
import matplotlib.pyplot as plt

snr = 5

signal = []
noise = []
general_data = []

def avarage_count(data):
    value = 0.0
    for i in data:
        value += float(i["U"])
    return value / len(data)

def read_my_csv(data, filename):
    with open(filename, "r") as f:
        reader = csv.DictReader(f, delimiter=',')
        for line in reader:
            k = {}
            k["t"] = float(line["t"])
            k["U"] = float(line["U"])
            data.append(k)

def graph3():
    x1 = []
    x2 = []
    for i in general_data:
        if i["t"] >= 0.05000 and i["t"] <= 0.055:
            x1.append(i["t"])
            x2.append(i["U"])
    plt.scatter(x1, x2)
    plt.title('signal + noise sample (5%)')
    plt.xlabel('t, c')
    plt.ylabel('U, В')
    plt.grid(True)
    plt.savefig(fname='graphics/1', fmt='png')
    plt.close()

if __name__ == "__main__":
    read_my_csv(signal, "../1/12_signal.csv")
    read_my_csv(noise, "../2/12_noise.csv")

    avar = avarage_count(signal)
    print("avar: ", avar)

    rmss = ((sum([(i["U"]-avar)**2 for i in signal]))/len(signal)) ** (1/2)
    print("rmss: ", rmss)

    rmsn = ((sum([i["U"]**2 for i in noise]))/len(noise)) ** (1/2)
    print("rmsn: ", rmsn)

    wanted_rmsn = rmss / (10 ** (snr / 20))
    print("wanted_rmsn: ", wanted_rmsn)

    k = 1/((sum([i["U"]**2 for i in noise]) / len(noise) / (wanted_rmsn**2)) ** (1/2))
    print("k: ", k)

    for i in range(len(signal)):
        l = {}
        l["t"] = signal[i]["t"]
        l["U"] = signal[i]["U"] + (noise[i]["U"]*k) - avar
        general_data.append(l)
    # graph3()
    with open("12_sn.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["t", "U"])
        writer.writeheader()
        for i in general_data:
            i["t"] = "%.5f" % i["t"]
            i["U"] = "%.8f" % i["U"]
        writer.writerows(general_data)
    
    print(f'Амплитудный коэффициент для шумовых отсчетов {"%.6f" % k}')
