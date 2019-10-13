import os, sys
# controll.py
sd = os.path.dirname(os.path.abspath(__file__))
sys.path.append(sd)
# エラーをログに保存
def create(error):
    f = open(sd + '/log.txt','a')
    f.write('error: {}\n'.format(str(error)))
    f.close()