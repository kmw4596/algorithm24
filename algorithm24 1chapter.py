def gcd(a,b):
    while(b !=0):
        r = a%b
        a = b
        b =r
    return a

num1 = int(input("첫 번째 숫자를 입력하세요: "))
num2 = int(input("두 번째 숫자를 입력하세요: "))

num =gcd(num1, num2)
print("두 숫자의 최대공약수는", num, "입니다.")
