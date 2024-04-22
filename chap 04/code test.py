'''
def insertion_sort(A):
    n = len(A)
    for i in range(1, n):
        key = A[i]
        j = i - 1
        while j >= 0 and A[j] > key:
            A[j + 1] = A[j]
            j = j - 1
        A[j + 1] = key

def print_list(arr):
    for element in arr:
        print(element, end=" ")
    print()

test_list = [5, 2, 4, 6, 1, 3]

print("Original list:")
print_list(test_list)

insertion_sort(test_list)

print("Sorted list:")
print_list(test_list)
'''
'''
def binary_search(A, key, low, high):
    if low <= high:
        mid = (low + high) // 2
        if key == A[mid]:
            return mid
        elif key < A[mid]:
            return binary_search(A, key, low, mid - 1)
        else:
            return binary_search(A, key, mid + 1, high)
    return -1

test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
key = 5
result = binary_search(test_list, key, 0, len(test_list) - 1)
if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")

def slow_power(x, n):
    result = 1.0
    for i in range(n):
        result = result * x
    return result

x = 2
n = 3
result = slow_power(x, n)
print(f"{x}의 {n} 거듭제곱 값은 {result}입니다.")
'''
def quick_select(A, left, right, k):
    pos = partition(A, left, right)
    if pos + 1 == k:
        return A[pos]
    elif pos + 1 > k:
        return quick_select(A, left, pos - 1, k)
    else:
        return quick_select(A, pos + 1, right, k)

def partition(A, left, right):
    pivot = A[right]
    i = left - 1
    for j in range(left, right):
        if A[j] <= pivot:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[right] = A[right], A[i + 1]
    return i + 1

# 테스트 리스트
test_list = [3, 2, 1, 5, 4]
# k번째 작은 수
k = 3
# k번째 작은 수 찾기
result = quick_select(test_list, 0, len(test_list) - 1, k)
print(f"{k}번째 작은 수는 {result}입니다.")
