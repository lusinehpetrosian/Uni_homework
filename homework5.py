# -*- coding: utf-8 -*-
"""Homework5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_Yayh3lfMhp4cmeEjwzSjUk9D0S9xe9P

#1
"""

n = int(input('Enter the number\n>>'))
for i in range(2,n+1):
  if n % i == 0:
    print(i)
    break

"""#2"""

k = 0
max = float('-inf')
while True:
  n = int(input('Enter the number\n>>'))
  if n == 0:
    break
  elif n == max:
    k += 1
  elif n > max:
    max = n
    k = 1
print(k)

"""#3

"""

numbers  = [1, 2, 4, 6, 8, 10, 34, 15, 19, 21]
for i in numbers:
  if i % 2 == 1 and  (i < 3 or  i > 7) and (i < 11 or  i > 13) and (i < 17 or  i > 23):
    print(i)

"""#4"""

text = input('Enter the string\n>>>')
text = text.strip()
text = text.split()
print(len(text))

"""#5"""

text = input('Enter the string\n>>>')
text = text.split()
for i in range(len(text)):
  print(text[i], end = '\n')

"""#6

"""

text = input('Enter the string\n>>>')
text = text.replace('\\', '/')
text = text.replace('C:','/home')
print(text)

"""#7

"""

lst = []
for i in range(5):
  word = input('Enter the string\n>>>')
  lst.append(word)
for i in range(len(lst)-1):
  print(lst[i], end = '-->')
print(lst[-1])

"""#8"""

n = int(input('Enter the number\n>>'))
lst = []
for i in range(n):
  numbers = int(input('number is '))
  lst.append(numbers)
lst = sorted(lst)
print(*lst)

"""#9

"""

lst = [12, 443, 454, 22]
maxind = lst.index(max(lst))
minind = lst.index(min(lst))
k = lst[maxind]
lst[maxind]=lst[minind]
lst[minind]=k
print(*lst)

"""#10

"""

n = int(input('Enter the number\n>>'))
lst = []
for i in range(1, n+1):
  lst.append(i)
  print(*lst)

"""#11

"""

# n = int(input('Enter the number\n>>'))
numbers = input('numbers are\n>>>')
lst = numbers.split()
for i in range(len(lst)):
  x = list(lst[i])
  sorted2 = sorted(x)
  lst[i] = ''.join(sorted2)
for i in range(len(lst)):
  lst[i] = int(lst[i])
sorted1 = sorted(lst)
print(*sorted1)

"""#12

"""

n = int(input('Enter the number\n>>'))
matrix = []
yes = True
for i in range(n):
  l = []
  for j in range(n):
    l.append(int(input()))
  matrix.append(l)
print(matrix)
for i in range(n):
  for j in range(i):
    if matrix[i][j] != matrix[j][i]:
      yes = False
if yes == True:
  print('Yes')
else:
  print('No')

"""#13

"""

l = input('a = ? and b = ?').split()
a, b = int(l[0]), int(l[-1])
for i in range(a, b+1):
  print(i**2)

"""#14

"""

l = input().split()
for i in range(len(l)):
  l[i]= int(l[i])
for i in l:
  print(i**(1/2))

"""#15

"""

l = input().split()
for i in range(len(l)):
  l[i]= int(l[i])
for i in l:
  if i % 2 == 0:
    print(i**(1/3), end =' ')

"""#16

"""

for i in range(1,9):
  l = []
  for j in 'ABCDEFGH':
    l.append(j + str(i))
  print(*l)

"""#17

"""

l = input('h = ? and w = ?').split()
h, w = int(l[0]), int(l[-1])
lst = []
for i in range(h*w):
  lst.append(int(input('Enter a number\n>>')))
for i in range(0,h*w, w):
  new_list = lst[i:i+w]
  print(*new_list)

"""#18

"""

n = int(input())
lst = []
for i in range(n):
  lst.append(input('Name is:'))

print(tuple(lst))

"""#19

"""

n = int(input())
lst = []
for i in range(n):
  lst.append(input('Name is:'))
set = set(lst)
for i in set:
  print(i)

l = input().split()
last_letters = []
for i in l:
  if i[-1] not in last_letters:
    last_letters.append(i[-1])
print(*sorted(last_letters))



_

