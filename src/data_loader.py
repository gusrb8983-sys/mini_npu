import json

def load_json(path):
    """JSON 파일을 읽어 딕셔너리로 반환. 실패하면 None과 에러 메시지."""
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)           
    except FileNotFoundError:
        print(f"파일을 찾을 수 없습니다: {path}")
        return None
    except json.JSONDecodeError:
        print(f"JSON 형식이 올바르지 않습니다: {path}")
        return None
    return data

def parse_size_from_key(key):
    """'size_5_1' 같은 패턴 키에서 크기(N)를 추출. 형식이 이상하면 None 반환."""
    parts = key.split("_")    
    try:
        n = int(parts[1])               
    except (IndexError, ValueError):
        return None
    return n

def get_filter_set(data, n):
    """data['filters']에서 size_N에 해당하는 필터 세트(dict)를 반환.
       해당 크기가 없으면 None."""
    key = f"size_{n}"
    return data["filters"].get(key)