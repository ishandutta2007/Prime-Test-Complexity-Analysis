# Complexity-Analysis

# prime_counting_complexity_analysis.py


|          n |       t_legendre |          t_magic |        t_meissel |         t_lehmer |            t_lmo |   t_del_riv or t_gordon |
| ----------:| ----------------:| ----------------:| ----------------:| ----------------:| ----------------:| ----------------:|
|     10     |      0.9         |      0.5         |      0.3         |      0.1         |      8           |             0.4         |
|    100     |      2.3         |      0.7         |      0.3         |      0.1         |     58.9         |             0.5         |
|   1000     |     10.1         |      1.8         |      1           |      0.1         |    331.7         |             1           |
|  10000     |     56.6         |      5.7         |      4.3         |      0.3         |   1732.3         |             2.6         |
| 100000     |    362.5         |     20.4         |     21.8         |      1.3         |   8734           |             7.8         |
|      1e+06 |   2517.2         |     79.6         |    126.3         |      6.3         |  43169.8         |            25.2         |
|      1e+07 |  18493.7         |    328.9         |    795.3         |     34.2         | 210699           |            85.8         |
|      1e+08 | 141592           |   1415.9         |   5327.9         |    200.5         |      1.01948e+06 |           305.1         |
|      1e+09 |      1.11875e+06 |   6291.2         |  37419.8         |   1251.6         |      4.90195e+06 |          1118.8         |
|      1e+10 |      9.06191e+06 |  28656.3         | 272790           |   8211.8         |      2.34584e+07 |          4206.2         |
|      1e+11 |      7.48918e+07 | 133178           |      2.04952e+06 |  56087.8         |      1.11846e+08 |         16134.9         |
|      1e+12 |      6.29299e+08 | 629299           |      1.57865e+07 | 396017           |      5.31698e+08 |         62929.9         |
|      1e+13 |      5.36207e+09 |      3.01532e+06 |      1.24165e+08 |      2.87518e+06 |      2.52152e+09 |        248885           |
|      1e+14 |      4.62342e+10 |      1.46205e+07 |      9.94135e+08 |      2.1376e+07  |      1.19342e+10 |        996086           |
|      1e+15 |      4.02751e+11 |      7.16204e+07 |      8.08268e+09 |      1.62209e+08 |      5.63891e+10 |             4.02751e+06 |
|      1e+16 |      3.53981e+12 |      3.53981e+08 |      6.65993e+10 |      1.25302e+09 |      2.66057e+11 |             1.64303e+07 |
|      1e+17 |      3.13561e+13 |      1.76328e+09 |      5.55242e+11 |      9.83203e+09 |      1.25377e+12 |             6.75546e+07 |
|      1e+18 |      2.79688e+14 |      8.84453e+09 |      4.67748e+12 |      7.82256e+10 |      5.90195e+12 |             2.79688e+08 |
|      1e+19 |      2.51022e+15 |      4.46388e+10 |      3.97712e+13 |      6.30122e+11 |      2.77565e+13 |             1.16514e+09 |
|      1e+20 |      2.26548e+16 |      2.26548e+11 |      3.40988e+14 |      5.13238e+12 |      1.30428e+14 |             4.88082e+09 |
|      1e+21 |      2.05485e+17 |      1.15553e+12 |      2.94558e+15 |      4.22242e+13 |      6.12434e+14 |             2.05485e+10 |
|      1e+22 |      1.87229e+18 |      5.92072e+12 |      2.56189e+16 |      3.50549e+14 |      2.87382e+15 |             8.69042e+10 |
|      1e+23 |      1.71303e+19 |      3.04624e+13 |      2.24205e+17 |      2.93446e+15 |      1.34772e+16 |             3.6906e+11  |
|      1e+24 |      1.57325e+20 |      1.57325e+14 |      1.97331e+18 |      2.47511e+16 |      6.31698e+16 |             1.57325e+12 |
|      1e+25 |      1.4499e+21  |      8.15341e+14 |      1.74586e+19 |      2.10222e+17 |      2.95942e+17 |             6.72986e+12 |
|      1e+26 |      1.34052e+22 |      4.23909e+15 |      1.55206e+20 |      1.79699e+18 |      1.38583e+18 |             2.88806e+13 |
|      1e+27 |      1.24306e+23 |      2.21051e+16 |      1.38592e+21 |      1.5452e+19  |      6.48691e+18 |             1.24306e+14 |
|      1e+28 |      1.15586e+24 |      1.15586e+17 |      1.24267e+22 |      1.336e+20   |      3.03531e+19 |             5.36501e+14 |


# prime_test_complexity_analysis.py

|          n |     t_aks |        t_gordon |   t_miller_rabins |
|-----------:|----------:|----------------:|------------------:|
|     10     |     36.66 |               0 |       1.78        |
|    100     |    293.27 |               0 |       3.16        |
|   1000     |    989.77 |               1 |       5.62        |
|  10000     |   2346.12 |               2 |      10           |
| 100000     |   4582.27 |               7 |      17.78        |
|      1e+06 |   7918.16 |              25 |      31.62        |
|      1e+07 |  12573.8  |              85 |      56.23        |
|      1e+08 |  18769    |             305 |     100           |
|      1e+09 |  26723.8  |            1118 |     177.83        |
|      1e+10 |  36658.2  |            4206 |     316.23        |
|      1e+11 |  48792    |           16134 |     562.34        |
|      1e+12 |  63345.3  |           62929 |    1000           |
|      1e+13 |  80538    |          248885 |    1778.28        |
|      1e+14 | 100590    |          996085 |    3162.28        |
|      1e+15 | 123721    |         4027513 |    5623.41        |
|      1e+16 | 150152    |        16430328 |   10000           |
|      1e+17 | 180102    |        67554616 |   17782.8         |
|      1e+18 | 213790    |       279688451 |   31622.8         |
|      1e+19 | 251438    |      1165142407 |   56234.1         |
|      1e+20 | 293265    |      4880821068 |  100000           |
|      1e+21 | 339491    |     20548539294 |  177828           |
|      1e+22 | 390336    |     86904216749 |  316228           |
|      1e+23 | 446020    |    369060194247 |  562341           |
|      1e+24 | 506762    |   1573247539747 |       1e+06       |
|      1e+25 | 572784    |   6729862545101 |       1.77828e+06 |
|      1e+26 | 644304    |  28880598040950 |       3.16228e+06 |
|      1e+27 | 721543    | 124305978449185 |       5.62341e+06 |
|      1e+28 | 804720    | 536500521771487 |       1e+07       |

Gordon do not have a prime testing algo, we are talking about using prime counting algo to test primes in deterministic way.ie `is_prime(n)<==>(gordon_pi(n)-gordon_pi(n-1)==1)`

### It is interesting to note gordon's method is not only faster than AKS but also Miller Rabins for n < 1e7. So till 1e7 we can use Gordon's prime counting to test primality over Miller Rabins. And if we are taking about deterministic then we can use Gordon over AKS till 1e12.

### Another interesting think is from 1e25 onwards AKS is faster than Miller Rabins
