
# input

# 读取一行输入

# line = list(map(int, input().strip().split()))

# 读取多行输入（指定行数）

# n, m = map(int, input().strip().split())
# lis = []
# for i in range(n):
#     tmp = list(map(int, input().strip().split()))
#     lis.append(tmp)
# print(lis)

# B2001

# line = list(map(int,input().strip().split()))
# total = line[0] + line[1]
# print(total)

# B2002

# print('Hello,World!')

# B2003

# line = list(map(int, input().strip().split()))
# print(line[1])

# B2004

# line = list(map(int, input().strip().split()))
#
# a = '%8d' % line[0]
# b = '%8d' % line[1]
# c = '%8d' % line[2]
#
# print(a + ' ' + b + ' ' + c)

# B2006

# line = list(map(int, input().strip().split()))
# total = line[2] * line[3] - line[0] * line[1]
# final = total / (line[3] - line[1])
# print('%.2f' % final)

# B2007

# a, b = map(int,input().strip().split())
# print(a + b)

# B2008

# a ,b, c = map(int, input().strip().split())
# print((a + b) // c)

# / 与 // 不同

# B2009

# a, b = map(int,input().strip().split())
# final1 = a // b
# final2 = a % b
# print(str(final1) + ' ' + str(final2))

# B2011

# line = list(map(float,input().strip().split()))
# final = line[0] / line[1]
# print('%.9f' % final)

# B2012

# a = input()
# b = input()
# final = (int(b) / int(a) * 100)
# print('%.3f%%' % final)

# 注意输入的方式

# B2013

# a = input()
# final = 5.0 * (float(a) - 32) / 9
# print('%.5f' % final)

# B2014

# PI = 3.14159
# r = float(input())
# d = 2 * r
# c = 2 * r * PI
# s = r * r * PI
# print('%.4f' % d + ' ' + '%.4f' % c + ' ' + '%.4f' % s)

# B2015

# a, b = map(int, input().strip().split())
# final = 1 / ((1 / a) + (1 / b))
# print('%.2f' % final)

# B2016

# import math
#
# a = float(input())
#
# if a >= 0:
#     print(math.floor(a))     # 向下取整
# else:
#     print(math.ceil(a))      # 向上取整

# B2017

# a = input().strip()   # 删去多余的空格
# print(ord(a))

# B2018

# a = input().strip()
# print(chr(int(a)))

# B2019   ??

# a = input()
# print(int(bool(eval(a))))

# B2020

# eat = 0
# start = list(map(int, input().strip().split()))
# for i in range(0, 5):              # 包前不包后
#     if i == 0:
#         eat += start[i] % 3
#         start[4] += start[i] // 3
#         start[i + 1] += start[i] // 3
#     elif i == 4:
#         eat += start[i] % 3
#         start[i - 1] += start[i] // 3
#         start[0] += start[i] // 3
#     else:
#         eat += start[i] % 3
#         start[i - 1] += start[i] // 3
#         start[i + 1] += start[i] // 3
#     start[i] = start[i] // 3
# for i in start:
#     print(i, end=' ')               # 输出为一行，以空格相隔
# print()
# print(eat)

# B2021
# Python float类型主要是双精度浮点型
# import numpy
# a = numpy.float32(input())
# print('%.3f' % a)

# B2022

# a = float(input())
# print('%.12f' % a)

# B2023
# 注意strip()
# import numpy
# a = input().strip()
# b = int(input().strip())
# c = float(input().strip())
# d = numpy.float32(input().strip())
#
# print(a, b, '%.6f' % c, '%.6f' % d, end=' ')

# B2024

# a = float(input().strip())
# print('%f' % a)
# print('%.5f' % a)
# print('%e' % a)
# print('%g' % a)

# B2025

# line = list(map(float, input().strip().split()))
# final = line[0] % line[1]
# print('%.4f' % final)

# B2026

# PI = 3.14
# a = int(input())
# S = 4 / 3 * PI * a * a * a
# print('%.5f' % S)

# B2027

# a = int(input())
# b = a % 10
# c = a // 10 % 10
# d = a // 100
# print('%d' % b + '%d' % c + '%d' % d)

