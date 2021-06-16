import paho.mqtt.client as mqtt

"""
on_connect는 subscriber가 브로커에 연결하면서 호출할 함수
rc가 0이면 정상접속이 됐다는 의미
"""


def on_connect(client, userdata, flags, rc):
    print("connect.." + str(rc))
    if rc == 0:
        client.subscribe("eyeson/#")
    else:
        print("연결실패")


# 메시지가 도착됐을때 처리할 일들 - 여러가지 장비 제어하기, Mongodb에 저장
def on_message(client, userdata, msg):
    topicData = msg.topic.split("/")
    uuid = topicData[1]
    if str(type(msg.payload)) == "<class 'bytes'>":
        with open('/home/lab19/ai_env_mino/yolov5/%s.jpg' %uuid, 'wb') as fd: #iris.jpg이름으로 파일 쓰기(wb는 바이트로 쓸때)
            fd.write(msg.payload) # 메세지 받은걸 파일에 쓰기
            fd.close()

mqttClient = mqtt.Client()  # 클라이언트 객체 생성
# 브로커에 연결이되면 내가 정의해놓은 on_connect함수가 실행되도록 등록
mqttClient.on_connect = on_connect

# 브로커에서 메시지가 전달되면 내가 등록해 놓은 on_message함수가 실행
mqttClient.on_message = on_message

# 브로커에 연결하기
mqttClient.connect("15.164.46.54", 1883, 60)

# 토픽이 전달될때까지 수신대기
mqttClient.loop_forever()
