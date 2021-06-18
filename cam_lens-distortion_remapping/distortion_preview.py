import cv2
import time
from threading import Thread
import numpy as np

def VideoTest():    
    cap = cv2.VideoCapture(0)

    while cap.isOpened():
        ret, img = cap.read()
        
        rows, cols = img.shape[:2]
        # ---① 설정 값 셋팅
        exp = 0.9       # 볼록, 오목 지수 (오목 : 0.1 ~ 1, 볼록 : 1.1~)
        scale = 1           # 변환 영역 크기 (0 ~ 1)
        # 매핑 배열 생성 ---②
        mapy, mapx = np.indices((rows, cols),dtype=np.float32)
        # 좌상단 기준좌표에서 -1~1로 정규화된 중심점 기준 좌표로 변경 ---③
        mapx = 2*mapx/(cols-1)-1
        mapy = 2*mapy/(rows-1)-1
        # 직교좌표를 극 좌표로 변환 ---④
        r, theta = cv2.cartToPolar(mapx, mapy)
        # 왜곡 영역만 중심확대/축소 지수 적용 ---⑤
        r[r< scale] = r[r<scale] **exp  
        # 극 좌표를 직교좌표로 변환 ---⑥
        mapx, mapy = cv2.polarToCart(r, theta)
        # 중심점 기준에서 좌상단 기준으로 변경 ---⑦
        mapx = ((mapx + 1)*cols-1)/2
        mapy = ((mapy + 1)*rows-1)/2
        # 재매핑 변환
        distorted = cv2.remap(img,mapx,mapy,cv2.INTER_LINEAR)
        
        if ret:
            cv2.imshow("distort preview!!!", distorted)
        if cv2.waitKey(1) & 0xFF == 27: # ESC 누르면 종료
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    thread = Thread(target=VideoTest)
    thread.start()