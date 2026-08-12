import time
from mac import mac

def measure_mac_time(pattern, filt, n, repeat=10):
    """MAC 연산을 repeat번 반복 측정해 평균 시간(ms)을 반환"""
    times = []
    for _ in range(repeat):
        start = time.perf_counter()
        mac(pattern, filt, n)
        end = time.perf_counter()
        times.append((end - start) * 1000)
    average = sum(times)/len(times)
    return average

def make_dummy_grid(n):
    """성능 측정 전용 n×n 격자 생성 (값 자체는 의미 없음)"""
    return [[1.0 for _ in range(n)] for _ in range(n)]

def print_performance_table(sizes):
    print(f"{'크기':<10}{'평균 시간(ms)':<16}{'연산 횟수':<10}")
    print("-" * 40)
    for n in sizes:
        pattern = make_dummy_grid(n)
        filt = make_dummy_grid(n)
        avg_ms = measure_mac_time(pattern, filt, n)
        op_count = n ** 2
        label = f"{n}×{n}"
        print(f"{label:<10}{avg_ms:<16.3f}{op_count:<10}")