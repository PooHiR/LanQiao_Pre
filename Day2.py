# B2029

# h, r = map(int, input().strip().split())
# a = 20000 / (3.14 * r * r * h) + 1
# print('%d' % a)
import math


# B2030

# import math
#
# a = list(map(int, input().strip().split()))
# b = list(map(int, input().strip().split()))
# final = math.sqrt((a[0] - b[0]) * (a[0] - b[0]) + (a[1] - b[1]) * (a[1] - b[1]))
# print('%.3f' % final)

# B2031

# import math             # 记得导入使用的包
# def dis(x1, y1, x2, y2):
#     return math.sqrt(math.pow((x1 - x2), 2) + math.pow((y1 - y2), 2))
#
#
# line = list(map(float, input().strip().split()))
# x1 = line[0]
# y1 = line[1]
# x2 = line[2]
# y2 = line[3]
# x3 = line[4]
# y3 = line[5]
#
# a = dis(x1, y1, x2, y2)
# b = dis(x2, y2, x3, y3)
# c = dis(x3, y3, x1, y1)
#
# p = (a + b + c) / 2
#
# print('%.2f' % math.sqrt(p * (p - a) * (p - b) * (p - c)))

# B2032

# line = list(map(int, input().strip().split()))
# a1 = line[0]
# a2 = line[1]
# number = line[2]
# wide = a2 - a1
# anumber = a1 + wide * (number - 1)
# print(anumber)

# B2033

# a, b = map(float, input().strip().split())
# final = a * b
# print("%d" % final)

# B2034

# import math
# n = int(input())
# print('%d' % math.pow(2, n))

# B2035

# N = float(input())
# if N > 0:
#     print('positive')
# elif N == 0:
#     print('zero')
# else:
#     print('negative')

# B2036

# import numpy
# n = numpy.float32(input())
# print('%.2f' % abs(n))

# B2037

# n = int(input())
# if n % 2 == 0:
#     print('even')
# else:
#     print('odd')

# B2038

# a = input()
# number = ord(a)
# if number % 2 == 0:
#     print('NO')
# else:
#     print('YES')

# B2039

# a, b = map(float, input().strip().split())
# if a > b:
#     print('>')
# elif a == b:
#     print('=')
# else:
#     print('<')

# B2040

# a = int(input())
# if a < 10 or a > 99:
#     print('0')
# else:
#     print('1')

# B2041

# a, b = map(int, input().strip().split())
# if a >= 10 or b >= 20:
#     print('1')
# else:
#     print('0')

# B2042

# a = int(input())
# if a % 3 == 0 and a % 5 == 0:
#     print('YES')
# else:
#     print('NO')

# B2043

# final = []
# x = int(input())
# if x % 3 == 0:
#     final += [3]
# if x % 5 == 0:
#     final += [5]
# if x % 7 == 0:
#     final += [7]
# if final:
#     for i in final:
#         print(i, end=' ')
# else:
#     print('n')

# B2044

# number = 0
# line = list(map(int, input().strip().split()))
# for i in line:
#     if i < 60:
#         number += 1
# if number == 1:
#     print('1')
# else:
#     print('0')

# B2045

# bad = [1, 3, 5]
# Flag = 0
# a = int(input())
# for i in bad:
#     if i == a:
#         print('NO')
#         Flag = 1
# if Flag != 1:
#     print('YES')

# B2046
# import numpy
#
# a = numpy.float32(input())
# walk_time = a / 1.2
# Bike_time = a / 3.0 + 50
# if walk_time == Bike_time:
#     print('All')
# elif walk_time > Bike_time:
#     print('Bike')
# else:
#     print('Walk')

# B2047
# import numpy
#
# x = numpy.float32(input())
# if 0 <= x < 5:
#     ans = -x + 2.5
# elif 5 <= x < 10:
#     ans = 2 - 1.5 * (x - 3) * (x - 3)
# else:
#     ans = x / 2 - 1.5
# print('%.3f' % ans)

# B2048

# a, b = input().strip().split()
# A = int(a)
# if A <= 1000:
#     First = 8
# else:                                    # 注意判断整除的情况
#     if (A - 1000) % 500 == 0:
#         First = 8 + ((A - 1000) // 500) * 4
#     else:
#         First = 8 + ((A - 1000) // 500 + 1) * 4
# if b == 'n':
#     print('%d' % First)
# else:
#     First += 5
#     print('%d' % First)

# B2049

# MAX = -9223372036854775808  # 注意负数 不能初值设为0
# line = list(map(int, input().strip().split()))
# for i in line:
#     if i > MAX:
#         MAX = i
# print(MAX)

# B2050

# a, b, c = map(int, input().strip().split())
# if a + b <= c or a + c <= b or b + c <= a:
#     print('0')
# else:
#     print('1')

# B2051

# x ,y = map(int, input().strip().split())
# if -1 <= x <= 1 and -1 <= y <= 1:
#     print('yes')
# else:
#     print('no')

# B2052

# a, b, c = input().split()         #WA 不知为何 用此通过
# a = int(a)
# b = int(b)
# if c == "+":
#     print(a+b)
# elif c == "-":
#     print(a-b)
# elif c == "*":
#     print(a*b)
# elif c == "/":
#     if b == 0:
#         print("Divided by zero!")
#     else:
#         print(a//b)
# else:
#     print("Invalid operator!")

# B2065

# a = int(input())
# ans = []
# for i in range(0, a):
#     a, b = map(int, input().strip().split())
#     if i == 0:
#         x = b / a
#     else:
#         y = b / a
#         if x - y > 0.05:
#             ans.append('worse')
#         elif y - x > 0.05:
#             ans.append('better')
#         else:
#             ans.append('same')
# print(*ans, sep='\n')    # 解包数组，换行逐个输出

# B2066

# import math
#
# n = int(input())
# ans = 0
# for _ in range(n):
#     line = list(map(float, input().strip().split()))
#     distance_time = math.hypot(line[0], line[1]) / 50 * 2   # math.hypot() 求三角形斜边
#     people_time = line[2] * 1.5
#     ans += distance_time + people_time
# print(math.ceil(ans))

# B2067

# total = int(input())
# people = int(input())
# line = list(map(int, input().strip().split()))
# ans = 0
# for i in range(0, people):
#     if total >= line[i]:
#         total -= line[i]
#     else:
#         ans += 1
# print(ans)
