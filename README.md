## boot_auto_exec

#### 적용한 방법

- 터미널에서 다음 파일 실행

```bash
sudo nano /etc/xdg/lxsession/LXDE-pi/autostart
```

- screensaver 윗줄에 입력

```bash
lxterminal -e python /home/pi/eyes-on/test.py
```



#### 부팅 시 자동 실행 관련 링크

- https://m.blog.naver.com/emperonics/221770579539
- https://m.blog.naver.com/emperonics/221770579539
- https://1d1cblog.tistory.com/38
- https://frogbam07.tistory.com/1





---





## cam_lens-distortion_remapping

#### 추가 할 일

- 볼록 오목 지수는 0.9로 셋팅 완료

- scale 조절해서 화질저하 체크 및 변환 정도 좀 더 확인해볼 것



#### 렌즈왜곡 보상 관련 링크

- [https://bkshin.tistory.com/entry/OpenCV-15-%EB%A6%AC%EB%A7%A4%ED%95%91Remapping-%EC%98[…\]tion-%EB%B0%A9%EC%82%AC-%EC%99%9C%EA%B3%A1Radial-Distortion](https://bkshin.tistory.com/entry/OpenCV-15-리매핑Remapping-오목볼록-렌즈-왜곡Lens-Distortion-방사-왜곡Radial-Distortion)

