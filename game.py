import gdi_capture
import numpy as np
import cv2
import time
from time import perf_counter
# from PIL import ImageGrab
# import win32gui
# import pygetwindow

alpha=255
# alpha=0
# These are colors taken from the mini-map in BGRA format.
PLAYER_BGRA = (68, 221, 255, alpha)
RUNE_BGRA = (255, 102, 221, alpha)
ENEMY_BGRA = (0, 0, 255, alpha)
GUILD_BGRA = (255, 102, 102, alpha)
BUDDY_BGRA = (225, 221, 17, alpha)

EB3BGR = (0, 34, 204, alpha)
EBBGR = (238, 255, 255, alpha) # yellow timer (x+405, y+75, x+406, y+76) (397,44)
LDBGR = (136, 51, 170, alpha)
RDBGR = (0, 0, 255, alpha)
GDBGR = (221, 170, 170, alpha)
WDBGR = (255, 255, 255, alpha)
DCBGR = (187, 221, 238, alpha)
OKBGR = (17,187,170, alpha) # broid die #normalpc
# OKBGR = (17,187,153, alpha) # broid die 
# OKBGR = (0,187,170, alpha) # died_ok [0 187 170] [0 204 153]
ORBGR = (1,136,245, alpha) # orange_mushroom [1 136 245] [] #normalpc
LOBGR = (17,170,136, alpha) # 
# POBGR = (17,85,238, alpha) # 
POBGR = (102,136,255, alpha) # 
PO2BGR = (0,0,255, alpha) # 
VIBGR = (136,57,170, alpha) # violetta detector (x+701, y+472, x+702, y+473) (693,441)
SWBGR = (238,255,255, alpha) # storming will always be 0 stormwing habitat detector (timer) (221,255,255, 255) (x+405, y+75, x+406, y+76) (397,44)
ESBGR = (51,187,255, alpha) # especia please use the dot especia detector (timer) (221,255,255, 255) (x+405, y+75, x+406, y+76) (397,44)
TIBGR = (204,204,204, alpha) # timer gray dot (304,48)
GMBGR = (222,218,206, alpha) # 
DABGR = (0,0,0, alpha) # 
ROBGR = (187,187,204, alpha) # mapril island infinity race rock light brown bgr value


