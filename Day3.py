# B2068
import math


# num = int(input())
# line = list(map(int, input().strip().split()))
# ans = 0
# for i in range(0, num):
#     ge = line[i] % 10
#     shi = line[i] % 100 // 10
#     bai = line[i] // 100 % 10
#     qian = line[i] // 1000
#     if ge - shi - bai - qian > 0:
#         ans += 1
# print(ans)

# B2069

# n = int(input())
# a = 2
# b = 1
# ans = 0
# for i in range(1, n + 1):
#     ans += a / b
#     temp = b
#     b = a
#     a += temp
# print('%.4f' % ans)

# B2070

# n = int(input())
# ans = 0
# num = 1
# for i in range(1, n+1):
#     if i % 2 != 0:
#         ans += 1 / num
#         num += 1
#     else:
#         ans += 1 / num * -1
#         num += 1
# print('%.4f' % ans)

# B2071

# line = list(map(int, input().strip().split()))
# x = 2
# flag = 1
# while flag:
#     a = line[0] % x
#     b = line[1] % x
#     c = line[2] % x
#     if a == b & b == c:
#         flag = 0
#     else:
#         x += 1
# print(x)

# B2072

# n = int(input())
# num = 1
# ans = 0
# for i in range(0, n):
#     ans += num
#     num += 1
# print(ans)

# B2073

# a, b, No = list(map(int, input().strip().split()))  # 模拟竖式算数
# c = a % b
# for i in range(0, No):
#     d = c * 10 // b
#     c = c * 10 % b
# print(d)

# B2074

# dic = {'1': 'Monday', '2': 'Tuesday', '3': 'Wednesday',
#        '4': 'Thursday', '5': 'Friday', '6': 'Saturday', '0': 'Sunday'}
#
# ans = 1
# a, b = list(map(int, input().strip().split()))  # 边模边乘
# for i in range(1, b + 1):
#     ans *= a
#     ans %= 7
# print(dic.get('%s' % str(ans)))

# B2075

# a, b = list(map(int, input().strip().split()))
# c = 1
# for i in range(1, b + 1):
#     c *= a
#     c %= 1000
# print('%03d' % c)

# B2076

# h = float(input())
# count = 0
# for i in range(0, 10):
#     if i == 0:
#         count += h
#         h /= 2.0
#     else:
#         count += 2 * h
#         h /= 2.0
# print('%.4f' % count)
# print('%.7f' % h)

# B2077

# N = int(input())
# flag = 1
# while flag:
#     if N == 1:
#         flag = 0
#         print('End')
#         break
#     if N % 2 != 0:
#         Fir = N
#         N = N * 3 + 1
#         print(str(Fir) + '*3+1=' + str(N))
#     else:
#         Fir = N
#         N = N // 2
#         print(str(Fir) + '/2=' + str(N))

# B2078

# m, k = list(map(str, input().strip().split()))
# ans = 0
# for i in m:
#     if i == '3':
#         ans += 1
# if str(ans) == k:
#     print('YES')
# else:
#     print('NO')

# B2079

# n = int(input())
# e = 1
# total = 1
# for i in range(1, n+1):
#     total *= i
#     e += 1 / total
# print('%.10f' % e)

# 2080

# import math
# import numpy
#
# x, n = list(map(numpy.float32, input().strip().split()))
# n = int(n)
# ans= 0
# for i in range(0, n+1):
#     ans += math.pow(x, i)
# print('%.2f' % ans)

# 2081

# n = int(input())
# ans = 0
# for i in range(1, n+1):
#     m = str(i)
#     if i % 7 == 0:
#         continue
#     else:
#         if '7' not in m:
#             ans += i * i
# print(ans)

# 2082

# x, y = list(map(int, input().strip().split()))
# ans = 0
# for i in range(x, y+1):
#     i_1 = str(i)
#     for j in i_1:
#         if j == '2':
#             ans += 1
# print(ans)

# 2083

# a, b, c, f = list(map(str, input().strip().split()))
# a = int(a)
# b = int(b)
# f = int(f)
# ans = ''
# if f == 0:
#     d = ' '
# else:
#     d = '%s' % c
# for i in range(0, a):
#     for j in range(0, b):
#         if i == 0 or i == a - 1:
#             ans += '%s' % c
#         elif j == 0 or j == b-1:
#             ans += '%s' % c
#         else:
#             ans += '%s' % d
#     print(ans)
#     ans = ''


# 2084

# n = int(input())
# for i in range(2, n+1):
#     if n % i == 0:      # 从最小的开始查找 找到最小的那个值，反除就可以得到最大的
#         print('%d' % (n / i))
#         break

# ans = [0,0]
# n = int(input())
# for i in range(1, n + 1):
#     line = list(map(int, input().strip().split()))
#     if line[0] == line[1]:
#         continue;
#     elif 20 in line and 10 in line or 20 in line and 5 in line:
#         if line[0] == 20:
#             ans[1] += 10
#         else:
#             ans[0] += 10
#     else:
#         if line[0] > line[1]:
#             ans[0] += line[0] - line[1]
#         else:
#             ans[1] += line[1] - line[0]
# print(' '.join(str(x) for x in ans))

# ans = 0
# s = str(input())
# length = len(s)
# for i in range(0,length-2):
#     if s[i] != 'Q':
#         continue;
#     else:
#         for j in range(i + 1,length-1):
#             if s[j] != 'A':
#                 continue;
#             else:
#                 for k in range(j + 1, length):
#                     if s[k] != 'Q':
#                         continue;
#                     else:
#                         ans += 1
# print(ans)

