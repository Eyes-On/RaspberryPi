from picamera import PiCamera
import paho.mqtt.publish as publish
import paho.mqtt.client as mqtt
import threading

"""
on_connect는 subscriber가 브로커에 연결하면서 호출할 함수
rc가 0이면 정상접속이 됐다는 의미
"""

# 전역변수
uuid = ""


class Check():
    def __init__(self):
        self.data = 0

    def getData(self):
        return self.data

    def setData(self, data):
        self.data = data


class MqttCamera():
    def __init__(self):
        client = mqtt.Client()
        client.on_connect = self.on_connect
        client.on_message = self.on_message
        client.connect("15.164.46.54", 1883, 60)
        self.thread = None
        self.camera = PiCamera()
        self.camera.rotation = 270
        self.check = Check()
        client.loop_forever()

    def on_connect(self, client, userdata, flags, rc):
        print("connect.." + str(rc))
        if rc == 0:
            client.subscribe("eyeson/#")
        else:
            print("연결실패")

    def mywhileRun(self):
        global uuid
        

    # 메시지가 도착됐을때 처리할 일들 - 여러가지 장비 제어하기, Mongodb에 저장
    def on_message(self, client, userdata, msg):
        global uuid
        try:
            myval = msg.payload.decode("utf-8")
            myval = myval.split("/")
            mytopic = msg.topic.split("/")
            uuid = mytopic[1]
            if myval[0] == "android":
                if myval[1] == "camera":
                    if myval[2] == "on":
                        print(1)
                        self.camera.start_preview()
                        self.camera.start_recording("/home/pi/eyeson/video6.h264")
                    else:
                        print(2)
                        self.camera.stop_recording()
                        self.camera.stop_preview()
        except:
            pass


if __name__ == "__main__":
    try:
        mymqtt = MqttCamera()

    except KeyboardInterrupt:
        print("종료")
