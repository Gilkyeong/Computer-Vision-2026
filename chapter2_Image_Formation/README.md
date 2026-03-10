
## 🌀 문제 1 체크보드 기반 카메라 캘리브레이션

---

### 📄 코드 
- calibration.py

### :octocat: 실행 결과

Camera Matrix K: <br><br>
[[536.07345237   0.         342.37046832]<br><br>
 [  0.         536.01636205 235.5368717 ]<br><br>
 [  0.           0.           1.        ]]<br><br>

Distortion Coefficients:
[[-0.26509041 -0.04674209  0.00183302 -0.00031469  0.252312  ]]
<br><br>
<img width="1585" height="638" alt="스크린샷 2026-03-10 103941" src="https://github.com/user-attachments/assets/f673cec9-b586-40e5-be53-4ad2e7256fc3" />

<br><br>

## 🌀 문제 2 이미지 Rotation & Transformation

---

### 📄 코드 
- transform.py

### :octocat: 실행 결과

<img width="572" height="199" alt="Figure 2026-03-09 185036" src="https://github.com/user-attachments/assets/a48e9c9e-eb99-4bcb-9eba-9f7121296ea3" />


<br><br>

## 🌀 문제 3 Stereo Disparity 기반 Depth 추정

---

### 📄 코드 
- depth.py

### :octocat: 실행 결과

=== ROI별 평균 Disparity / 평균 Depth === <br><br>
Painting <br><br>
  Mean Disparity : 18.54 <br><br>
  Mean Depth     : 4.5375 <br><br>
Frog <br><br>
  Mean Disparity : 33.66 <br><br>
  Mean Depth     : 2.5069 <br><br>
Teddy <br><br>
  Mean Disparity : 22.43 <br><br>
  Mean Depth     : 3.8894 <br><br>
<br><br>
=== 해석 === <br><br>
가장 가까운 영역: Frog <br><br>
가장 먼 영역: Painting <br><br>
<br><br>



