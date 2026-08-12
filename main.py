from perf import print_performance_table
from io_console import read_grid, print_grid
from mac import mac
from judge import judge
from data_loader import load_json, parse_size_from_key, get_filter_set
from labels import normalize_label, to_standard_label

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
    print()
    print_performance_table([3])

elif choice == "2":
    data = load_json("data.json")
    if data is None:
        print("data.json을 불러올 수 없어 모드 2를 진행할 수 없습니다.")
    else:
        for key, pattern_info in data["patterns"].items():
            n = parse_size_from_key(key)
            if n is None:
                print(f"{key}: 키 형식 오류 → FAIL")
                continue

            filter_set = get_filter_set(data, n)
            if filter_set is None:
                print(f"{key}: size_{n} 필터를 찾을 수 없음 → FAIL")
                continue

            try:
                pattern = pattern_info["input"]
                expected_raw = pattern_info["expected"]
                cross_filter = filter_set["cross"]
                x_filter = filter_set["x"]
            except KeyError as e:
                print(f"{key}: 스키마 오류 (누락된 키: {e}) → FAIL")
                continue

            if len(pattern) != n:
                print(f"{key}: 패턴 크기가 {n}이 아님 → FAIL")
                continue

            cross_score = mac(pattern, cross_filter, n)
            x_score = mac(pattern, x_filter, n)

            result = judge(cross_score, x_score)
            my_label = to_standard_label(result)
            expected_label = normalize_label(expected_raw)
            pass_fail = "PASS" if my_label == expected_label else "FAIL"

            print(f"--- {key} ---")
            print(f"Cross 점수: {cross_score}")
            print(f"X 점수: {x_score}")
            print(f"판정: {my_label} | expected: {expected_label} | {pass_fail}")

        print()
        print_performance_table([3, 5, 13, 25])