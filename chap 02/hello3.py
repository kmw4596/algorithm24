def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

# 팩토리얼 함수를 테스트하기 위한 테스트 코드
def test_factorial():
    test_cases = [0, 1, 2, 3, 4, 5]  # 테스트할 입력값
    expected_results = [1, 1, 2, 6, 24, 120]  # 각 입력값에 대한 기대 결과

    for i, test_case in enumerate(test_cases):
        result = factorial(test_case)
        expected_result = expected_results[i]
        print(f"Test case {test_case}: Expected {expected_result}, Result: {result}")

# 테스트 실행
test_factorial()
