

import ctypes
import ctypes.wintypes
import pyautogui
from collections import namedtuple
import time
from time import perf_counter
import unittest
# from initinterception import sleep
import asyncio
import win32gui
from pytweening import easeInPoly, easeOutPoly, easeInOutPoly
from humancursor import SystemCursor
from helper import Helper
from runesolver import RuneSolver
from action import Action

# These ctypes structures are for Win32 INPUT, MOUSEINPUT, KEYBDINPUT, and HARDWAREINPUT structures,
# used by SendInput and documented here: http://msdn.microsoft.com/en-us/library/windows/desktop/ms646270(v=vs.85).aspx
# Thanks to BSH for this StackOverflow answer: https://stackoverflow.com/questions/18566289/how-would-you-recreate-this-windows-api-structure-with-ctypes
class MOUSEINPUT(ctypes.Structure):
    _fields_ = [
        ('dx', ctypes.wintypes.LONG),
        ('dy', ctypes.wintypes.LONG),
        ('mouseData', ctypes.wintypes.DWORD),
        ('dwFlags', ctypes.wintypes.DWORD),
        ('time', ctypes.wintypes.DWORD),
        ('dwExtraInfo', ctypes.POINTER(ctypes.wintypes.ULONG)),
    ]

class KEYBDINPUT(ctypes.Structure):
    _fields_ = [
        ('wVk', ctypes.wintypes.WORD),
        ('wScan', ctypes.wintypes.WORD),
        ('dwFlags', ctypes.wintypes.DWORD),
        ('time', ctypes.wintypes.DWORD),
        ('dwExtraInfo', ctypes.POINTER(ctypes.wintypes.ULONG)),
    ]

class HARDWAREINPUT(ctypes.Structure):
    _fields_ = [
        ('uMsg', ctypes.wintypes.DWORD),
        ('wParamL', ctypes.wintypes.WORD),
        ('wParamH', ctypes.wintypes.DWORD)
    ]

class INPUT(ctypes.Structure):
    class _I(ctypes.Union):
        _fields_ = [
            ('mi', MOUSEINPUT),
            ('ki', KEYBDINPUT),
            ('hi', HARDWAREINPUT),
        ]

    _anonymous_ = ('i', )
    _fields_ = [
        ('type', ctypes.wintypes.DWORD),
        ('i', _I),
    ]
# End of the SendInput win32 data structures.



def sleep(dur):
    now = perf_counter()
    end = now + dur
    while perf_counter() < end:
        pass








def _mouseMoveDrag(moveOrDrag, x, y, xOffset, yOffset, duration, tween, button=None):    
    def getPointOnLine(x1, y1, x2, y2, n):
        """
        Returns an (x, y) tuple of the point that has progressed a proportion ``n`` along the line defined by the two
        ``x1``, ``y1`` and ``x2``, ``y2`` coordinates.

        This function was copied from pytweening module, so that it can be called even if PyTweening is not installed.
        """
        x = ((x2 - x1) * n) + x1
        y = ((y2 - y1) * n) + y1
        return (x, y)
    MINIMUM_DURATION = 0.1
    MINIMUM_SLEEP = 0.05
    xOffset = int(xOffset) if xOffset is not None else 0
    yOffset = int(yOffset) if yOffset is not None else 0
    if x is None and y is None and xOffset == 0 and yOffset == 0:
        return  # Special case for no mouse movement at all.
    startx, starty = pyautogui.position()
    x = int(x) if x is not None else startx
    y = int(y) if y is not None else starty
    # x, y, xOffset, yOffset are now int.
    x += xOffset
    y += yOffset
    width, height = pyautogui.size()
    # Make sure x and y are within the screen bounds.
    # x = max(0, min(x, width - 1))
    # y = max(0, min(y, height - 1))
    # If the duration is small enough, just move the cursor there instantly.
    steps = [(x, y)]
    if duration > MINIMUM_DURATION:
        # Non-instant moving/dragging involves tweening:
        num_steps = max(width, height)
        sleep_amount = duration / num_steps
        if sleep_amount < MINIMUM_SLEEP:
            num_steps = int(duration / MINIMUM_SLEEP)
            sleep_amount = duration / num_steps
        steps = [getPointOnLine(startx, starty, x, y, tween(n / num_steps)) for n in range(num_steps)]
        # Making sure the last position is the actual destination.
        steps.append((x, y))
    # print(f'{len(steps)=} {steps=} {sleep_amount=} {duration=} {num_steps=} {width=} {height=}')
    print(f'{len(steps)=} {sleep_amount=} {duration=} {num_steps=} {width=} {height=}')
    for tweenX, tweenY in steps:
        if len(steps) > 1:
            # print(f'{steps=} {sleep_amount=}')
            # A single step does not require tweening.
            time.sleep(sleep_amount)
            # await sleep(sleep_amount)
            # sleep(sleep_amount)
        tweenX = int(round(tweenX))
        tweenY = int(round(tweenY))
        print(f'{tweenX=} {tweenY=}')
        ctypes.windll.user32.SetCursorPos(tweenX, tweenY)        
        # pyautogui.leftClick(tweenX,tweenY)
        x,y=pyautogui.position()
        # width, height = (ctypes.windll.user32.GetSystemMetrics(0), ctypes.windll.user32.GetSystemMetrics(1))
        width, height = 1920, 1080
        convertedX = 65536 * x // width + 1
        convertedY = 65536 * y // height + 1
        ctypes.windll.user32.mouse_event(0x0002, ctypes.c_long(convertedX), ctypes.c_long(convertedY), 0, 0)
        ctypes.windll.user32.mouse_event(0x0004, ctypes.c_long(convertedX), ctypes.c_long(convertedY), 0, 0)
        # time.sleep(.5)
        # pyautogui.mouseDown(tweenX,tweenY)





















