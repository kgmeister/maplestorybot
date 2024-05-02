



import time
from time import perf_counter
from initinterception import left_click, right_click, mouse_position
from humancursor import SystemCursor




class Helper:

    def __init__(self) -> None:
        self.hc = SystemCursor()
        pass

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