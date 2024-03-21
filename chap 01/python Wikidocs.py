#파이썬 기본을 갈고 닦자! 19장 (for in 반복문,range,enumerate)
'''
num = int(input("구구단 중 출력할 단을 입력하세요: "))

print(f"구구단 {num}단을 출력합니다:")
for i in range(1, 10):
    print(f"{num} x {i} = {num*i}")
'''
words = input("단어 목록을 입력하세요.: ").split()

print("단어 목록:")
for index, word in enumerate(words):
    print(f"{index}: {word}")

