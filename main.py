import pyautogui
import time
import pyperclip
import os
import random

def send_msg(my_msg, repeat_number):
    for i in range(int(repeat_number)):
        time_wait = random.uniform(1,3)
        print('Repeat Number : ', i + 1, end='')
        print(' // Time wait : ', time_wait)
        time.sleep(time_wait)
        pyautogui.keyDown('enter')
        pyperclip.copy(my_msg)
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.keyDown('enter')
        pyautogui.keyDown('esc')
        pyautogui.keyDown('down')

def filter_friend(filter_keyword, init_number):
    # 사람 아이콘 클릭
    try:
        click_img(img_path + 'person_icon.png')
        try:
            click_img(img_path + 'person_icon2.png')
        except Exception as e : 
            print('e ', e)
    except Exception as e : 
        print('e ', e)
    # X 버튼이 존재한다면 클릭하여 내용 삭제
    try:
        click_img(img_path + 'x.png')
    except:
        pass
    time.sleep(1)
    # 돋보기 아이콘 오른쪽 클릭
    click_img_plus_x(img_path+'search_icon.png', 30)
    if filter_keyword == '':
        pyautogui.keyDown('esc')
    else:
        pyperclip.copy(filter_keyword)
    pyautogui.hotkey('ctrl', 'v')
    for i in range(int(init_number)-1):
        pyautogui.keyDown('down')
    time.sleep(2)

def click_img(imagePath):
    location = pyautogui.locateCenterOnScreen(imagePath, confidence = conf)
    x, y = location
    pyautogui.click(x, y)

def click_img_plus_x(imagePath, pixel):
    location = pyautogui.locateCenterOnScreen(imagePath, confidence = conf)
    x, y = location
    pyautogui.click(x + pixel, y)

def doubleClickImg (imagePath):
    location = pyautogui.locateCenterOnScreen(imagePath, confidence = conf)
    x, y = location
    pyautogui.click(x, y, clicks=2)

def initialize():
    print('Monitor size : ', end='')
    print(pyautogui.size())
    print(pyautogui.position())
    filter_keyword = input("필터링할 친구 이름. 없으면 그냥 enter.  ex) 학생 직장 99 : ")
    init_number = input("필터링한 친구 기준 시작지점(ex. 필터링된 친구 시작지점) : ")
    repeat_number = input("반복할 횟수(ex. 필터링 검색된 친구 수) : ")
    my_msg = input("전송할 메세지 : ")
    print('=================')
    print('메세지 전송 시작!')
    print('=================')
    return (filter_keyword, init_number, repeat_number, my_msg)

# config
img_path = os.path.dirname(os.path.realpath(__file__)) + '/img/'
conf = 0.90
pyautogui.PAUSE = 0.5

if __name__ == "__main__":
    (filter_keyword, init_number, repeat_number, my_msg) = initialize()
    filter_friend(filter_keyword, init_number)
    send_msg(my_msg, repeat_number)
    # send_msg(long_msg, repeat_number)
