import os
# コマンドラインを一括で実行する
print("Start WebIO")
try:
    os.system("nohup /usr/local/bin/mjpg_streamer -i \"input_raspicam.so -x 640 -y 480 -fps 15 -q 80\" -o \"output_http.so -p 8080 -w /usr/local/share/mjpg-streamer/www\" &")
    print("Stream Start")
    os.system("sudo systemctl start webiopi")
    print("WebIOPi Start")
    print("Working : http://[IP address]:8000/")
except Exception as e:
    print(str(e))