# __future__
import Servomotor
import PWmotor
import hall_sensor
import OpenCV
import time

from socket import *
from time import ctime
import RPi.GPIO as GPIO

print('\nKartalGozu-Kontrol.Yazilimi by Halil Ibrahim ILHAN\n')

Servomotor.setup()
PWmotor.setup()
hall_sensor.setup()

ctrCmd = ['Up.', 'Down.', 'Left.', 'Right.', 'Center.', 'One.', 'Two.', 'Three.', 'Four.', 'Five.', 'Six.', 'Seven.',
          'Turbo.',
          'Glide.', 'Close.', 'OpenCV.', 'UpRight.', 'UpLeft.', 'DownLeft.', 'DownRight.', 'Takla.', 'takla.']

# ---------------------------------------------------------------#

global cv
cv = 0  # opencv nin durumunu anlamak icin


def closeKontrol():
    if cv == 1:
        OpenCV.CloseCV()  # opencv yi kapat
        global cv
        cv = 0
        print('\n\n.....MANUEL MODE.....\n\n')
    return cv


def openKontrol():
    if cv == 0:
        OpenCV.OpenCV()  # opencv yi ac
        global cv
        cv = 1
        print('\n\n.....AUTO-Pilot.....\n')

    else:
        print('\nAUTO-Pilot is already opened.\n')
    return cv

# ---------------------------------------------------------------#
HOST = ''
PORT = 21567
BUFSIZE = 1024
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

while True:
    print('Waiting for connection')
    tcpCliSock, addr = tcpSerSock.accept()
    print('...connected from :', addr)
    data = ''
    while True:
        data += tcpCliSock.recv(BUFSIZE).decode()

        if not "." in data:
            continue

        if data == ctrCmd[0]:
            closeKontrol()
            Servomotor.ServoUp()
            print('UP')
            break

        if data == ctrCmd[1]:
            closeKontrol()
            Servomotor.ServoDown()
            print('DOWN')
            break

        if data == ctrCmd[2]:
            closeKontrol()
            Servomotor.ServoLeft()
            print('LEFT')
            break

        if data == ctrCmd[3]:
            closeKontrol()
            Servomotor.ServoRight()
            print('RIGHT')
            break

        if data == ctrCmd[4]:
            closeKontrol()
            Servomotor.ServoCenter()
            print('CENTER')
            break

        if data == ctrCmd[5]:
            closeKontrol()
            PWmotor.PwOne()
            print('1')
            break

        if data == ctrCmd[6]:
            closeKontrol()
            PWmotor.PwTwo()
            print('2')
            break

        if data == ctrCmd[7]:
            closeKontrol()
            PWmotor.PwThree()
            print('3')
            break

        if data == ctrCmd[8]:
            closeKontrol()
            PWmotor.PwFour()
            print('4')
            break

        if data == ctrCmd[9]:
            closeKontrol()
            PWmotor.PwFive()
            print('5')
            break

        if data == ctrCmd[10]:
            closeKontrol()
            PWmotor.PwSix()
            print('6')
            break

        if data == ctrCmd[11]:
            closeKontrol()
            PWmotor.PwSeven()
            print('7')
            break

        if data == ctrCmd[12]:
            closeKontrol()
            PWmotor.PwTurbo()
            print('TURBO')
            break

        if data == ctrCmd[13]:
            closeKontrol()
            hall_sensor.stpGlide()
            print('GLIDE')
            break

        if data == ctrCmd[15]:
            openKontrol()
            break

        if data == ctrCmd[16]:
            closeKontrol()
            Servomotor.UpRight()
            print('UP-RIGHT')
            break

        if data == ctrCmd[17]:
            closeKontrol()
            Servomotor.UpLeft()
            print('UP-LEFT')
            break

        if data == ctrCmd[18]:
            closeKontrol()
            Servomotor.DownLeft()
            print('DOWN-LEFT')
            break

        if data == ctrCmd[19]:
            closeKontrol()
            Servomotor.DownRight()
            print('DOWN-RIGHT')
            break

        if data == ctrCmd[20] or data == ctrCmd[21]:
            closeKontrol()
            tumble()
            print('TUMBLE')
            break

        if data == ctrCmd[14]:
            PWmotor.close()
            GPIO.cleanup()
            OpenCV.CloseCV()  # opencvkapat
            print('close')
            tcpSerSock.close();
            break
        else:
            print('\n!!!!INVALID COMMAND: \n', data)
            break
        data = ''

# tcpSerSock.close(); # in the top condition now
