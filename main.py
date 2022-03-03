import random
import math

import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
from sklearn import datasets
iris = datasets.load_iris()

N = 1000000
NN = 10


def generate_test_series():
    result_test_series = 0
    for i in range(NN):
        x = random.randint(0, 1)
        result = 1
        while x:
            x = random.randint(0, 1)
            result = result * 2
        result_test_series += result
    return result_test_series


def generate_paradox_test(max_depth=0):
    x = random.randint(0, 1)
    result = 1
    depth = 1
    while x and (max_depth == 0 or depth <= max_depth):
        x = random.randint(0, 1)
        result = result * 2
        depth += 1
    return result


def generate_key_paradox_sample(sample_len, max_depth=0):
    key_sample = {}
    for i in range(sample_len):
        result = generate_paradox_test(max_depth)
        if result in key_sample:
            key_sample[result] += 1
        else:
            key_sample[result] = 1
    return_key_sample = {}
    for key in sorted(key_sample.keys()):
        return_key_sample[key] = (key_sample[key],
                                  key_sample[key] / N)
    return return_key_sample


def generate_paradox_sample():
    sample = []
    for i in range(N):
        result = generate_test_series()
        sample.append(result)
    return sample


def calculate_sample_mean(sample, sample_len):
    sample_sum = 0
    for key in sample:
        sample_sum += key * sample[key][0]
    return sample_sum / sample_len


def calculate_sample_dispersion(sample, sample_len):
    sample_mean = calculate_sample_mean(sample, sample_len)

    dispersion = 0
    for key in sample:
        dispersion += (key - sample_mean) ** 2 * sample[key][0]
    dispersion = dispersion / sample_len
    return dispersion


def calculate_median(sample, sample_len):
    pos = sample_len // 2
    for key in sample:
        pos -= sample[key][0]
        if pos < 0:
            return key
    return None


if __name__ == '__main__':
    # paradox_sample = generate_paradox_sample()
    x = []
    paradox_medians = {}
    paradox_sample_means = {}
    for i in [100, 1000, 10000, 100000, 1000000, 10000000, 100000000]:
        x.append(int(math.log10(i)))
        for d in [0, 10]:
            print(f'{i} max_depth: {d}')
            paradox_key_sample = generate_key_paradox_sample(i, max_depth=d)
            paradox_median = calculate_median(paradox_key_sample, sample_len=i)
            paradox_sample_mean = calculate_sample_mean(paradox_key_sample, sample_len=i)
            for key in paradox_key_sample:
                print(f'{key} : '
                      f'{paradox_key_sample[key][0]}, '
                      f'{paradox_key_sample[key][1]}')
            if d not in paradox_sample_means:
                paradox_sample_means[d] = [paradox_sample_mean]
            else:
                paradox_sample_means[d].append(paradox_sample_mean)
            if d not in paradox_medians:
                paradox_medians[d] = [paradox_median]
            else:
                paradox_medians[d].append(paradox_median)

            print(paradox_median, paradox_sample_mean)
            print()
    # x = [2, 3, 4, 5, 6, 7, 8]
    # paradox_sample_means = {0: [3.09, 4.499, 10.5837, 8.14035, 547.776749, 15.3412161, 12.80044241],
    #                         10: [4.22, 6.368, 5.4263, 6.12253, 5.986214, 5.9937484, 5.99767625]}
    plt.figure(figsize=(13, 10), dpi=80)
    plt.tick_params(axis='both', which='major', labelsize=22)
    plt.plot(x, paradox_sample_means[0], 'ro-', label=f'sample_means, max depth = infty', linewidth=2)
    plt.plot(x, paradox_sample_means[10], 'go-', label=f'sample_means, max depth = 10', linewidth=2)
    plt.show()
    # for key in paradox_key_sample:
    #     print(f'{key // 10}&\t{key}&\t'
    #           f'{paradox_key_sample[key][0]}&\t{paradox_key_sample[key][1]}&\t')
    # paradox_sample_dispersion = calculate_sample_dispersion(paradox_key_sample)
    # plt.figure(figsize=(13, 10), dpi=80)
    # sns_plot = sns.histplot(paradox_sample, color="red",
    #                         kde=True,
    #                         stat="density",
    #                         binwidth=10,
    #                         linewidth=0)
    # plt.xlim(NN, NN+1500)
    # plt.ylabel("Density", fontsize=22)
    # plt.tick_params(axis='both', which='major', labelsize=22)
    # plt.title(f'N={N}, E={paradox_sample_mean}, Median={paradox_median}, '
    #           f'x={NN}..{NN+1500}', fontsize=22)
    # plt.show()
    # fig = sns_plot.get_figure()
    # fig.savefig(f'output{N}_{NN}_1000.png')
    # plt.figure(figsize=(13, 10), dpi=80)
    # sns_plot = sns.histplot(paradox_sample, color="red",
    #                         kde=True,
    #                         stat="density",
    #                         binwidth=5,
    #                         linewidth=0)
    # plt.xlim(NN, NN+100)
    # plt.ylabel("Density", fontsize=22)
    # plt.tick_params(axis='both', which='major', labelsize=22)
    # plt.title(f'N={N}, E={paradox_sample_mean}, Median={paradox_median}, '
    #           f'x={NN}..{NN+200}', fontsize=22)
    # plt.show()
    # fig = sns_plot.get_figure()
    # fig.savefig(f'output{N}_{NN}_100.png')
    # print(paradox_sample_mean)
    # print(paradox_median)
    # print(paradox_sample_dispersion)
