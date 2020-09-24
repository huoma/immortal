# -*- coding: utf-8 -*-
# @Project: code
# @Author : huoma
# @Email  : 2292474203s@gmail.com
# @File   : quickSort.py
# @Create time: 2020/8/14 18:25
import random

# def qs(arr):
#     quick_sort(arr, 0, len(arr)-1)
#
#
# def quick_sort(arr, p, r):
#     if p < r:
#         q = partition(arr, p, r)
#
#         quick_sort(arr, p, q - 1)
#         quick_sort(arr, q + 1, r)
#
#
# def partition(arr, p, r):
#     pivot = arr[p]
#     while p < r:
#         while p < r and arr[r] >= pivot:
#             r -= 1
#         arr[p] = arr[r]
#         while p < r and arr[p] <= pivot:
#             p += 1
#         arr[r] = arr[p]
#     arr[p] = pivot
#     return p
#
#
# qq = [12, 7, 2, 3, 4, 1, 1, 2, 2, 2]
# qs(qq)
# print(qq)
# qq.sort()


# 基准元素为最右边元素，按照算法导论上的来
# def swap(arr, a, b):
#     tmp = arr[a]
#     arr[a] = arr[b]
#     arr[b] = tmp
#
#
# def partition(arr, left, right):
#     i = left - 1
#     pivot = arr[right]
#     for j in range(left, right):  # 问题出在这了，非得加上left,分治之后的数组长度会改变，left,right都会改变
#         if arr[j] <= pivot:  # 非增序排列，arr[j]>=pivot
#             i += 1
#             arr[i], arr[j] = arr[j], arr[i]
#             # swap(arr, i, j)
#     # swap(arr, i + 1, right)
#     arr[i + 1], arr[right] = arr[right], arr[i + 1]
#     return i + 1
#
#
# def quick_sort(arr, left, right):
#     if left < right:
#         q = partition(arr, left, right)
#
#         quick_sort(arr, left, q - 1)
#         quick_sort(arr, q + 1, right)
#
#
# def qs(arr):
#     quick_sort(arr, 0, len(arr) - 1)

# qq = [12, 7, 3, 4, 1, 2, 6]
# print(len(qq))
# qs(qq)
# print(qq)

# a = []
# a += qq[3:]
# print(a)


# 基准元素为首元素
# 设定两个参数i和j，他们的初值分别为待排序列的下界和上界，即i=low，j=high。
# 选取待排序列的第一个元素R[low]为基准元素，并将该值赋值给变量pivot。
# 令j自j位置开始向左扫面，如果j位置所对应的元素的值大于等于pivot，则j前移一个位置（即j- -）。
#     重复该过程，直到找到第一个小于pivot的元素R[j]，将R[j]和R[i]进行交换，i++。 其实交换后R[j]所对应的元素就是pivot。
# 令i自i位置开始向右扫描，如果i位置所对应的元素的值小于等于pivot，则i后移（即i++）。
#     重复该过程，直至找到第一个大于pivot的元素R[i]，将R[i]与R[j]进行交换，j–-。其实交换后R[i]所对应的元素就是pivot。
# 重复步骤3、4，交替改变扫描方向，从两端各自往中间靠拢直至i==j。此时i和j指向同一个位置，即基准元素pivot的最终位置。

#  partition函数双向扫描1(交换法)


def partition(arr, low, high):
    pivot = arr[low]
    while low < high:
        while low < high and pivot <= arr[high]:
            high = high - 1
        arr[high], arr[low] = arr[low], arr[high]
        while low < high and pivot >= arr[low]:
            low = low + 1
        arr[low], arr[high] = arr[high], arr[low]
    return low


def quick_sort(arr, low, high):
    if low < high:
        q = partition(arr, low, high)
        quick_sort(arr, low, q - 1)
        quick_sort(arr, q + 1, high)


def qs(arr):
    quick_sort(arr, 0, len(arr) - 1)


def randomized_partition(arr, low, high):
    i = random.randint(low, high)  # 随机的变化
    arr[i], arr[high] = arr[high], arr[i]
    return partition(arr, low, high)


def randomized_quick_sort(arr, low, high):
    if low < high:  # 分治
        q = randomized_partition(arr, low, high)
        randomized_quick_sort(arr, low, q - 1)
        randomized_quick_sort(arr, q + 1, high)


def rqs(arr):
    randomized_quick_sort(arr, 0, len(arr) - 1)

#  partition函数双向扫描2(填坑法)
# def partition(arr, low, high):
#     pivot = arr[low]
#     while low < high:
#         while low < high and pivot <= arr[high]:
#             high = high - 1
#         arr[low] = arr[high]
#         while low < high and pivot >= arr[low]:
#             low = low + 1
#         arr[high] = arr[low]
#     arr[high] = pivot  # high==low,同时指向一个元素
#     return high
#
#
# def quick_sort(arr, low, high):
#     if low < high:
#         q = partition(arr, low, high)
#         quick_sort(arr, low, q-1)
#         quick_sort(arr, q+1, high)
#
#
# def qs(arr):
#     quick_sort(arr, 0, len(arr)-1)


if __name__ == '__main__':
    qq = [12, 7, 3, 4, 1, 2, 6]
    # qq = [1, 2, 3, 4]
    rqs(qq)
    print(len(qq))
    # qs(qq)
    print(qq)
