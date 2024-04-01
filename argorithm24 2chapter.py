#알고리즘2.6 이진수 변환에서 총 비트수 계산(반복 알고리즘)
'''
def binary_digits(n):
    count = 1
    while n > 1:
        count = count +1
        n = n // 2
    return count

number = int(input("양의 정수를 입력하세요: "))

result = binary_digits(number)
print("총 비트수:", result)
'''

#알고리즘2.7 순환적인 팩토리얼 알고리즘(순환 알고리즘)

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
    
number = int(input("숫자를 입력하시오: "))
result = factorial(number)
print(result)