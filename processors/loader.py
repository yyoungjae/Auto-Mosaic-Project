import cv2
import os
import glob
import numpy as np 

# 이미지 확장자 목록 (이 목록에 있는 파일만 처리 대상으로 간주합니다.)
IMAGE_EXTENSIONS = ['*.jpg', '*.jpeg', '*.png', '*.bmp', '*.tiff']

def load_image(file_path):
    """
    주어진 경로에서 이미지를 읽어 OpenCV(Numpy 배열) 형식으로 반환합니다.
    
    Args:
        file_path (str): 로드할 이미지 파일의 경로.
        
    Returns:
        numpy.ndarray or None: 로드된 이미지 데이터 (Numpy 배열). 파일을 찾지 못하면 None을 반환합니다.
    """
    if not os.path.exists(file_path):
        print(f"[ERROR] 파일을 찾을 수 없습니다: {file_path}")
        return None
        
    # cv2.imread를 사용하여 이미지를 읽습니다. (기본 BGR 형식)
    image = cv2.imread(file_path, cv2.IMREAD_COLOR)
    
    if image is None:
        print(f"[ERROR] 이미지 파일을 로드하는 데 실패했습니다: {file_path}")
        
    return image

def save_image(image, file_path, quality=95):
    """
    처리된 이미지를 지정된 경로에 저장합니다.
    
    Args:
        image (numpy.ndarray): 저장할 이미지 데이터 (OpenCV 형식).
        file_path (str): 저장할 파일의 경로 및 이름.
        quality (int): JPEG 압축 품질 (0-100).
        
    Returns:
        bool: 저장 성공 여부 (True/False).
    """
    # 저장 경로의 디렉토리가 없으면 생성합니다.
    output_dir = os.path.dirname(file_path)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # 파일 확장자에 따라 압축 옵션을 설정합니다.
    extension = os.path.splitext(file_path)[1].lower()
    params = []
    
    if extension in ('.jpg', '.jpeg'):
        # JPEG 품질 설정
        params = [cv2.IMWRITE_JPEG_QUALITY, quality]
    elif extension == '.png':
        # PNG 압축 레벨 설정
        params = [cv2.IMWRITE_PNG_COMPRESSION, min(9, max(0, int(quality / 10)))]

    # cv2.imwrite를 사용하여 이미지를 저장합니다.
    success = cv2.imwrite(file_path, image, params=params)
    
    if not success:
        print(f"[ERROR] 이미지 저장에 실패했습니다: {file_path}")
        
    return success

def get_image_files(folder_path):
    """
    주어진 폴더 내에 있는 모든 이미지 파일의 경로 리스트를 가져옵니다.
    """
    if not os.path.isdir(folder_path):
        print(f"[ERROR] 유효하지 않은 폴더 경로입니다: {folder_path}")
        return []
        
    image_list = []
    for ext in IMAGE_EXTENSIONS:
        # glob.glob을 사용하여 패턴과 일치하는 모든 파일 경로를 찾습니다.
        pattern = os.path.join(folder_path, ext)
        image_list.extend(glob.glob(pattern))
        
    return sorted(image_list)

if __name__ == '__main__':
    # 이 파일 단독 테스트를 위한 임시 실행 코드
    print("--- loader.py 자가 테스트 ---")
    
    # 1. 가상의 파일 경로 설정
    TEST_IMAGE_PATH = "assets/test_image.jpg"
    OUTPUT_FOLDER = "processed_test"
    OUTPUT_IMAGE_PATH = os.path.join(OUTPUT_FOLDER, "mosaic_result.jpg")
    
    # 2. 이미지 로드 테스트 (실패 예상)
    print(f"이미지 로드 시도: {TEST_IMAGE_PATH}")
    test_image = load_image(TEST_IMAGE_PATH)

    if test_image is None:
        print("테스트 이미지가 없으므로, 더미 이미지를 생성하여 테스트를 계속합니다.")
        # 300x200, 3채널(BGR)의 흰색 이미지 생성
        test_image = np.full((200, 300, 3), 255, dtype=np.uint8) 
        
    # 3. 이미지 저장 테스트
    print(f"더미 이미지 저장 시도: {OUTPUT_IMAGE_PATH}")
    if save_image(test_image, OUTPUT_IMAGE_PATH):
        print(f"이미지 저장 성공: {OUTPUT_IMAGE_PATH}")
    
    # 4. 이미지 목록 가져오기 테스트
    print(f"assets 폴더의 이미지 파일 목록 가져오기 시도: assets/")
    image_files = get_image_files("assets/")
    
    if image_files:
        print(f"발견된 이미지 파일 수: {len(image_files)}")
    else:
        print("assets/ 폴더에서 이미지 파일을 찾지 못했습니다. (이미지 파일을 넣으면 숫자가 늘어납니다.)")
        
    print("--- 테스트 완료 ---")