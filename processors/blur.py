import cv2

def apply_mosaic(image):
    
    # 예외 처리: 이미지가 없으면 그냥 None 반환
    if image is None:
        print("[Blur] 입력된 이미지가 없습니다.")
        return None

    # Haar Cascade 모델 로드 (얼굴 인식용 미리 학습된 데이터)
    cascade_path = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
    face_cascade = cv2.CascadeClassifier(cascade_path)

    # 그레이스케일 변환 (인식 속도와 정확도를 높이기 위해 흑백으로 변환하여 분석)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 얼굴 탐지 실행
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # 탐지된 얼굴 개수 출력 
    print(f"[Blur] 탐지된 얼굴 개수: {len(faces)}")

    # 탐지된 얼굴 좌표(x, y, w, h)를 돌면서 블러 처리
    for (x, y, w, h) in faces:
       
        roi = image[y:y+h, x:x+w]
        roi = cv2.GaussianBlur(roi, (99, 99), 30)
        image[y:y+h, x:x+w] = roi
    return image


# 👇 테스트용 코드 (이 파일을 직접 실행했을 때만 동작함)
if __name__ == "__main__":
    # 테스트할 이미지 경로 (본인 컴퓨터에 있는 사진 경로로 바꾸세요)
    test_path = "../assets/sample.jpg" 
    # 이미지 읽기
    img = cv2.imread(test_path)
    # 함수 실행
    if img is not None:
        result = apply_mosaic(img)
        # 결과 눈으로 확인하기
        cv2.imshow("Original vs Blur", result)
        cv2.waitKey(0) 
        cv2.destroyAllWindows()
    else:
        print("테스트할 이미지를 찾지 못했습니다. 경로를 확인해주세요.")
