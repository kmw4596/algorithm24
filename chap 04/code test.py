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
