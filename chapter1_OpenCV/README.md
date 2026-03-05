## 🌀 문제 1 이미지 불러오기 및 그레이스케일 변환

> OpenCV를 활용하여 컬러 이미지를 불러온 후 **그레이스케일 변환 및 출력**
---

### 📄 코드 
- Grayscale.py


*전체 코드*
```python
import cv2 as cv
import sys
import numpy as np

img = cv.imread('soccer.jpg') 

if img is None:
    sys.exit('파일을 찾을 수 없습니다.')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

cv.imwrite('soccer_gray.jpg', gray)  

gray_3ch = cv.cvtColor(gray, cv.COLOR_GRAY2BGR)

imgs = np.hstack((img, gray_3ch))

cv.imshow('Color and Grayscale Image', imgs)

cv.waitKey(0)
cv.destroyAllWindows()
```
*핵심 코드* <br>
**🔷 grayscale 이미지 변환**
```python
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imwrite('soccer_gray.jpg', gray)  
```
🔹 cv.cvtColor() 함수는 이미지 색상 공간을 변환 <br>
🔹 cv.COLOR_BGR2GRAY를 사용하여 BGR 이미지를 grayscale로 변환
<br><br>
**🔷 grayscale 이미지를 3채널로 변환**
```python
gray_3ch = cv.cvtColor(gray, cv.COLOR_GRAY2BGR)
```
🔹 cv.COLOR_GRAY2BGR를 사용하여 흑백 이미지를 BGR 3채널 형식으로 변환
<br><br>
**🔷 원본 이미지와 변환된 이미지 나란히 붙이기**
```python
imgs = np.hstack((img, gray_3ch))
```
🔹 np.hstack() 이미지를 가로로 붙이는 함수
<br><br>

### :octocat: 실행 결과

![image](https://github.com/user-attachments/assets/233b22d6-aff2-490e-abff-1f231ca3de13)
<br><br>

## 🌀 문제 2 페인팅 붓 크기 조절 기능 추가

> 컬러 이미지를 불러와 마우스 입력으로 붓질과 **키보드 입력을 이용해 붓의 크기 조절**
---

### 📄 코드 
- BrushControl.py

### :octocat: 실행 결과

![image](https://github.com/user-attachments/assets/940f3aa2-4a55-4d78-a64f-1878cc5209bd)

<br><br>

## 🌀 문제 3 마우스로 영역 선택 및 ROI 추출

> 이미지를 불러와 사용자가 마우스를 제어하여 **ROI 선택 후 선택한 영역만 따로 저장하거나 표시**
---

### 📄 코드 
- ROI_print.py

### :octocat: 실행 결과

![image](https://github.com/user-attachments/assets/235df943-48de-49b3-8a72-ee39967e0764)


