
#1
# def triangle(n,c ='#'):
#   lst = []
#   for j in range(n):
#     lst.append((j + 1) * [c])
#   return lst
# print(triangle(2))
# print(triangle(3,['*']))
  
#2
# def gcd2(a, b):
#     while a != b:
#         if a > b:
#             a -= b
#         elif a < b:
#             b -= a
#     return a
# def gcd(*numbers):
#     lst = []
#     for i in numbers:
#         lst.append(i)
#     gcdall = gcd2(lst[0],lst[1])
#     for i in range(2, len(lst)):
#         gcdall = gcd2(lst[i], gcdall)
#         return gcdall

# print(gcd(5,10,15,20))
# print(gcd(21,14,70))


# 3
# def fib(n, lst = None):
#   if lst is None:
#     lst = [0]
#   lst[0]+=1
#   if n == 1 or n == 2 :
#     return 1, lst
#   else:
#     return fib(n-2,lst)[0] + fib(n-1, lst)[0], lst
# print(fib(4)[1][0])


#4
# def prime_factors(n): 
#     ls = []
#     i = 2
#     while n != 1:
#         if n % i == 0:
#             ls.append(i)
#         while n % i == 0:
#             n = n//i
            
#         else:
#             i +=1
#     return ls
# print(prime_factors(11))

#5
# def jumping_frog(lst, step):
#     for i in range(len(lst)-1):
#         if abs(lst[i] - lst[i+1]) > step:
#             return 'Game over'
#     return 'Frog wins'
# print(jumping_frog([1,3], 2))
# print(jumping_frog([4,5,2], 2))
