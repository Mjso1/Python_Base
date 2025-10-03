"""
Python 개발을 위한 유틸리티 함수들
"""

import os
import json
import csv
from datetime import datetime
from typing import List, Dict, Any


def create_directory(path: str) -> bool:
    """
    디렉토리를 생성합니다.
    
    Args:
        path: 생성할 디렉토리 경로
    
    Returns:
        bool: 성공 여부
    """
    try:
        os.makedirs(path, exist_ok=True)
        return True
    except Exception as e:
        print(f"디렉토리 생성 실패: {e}")
        return False


def save_json(data: Dict[str, Any], filepath: str) -> bool:
    """
    딕셔너리를 JSON 파일로 저장합니다.
    
    Args:
        data: 저장할 데이터
        filepath: 저장할 파일 경로
    
    Returns:
        bool: 성공 여부
    """
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        return True
    except Exception as e:
        print(f"JSON 저장 실패: {e}")
        return False


def load_json(filepath: str) -> Dict[str, Any]:
    """
    JSON 파일을 로드합니다.
    
    Args:
        filepath: 로드할 파일 경로
    
    Returns:
        Dict: 로드된 데이터
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"JSON 로드 실패: {e}")
        return {}


def save_csv(data: List[List[str]], filepath: str, headers: List[str] = None) -> bool:
    """
    리스트 데이터를 CSV 파일로 저장합니다.
    
    Args:
        data: 저장할 데이터
        filepath: 저장할 파일 경로
        headers: 컬럼 헤더
    
    Returns:
        bool: 성공 여부
    """
    try:
        with open(filepath, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            if headers:
                writer.writerow(headers)
            writer.writerows(data)
        return True
    except Exception as e:
        print(f"CSV 저장 실패: {e}")
        return False


def get_timestamp() -> str:
    """
    현재 시간의 타임스탬프를 반환합니다.
    
    Returns:
        str: 타임스탬프 문자열
    """
    return datetime.now().strftime("%Y%m%d_%H%M%S")


def log_message(message: str, level: str = "INFO") -> None:
    """
    로그 메시지를 출력합니다.
    
    Args:
        message: 로그 메시지
        level: 로그 레벨
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] {level}: {message}")


if __name__ == "__main__":
    # 테스트 코드
    print("유틸리티 모듈 테스트")
    
    # 디렉토리 생성 테스트
    test_dir = "../output/test"
    if create_directory(test_dir):
        log_message("테스트 디렉토리 생성 성공")
    
    # JSON 저장/로드 테스트
    test_data = {
        "name": "테스트",
        "version": "1.0",
        "timestamp": get_timestamp()
    }
    
    json_path = f"{test_dir}/test_data.json"
    if save_json(test_data, json_path):
        log_message("JSON 저장 성공")
        loaded_data = load_json(json_path)
        log_message(f"JSON 로드 성공: {loaded_data}")
    
    # CSV 저장 테스트
    csv_data = [
        ["김철수", "30", "개발자"],
        ["이영희", "25", "디자이너"],
        ["박민수", "35", "기획자"]
    ]
    headers = ["이름", "나이", "직업"]
    
    csv_path = f"{test_dir}/test_data.csv"
    if save_csv(csv_data, csv_path, headers):
        log_message("CSV 저장 성공")