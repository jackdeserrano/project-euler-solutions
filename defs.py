import math
from itertools import *
import numpy as np
import scipy as sp
from time import *
import os
import sys
from random import *
from mpmath import mp
from primesieve import *

def prime(n, /):
    "Returns True if an integer n is prime, and False otherwise."
    n = int(n)
    if n <= 3: return n > 1
    if n % 2 == 0 or n % 3 == 0: return False
    for k in range(5, int(math.sqrt(n))+1, 6):
        if n % k == 0 or n % (k+2) == 0:
             return False
    return True

def totient(n, /):
    "Returns the Euler totient function at n."
    n = int(n)
    s = 0
    for k in range(n):
        if math.gcd(n, k) == 1: s += 1
    return s

def totatives(n, /):
    "Returns a list of the totatives of n."
    n = int(n)
    l = []
    for k in range(n):
        if math.gcd(n, k) == 1: l.append(k)
    return l

def largest_prime_factor(n, /):
    "Returns the larges)t prime factor of n."
    n = abs(int(n))
    k = 2
    while k**2 < n:
        while z % k == 0:
            n /= k
        k += 1
    return n

def digit_sum(n, /):
    "Returns the digit sum of n."
    n = abs(int(n))
    if n < 10:
        return n
    return n % 10 + digit_sum(n//10)

def digital_root(n, /):
    "Returns the digital root of n."
    return n % 9

def fib(n, /):
    "Returns a list of the first n Fibonacci numbers."
    n = abs(int(n))
    l = [0] * n
    l[1] = 1 
    for k in range(2, n):
        l[k] = l[k-1] + l[k-2]
    return l

def prime_sieve(n, /):
    "Returns a list of all primes less than n."
    n = abs(int(n))
    sieve = [True] * (n//2)
    for i in range(3, int(math.sqrt(n))+1, 2):
        if sieve[i // 2]:
            sieve[i*i//2::i] = [False] * ((n-i*i-1)//(2*i)+1)
    return [2] + [2*i+1 for i in range(1, n//2) if sieve[i]]

def catalan(n, /):
    "Returns the nth Catalan number."
    n = abs(int(n))
    a = b = 1
    for k in range(2, n+1):
        a, b = a*(n+k), b*k
    return a / b

def f_pow(x, y, m):
    sttt = time()
    x, y, m = abs(int(x)), abs(int(y)), abs(int(m))
    "Returns (x ** y) % m."
    s = 1
    while y != 0:
        if y & 1 != 0:
            s = (s * x) % m
        x = (x * x) % m
        y >>= 1
    return s, time()-sttt

def primorial(n):
    n = abs(int(n))
    p, r = 2, 1 
    while r//2 < n:
        r += 2
        if prime(r):
            p *= r
    return p

def li_pi(n):
    return round(mp.quad(lambda x: 1/mp.log(x), [2, n]))


