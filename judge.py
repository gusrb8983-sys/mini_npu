EPSILON = 1e-9

def judge(score_a, score_b):
    """두 점수를 비교해 'A', 'B', 'UNDECIDED' 중 하나를 반환"""
    if abs(score_a - score_b) < EPSILON:
        return "UNDECIDED"
    elif score_a > score_b:
        return "A"
    else:
        return "B"