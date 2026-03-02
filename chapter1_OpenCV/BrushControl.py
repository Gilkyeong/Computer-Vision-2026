import cv2 as cv 
import sys

img = cv.imread('soccer.jpg')

if img is None:
    sys.exit('파일을 찾을 수 없습니다.')

BrushSiz = 5                  
MIN_BRUSH = 1
MAX_BRUSH = 15

LColor, RColor = (255,0,0), (0,0,255)  

def painting(event, x, y, flags, param):
    global BrushSiz

    if event == cv.EVENT_LBUTTONDOWN:
        cv.circle(img, (x,y), BrushSiz, LColor, -1)

    elif event == cv.EVENT_RBUTTONDOWN:
        cv.circle(img, (x,y), BrushSiz, RColor, -1)

    elif event == cv.EVENT_MOUSEMOVE and flags == cv.EVENT_FLAG_LBUTTON:
        cv.circle(img, (x,y), BrushSiz, LColor, -1)

    elif event == cv.EVENT_MOUSEMOVE and flags == cv.EVENT_FLAG_RBUTTON:
        cv.circle(img, (x,y), BrushSiz, RColor, -1)

    cv.imshow('Painting', img)

cv.namedWindow('Painting')
cv.imshow('Painting', img)
cv.setMouseCallback('Painting', painting)

while True:
    key = cv.waitKey(1) & 0xFF

    if key == ord('+'):
        BrushSiz = min(MAX_BRUSH, BrushSiz + 1)
        print("Brush Size:", BrushSiz)

    elif key == ord('-'):
        BrushSiz = max(MIN_BRUSH, BrushSiz - 1)
        print("Brush Size:", BrushSiz)

    elif key == ord('q'):
        break

cv.destroyAllWindows()