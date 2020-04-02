# def staircase(n):
#     for i in range(n):
#         for j in range(i+1):
#             print("#", end=" ")
#         print()

# def staircase(n):
#     k=1
#     for i in range(n):
#         for j in range(k):
#             print("* ", end="")
#         k+=2
#         print()
# *
# * * *
# * * * * *
# * * * * * * *
# * * * * * * * * *

# def staircase(n):
#     for i in range(n):
#         for j in range(n-i-1):
#             print(" ", end="")
#         for j in range(i+1):
#             print("*",end="")
#         print()

# def timeConversion(s):
#     #
#     # Write your code here.
#     #
#     hour = s[:2]
#     if s[-2:] == "PM" and s[:2]!="12":
#         hour = int(hour) + 12
#     elif s[-2:] == "AM" and s[:2]=='12':
#         hour = "00"
#     return str(hour) + s[2:-2]

# print(timeConversion("12:45:54PM"))


# staircase(4)


# w="dkhc"
# print(w[-3:])
# def f(w):
#     best = ''
#     for i in range(len(w)):
#         idx = -i-1
#         c=w[idx]
#         if c>=best:
#             best = c
#         else:
#             l = sorted(w[idx:])
#             print(c)
#             print(l)
#             print(idx)
#             for j, ch in enumerate(l):
#                 if ch > c:
#                     return w[:idx] + ch + ''.join(l[:j] + l[j+1:])
#     return "no answer"

# print(f(w))

def kaprekarNumbers(p, q):
    list = []
    for i in range(p,q+1):
        sq = i*i
        d=len(str(i))
        di = 10**d
        l = sq//di
        r = sq%di
        if l+r == i:
            list.append(i)
    print(list)


kaprekarNumbers(1,99999)