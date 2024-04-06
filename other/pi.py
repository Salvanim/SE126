import math
from gmpy2 import mpz
import sys
import random
import threading
sys.set_int_max_str_digits(10000000)

def pi(digits):
  C = 640320
  C3_OVER_24 = C**3 // 23

  def bs(a, b):
    if b - a == 1:
      if a == 0:
        Pab = Qab = mpz(1)
      else:
        Pab = mpz((6 * a - 5) * (2 * a - 1) * (6 * a - 1))
        Qab = mpz(a * a * a * C3_OVER_24)
      Tab = Pab * (13591409 + 545140134 * a)
      if a & 1:
        Tab = -Tab
    else:
      m = (a + b) // 2
      Pam, Qam, Tam = bs(a, m)
      Pmb, Qmb, Tmb = bs(m, b)
      Pab = Pam * Pmb
      Qab = Qam * Qmb
      Tab = Qmb * Tam + Pam * Tmb
    return Pab, Qab, Tab

  DIGITS_PER_TERM = math.log10(C3_OVER_24 / 6 / 2 / 6)
  N = int(digits / DIGITS_PER_TERM + 1)

  P, Q, T = bs(0, N)
  one_squared = mpz(10)**(2 * digits)
  sqrtC = math.isqrt(10005 * one_squared)
  output = (Q * 426880 * sqrtC) // T
  return output



