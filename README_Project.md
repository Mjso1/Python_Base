# Python_Base 프로젝트

Python 개발을 위한 기본 구성과 Jupyter Notebook 개발 환경입니다.

## 프로젝트 구조

```
Python_Base/
├── notebooks/          # Jupyter 노트북 파일들
│   └── 01_Python_Basics.ipynb
├── data/               # 데이터 파일들
├── src/                # Python 소스 코드
├── output/             # 결과 파일들
├── tests/              # 테스트 파일들
├── requirements.txt    # 패키지 의존성
└── README.md          # 프로젝트 설명
```

## 설치된 패키지

### 핵심 패키지
- **Jupyter**: 대화형 노트북 환경
- **JupyterLab**: 고급 웹 기반 개발 환경
- **NumPy**: 수치 계산 라이브러리
- **Pandas**: 데이터 조작 및 분석
- **Matplotlib**: 기본 시각화 라이브러리
- **Seaborn**: 고급 통계 시각화

### 머신러닝 & 분석
- **Scikit-learn**: 머신러닝 라이브러리
- **Plotly**: 인터랙티브 시각화

### 개발 도구
- **pytest**: 테스트 프레임워크
- **black**: 코드 포매터
- **flake8**: 코드 린터
- **mypy**: 타입 체커

## 시작하기

### 1. 환경 설정
```bash
# Python 환경이 설정되어 있는지 확인
python --version

# 패키지 설치
pip install -r requirements.txt
```

### 2. Jupyter 실행
```bash
# Jupyter Notebook 실행
jupyter notebook

# 또는 JupyterLab 실행
jupyter lab
```

### 3. 기본 사용법
1. `notebooks/01_Python_Basics.ipynb`에서 Python 기본 문법 학습
2. `data/` 폴더에 분석할 데이터 저장
3. `src/` 폴더에 재사용 가능한 Python 모듈 작성
4. `output/` 폴더에 결과 저장

## 노트북 가이드

### 01_Python_Basics.ipynb
Python 개발의 기본기를 다루는 노트북입니다:

1. **필수 라이브러리 가져오기** - 환경 설정 및 라이브러리 import
2. **기본 데이터 타입** - 문자열, 숫자, 불린 등
3. **변수와 연산자** - 산술, 비교, 논리 연산
4. **제어 구조** - 조건문과 반복문
5. **함수** - 함수 정의 및 활용
6. **데이터 구조** - 리스트와 딕셔너리
7. **파일 처리** - 텍스트 파일 읽기/쓰기
8. **예외 처리** - 오류 처리 및 안정적인 코드

## 개발 팁

### VS Code에서 Jupyter 사용
1. Python 확장 설치
2. Jupyter 확장 설치
3. `.ipynb` 파일을 VS Code에서 직접 편집 가능

### 가상환경 사용 (권장)
```bash
# 가상환경 생성
python -m venv venv

# 가상환경 활성화 (Windows)
venv\Scripts\activate

# 가상환경 활성화 (macOS/Linux)
source venv/bin/activate

# 패키지 설치
pip install -r requirements.txt
```

## 추가 학습 자료

### 공식 문서
- [Python 공식 문서](https://docs.python.org/3/)
- [Jupyter 문서](https://jupyter.org/documentation)
- [NumPy 문서](https://numpy.org/doc/stable/)
- [Pandas 문서](https://pandas.pydata.org/docs/)

### 추천 학습 순서
1. Python 기본 문법 (이 노트북)
2. NumPy 배열 조작
3. Pandas 데이터프레임
4. Matplotlib/Seaborn 시각화
5. 머신러닝 기초 (Scikit-learn)

## 라이선스

이 프로젝트는 학습 목적으로 자유롭게 사용 가능합니다.