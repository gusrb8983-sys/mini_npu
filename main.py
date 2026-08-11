from io_console import read_grid, print_grid
from mac import mac
from judge import judge

print("=== Mini NPU Simulator ===")
print("[모드 선택]")
print("1. 사용자 입력 (3x3)")
print("2. data.json 분석")
choice = input("선택: ")

if choice == "1":
    filter_a = read_grid(3, "필터 A")
    print_grid(filter_a, "필터 A")

    filter_b = read_grid(3, "필터 B")
    print_grid(filter_b, "필터 B")

    pattern = read_grid(3, "패턴")
    print_grid(pattern, "패턴")

    score_a = mac(pattern, filter_a, 3)
    score_b = mac(pattern, filter_b, 3)

    result = judge(score_a, score_b)
    display = "판정 불가" if result == "UNDECIDED" else result

    print("A 점수:", score_a)
    print("B 점수:", score_b)
    print(f"판정: {display}")