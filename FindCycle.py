# 2024 Hosung.Kim <hyongak516@mail.hongik.ac.kr>

# Collatz Conjecture ---------------------------
# This program finds cycles in the Colatz conjecture sequence.
# 
# x -> (3x+1)/2 -> (9x+5)/4 -> (27x+19)/8 -> ...
# 
# xn = (3^n * x + an) / 2^n
# 
# an+1 = 3an + 2^n
# an = 2^0 * 3^(n-1) + 2^1 * 3^(n-2) + ... + 2^(n-2) * 3^1 + 2^(n-1) * 3^0
# +---+---+---+---+---+---+---+---+
# | n | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
# +---+---+---+---+---+---+---+---+
# | an| 0 | 1 | 5 | 19| 65|211|665|
# +---+---+---+---+---+---+---+---+
# 
# an % (2^(n+k) - 3^n) = 0 
# k가 임의의 자연수일 때 위 식을 만족시키면 순환
# 
# n = 1000000 까지 테스트 완료
# 186,000,000,000

import FileManager
import sys
print = sys.stdout.write
sys.set_int_max_str_digits(1000000000)


# n = 0
# a = 0

n, a = FileManager.getProgress()

num2 = pow(2, n)
num3 = pow(3, n)
while True :
    while num2 <= num3 :
        num2 *= 2
    while num2-num3 <= a :
        if a % (num2-num3) == 0 :
            print("\n***************ANSWER***************\n")
            print(f"{n}\n")
            print("***************ANSWER***************\n")

            print(f"a{n} : {a}\n")
            print(f"2^{n}+l : {num2}\n")
            print(f"3^{n} : {num3}\n")
            print(f"below{n} : {num2-num3}\n")
            print(f"{n} : {a % (num2-num3)}\n")
            print("\n")
            exit()
            
        # print(f"{a}\n")
        # print(f"{num2-num3}\n")
        # print(f"{a % (num2-num3)}\n")
        # print("\n")
        num2 *= 2
    if n%100000 == 0 :
        print(f"count : {n}\n")
        # print(f"a{n} : {a}\n")
        print("\n")
        FileManager.saveProgress(n, a)
    a = a*3 + pow(2, n)
    num3 *= 3
    n += 1


# First Ver
    

# a = 0

# for n in range(1000000) :
#     num2 = int(pow(2, n))
#     num3 = int(pow(3, n))
#     while num2 <= num3 :
#         num2 *= 2
#     while num2-num3 <= a :
#         if a % (num2-num3) == 0 :
#             print("\n***************ANSWER***************\n")
#             print(f"count : {n}\n")
#             print("\n***************ANSWER***************\n")
            
#         # print(f"{a}\n")
#         # print(f"{num2-num3}\n")
#         # print(f"{a % (num2-num3)}\n")
#         # print("\n")
#         num2 *= 2
#     if n%10000 == 0 :
#         print(f"count : {n}\n")
#         print(f"a{n} : {a}\n")
#         print("\n")
#     a = a*3 + int(pow(2, n))