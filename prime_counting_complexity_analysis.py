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
    # legendre
    t_legendre = n / (log(n, 2) ** 2)

    # magic legendre
    t_magic = n ** (3 / 4) / (log(n, 2) ** 2)

    # LMO
    t_lmo = n ** (2 / 3) * log(log(n, 2), 2)

    # meissel
    t_meissel = n / (log(n, 2) ** 3)

    # lehmer
    t_lehmer = n / (log(n, 2) ** 4)

    #  Deleglise - Rivat 
    t_del_riv = n ** (2 / 3) / (log(n, 2) ** 2)

    # print(n, t_legendre, t_magic, t_meissel, t_lehmer, t_lmo)
    rows.append(
        [
            "{:e}".format(n),
            "{:.1f}".format(t_legendre),
            "{:.1f}".format(t_magic),
            "{:.1f}".format(t_meissel),
            "{:.1f}".format(t_lehmer),
            "{:.1f}".format(t_lmo),
            "{:.1f}".format(t_del_riv),
        ]
    )
    n *= 10

print(
    tabulate(
        rows,
        headers=[
            "n",
            "t_legendre",
            "t_magic",
            "t_meissel",
            "t_lehmer",
            "t_lmo",
            "t_del_riv or t_gordon"
        ],
        tablefmt="orgtbl",
    )
)
