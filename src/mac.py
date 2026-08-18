def mac(pattern, filt, n):
    total = 0.0                          # ① 점수 저장소. 0.0으로 시작
    for i in range(n):                   # ② 행 순회
        for j in range(n):               # ③ 열 순회
            total += pattern[i][j] * filt[i][j]   # ④ 곱해서 누적
    return total                         # ⑤ 최종 점수 돌려주기