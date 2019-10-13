import RPi.GPIO as GPIO
import webiopi
import sys
import os
sd = os.path.dirname(os.path.abspath(__file__))
sys.path.append(sd)
import log_py
#実際のボードのピン番号を使用しています
GPIO.setmode(GPIO.BOARD)

#どのピンでL298Nを駆動しているのかを定義します。
DirectionOnePin = 16  #IN1
DirectionTwoPin = 18  #IN2
DirectionOnePin2 = 7  #IN3
DirectionTwoPin2 = 11 #IN4
ENA = 12              #ENA
ENB = 13              #ENB

#これらのピンの使い方を定義します
GPIO.setup(DirectionOnePin, GPIO.OUT)
GPIO.setup(DirectionTwoPin, GPIO.OUT)
GPIO.setup(DirectionOnePin2, GPIO.OUT)
GPIO.setup(DirectionTwoPin2, GPIO.OUT)
GPIO.setup(ENA, GPIO.OUT)
GPIO.setup(ENB, GPIO.OUT)

#出力パワー
pww = GPIO.PWM(ENA, 60)
pww2 = GPIO.PWM(ENB, 60)
pww.start(0)
pww2.start(0)

@webiopi.macro
def advance(data): # 前進
    try:
        GPIO.output(DirectionTwoPin, GPIO.LOW)
        GPIO.output(DirectionTwoPin2, GPIO.LOW)
        GPIO.output(DirectionOnePin, GPIO.HIGH)
        GPIO.output(DirectionOnePin2, GPIO.HIGH)
        return "前進"
    except Exception as error:   
        log_py.create(str(error))
        return str(error)

@webiopi.macro
def reverse(data): # 後進
    try:
        GPIO.output(DirectionOnePin, GPIO.LOW)
        GPIO.output(DirectionOnePin2, GPIO.LOW)
        GPIO.output(DirectionTwoPin, GPIO.HIGH)
        GPIO.output(DirectionTwoPin2, GPIO.HIGH)
        return "後進"
    except Exception as error:   
        log_py.create(str(error))
        return str(error)

@webiopi.macro
def left(data): # 左回り
    try:
        GPIO.output(DirectionOnePin, GPIO.LOW)
        GPIO.output(DirectionTwoPin2, GPIO.LOW)
        GPIO.output(DirectionTwoPin, GPIO.HIGH)
        GPIO.output(DirectionOnePin2, GPIO.HIGH)
        return "左回り"
    except Exception as error:   
        log_py.create(str(error))
        return str(error)

@webiopi.macro
def right(data): # 右回り
    try:
        GPIO.output(DirectionOnePin2, GPIO.LOW)
        GPIO.output(DirectionTwoPin, GPIO.LOW)
        GPIO.output(DirectionTwoPin2, GPIO.HIGH)
        GPIO.output(DirectionOnePin, GPIO.HIGH)
        return "右回り"
    except Exception as error:   
        log_py.create(str(error))
        return str(error)

@webiopi.macro
def stop(data): # 停止
    try:
        GPIO.output(DirectionOnePin, GPIO.LOW)
        GPIO.output(DirectionTwoPin, GPIO.LOW)
        GPIO.output(DirectionOnePin2, GPIO.LOW)
        GPIO.output(DirectionTwoPin2, GPIO.LOW)
        return "停止"
    except Exception as error:   
        log_py.create(str(error))
        return str(error)

@webiopi.macro
def kill(data): # プロセスキル
    try:
        GPIO.cleanup()
        return "プロセスキル"
    except Exception as error:   
        log_py.create(str(error))
        return str(error)

@webiopi.macro
def slid(data): # 速度
    try:
        data = int(data)
        data = data * 10
        pww.ChangeDutyCycle(data)
        pww2.ChangeDutyCycle(data)
        return "速度"
    except Exception as error:   
        log_py.create(str(error))
        return str(error)
