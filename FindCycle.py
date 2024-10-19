# Hosung.Kim
# 2024.01.29

# Collatz Conjecture ---------------------------
# This program finds cycles in the Colatz conjecture sequence.
# 
#                                    x
#                         /                     \
#                       x/2                   3x+1/2
#                    /       \               /      \
#                  x/4    (3x/2+1)/2     3x+1/4   9x+5/4
# 
# xn = (3^n/2^ * x0 + an) / 2^n
# 
# +---+---+---+---+---+---+---+---+
# | n | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
# +---+---+---+---+---+---+---+---+
# | an| 0 | 1 | 5 | 19| 65|211|665|
# +---+---+---+---+---+---+---+---+
# an+1 = 3an + 2^n
# an = 2^0 * 3^(n-1) + 2^1 * 3^(n-2) + ... + 2^(n-2) * 3^1 + 2^(n-1) * 3^0
# an = Σ(k=0 to n-1) 2^k * 3^(n-1-k) = 3^n - 2^n
# 
# xn = (3^n/2^ * x0 + 3^n - 2^n) / 2^n
# 
# if xn = x0 * 2^, then cycle exists.
# x0 = 3^n - 2^n / (2^ - 3^n)
# 
# Find an integer x that satisfies the above condition.
# 
# Complete Calculation to n = 1400000

import FileManager
import sys
import math
print = sys.stdout.write
sys.set_int_max_str_digits(1000000000)

# n = 0
n = FileManager.getProgress()

log = math.log(3) / math.log(2)

nPower2 = pow(2, n)
nPower3 = pow(3, n)


while True :
    fPower2 = pow(2, int(n * log)+1)
    pDif = nPower3 - nPower2
    fDif = fPower2 - nPower3
    while fDif <= pDif :
        if pDif % fDif == 0 :
            print("\n***************ANSWER***************\n")
            print(f"{n}\n")
            print(f"x0 : {pDif/(fPower2-nPower3)}\n")
            FileManager.saveProgress(n)
            print("***************ANSWER***************\n")

            print("\n")
            exit()
        fPower2 *= 2
        fDif = fPower2 - nPower3
    if n%10000 == 0 :
        print(f"count : {n}\n")
        print("\n")
        FileManager.saveProgress(n)

    nPower2 *= 2
    nPower2 *= 3
    n += 1