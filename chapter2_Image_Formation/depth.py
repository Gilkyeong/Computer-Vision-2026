import cv2
import numpy as np
from pathlib import Path

# 출력 폴더 생성
output_dir = Path("./outputs")
output_dir.mkdir(parents=True, exist_ok=True)

# 좌/우 이미지 불러오기
left_color = cv2.imread('im2.png')
right_color = cv2.imread('im6.png')

if left_color is None or right_color is None:
    raise FileNotFoundError('좌/우 이미지를 찾지 못했습니다.')

# 그레이스케일 변환
left = cv2.cvtColor(left_color, cv2.COLOR_BGR2GRAY)
right = cv2.cvtColor(right_color, cv2.COLOR_BGR2GRAY)

# 카메라 파라미터
f = 700.0   # focal length
B = 0.12    # baseline

# ROI 설정
rois = {
    "Painting": (55, 50, 130, 110),
    "Frog": (90, 265, 230, 95),
    "Teddy": (310, 35, 115, 90)
}

# -----------------------------
# 1. Disparity map 계산
# -----------------------------
stereo = cv2.StereoBM_create(numDisparities=16 * 6, blockSize=15)
disparity = stereo.compute(left, right).astype(np.float32) / 16.0

# -----------------------------
# 2. Depth map 계산
# disparity > 0 인 픽셀만 사용
# Z = fB / d
# -----------------------------
depth_map = np.zeros_like(disparity, dtype=np.float32)
valid_mask = disparity > 0
depth_map[valid_mask] = (f * B) / disparity[valid_mask]

# -----------------------------
# 3. ROI별 평균 disparity, 평균 depth 계산
# -----------------------------
results = {}

for name, (x, y, w, h) in rois.items():
    roi_disp = disparity[y:y+h, x:x+w]
    roi_depth = depth_map[y:y+h, x:x+w]

    roi_valid = roi_disp > 0

    if np.any(roi_valid):
        mean_disp = np.mean(roi_disp[roi_valid])
        mean_depth = np.mean(roi_depth[roi_valid])
    else:
        mean_disp = 0.0
        mean_depth = 0.0

    results[name] = {
        "mean_disparity": mean_disp,
        "mean_depth": mean_depth
    }

# -----------------------------
# 4. 결과 출력
# -----------------------------
print("=== ROI별 평균 Disparity / 평균 Depth ===")
for name, value in results.items():
    print(f"{name}")
    print(f"  Mean Disparity : {value['mean_disparity']:.2f}")
    print(f"  Mean Depth     : {value['mean_depth']:.4f}")

# 가장 가까운 영역: disparity가 가장 큰 영역
closest_roi = max(results.items(), key=lambda x: x[1]["mean_disparity"])[0]

# 가장 먼 영역: depth가 가장 큰 영역
farthest_roi = max(results.items(), key=lambda x: x[1]["mean_depth"])[0]

print("\n=== 해석 ===")
print(f"가장 가까운 영역: {closest_roi}")
print(f"가장 먼 영역: {farthest_roi}")

# -----------------------------
# 5. 시각화
# -----------------------------
# disparity 시각화용 정규화
disp_vis = cv2.normalize(disparity, None, 0, 255, cv2.NORM_MINMAX)
disp_vis = np.uint8(disp_vis)

# depth 시각화용 정규화
depth_vis = cv2.normalize(depth_map, None, 0, 255, cv2.NORM_MINMAX)
depth_vis = np.uint8(depth_vis)

# 컬러맵 적용
disp_vis_color = cv2.applyColorMap(disp_vis, cv2.COLORMAP_JET)
depth_vis_color = cv2.applyColorMap(depth_vis, cv2.COLORMAP_JET)

# ROI 표시
left_vis = left_color.copy()
for name, (x, y, w, h) in rois.items():
    cv2.rectangle(left_vis, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.putText(left_vis, name, (x, y - 8),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

# 저장
cv2.imwrite(str(output_dir / "left_with_rois.png"), left_vis)
cv2.imwrite(str(output_dir / "disparity_map.png"), disp_vis_color)
cv2.imwrite(str(output_dir / "depth_map.png"), depth_vis_color)

# 출력
cv2.imshow("Left Image with ROIs", left_vis)
cv2.imshow("Disparity Map", disp_vis_color)
cv2.imshow("Depth Map", depth_vis_color)
cv2.waitKey(0)
cv2.destroyAllWindows()