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
