Auto Mosaic Project

얼굴을 자동으로 인식하고 모자이크(블러)를 적용하는 Python 기반 이미지 처리 프로젝트입니다.
OpenCV의 Haar Cascade 모델로 얼굴을 탐지하고 Gaussian Blur로 모자이크 처리를 수행합니다.

1. 프로젝트 개요

이 프로젝트는 다음 기능을 제공합니다:

얼굴 자동 탐지

Gaussian Blur 기반 모자이크 처리

여러 이미지 일괄 처리(batch processing)

입력 / 출력 폴더 자동 관리

확장 가능한 모듈 구조(loader.py, blur.py, main.py)

🗂️ 2. 프로젝트 구조
Auto-Mosaic-Project/
│  main.py
│  README.md
│  requirements.txt
│
├─ assets/                 # 입력 이미지 폴더
├─ output_processed/       # 모자이크 처리된 이미지 저장 폴더
├─ processors/
│     ├─ loader.py         # 이미지 로드/저장/파일 스캔
│     └─ blur.py           # 얼굴 인식 + 모자이크 알고리즘
│
└─ venv/ (가상환경)

🎬 3. 데모 (Before / After)
Before	After
(예시 이미지 삽입)	(모자이크 결과 삽입)

※ 위 이미지는 실제 assets → output_processed 과정을 통해 생성하여 직접 삽입해주세요.

🔧 4. 사용된 패키지 & 버전

requirements.txt 기준:

opencv-python==4.9.0
numpy==1.26.0


필요한 패키지는 자동 설치 가능하며, 버전은 프로젝트 실행 테스트 기준입니다.

📥 5. 설치 방법
1) 가상환경 생성 (선택)
python -m venv venv
source venv/bin/activate       # Mac / Linux
venv\Scripts\activate          # Windows

2) 라이브러리 설치
pip install -r requirements.txt

3) 입력 이미지 준비

assets/ 폴더 안에 처리할 이미지를 넣습니다.

assets/
 ├─ img1.jpg
 ├─ img2.png

▶ 6. 실행 방법
실행 명령어
python main.py

실행 후 출력 위치
output_processed/
 ├─ mosaic_img1.jpg
 ├─ mosaic_img2.png

주요 처리 과정 흐름

assets/ 이미지 스캔

이미지 로드

얼굴 탐지 (Haar Cascade)

Gaussian Blur 적용

output_processed/ 에 자동 저장

🧠 7. 주요 코드 구성
✔ main.py — 전체 플로우 제어

이미지 목록 스캔

모자이크 적용

결과 저장

전체 pipeline 수행

자동 폴더 생성


aa863d48-3679-418a-8f92-32b2f92…

✔ processors/loader.py — 이미지 입출력 유틸리티

이미지 로드 (OpenCV)

이미지 저장 (JPEG/PNG 옵션 자동 적용)

이미지 파일 목록 스캔


9ef323df-aa5d-4165-9fb4-5fdc1e3…

✔ processors/blur.py — 얼굴 인식 + 모자이크 처리

Haar Cascade 기반 얼굴 탐지

ROI 영역에 Gaussian Blur 적용

탐지된 얼굴 수 출력


6295c5e4-0f74-4d5b-8b21-29d28ae…

📚 8. 참고 자료

OpenCV 공식 문서
https://docs.opencv.org/

Haar Cascade 얼굴 탐지 모델
https://github.com/opencv/opencv/tree/master/data/haarcascades

Gaussian Blur 설명
https://docs.opencv.org/4.x/d4/d13/tutorial_py_filtering.html

이미지 처리 기초
https://realpython.com/working-with-images-python/

✨ 9. 기여자 정보

팀원 A — 이미지 로드/저장 모듈(loader.py) 개발

팀원 B — 얼굴 인식 및 모자이크 처리(blur.py) 개발

팀 조립 담당 — main.py 통합 및 전체 실행 구성

필요하면 더 꾸며줄게!

프로젝트 배지(shields.io)

동작 흐름 다이어그램(dot, mermaid)

데모 GIF 제작

FAQ 섹션 추가

전부 추가해줄 수 있어 😊