class Game:
    def __init__(self, region):
        self.hwnd = gdi_capture.find_window_from_executable_name("MapleStory.exe")
        # self.hwnd = gdi_capture.find_window_from_executable_name("Honeyview.exe")
        # These values should represent pixel locations on the screen of the mini-map.
        self.top, self.left, self.bottom, self.right = region[0], region[1], region[2], region[3]
        # self.left, self.top, self.bottom, self.right = region[0], region[1], region[2], region[3]
        self.pololocations = None

    def get_rune_image(self):
        with gdi_capture.CaptureWindow(self.hwnd) as img:
            if img is None:
                print("MapleStory.exe was not found.")
                return None
            return img.copy()

    def locate(self, *color):
        with gdi_capture.CaptureWindow(self.hwnd) as img:
            locations = []
            if img is None:
                print("MapleStory.exe was not found.")
            else:
                # cv2.imshow('img', img)
                # cv2.waitKey(0)
                # cv2.destroyAllWindows()
                # Crop the image to show only the mini-map.
                img_cropped = img[self.left:self.right, self.top:self.bottom]
                # for img in img_cropped:
                #     print(f'{img=}')
                # img_cropped = img[self.top:self.bottom, self.left:self.right]
                height, width = img_cropped.shape[0], img_cropped.shape[1]
                # Reshape the image from 3-d to 2-d by row-major order.
                img_reshaped = np.reshape(img_cropped, ((width * height), 4), order="C")
                # cv2.imshow('img_reshaped', img_reshaped)
                # print(f'{img_cropped=}')
                # cv2.imshow('img_cropped', img_cropped)
                # cv2.waitKey(0)
                # cv2.destroyAllWindows()
                for c in color:
                    # print(f'{c=}')
                    sum_x, sum_y, count = 0, 0, 0
                    # Find all index(s) of np.ndarray matching a specified BGRA tuple.
                    matches = np.where(np.all((img_reshaped == c), axis=1))[0]
                    # print(f'{matches=}')
                    for idx in matches:
                        # Calculate the original (x, y) position of each matching index.
                        sum_x += idx % width
                        sum_y += idx // width
                        count += 1
                    if count > 0:
                        x_pos = sum_x / count
                        y_pos = sum_y / count
                        locations.append((x_pos, y_pos))
            return locations

    def get_player_location(self):
        location = self.locate(PLAYER_BGRA)
        return location[0] if len(location) > 0 else None

    def get_rune_location(self):
        location = self.locate(RUNE_BGRA)
        return location[0] if len(location) > 0 else None

    def get_other_location(self):
        location = self.locate(ENEMY_BGRA, GUILD_BGRA, BUDDY_BGRA)
        return len(location) > 0

    def get_screenshot(self):
        with gdi_capture.CaptureWindow(self.hwnd) as img:
            if img is None:
                print("MapleStory.exe was not found.")
                return None
            return img.copy()
    
    def get_screenshot_bytes(self):
        with gdi_capture.CaptureWindow(self.hwnd) as img:
            if img is None:
                print("MapleStory.exe was not found.")
                return None
            print(f'{img.size=} {img.shape}')
            return img.copy().tobytes()

    def checker(self, *color, x=0,y=0,w=800,h=600):
        with gdi_capture.CaptureWindow(self.hwnd) as img:
            locations = []
            if img is None:
                print("MapleStory.exe was not found.")
            else:
                # print(f'{img}')
                # print(f'{img.ndim}')
                # print(f'{img.shape[0]}')
                # print(f'{img.shape[1]}')
                # print(f'{img.shape[2]}')
                img_cropped = img[y:h, x:w]
                # img_cropped = img[0:600, 0:800]
                # print(f'{img_cropped.shape[0]}')
                # print(f'{img_cropped.shape[1]}')
                # print(f'{img_cropped.ndim}')
                # img_cropped = img[self.left:self.right, self.top:self.bottom]
                # print(f'{img_cropped[60:61][60:61]}')
                height, width = img_cropped.shape[0], img_cropped.shape[1]
                # Reshape the image from 3-d to 2-d by row-major order.
                img_reshaped = np.reshape(img_cropped, ((width * height), 4), order="C")
                for c in color:
                    sum_x, sum_y, count = 0, 0, 0
                    # Find all index(s) of np.ndarray matching a specified BGRA tuple.
                    matches = np.where(np.all((img_reshaped == c), axis=1))[0]
                    # print(f'{matches=}')
                    for idx in matches:
                        # Calculate the original (x, y) position of each matching index.
                        sum_x += idx % width
                        sum_y += idx // width
                        count += 1
                        # print(f'{sum_x=} {sum_y=} {count=}')
                        # print(f'{idx % width=} {idx // width=} {idx % height=} {idx // height=} {width=} {count=}')
                        # print(f'{idx % width=} {idx // width=} {width=} {count=}')
                    if count > 0:
                        x_pos = sum_x / count
                        y_pos = sum_y / count
                        locations.append((x_pos, y_pos))
            # print(f'{locations=}')
            return locations

    def died_checker(self):        
        location = self.checker(OKBGR, x=300,y=300,w=400,h=400)
        # location = self.checker(OKBGR, x=360,y=360,w=361,h=361)
        # location = self.checker(PLAYER_BGRA)
        return location[0] if len(location) > 0 else None

    def reddot_checker(self):
        location = self.locate(ENEMY_BGRA)
        return location[0] if len(location) > 0 else None

    def liedetector_checker(self):
        location = self.checker(LOBGR, x=430,y=375,w=431,h=376)
        return location[0] if len(location) > 0 else None

    def polo_checker(self):
        location = self.locate(POBGR)
        # location = self.checker(PLAYER_BGRA)
        if len(location) > 0:
            self.pololocations = location[0]
            return location[0]
        else:
            return None
        # return location[0] if len(location) > 0 else None

    def get_polo_locations(self):
        return self.pololocations

    def polo2_checker(self): # Polo or Frito
        location = self.checkertest(PO2BGR,x=200,y=253,w=201,h=254)
        # location = self.checker(PLAYER_BGRA)
        return location[0] if len(location) > 0 else None

    def polo3_checker(self): # Flamewolf portal
        location = self.checkertest(PO2BGR,x=172,y=233,w=173,h=234)
        # location = self.checker(PLAYER_BGRA)
        return location[0] if len(location) > 0 else None

    def polo4_checker(self): # Especia portal
        location = self.checkertest(PO2BGR,x=199,y=244,w=200,h=245)
        # location = self.checker(PLAYER_BGRA)
        return location[0] if len(location) > 0 else None

    def especia_dot_checker(self): # Especia dot detector
        location = self.checkertest(ESBGR,x=422,y=68,w=423,h=69)
        # location = self.especiatest(ESBGR,x=400,y=60,w=450,h=110)
        # location = self.checkertest(ESBGR,x=400,y=80,w=450,h=120)
        # location = self.checkertest(ESBGR,x=422,y=98,w=423,h=99) # y=68
        # location = self.checker(PLAYER_BGRA)
        return location[0] if len(location) > 0 else None

    def hunting_map_checker(self): # Hidden Street Bounty Hunt
        # location = self.checkertest(WDBGR,x=85,y=8,w=86,h=9) # minimap white text dot
        location = self.checkertest(WDBGR,x=330,y=100,w=331,h=101) # S of Stage 1
        # location = self.checkertest(WDBGR,x=85,y=9,w=86,h=10)
        # location = self.checker(PLAYER_BGRA)
        return location[0] if len(location) > 0 else None
    
    def hunting_map2_checker(self): # Hidden Street Guarding The Castle Wall
        # location = self.checkertest(WDBGR,x=87,y=8,w=88,h=9) # this 1 is the minimap text white dot, if announcement cant be detected
        # location = self.checkertest2(WDBGR,x=328,y=131,w=329,h=132) # this 1 is the W of the center word Wave 1
        location = self.checkertest2(WDBGR,x=328,y=101,w=329,h=102) # this 1 is the W of the center word Wave 1
        # location = self.checkertest(WDBGR,x=87,y=9,w=88,h=10)
        # location = self.checker(PLAYER_BGRA)
        return location[0] if len(location) > 0 else None
    
    def hunting_map3_checker(self): # Hidden Street Golden Bird (Stormwing Habitat)
        location = self.checkertest(SWBGR,x=397,y=44,w=398,h=45)
        # location = self.checker(PLAYER_BGRA)
        return location[0] if len(location) > 0 else None

    def hunting_map_timer_checker(self): # clock
        location = self.checkertest(TIBGR,x=304,y=48,w=305,h=49)
        # location = self.checker(PLAYER_BGRA)
        return location[0] if len(location) > 0 else None

    def white_dot_checker(self):
        location = self.checkertest(WDBGR,x=292,y=329,w=293,h=330)
        # location = self.checker(PLAYER_BGRA)
        return location[0] if len(location) > 0 else None
    
    def dark_checker(self):
        location = self.checkertest(DABGR,x=292,y=329,w=293,h=330)
        # location = self.checker(PLAYER_BGRA)
        return location[0] if len(location) > 0 else None

    def rock_checker(self):
        location = self.checkertest3(ROBGR,x=430,y=292,w=460,h=293)
        return location
    
    def rock_checker2(self):
        location = self.checkertest3(ROBGR,x=460,y=292,w=490,h=293)
        return location

    def rock_checker3(self):
        location = self.checkertest3(ROBGR,x=500,y=292,w=530,h=293)
        return location
        
    def vdance_checker(self):
        location = self.checkertest4(DABGR,x=435,y=691,w=1034,h=693)
        # location = self.checkertest4(DABGR,x=159,y=523,w=660,h=525)
        # return location[0] if len(location) > 0 else None
        return location # count actually

    def vdance_checker2(self):
        location = self.checkertest5(DABGR,x=435,y=719,w=1034,h=720) # 1366x768 # use this for 49 combo perfect score! best of the best!
        # location = self.checkertest5(DABGR,x=392,y=671,w=991,h=672) # 1280x720 # not as good because the pink gap is narrower unfortunately
        # location = self.checkertest5(DABGR,x=264,y=719,w=863,h=720) # 1024x768 # even worse, very narrow and the V speed is too fast. 
        return location

    def pure_test(self): 
        location = self.checkertest(PLAYER_BGRA,x=self.top,y=self.left,w=self.bottom,h=self.right)
        return location

    def gma_detector(self):
        location = self.gma_detector_checker(GMBGR,x=0,y=300,w=400,h=550)
        # location = self.gma_detector_checker((119,170,179,255),x=0,y=250,w=15,h=265)
        # location = self.checker(PLAYER_BGRA)
        return location[0] if len(location) > 0 else None




    def gma_detector_checker(self, *color, x,y,w,h):
        with gdi_capture.CaptureWindow(self.hwnd) as img:
            locations = []
            if img is None:
                print("MapleStory.exe was not found.")
                # print("Honeyview.exe was not found.")
            else:
                # print(f'{img}')
                # print(f'{img.ndim}')
                # print(f'{img.shape[0]}')
                # print(f'{img.shape[1]}')
                # print(f'{img.shape[2]}')
                img_cropped = img[y:h, x:w]
                # img_cropped = img[0:600, 0:800]
                # print(f'{img_cropped.shape[0]}')
                # print(f'{img_cropped.shape[1]}')
                # print(f'{img_cropped.ndim}')
                # img_cropped = img[self.left:self.right, self.top:self.bottom]
                height, width = img_cropped.shape[0], img_cropped.shape[1]
                # Reshape the image from 3-d to 2-d by row-major order.
                img_reshaped = np.reshape(img_cropped, ((width * height), 4), order="C")
                # print(f'{img_reshaped=}')
                # print(f'{img_reshaped[:,0]=}')
                # cv2.imshow('img_reshaped', img_reshaped)
                cv2.imshow('img', img)
                # cv2.imshow('img_cropped', img_cropped)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
                # print(f'{color=}')
                for c in color:
                    # print(f'{c=}')
                    sum_x, sum_y, count = 0, 0, 0
                    # Find all index(s) of np.ndarray matching a specified BGRA tuple.
                    # print(f'{np.where(np.all((img_reshaped == c), axis=1))=}')
                    # print(f'{np.where(np.all((img_reshaped == c), axis=1))[0]=}')
                    # matches = np.where(np.all((img_reshaped == c), axis=1))[0]
                    matches = np.where(
                        (img_reshaped[:,0] >= 201) & (img_reshaped[:,0] <= 225) &
                        (img_reshaped[:,1] >= 201) & (img_reshaped[:,1] <= 225) &
                        (img_reshaped[:,2] >= 201) & (img_reshaped[:,2] <= 225) 
                        )[0]
                    # matches = np.where(
                    #     (img_reshaped[:,0] >= 201) & (img_reshaped[:,0] <= 225) &
                    #     (img_reshaped[:,1] >= 201) & (img_reshaped[:,1] <= 225) &
                    #     (img_reshaped[:,2] >= 201) & (img_reshaped[:,2] <= 225) 
                    #     )
                    print(f'{matches=}')
                    for idx in matches:
                        # Calculate the original (x, y) position of each matching index.
                        sum_x += idx % width
                        sum_y += idx // width
                        count += 1
                        # print(f'{sum_x=} {sum_y=} {count=}')
                        # print(f'{idx % width=} {idx // width=} {width=} {img_reshaped[idx]} {count=}')
                    if count > 0:
                        x_pos = sum_x / count
                        y_pos = sum_y / count
                        locations.append((x_pos, y_pos))
            # print(f'{locations=}')
            return locations


        
    def especiatest(self, *color, x,y,w,h):
        with gdi_capture.CaptureWindow(self.hwnd) as img:
            locations = []
            if img is None:
                print("MapleStory.exe was not found.")
            else:
                # print(f'{img}')
                # print(f'{img.ndim}')
                # print(f'{img.shape[0]}')
                # print(f'{img.shape[1]}')
                # print(f'{img.shape[2]}')
                img_cropped = img[y:h, x:w]
                # img_cropped = img[0:600, 0:800]
                # print(f'{img_cropped.shape[0]}')
                # print(f'{img_cropped.shape[1]}')
                # print(f'{img_cropped.ndim}')
                # img_cropped = img[self.left:self.right, self.top:self.bottom]
                height, width = img_cropped.shape[0], img_cropped.shape[1]
                # Reshape the image from 3-d to 2-d by row-major order.
                img_reshaped = np.reshape(img_cropped, ((width * height), 4), order="C")
                # cv2.imshow('img_reshaped', img_reshaped)
                cv2.imshow('img_cropped', img_cropped)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
                for c in color:
                    sum_x, sum_y, count = 0, 0, 0
                    # Find all index(s) of np.ndarray matching a specified BGRA tuple.
                    matches = np.where(np.all((img_reshaped == c), axis=1))[0]
                    # print(f'{matches=}')
                    for idx in matches:
                        # Calculate the original (x, y) position of each matching index.
                        sum_x += idx % width
                        sum_y += idx // width
                        count += 1
                        # print(f'{sum_x=} {sum_y=} {count=}')
                        # print(f'{idx % width=} {idx // width=} {idx % height=} {idx // height=} {width=} {count=}')
                        print(f'{idx % width=} {idx // width=} {width=} {count=}')
                    if count > 0:
                        x_pos = sum_x / count
                        y_pos = sum_y / count
                        locations.append((x_pos, y_pos))
            # print(f'{locations=}')
            return locations

    # def init_maple_windows(self):
    #     windows=[]
    #     winlist=[]
    #     winlist = pygetwindow.getWindowsWithTitle('MapleStory')
    #     for w in winlist:
    #         windows.append(w._hWnd)
    #     for windowhwnd in windows:
    #         position = win32gui.GetWindowRect(windowhwnd)
    #         x, y, w, h = position
    #         if w-x == 410:
    #             self.chathwnd=windowhwnd
    #         else:
    #             self.maplehwnd=windowhwnd
    #     self.position = win32gui.GetWindowRect(self.maplehwnd)
                
    def checkertest(self, *color, x,y,w,h):
        # now=perf_counter()
        # screenshot = ImageGrab.grab(self.position)
        # screenshot = np.array(screenshot)
        # img = cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR)
        # now1=perf_counter()-now
        # print(f'{now1=}')
        # now2=perf_counter()
        with gdi_capture.CaptureWindow(self.hwnd) as img:
            # now3=perf_counter()-now2
            locations = []
            if img is None:
                print("MapleStory.exe was not found.")
            else:
                # print(f'{img=} {img.ndim=}')
                # print(f'{img.ndim}')
                # print(f'{img.shape[0]}')
                # print(f'{img.shape[1]}')
                # print(f'{img.shape[2]}')
                img_cropped = img[y:h, x:w]
                # now2=perf_counter()-now
                # img_cropped = img[0:600, 0:800]
                # print(f'{img_cropped.shape[0]}')
                # print(f'{img_cropped.shape[1]}')
                # print(f'{img_cropped.ndim}')
                # img_cropped = img[self.left:self.right, self.top:self.bottom]
                height, width = img_cropped.shape[0], img_cropped.shape[1]
                # Reshape the image from 3-d to 2-d by row-major order.
                img_reshaped = np.reshape(img_cropped, ((width * height), 4), order="C")
                # now3=perf_counter()-now
                # cv2.imshow('img_reshaped', img_reshaped)
                # cv2.imshow('img_cropped', img_cropped)
                # cv2.waitKey(0)
                # cv2.destroyAllWindows()
                # print(f'{img_cropped=}')
                for c in color:
                    sum_x, sum_y, count = 0, 0, 0
                    # Find all index(s) of np.ndarray matching a specified BGRA tuple.
                    # now4=perf_counter()
                    matches = np.where(np.all((img_reshaped == c), axis=1))[0]
                    # now5=perf_counter()-now4
                    # print(f'n3={now3:.10f}')
                    # print(f'n1={now1:.10f} n3={now3:.10f} n5={now5:.10f}')
                    # print(f'{matches=}')
                    for idx in matches:
                        # Calculate the original (x, y) position of each matching index.
                        sum_x += idx % width
                        sum_y += idx // width
                        count += 1
                        # print(f'{sum_x=} {sum_y=} {count=}')
                        # print(f'{idx % width=} {idx // width=} {idx % height=} {idx // height=} {width=} {count=}')
                        # print(f'{idx % width=} {idx // width=} {width=} {count=}')
                    if count > 0:                        
                        # print(f'{img_cropped=}')
                        x_pos = sum_x / count
                        y_pos = sum_y / count
                        locations.append((x_pos, y_pos))
            # print(f'{locations=}')
            return locations
            
    def checkertest2(self, *color, x,y,w,h):
        with gdi_capture.CaptureWindow(self.hwnd) as img:
            locations = []
            if img is None:
                print("MapleStory.exe was not found.")
            else:
                img_cropped = img[y:h, x:w]
                print(f'{img_cropped=}')
                height, width = img_cropped.shape[0], img_cropped.shape[1]
                # Reshape the image from 3-d to 2-d by row-major order.
                img_reshaped = np.reshape(img_cropped, ((width * height), 4), order="C")
                # cv2.imshow('img_reshaped', img_reshaped)
                # cv2.imshow('img_cropped', img_cropped)
                # cv2.waitKey(0)
                # cv2.destroyAllWindows()
                for c in color:
                    sum_x, sum_y, count = 0, 0, 0
                    # Find all index(s) of np.ndarray matching a specified BGRA tuple.
                    matches = np.where(np.all((img_reshaped == c), axis=1))[0]
                    for idx in matches:
                        # Calculate the original (x, y) position of each matching index.
                        sum_x += idx % width
                        sum_y += idx // width
                        count += 1
                        print(f'{idx % width=} {idx // width=} {width=} {count=}')
                    if count > 0:
                        x_pos = sum_x / count
                        y_pos = sum_y / count
                        locations.append((x_pos, y_pos))
            return locations

            
    def checkertest3(self, *color, x,y,w,h):
        with gdi_capture.CaptureWindow(self.hwnd) as img:
            locations = []
            if img is None:
                print("MapleStory.exe was not found.")
            else:
                img_cropped = img[y:h, x-15:w-15]
                img_cropped2 = img[y+50:h+50,x:w]
                # print(f'{img_cropped=}')
                height, width = img_cropped.shape[0], img_cropped.shape[1]
                # Reshape the image from 3-d to 2-d by row-major order.
                img_reshaped = np.reshape(img_cropped, ((width * height), 4), order="C")
                img_reshaped2 = np.reshape(img_cropped2, ((width * height), 4), order="C")
                # cv2.imshow('img_reshaped', img_reshaped)
                # cv2.imshow('img_cropped', img_cropped)
                # cv2.waitKey(0)
                # cv2.destroyAllWindows()
                for c in color:
                    sum_x, sum_y, count = 0, 0, 0
                    count2=0
                    # Find all index(s) of np.ndarray matching a specified BGRA tuple.
                    matches = np.where(np.all((img_reshaped == c), axis=1))[0]
                    for idx in matches:
                        # Calculate the original (x, y) position of each matching index.
                        # sum_x += idx % width
                        # sum_y += idx // width
                        count += 1
                        # print(f'{idx % width=} {idx // width=} {width=} {count=}')
                    if count > 0:
                        # x_pos = sum_x / count
                        # y_pos = sum_y / count
                        # locations.append((x_pos, y_pos))
                        return (True,False)
                    matches2 = np.where(np.all((img_reshaped2 == c), axis=1))[0]
                    for idx in matches2:
                        count2 += 1
                    if count2 > 0:
                        return (False,True)
            # return locations
            return None



    def checkertest4(self, *color, x,y,w,h):
        with gdi_capture.CaptureWindow(self.hwnd) as img:
            locations = []
            if img is None:
                print("MapleStory.exe was not found.")
            else:
                img_cropped = img[y:h, x:w]
                # print(f'{img_cropped=}')
                height, width = img_cropped.shape[0], img_cropped.shape[1]
                # Reshape the image from 3-d to 2-d by row-major order.
                img_reshaped = np.reshape(img_cropped, ((width * height), 4), order="C")
                # cv2.imshow('img_reshaped', img_reshaped)
                # cv2.imshow('img_cropped', img_cropped)
                # cv2.waitKey(0)
                # cv2.destroyAllWindows()
                for c in color:
                    sum_x, sum_y, count = 0, 0, 0
                    # Find all index(s) of np.ndarray matching a specified BGRA tuple.
                    # matches = np.where(np.all((img_reshaped == c), axis=1))[0]
                    matches = np.where(
                        (img_reshaped[:,0] >= 227) & (img_reshaped[:,0] <= 239) &
                        (img_reshaped[:,1] >= 166) & (img_reshaped[:,1] <= 180) &
                        (img_reshaped[:,2] >= 247) & (img_reshaped[:,2] <= 248) 
                        )[0]
                    for idx in matches:
                        # Calculate the original (x, y) position of each matching index.
                        sum_x += idx % width
                        sum_y += idx // width
                        count += 1
                        # print(f'{idx % width=} {idx // width=} {width=} {count=}')
                    # if count > 0:
                    #     x_pos = sum_x / count
                    #     y_pos = sum_y / count
                    #     locations.append((x_pos, y_pos))
            # return locations
            return count
            
    def checkertest5(self, *color, x,y,w,h):
        with gdi_capture.CaptureWindow(self.hwnd) as img:
            locations = []
            if img is None:
                print("MapleStory.exe was not found.")
            else:
                img_cropped = img[y:h, x:w]
                img_cropped2 = img[y-2:h-2, x:w]
                height, width = img_cropped.shape[0], img_cropped.shape[1]
                img_reshaped = np.reshape(img_cropped, ((width * height), 4), order="C")
                img_reshaped2 = np.reshape(img_cropped2, ((width * height), 4), order="C")
                for c in color:
                    sum_x, sum_y, count = 0, 0, 0
                    # matches = np.where(
                    #     (img_reshaped[:,0] >= 237) & (img_reshaped[:,0] <= 239) &
                    #     (img_reshaped[:,1] >= 135) & (img_reshaped[:,1] <= 137) &
                    #     (img_reshaped[:,2] >= 253) & (img_reshaped[:,2] <= 255) 
                    #     )[0]
                    matches = np.where(
                        (img_reshaped[:,0] >= 180) & (img_reshaped[:,0] <= 239) &
                        (img_reshaped[:,1] >= 135) & (img_reshaped[:,1] <= 195) &
                        (img_reshaped[:,2] >= 253) & (img_reshaped[:,2] <= 255) 
                        )[0]
                    # print(f'{matches=}')
                    # for idx in matches:
                    #     pass
                    for idx in matches:
                        # print(f'{img_reshaped2[idx]=}')
                        if img_reshaped2[idx,0]+66 < 255:
                            if img_reshaped2[idx,1]+66 < 255:
                                if img_reshaped2[idx,2]+66 < 255:
                                    # print(f'press npc key now. {img_reshaped2[idx]}')
                                    return idx
                        # print(f'{sum_x=} {sum_y=} {count=}')
                        # sum_x += idx % width
                        # sum_y += idx // width
                        count += 1
                    # print(f'{sum_x=} {sum_y=} {count=}')
                    # if count > 0:
                    #     x_pos = sum_x / count
                    #     y_pos = sum_y / count
                    #     locations.append((x_pos, y_pos))
                    # print(f'{locations=}')
            return 0