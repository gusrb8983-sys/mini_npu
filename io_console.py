def read_line(n, prompt):
    """숫자 n개짜리 한 줄을 입력받아 리스트로 반환"""
    while True:
        s = input(prompt)
        try:
            row = [float(x) for x in s.split()]  # 공백으로 나누어 float로 변환
        except ValueError:
            print("숫자만 공백으로 구분해 입력하세요.")
            continue

        if len(row) != n:
            print(f"{n}개의 숫자를 입력하세요.")
            continue
        return row      # 성공했을 때만 반환


def read_grid(n, title):
    """n줄을 입력받아 n×n 2차원 리스트로 반환"""
    print(f"{title} ({n}줄 입력, 공백 구분)")
    grid = []
    for i in range(n):
        row = read_line(n, "")  # read_line을 호출해서
        grid.append(row)                     # grid에 추가
    return grid

def print_grid(grid, title):
    print(f"[{title} 저장 완료]")
    for row in grid:
        print(" ".join(str(int(v)) if v == int(v) else str(v) for v in row))