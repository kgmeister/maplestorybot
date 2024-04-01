import random
import time
from configparser import ConfigParser
# from initinterception import interception, move_to, move_relative, left_click, keydown, keyup, sleep
from initinterception import keydown, keyup, sleep














class Action:

    def __init__(self):            
        self.config = ConfigParser()
        self.config.read('settings.ini')
        self.atk = self.config.get('keybind', 'attack')
        self.jump = self.config.get('keybind', 'jump')
        self.teleport = self.config.get('keybind', 'teleport')
        self.ropeconnect = self.config.get('keybind', 'ropeconnect')
        self.npc = self.config.get('keybind', 'npc')
        self.offsety=10
        self.offsetx=10
        ## for stormwing map
        self.top=29.0
        self.left=35.0 # 18.0 # 27.0
        self.right=130 # 125.0 # 135.0 140.0 132.5
        self.btm=58.0 # 54.5
    
    def refreshkeybind(self):
        self.config.read('settings.ini')
        self.atk = self.config.get('keybind', 'attack')
        self.jump = self.config.get('keybind', 'jump')
        self.teleport = self.config.get('keybind', 'teleport')
        self.ropeconnect = self.config.get('keybind', 'ropeconnect')
        self.npc = self.config.get('keybind', 'npc')

    async def leftp(self,x=31,y=101):
        keydown('left')
        r = random.randint(x, y)
        r /= 1000
        await sleep(r)

    async def leftr(self,x=31,y=101):
        keyup('left')
        r = random.randint(x, y)
        r /= 1000
        await sleep(r)

    async def rightp(self,x=31,y=101):
        keydown('right')
        r = random.randint(x, y)
        r /= 1000
        await sleep(r)

    async def rightr(self,x=31,y=101):
        keyup('right')
        r = random.randint(x, y)
        r /= 1000
        await sleep(r)

    async def upp(self,x=31,y=101):
        keydown('up')
        r = random.randint(x, y)
        r /= 1000
        await sleep(r)

    async def upr(self,x=31,y=101):
        keyup('up')
        r = random.randint(x, y)
        r /= 1000
        await sleep(r)

    async def downp(self,x=31,y=101):
        keydown('down')
        r = random.randint(x, y)
        r /= 1000
        await sleep(r)

    async def downr(self,x=31,y=101):
        keyup('down')
        r = random.randint(x, y)
        r /= 1000
        await sleep(r)

    async def jumpp(self,x=31,y=101):
        keydown(self.jump)
        r = random.randint(x, y)
        r /= 1000
        await sleep(r)

    async def jumpr(self,x=31,y=101):
        keyup(self.jump)
        r = random.randint(x, y)
        r /= 1000
        await sleep(r)

    async def teleportp(self,x=31,y=101):
        keydown(self.teleport)
        r = random.randint(x, y)
        r /= 1000
        await sleep(r)

    async def teleportr(self,x=31,y=101):
        keyup(self.teleport)
        r = random.randint(x, y)
        r /= 1000
        await sleep(r)

    async def npcp(self,x=31,y=101):
        keydown(self.npc)
        r = random.randint(x, y)
        r /= 1000
        await sleep(r)

    async def npcr(self,x=31,y=101):
        keyup(self.npc)
        r = random.randint(x, y)
        r /= 1000
        await sleep(r)

    async def attackp(self,x=31,y=101):
        keydown(self.atk)
        r = random.randint(x, y)
        r /= 1000
        await sleep(r)

    async def attackr(self,x=31,y=101):
        keyup(self.atk)
        r = random.randint(x, y)
        r /= 1000
        await sleep(r)

    async def ropeconnectp(self,x=31,y=101):
        keydown(self.ropeconnect)
        r = random.randint(x, y)
        r /= 1000
        await sleep(r)

    async def ropeconnectr(self,x=31,y=101):
        keyup(self.ropeconnect)
        r = random.randint(x, y)
        r /= 1000
        await sleep(r)

    async def ropeconnectpr(self):
        await self.ropeconnectp()
        await self.ropeconnectr()
    
    async def leftattack(self):
        print(f'leftattack')
        await self.leftp()
        await self.attackp()
        await self.attackr()
        await self.leftr()

    async def rightattack(self):
        print(f'rightattack')
        await self.rightp()
        await self.attackp()
        await self.attackr()
        await self.rightr()

    async def leftattackk(self):
        print(f'leftattackk')
        await self.leftp()
        await self.attackp()
        await self.attackr()
        await self.attackp()
        await self.attackr()
        await self.leftr()

    async def rightattackk(self):
        print(f'rightattackk')
        await self.rightp()
        await self.attackp()
        await self.attackr()
        await self.rightr()

    async def goleftattack(self):
        print(f'self.goleftattack')
        await self.leftp()
        await self.teleportp()
        await self.teleportr()
        await self.attackp()
        await self.attackr()
        await self.leftr()

    async def goleftattackk(self):
        print(f'self.goleftattackk')
        await self.leftp()
        await self.teleportp()
        await self.teleportr()
        await self.attackp()
        await self.attackr()
        await self.attackp()
        await self.attackr()
        await self.leftr()

    async def goattackleft(self):
        print(f'self.goattackleft')
        await self.leftp()
        await self.attackp()
        await self.attackr()
        await self.teleportp()
        await self.teleportr()
        await self.leftr()

    async def goattackkleft(self):
        print(f'self.goattackkleft')
        await self.leftp()
        await self.attackp()
        await self.attackr()
        await self.attackp()
        await self.attackr()
        await self.teleportp()
        await self.teleportr()
        await self.leftr()

    async def gorightattack(self):
        print(f'self.gorightattack')
        await self.rightp()
        await self.teleportp()
        await self.teleportr()
        await self.attackp()
        await self.attackr()
        await self.rightr()

    async def gorightattackk(self):
        print(f'self.gorightattackk')
        await self.rightp()
        await self.teleportp()
        await self.teleportr()
        await self.attackp()
        await self.attackr()
        await self.attackp()
        await self.attackr()
        await self.rightr()

    async def goattackright(self):
        print(f'self.goattackright')
        await self.rightp()
        await self.attackp()
        await self.attackr()
        await self.teleportp()
        await self.teleportr()
        await self.rightr()

    async def goattackkright(self):
        print(f'self.goattackkright')
        await self.rightp()
        await self.attackp()
        await self.attackr()
        await self.attackp()
        await self.attackr()
        await self.teleportp()
        await self.teleportr()
        await self.rightr()

    async def goupattack(self):
        print(f'goupattack')
        await sleep(.1)
        await self.upp()
        await self.teleportp()
        await self.teleportr()
        await self.upr()
        await self.attackp()
        await self.attackr()
        await sleep(.1)

    async def goupattack_v2(self):
        print(f'goupattack_v2')
        await self.rightp()
        await self.ropeconnectp()
        await self.ropeconnectr()
        await self.attackp()
        await self.attackr()
        await self.rightr()

    async def goupattack_v3(self):
        print(f'goupattack_v3')
        await sleep(.1)
        await self.jumpp()
        await self.jumpr()
        await self.ropeconnectp(31,101)
        await self.ropeconnectr(31,101)
        await sleep(.333)
        await self.attackp()
        await self.attackr()
        await self.attackp()
        await self.attackr()
        await sleep(.1)

    async def upjumpattack(self):
        print(f'upjumpattack')
        await sleep(.1)
        await self.upp()
        await self.teleportp()
        await self.teleportr()
        await self.upr()
        await self.attackp()
        await self.attackr()
        await sleep(.1)

    async def godownattack(self):
        print(f'godownattack')
        await self.downp()
        await self.teleportp()
        await self.teleportr()
        await self.downr()
        await self.attackp()
        await self.attackr()
        await sleep(.1)




    async def goleftattack_fjump(self):
        print(f'self.goleftattack_fjump')
        await self.leftp()
        await self.jumpp()
        await self.jumpr()    
        await self.jumpp()
        await self.jumpr()
        await self.attackp()
        await self.attackr()
        await self.leftr()

    async def gorightattack_fjump(self):
        print(f'self.gorightattack_fjump')
        await self.rightp()
        await self.jumpp()
        await self.jumpr()    
        await self.jumpp()
        await self.jumpr()
        await self.attackp()
        await self.attackr()
        await self.rightr()

    async def goupattack_fjump(self): # adele upjump
        print(f'goupattack_fjump')
        await sleep(.1)
        await self.jumpp()
        await self.jumpr()
        await self.upp()
        await self.jumpp()
        await self.jumpr()
        await self.upr()
        await self.attackp()
        await self.attackr()
        await self.attackp()
        await self.attackr()
        await sleep(.1)

    async def godownattack_fjump(self):
        print(f'godownattack_fjump')
        await self.downp()    
        await self.jumpp()
        await self.jumpr()
        await self.attackp()
        await self.attackr()
        await self.downr()
        
    async def leftwalk(self):
        print(f'leftwalk')
        await self.leftp(222,333)
        await self.leftr()

    async def rightwalk(self):
        print(f'rightwalk')
        await self.rightp(222,333)
        await self.rightr()
        
    async def downjump(self):
        await self.downp()
        await self.jumpp()
        await self.jumpr()
        await self.downr()

    # polo portal hunting map rotation patch

    async def upjumpup(self):
        print(f'upjumpup')
        await self.jumpp()
        await self.jumpr()
        await self.upp()
        await self.jumpp()
        await self.jumpr()
        await self.upr()

    async def bountyhuntrotation(self):
        print(f'bountyhuntrotation')
        for i in range(5):
            await random.choice([self.goleftattack,self.goattackleft,self.goleftattackk,self.goattackkleft])()
            time.sleep(.502)
        for i in range(5):
            await random.choice([self.gorightattack,self.goattackright,self.gorightattackk,self.goattackkright])()
            time.sleep(.502)

    async def bountyhuntrotationv2(self): # adele flash jump
        print(f'bountyhuntrotationv2')
        for i in range(4):
            await self.goleftattack()
            time.sleep(.502)
        for i in range(4):
            await self.gorightattack()
            time.sleep(.502)

    async def castlewallrotation(self):
        print(f'castlewallrotation') 
        await random.choice([self.goleftattack,self.goattackleft,self.goleftattackk,self.goattackkleft, self.leftattack, self.rightattack, self.leftattackk, self.rightattackk])()
        time.sleep(.5)
        await random.choice([self.gorightattack,self.goattackright,self.gorightattackk,self.goattackkright, self.leftattack, self.rightattack, self.leftattackk, self.rightattackk])()
        time.sleep(.5)
        # await self.goleftattack()
        # time.sleep(.502)
        await self.upjumpup()
        time.sleep(.802)
        await random.choice([self.goleftattack,self.goattackleft,self.goleftattackk,self.goattackkleft, self.leftattack, self.rightattack, self.leftattackk, self.rightattackk])()
        time.sleep(.5)
        await random.choice([self.gorightattack,self.goattackright,self.gorightattackk,self.goattackkright, self.leftattack, self.rightattack, self.leftattackk, self.rightattackk])()
        time.sleep(.5)
        # await self.gorightattack()
        # time.sleep(.502)
        await self.downjump()
        time.sleep(.702)

    async def castlewallrotationv3(self):
        print(f'castlewallrotationv3')
        await self.leftattack()
        time.sleep(.5)
        await self.rightattack()
        time.sleep(.5)
        # await self.goleftattack()
        # time.sleep(.502)
        await self.ropeconnectpr()
        time.sleep(.802)
        await self.leftattack()
        time.sleep(.5)
        await self.rightattack()
        time.sleep(.5)
        # await self.gorightattack()
        # time.sleep(.502)
        await self.downjump()
        time.sleep(.702)

    async def castlewallrotationv2(self):
        print(f'castlewallrotationv2')
        for i in range(2):
            await self.goleftattack()
            time.sleep(.502)
        await self.ropeconnectpr()
        time.sleep(.802)
        for i in range(2):
            await self.gorightattack()
            time.sleep(.502)
        await self.downjump()
        time.sleep(.702)
        await self.attackp()
        await self.attackr()
        time.sleep(.502)

    async def stormwingrotation(self):
        print(f'stormwingrotation')
        for i in range(5):
            await self.goleftattack()
            time.sleep(.502)
        await self.ropeconnectpr()
        time.sleep(.602)
        for i in range(5):
            await self.gorightattack()
            time.sleep(.502)
        for i in range(5):
            await self.downjump()
            time.sleep(.302)

    async def stormwing(self,x,y,goleft,goright):
        if goright:
            if x > self.right:
                if y < self.btm:
                    await self.godownattack()
                    time.sleep(.3)
                    await random.choice([self.goleftattack,self.goattackleft,self.goleftattackk,self.goattackkleft])()
                    time.sleep(.1)
                elif y > self.top:
                    await self.upjumpattack()
                    time.sleep(.3)
                goright=False
                goleft=True
            else:
                await random.choice([self.gorightattack,self.goattackright,self.gorightattackk,self.goattackkright])()
                time.sleep(.3)
            if x < self.left: # only if x < left
                if y < self.btm:
                    await self.godownattack()
                    time.sleep(.3)
        elif goleft:
            if x < self.left: # only if x < left
                if y > self.top:
                    time.sleep(.1)
                    await self.upjumpattack()
                    time.sleep(.3)
                elif y < self.top:
                    await self.godownattack()
                    time.sleep(.3)
                    await random.choice([self.gorightattack,self.goattackright,self.gorightattackk,self.goattackkright])()
                    time.sleep(.3)
                goright=True
                goleft=False
            else:
                await random.choice([self.goleftattack,self.goattackleft,self.goleftattackk,self.goattackkleft])()
                time.sleep(.3)
            if x > self.right: # only if x > right
                if y < self.btm:
                    await self.godownattack()
                    time.sleep(.3)
        return goleft,goright


    # randomiser patch

    async def send2(self, code):
        keydown(code)
        r = random.randint(31, 131)
        r /= 1000
        await sleep(r)

    async def send3(self, code):
        keyup(code)
        r = random.randint(31, 131)
        r /= 1000
        await sleep(r)

    # test purpose

    async def testnpc(self):
        await self.npcp()
        await self.npcr()
