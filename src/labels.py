LABEL_MAP = {
    "+": "Cross",
    "cross": "Cross",
    "x": "X",
}

def normalize_label(raw):
    """'+'/'x'/'cross' 등 다양한 표기를 표준 라벨(Cross/X)로 변환.
       매핑에 없는 값이면 None 반환."""
    return LABEL_MAP.get(raw)

RESULT_MAP = {
    "A": "Cross",
    "B": "X",
    "UNDECIDED": "UNDECIDED",   # 이건 그대로 유지
}

def to_standard_label(judge_result):
    """judge()가 낸 'A'/'B'/'UNDECIDED'를 표준 라벨(Cross/X/UNDECIDED)로 변환."""
    return RESULT_MAP.get(judge_result)