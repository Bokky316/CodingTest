import sys

# 1. 구구단 출력하기
def multiplication_table():
    N = int(input())
    for _ in range(9):
        print(N, "*", _ + 1, "=", N * (_ + 1))

# 2. 여러 번의 A+B 계산
def sum_multiple():
    T = int(input())
    for _ in range(T):
        a, b = map(int, input().split())
        print(a + b)

# 3. 1부터 n까지의 합 구하기
def sum_up_to_n():
    n = int(input())
    Sn = (1 + n) * n // 2
    print(Sn)

# 4. 영수증 검증하기
def receipt_check():
    x = int(input())
    n = int(input())
    t = 0
    for _ in range(n):
        a, b = map(int, input().split())
        t += a * b
    print("Yes" if x == t else "No")

# 5. 코딩은 체육과목입니다 (long 키워드 출력)
def coding_as_pe():
    n = int(input())
    for _ in range(n // 4):
        print("long", end=" ")
    print("int")

# 6. 빠른 A+B 계산
def quick_sum():
    T = int(sys.stdin.readline())
    for _ in range(T):
        a, b = map(int, sys.stdin.readline().split())
        print(a + b)

# 7. 케이스 번호와 함께 A+B 출력
def sum_with_case_number():
    T = int(sys.stdin.readline())
    for i in range(T):
        a, b = map(int, sys.stdin.readline().split())
        print(f"Case #{i + 1}: {a + b}")

# 8. 자세한 케이스와 함께 A+B 출력
def sum_with_detailed_case():
    T = int(sys.stdin.readline())
    for i in range(T):
        a, b = map(int, sys.stdin.readline().split())
        print(f"Case #{i + 1}: {a} + {b} = {a + b}")

# 9. 왼쪽 정렬 별 찍기
def print_stars_left_aligned():
    n = int(sys.stdin.readline())
    for i in range(1, n + 1):
        print('*' * i)

# 10. 오른쪽 정렬 별 찍기
def print_stars_right_aligned():
    n = int(sys.stdin.readline())
    for i in range(1, n + 1):
        print(('*' * i).rjust(n))

# 11. 0이 나올 때까지 A+B 계산
def sum_until_zero():
    while True:
        a, b = map(int, sys.stdin.readline().split())
        if a == 0 and b == 0:
            break
        print(a + b)

# 12. 예외 처리를 통한 A+B 계산
def sum_with_exception_handling():
    while True:
        try:
            a, b = map(int, sys.stdin.readline().split())
            print(a + b)
        except:
            break