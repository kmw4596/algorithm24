'''
def merge_sort(A, left, right):
    if left < right:
        mid = (left + right) // 2
        merge_sort(A, left, mid)
        merge_sort(A, mid + 1, right)
        merge(A, left, mid, right)

def merge(A, left, mid, right):
    L = A[left:mid + 1]
    R = A[mid + 1:right + 1]
    i = j = 0
    k = left
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
        k += 1
    while i < len(L):
        A[k] = L[i]
        i += 1
        k += 1
    while j < len(R):
        A[k] = R[j]
        j += 1
        k += 1
test_list = [12, 11, 13, 5, 6, 7]
print("Original list:", test_list)
merge_sort(test_list, 0, len(test_list) - 1)
print("Sorted list:", test_list)


def partition(A, left, right):
    pivot = A[right]
    i = left - 1
    for j in range(left, right):
        if A[j] <= pivot:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[right] = A[right], A[i + 1]
    return i + 1

def quick_sort(A, left, right):
    if left < right:
        mid = partition(A, left, right)
        quick_sort(A, left, mid - 1)
        quick_sort(A, mid + 1, right)
test_list = [10, 7, 8, 9, 1, 5]
print("Original list:", test_list)
quick_sort(test_list, 0, len(test_list) - 1)
print("Sorted list:", test_list)
'''

def merge(A, left, mid, right):
    k = left
    i = left
    j = mid + 1
    while i <= mid and j <= right:
        if A[i] <= A[j]:
            sorted[k] = A[i]
            i, k = i + 1, k + 1
        else:
            sorted[k] = A[j]
            j, k = j + 1, k + 1
    if i > mid:
        sorted[k:k + right - j + 1] = A[j:right + 1]
    if j > right:
        sorted[k:k + mid - i + 1] = A[i:mid + 1]
    A[left:right + 1] = sorted[left:right + 1]

list1 = [1, 3, 5, 7, 9]
list2 = [2, 4, 6, 8, 10]
print("List 1:", list1)
print("List 2:", list2)

merged_list = list1 + list2
sorted = [0] * len(merged_list)
merge(merged_list, 0, len(list1) - 1, len(merged_list) - 1)
print("Merged and sorted list:", merged_list)
