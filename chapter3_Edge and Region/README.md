## 🌀 문제 1 소벨 에지 검출 및 결과 시각화

> 이미지 그레이 스케일로 변환 후 **Sobel 필터를 사용하여 x축과 y축 방향의 에지 검출**
> 검출된 에지 강도(edge strength) 이미지를 시각화
---

### 📄 코드 
- Sobel_edge.py

### :octocat: 실행 결과

![Figure 2025-03-25 153940](https://github.com/user-attachments/assets/ad7436ff-95ce-4383-9dee-fbb7bfa408f0)
<br><br>
## 🌀 문제 2 케니 에지 및 허프 변환을 이용한 직선 검출

> Canny 에지 검출을 사용하여 에지 맵 생성 후 **허프 변환을 사용하여 이미지에서 직선 검출**
---

### 📄 코드 
- Hough.py

### :octocat: 실행 결과

![Figure 2025-03-25 154707](https://github.com/user-attachments/assets/ccb52f88-6890-44e7-bf53-1231e55932af)
lines = cv.HoughLinesP(edges, rho=1, theta=np.pi/180, threshold=90, minLineLength=40, maxLineGap=10) <br><br>
![Figure 2025-03-25 154813](https://github.com/user-attachments/assets/a76c3340-c82b-4a33-9736-e0080f56f013)
lines = cv.HoughLinesP(edges, rho=1, theta=np.pi/180, threshold=90, minLineLength=40, maxLineGap=5)
![image](https://github.com/user-attachments/assets/1693c32a-3089-427c-bbe5-f0f314c3afe3)
lines = cv.HoughLinesP(edges, rho=1, theta=np.pi/180, threshold=90, minLineLength=15, maxLineGap=5)
<br><br>

## 🌀 문제 3 GrabCut을 이용한 대화식 영역 분할 및 객체 추출 

> 사용자가 지정한 영역을 바탕으로 **GrabCut 알고리즘을 사용하여 객체 추출**
> 객체 추출 결과를 마스크 형태로 시각화 후 원본 이미지에서 배경을 제거하고 객체만 남은 이미지를 출력
---

### 📄 코드 
- Grabcut.py

### :octocat: 실행 결과

![Figure 2025-03-25 155538](https://github.com/user-attachments/assets/1307ca06-143f-45df-89a3-d3867e98a63c)