class P(namedtuple("P", ["x", "y"])):
    """Simple, immutable, 2D point/vector class, including some basic
    arithmetic functions.
    """

    def __str__(self):
        return "{0},{1}".format(self.x, self.y)

    def __repr__(self):
        return "P({0}, {1})".format(self.x, self.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return self.x != other.x and self.y != other.y

    def __add__(self, other):
        return P(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return P(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return P(self.x * other, self.y * other)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __floordiv__(self, other):
        return P(self.x // other, self.y // other)

    def __truediv__(self, other):
        return P(self.x / other, self.y / other)

    def __neg__(self):
        return P(-self.x, -self.y)

    def __pos__(self):
        return self

    def __neg__(self):
        return P(abs(self.x), abs(self.y))

class MyMouse(unittest.TestCase):

    TWEENS = [
        # "linear",
        # "easeInElastic",
        # "easeOutElastic",
        # "easeInOutElastic",
        # "easeInBack",
        # "easeOutBack", # this so good
        # "easeInOutBack", # this
        # "easeInBounce",
        # "easeOutBounce", # this
        # "easeInOutBounce",
        # "easeInPoly",
        # "easeOutPoly",
        # "easeInOutPoly",
        # "easeInCirc",
        # "easeOutCirc", # not bad
        "easeInOutCirc", # actually not bad, start slow end slow, mid fast
        # "easeInExpo",
        # "easeOutExpo", # good, start fast end slow
        # "easeInOutExpo", # good, start very slow, end very slow
        # "easeInSine",
        # "easeOutSine", # nothing special
        # "easeInOutSine",
        # "easeInQuint",
        # "easeOutQuint",
        # "easeInOutQuint", # not bad, start slow, end slow
        # "easeInQuart",
        # "easeOutQuart",
        # "easeInOutQuart",
        # "easeInCubic",
        # "easeOutCubic",
        # "easeInOutCubic",
        # "easeInQuad",
        # "easeOutQuad",
        # "easeInOutQuad",
    ]
    
    def setUp(self):
        self.oldFailsafeSetting = pyautogui.FAILSAFE
        self.center = P(*pyautogui.size()) // 2
        self.humancursor = SystemCursor()

        pyautogui.FAILSAFE = False
        pyautogui.moveTo(*self.center)  # make sure failsafe isn't triggered during this test
        pyautogui.FAILSAFE = True

    def test_moveToWithTween(self):
        # origin = self.center - P(100, 100)
        # destination = self.center + P(100, 100)
        origin = self.center - P(200, -200)
        destination = self.center + P(200, -200)
        print(f'{origin=} {destination=}')

        def resetMouse():
            pyautogui.moveTo(*origin)
            mousepos = P(*pyautogui.position())
            self.assertEqual(mousepos, origin)

        for tweenName in self.TWEENS:
            tweenFunc = getattr(pyautogui, tweenName)
            # tweenFunc = easeOutPoly
            print(tweenName)
            resetMouse()
            now=perf_counter()
            # pyautogui.moveTo(destination.x, destination.y, duration=pyautogui.MINIMUM_DURATION * 2, tween=tweenFunc)
            # pyautogui.moveTo(destination.x, destination.y, duration=1 * 2, tween=tweenFunc)
            # x, y = pyautogui._normalizeXYArgs(destination.x, destination.y)
            # _mouseMoveDrag("move", x, y, 0, 0, 1., tweenFunc)
            self.humancursor.move_to((destination.x,destination.y))
            print(f'{(perf_counter()-now)=}')
            mousepos = P(*pyautogui.position())
            pyautogui.leftClick(mousepos)
            self.assertEqual(
                mousepos,
                destination,
                "%s tween move failed. mousepos set to %s instead of %s" % (tweenName, mousepos, destination),
            )
            
    def test_moveRelWithTween(self):
        origin = self.center - P(200, -200)
        delta = P(400, -400)
        destination = origin + delta

        def resetMouse():
            pyautogui.moveTo(*origin)
            mousepos = P(*pyautogui.position())
            self.assertEqual(mousepos, origin)

        for tweenName in self.TWEENS:
            tweenFunc = getattr(pyautogui, tweenName)
            # tweenFunc = easeOutPoly
            print(tweenName)
            resetMouse()
            now=perf_counter()
            # pyautogui.moveRel(delta.x, delta.y, duration=pyautogui.MINIMUM_DURATION * 2, tween=tweenFunc)
            # pyautogui.moveRel(delta.x, delta.y, duration=1 * 2, tween=tweenFunc)
            x, y = pyautogui._normalizeXYArgs(delta.x, delta.y)
            _mouseMoveDrag("move", None, None, x, y, 1.*2, tweenFunc)
            print(f'{(perf_counter()-now)=}')
            mousepos = P(*pyautogui.position())
            pyautogui.leftClick(mousepos)
            self.assertEqual(
                mousepos,
                destination,
                "%s tween move failed. mousepos set to %s instead of %s" % (tweenName, mousepos, destination),
            )











async def main():
    print("Main function started")
    
    # mymouse = MyMouse()
    # mymouse.setUp()
    # print(f'testing test_moveToWithTween')
    # time.sleep(1)
    # mymouse.test_moveToWithTween()
    # print(f'finished test_moveToWithTween. ')
    # # time.sleep(2)
    # print(f'testing test_moveRelWithTween')
    # # time.sleep(1)
    # # mymouse.test_moveRelWithTween()
    # print(f'finished test_moveRelWithTween. ')
    # print("Main function completed")

    # runesolver = RuneSolver()
    # maplehwnd=None
    # chathwnd=None
    # hwnd = 0
    # windows=[]
    # while True:
    #     print(f'{hwnd}')
    #     hwnd = win32gui.FindWindowEx(0,hwnd,None, "MapleStory")
    #     if hwnd == 0:
    #         break
    #     windows.append(hwnd)
    # for windowhwnd in windows:
    #     position = win32gui.GetWindowRect(windowhwnd)
    #     x, y, w, h = position
    #     if w-x == 410:
    #         chathwnd=windowhwnd
    #     else:
    #         maplehwnd=windowhwnd            
    #         runesolver.set_maplehwnd(maplehwnd)
    #         print(f'{maplehwnd}')
    #     print(f'{x} {y} {w} {h}')
    # he = Helper()
    # for i in range(10):
    #     # await he.move_to_and_click(x+100,y+100)
    #     await runesolver.mock()
    #     time.sleep(3)
    #     print(f'done')

    # for i in range(10):
    #     action = Action()
    #     await action.testnpc()
    #     print(f'pressed. ')
    #     time.sleep(1)

    async def func(a,b):
        return a,b    
    async def func2(a,b):
        return await func(a,b)
    a,b = await func2(1,2)
    print(a,b)



# Run the event loop
if __name__ == "__main__":
    asyncio.run(main())