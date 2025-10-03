"""
utils.py 모듈에 대한 테스트
"""

import unittest
import os
import sys
import tempfile
import json

# 상위 디렉토리의 src 모듈을 import하기 위한 경로 추가
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from utils import create_directory, save_json, load_json, save_csv, get_timestamp, log_message


class TestUtils(unittest.TestCase):
    """유틸리티 함수들에 대한 테스트 클래스"""
    
    def setUp(self):
        """테스트 전 준비"""
        self.test_dir = tempfile.mkdtemp()
    
    def test_create_directory(self):
        """디렉토리 생성 테스트"""
        test_path = os.path.join(self.test_dir, "new_directory")
        result = create_directory(test_path)
        
        self.assertTrue(result)
        self.assertTrue(os.path.exists(test_path))
    
    def test_save_and_load_json(self):
        """JSON 저장 및 로드 테스트"""
        test_data = {
            "name": "테스트",
            "number": 42,
            "list": [1, 2, 3],
            "nested": {"key": "value"}
        }
        
        json_path = os.path.join(self.test_dir, "test.json")
        
        # JSON 저장 테스트
        save_result = save_json(test_data, json_path)
        self.assertTrue(save_result)
        self.assertTrue(os.path.exists(json_path))
        
        # JSON 로드 테스트
        loaded_data = load_json(json_path)
        self.assertEqual(test_data, loaded_data)
    
    def test_save_csv(self):
        """CSV 저장 테스트"""
        test_data = [
            ["김철수", "30", "개발자"],
            ["이영희", "25", "디자이너"]
        ]
        headers = ["이름", "나이", "직업"]
        
        csv_path = os.path.join(self.test_dir, "test.csv")
        
        result = save_csv(test_data, csv_path, headers)
        self.assertTrue(result)
        self.assertTrue(os.path.exists(csv_path))
        
        # 파일 내용 확인
        with open(csv_path, 'r', encoding='utf-8') as f:
            content = f.read()
            self.assertIn("이름,나이,직업", content)
            self.assertIn("김철수,30,개발자", content)
    
    def test_get_timestamp(self):
        """타임스탬프 생성 테스트"""
        timestamp = get_timestamp()
        
        # 타임스탬프 형식 확인 (YYYYMMDD_HHMMSS)
        self.assertEqual(len(timestamp), 15)
        self.assertTrue(timestamp[8] == "_")
        self.assertTrue(timestamp[:8].isdigit())
        self.assertTrue(timestamp[9:].isdigit())
    
    def test_log_message(self):
        """로그 메시지 테스트 (출력 확인용)"""
        # 실제로는 출력을 캡처해서 테스트해야 하지만, 
        # 여기서는 단순히 예외가 발생하지 않는지 확인
        try:
            log_message("테스트 메시지")
            log_message("에러 메시지", "ERROR")
            log_message("경고 메시지", "WARNING")
        except Exception as e:
            self.fail(f"log_message에서 예외 발생: {e}")


if __name__ == "__main__":
    # 테스트 실행
    unittest.main(verbosity=2)