



import time
from time import perf_counter
from initinterception import left_click, right_click, mouse_position, move_relative, sleep
from humancursor import SystemCursor
import win32gui
from PIL import ImageGrab
import cv2
import numpy as np
import random



## a helper class for main.py or just any other file in the program. 
## because don't want the main.py to be too messy. 
## this class may contain some of the ugliest code in the entire planet. 
class Helper:

    def __init__(self) -> None:
        self.hc = SystemCursor()
        pass

    ##### HUMAN MOUSE CLICK SECTION #####
    async def move_to(self,x,y):
        self.hc.move_to((x,y))

    def movetoandclick(self,x,y,duration=None,sleep=.01):
        # print(f'left click')
        mx,my = mouse_position()
        if mx >= x-2 and mx <= x+2:
            if my >= y-2 and my <= y+2:
                pass
            else:
                # print(f'left click movey')
                self.hc.move_to(point=(x,y),duration=duration)
        else:
            # print(f'left click movex')
            self.hc.move_to(point=(x,y),duration=duration)
        time.sleep(.01)
        left_click()
        time.sleep(sleep)

    def movetoandrclick(self,x,y,duration=None):
        # print(f'right click')
        mx,my = mouse_position()
        if mx >= x-2 and mx <= x+2:
            if my >= y-2 and mx <= y+2:
                pass
            else:
                # print(f'right click movey')
                self.hc.move_to(point=(x,y),duration=duration)
        else:
            # print(f'right click movex')
            self.hc.move_to(point=(x,y),duration=duration)
        time.sleep(.01)
        # right_click()
        # time.sleep(.15)

    async def move_to_and_click(self,x,y):
        self.hc.move_to((x,y))
        time.sleep(.1)
        left_click()
        time.sleep(.1)

    async def move_to_and_click_and_move_away(self,x,y):
        self.hc.move_to((x,y))
        time.sleep(.1)
        left_click()
        time.sleep(.1)
        move_relative(10,0)


    ##### CHANGING CHANNEL SECTION: FUNCTIONS FOR BOTH ROTATIONS AND SCRIPTS #####
    # directly copy pasta from my old bot. how to make it prettier you ask? idk .. for me ugly = pretty; pretty = ugly. 
    def still_in_zakum_map2(self,g,hwnd):
        stillinzakummap = 0
        notinzakummap = 0
        rdbgr = (0, 0, 255)
        yellowbgr = (68, 221, 255)
        # 255 0 0 rgb
        # hwnd = win32gui.FindWindow(None, "MapleStory")
        position = win32gui.GetWindowRect(hwnd)
        x, y, w, h = position
        position1 = (x+11, y+88, x+200, y+200)  # void3
        while True:
            while True:
                screenshot = ImageGrab.grab(position1)
                screenshot = np.array(screenshot)
                img = cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR)
                if img is not None:
                    print(img.shape)
                    print(img[40][30])
                    print(img[41][30])
                    print(img[42][30])
                    print(img[43][30])
                    print(img[44][30])
                    print(img[45][30])
                    # print(img[45][35])
                    # hfakeclick(x+11+30,y+88+40)
                if img[45][35][0] < 10 and img[45][35][1] < 10:
                # if img[40][30][0] < 10 and img[40][30][1] < 10 and img[40][30][2] < 10:
                    print(f'map transition ..')
                    time.sleep(1.5)
                    continue
                # elif img[45][35][0] == 189 or img[45][35][0] == 187:
                # elif img[40][30][0] >= 187 and img[40][30][0] <= 189:
                elif img[45][35][0] >= 187 and img[45][35][0] <= 189:
                    print(f'still in zakum map .. {stillinzakummap}')
                    stillinzakummap += 1
                    if stillinzakummap > 1:
                        return True
                else:
                    print(f'not in zakum map .. {notinzakummap}')
                    notinzakummap += 1
                    if notinzakummap > 3:
                        return False
                time.sleep(.5)

    # you want to adjust your character to align the zakum entrance portal so that you can press up. 
    async def adjustportal2(self,g, spot=42, distx=75, docorrection=False, tolerance=5, ca=None): # ca stands for character.action
        async def correction(indicesyellow10, distx=30):
            if indicesyellow10 > distx:
                await ca.leftp(31, 81)
                await ca.leftr(331, 881)
            elif indicesyellow10 < distx:
                await ca.rightp(31, 81)
                await ca.rightr(331, 881)
        while (True):
            while (True):
                r = random.randint(1, 4)
                r /= 1000
                await sleep(r)
                g_variable = g.get_player_location()
                x, y = (None, None) if g_variable is None else g_variable
                if x == None:
                    print(f'x==None..continue..means..no..player..something blocking bruh ..f')
                    r = random.randint(900, 1100)
                    r /= 1000
                    await sleep(r)
                else:
                    break
            if (x >= distx-3 and x <= distx+3):
                if docorrection:
                    print(f'correct distx: {distx}, yellowbgr: {x}')
                    if x == distx:
                        donecorrection = True
                    else:
                        donecorrection = False
                        print('correction')
                        await correction(x, distx)
                else:
                    donecorrection = True
                if donecorrection:
                    if y >= spot-tolerance and y <= spot+tolerance:
                        r = random.randint(100, 400)
                        r /= 1000
                        await sleep(r)
                        return
                    else:
                        print('height: ', y)
                        if y > spot:
                            print(f'indicesyellow[0][0] > spot goupattack()')
                            await ca.goupattack()
                        else:
                            print(f'indicesyellow[0][0] < spot downjump()')
                            await ca.downjump()
                        r = random.randint(500, 900)
                        r /= 1000
                        await sleep(r)
            else:
                print('height2: ', y)
                distance = x - distx
                if distance > 30 or distance < -30:
                    if distance > 30:
                        print('hey distance > 30', distance)
                        await ca.goleftattack()
                    if distance < -30:
                        await ca.gorightattack()
                elif distance > 0:
                    distances = int(distance * 40)  # 50
                    print(f'> 0 {distances}')
                    await ca.leftp(distances-30, distances-0)
                    await ca.leftr(10, 100)
                elif distance < 0:
                    distances = int(abs(distance) * 40)  # 50
                    print(f'< 0 {distances}')
                    await ca.rightp(distances-30, distances-0)
                    await ca.rightr(10, 100)

    # check for red dot after coming out from zakum map. 
    async def checkreddotaftercomeoutfromzakummap(self,hwnd, ca=None, position1=None):
        rdbgr = (0, 0, 255)
        yellowbgr = (68, 221, 255)
        # 255 0 0 rgb
        # hwnd = win32gui.FindWindow(None, "MapleStory")
        position = win32gui.GetWindowRect(hwnd)
        x, y, w, h = position
        # position1 = (x+11, y+88, x+200, y+200)  # void3
        while True:
            while True:
                screenshot = ImageGrab.grab(position1)
                screenshot = np.array(screenshot)
                img = cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR)
                indicesyellow = np.where(np.all(img == yellowbgr, axis=-1))
                if len(indicesyellow[0]) != 0:
                    index = np.where(np.all(img == rdbgr, axis=-1))
                    if len(index[0] != 0):
                        print(f'got red dot')
                        time.sleep(1)
                        await ca.ccbuttonpr()
                        r = random.randint(1, 5)
                        for i in range(r):
                            await ca.leftp()
                            await ca.leftr(1, 31)
                        await ca.enterp()
                        await ca.enterr()
                        time.sleep(3)
                    else:
                        print(f'no red dot')
                        return
                else:
                    time.sleep(1)