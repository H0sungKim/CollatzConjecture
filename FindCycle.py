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

import sys
print = sys.stdout.write

a = 0
num2 = 1
num3 = 1
for n in range(10000000) :
    while num2 <= num3 :
        num2 *= 2
    while num2-num3 <= a :
        if a % (num2-num3) == 0 :
            print("\n***************ANSWER***************\n")
            print(f"{n}\n")
            print("\n***************ANSWER***************\n")

            print(f"a{n} : {a}\n")
            print(f"2^{n}+l : {num2}\n")
            print(f"3^{n} : {num3}\n")
            print(f"below{n} : {num2-num3}\n")
            print(f"{n} : {a % (num2-num3)}\n")
            print("\n")
            
        # print(f"{a}\n")
        # print(f"{num2-num3}\n")
        # print(f"{a % (num2-num3)}\n")
        # print("\n")
        num2 *= 2
    if n%1000 == 0 :
        print(f"count : {n}\n")
    a = a*3 + int(pow(2, n))
    num3 *= 3





# First Ver
    
# import sys
# print = sys.stdout.write

# a = 0

# for n in range(100) :
#     num2 = int(pow(2, n))
#     num3 = int(pow(3, n))
#     while num2 <= num3 :
#         num2 *= 2
#     while num2-num3 <= a :
#         if a % (num2-num3) == 0 :
#             print("\n***************ANSWER***************\n")
#         print(f"a{n} : {a}\n")
#         print(f"2^{n}+l : {num2}\n")
#         print(f"3^{n} : {num3}\n")
#         print(f"below{n} : {num2-num3}\n")
#         print(f"{n} : {a % (num2-num3)}\n")
#         print("\n")
            
#         # print(f"{a}\n")
#         # print(f"{num2-num3}\n")
#         # print(f"{a % (num2-num3)}\n")
#         # print("\n")
#         num2 *= 2
#     if n%1000 == 0 :
#         print(f"count : {n}\n")
#     a = a*3 + int(pow(2, n))