from math import log
from tabulate import tabulate
import pandas as pd

pd.options.display.float_format = "{:.2f}".format
import numpy as np

np.set_printoptions(suppress=True)

# print("n", "t_aks", "t_gor", "t_mr")

n = 10
rows = []
while n < 10 ** 29:
    # AKS_deteministic_primality_test
    t_aks = log(n, 2) ** 3

    # Gordon_prime_counting_deteministic_primality_test
    t_gor = n ** (2 / 3) / ((log(n, 2)) ** 2)

    # Miller rabin probablistic _primality_test
    t_mr = n ** (1 / 4)
    # print(n, t_aks, t_gor, t_mr)
    rows.append([n, "{:.2f}".format(t_aks), int(t_gor), "{:.2f}".format(t_mr)])
    n *= 10
print(
    tabulate(
        rows, headers=["n", "t_aks", "t_gordon", "t_miller_rabins"], tablefmt="orgtbl"
    )
)


# It is interesting to note gordon's method is not only faster than AKS but also miller rabins for n < 1e7
# Another interesting think is from 1e25 onwards AKS is faster than MR
