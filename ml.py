import pandas as pd
import matplotlib.pyplot as plt


if __name__ == '__main__':
    arr = [1]*8
    arr.extend([2]*5)
    plt.hist(arr, color='blue', label='gamma', alpha=0.7, density=True)
    arr1 = [3]*4
    arr1.extend([2]*7)
    plt.hist(arr1, color='red', label='hidro', alpha=0.7, density=True)
    plt.show()

