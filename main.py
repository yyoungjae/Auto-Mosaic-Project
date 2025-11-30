#commit을 위한 파일 변경
import os
# [팀원 A]가 완성한 기능 import
from processors.loader import load_image, save_image, get_image_files

# [팀원 B]가 완성할 기능 import (현재 blur.py 파일이 없으므로 임시 예외 처리)
try:
    from processors.blur import apply_mosaic
except ImportError:
    # blur.py가 구현되지 않았을 때 임시로 사용할 더미 함수
    def apply_mosaic(image):
        print("경고: apply_mosaic() 함수가 아직 구현되지 않았습니다. 원본 이미지를 반환합니다.")
        return image


# --- 환경 설정 및 경로 정의 ---
APP_TITLE = "자동 모자이크 처리기"
ASSETS_DIR = "assets"
OUTPUT_DIR = "output_processed"

def setup_directories():
    """필요한 출력 폴더가 없으면 생성합니다."""
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
        print(f"[{APP_TITLE}] 출력 폴더 생성: {OUTPUT_DIR}")

def process_all_images():
    """
    assets 폴더 내 모든 이미지를 처리하고 OUTPUT_DIR에 저장하는 메인 함수.
    이 함수는 로드맵의 핵심 로직 흐름을 따릅니다.
    """
    setup_directories()
    
    # 1. [팀원 A] 모든 이미지 파일 목록 가져오기
    image_paths = get_image_files(ASSETS_DIR)
    
    if not image_paths:
        print(f"[{APP_TITLE}] 처리할 이미지가 assets/ 폴더에 없습니다. 테스트 이미지를 넣어주세요.")
        return

    print(f"[{APP_TITLE}] 총 {len(image_paths)}개의 이미지를 처리합니다.")

    for input_path in image_paths:
        # 출력 파일 경로 설정
        filename = os.path.basename(input_path)
        output_path = os.path.join(OUTPUT_DIR, f"mosaic_{filename}")
        
        print(f"\n--- 처리 시작: {filename} ---")
        
        # 2. [팀원 A] 이미지 로드
        original_image = load_image(input_path)
        
        if original_image is None:
            # 로드 실패 시 다음 파일로 건너뜀
            continue

        # 3. [팀원 B] 얼굴 인식 및 모자이크 처리 핵심 로직 호출
        print("  > 모자이크 알고리즘 적용 중...")
        processed_image = apply_mosaic(original_image)
        
        # 4. [팀원 A] 처리된 이미지 저장
        if processed_image is not None:
            if save_image(processed_image, output_path):
                print(f"  > [성공] 처리 완료 및 저장: {output_path}")
            else:
                print(f"  > [실패] 이미지 저장 오류 발생.")
        else:
            print("  > [SKIP] 처리된 이미지가 유효하지 않아 저장하지 않습니다.")
            
    print("\n[{APP_TITLE}] 모든 이미지 처리 작업 완료.")


if __name__ == "__main__":
    process_all_images()