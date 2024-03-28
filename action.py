import random
import time
from configparser import ConfigParser
from initinterception import interception, move_to, move_relative, left_click, keydown, keyup, sleep









config = ConfigParser()
config.read('settings.ini')
atk = config.get('keybind', 'attack')
jump = config.get('keybind', 'jump')
teleport = config.get('keybind', 'teleport')
ropeconnect = config.get('keybind', 'ropeconnect')
npc = config.get('keybind', 'npc')


async def leftp(x=31,y=101):
    keydown('left')
    r = random.randint(x, y)
    r /= 1000
    await sleep(r)

async def leftr(x=31,y=101):
    keyup('left')
    r = random.randint(x, y)
    r /= 1000
    await sleep(r)

async def rightp(x=31,y=101):
    keydown('right')
    r = random.randint(x, y)
    r /= 1000
    await sleep(r)

async def rightr(x=31,y=101):
    keyup('right')
    r = random.randint(x, y)
    r /= 1000
    await sleep(r)

async def upp(x=31,y=101):
    keydown('up')
    r = random.randint(x, y)
    r /= 1000
    await sleep(r)

async def upr(x=31,y=101):
    keyup('up')
    r = random.randint(x, y)
    r /= 1000
    await sleep(r)

async def downp(x=31,y=101):
    keydown('down')
    r = random.randint(x, y)
    r /= 1000
    await sleep(r)

async def downr(x=31,y=101):
    keyup('down')
    r = random.randint(x, y)
    r /= 1000
    await sleep(r)

async def jumpp(x=31,y=101):
    keydown(jump)
    r = random.randint(x, y)
    r /= 1000
    await sleep(r)

async def jumpr(x=31,y=101):
    keyup(jump)
    r = random.randint(x, y)
    r /= 1000
    await sleep(r)

async def teleportp(x=31,y=101):
    keydown(teleport)
    r = random.randint(x, y)
    r /= 1000
    await sleep(r)

async def teleportr(x=31,y=101):
    keyup(teleport)
    r = random.randint(x, y)
    r /= 1000
    await sleep(r)

async def npcp(x=31,y=101):
    keydown(npc)
    r = random.randint(x, y)
    r /= 1000
    await sleep(r)

async def npcr(x=31,y=101):
    keyup(npc)
    r = random.randint(x, y)
    r /= 1000
    await sleep(r)

async def attackp(x=31,y=101):
    keydown(atk)
    r = random.randint(x, y)
    r /= 1000
    await sleep(r)

async def attackr(x=31,y=101):
    keyup(atk)
    r = random.randint(x, y)
    r /= 1000
    await sleep(r)

async def ropeconnectp(x=31,y=101):
    keydown(ropeconnect)
    r = random.randint(x, y)
    r /= 1000
    await sleep(r)

async def ropeconnectr(x=31,y=101):
    keyup(ropeconnect)
    r = random.randint(x, y)
    r /= 1000
    await sleep(r)

async def ropeconnectpr():
    await ropeconnectp()
    await ropeconnectr()





class Action:

    def __init__(self):
        pass

    
    async def leftattack(self):
        print(f'leftattack')
        await leftp()
        await attackp()
        await attackr()
        await leftr()

    async def rightattack(self):
        print(f'rightattack')
        await rightp()
        await attackp()
        await attackr()
        await rightr()

    async def leftattackk(self):
        print(f'leftattackk')
        await leftp()
        await attackp()
        await attackr()
        await attackp()
        await attackr()
        await leftr()

    async def rightattackk(self):
        print(f'rightattackk')
        await rightp()
        await attackp()
        await attackr()
        await rightr()

    async def goleftattack(self):
        print(f'self.goleftattack')
        await leftp()
        await teleportp()
        await teleportr()
        await attackp()
        await attackr()
        await leftr()

    async def goleftattackk(self):
        print(f'self.goleftattackk')
        await leftp()
        await teleportp()
        await teleportr()
        await attackp()
        await attackr()
        await attackp()
        await attackr()
        await leftr()

    async def goattackleft(self):
        print(f'self.goattackleft')
        await leftp()
        await attackp()
        await attackr()
        await teleportp()
        await teleportr()
        await leftr()

    async def goattackkleft(self):
        print(f'self.goattackkleft')
        await leftp()
        await attackp()
        await attackr()
        await attackp()
        await attackr()
        await teleportp()
        await teleportr()
        await leftr()

    async def goleftattackv2(self):
        print(f'self.goleftattackv2')
        await leftp()
        await jumpp()
        await jumpr()    
        await jumpp()
        await jumpr()
        await attackp()
        await attackr()
        await leftr()

    async def gorightattack(self):
        print(f'self.gorightattack')
        await rightp()
        await teleportp()
        await teleportr()
        await attackp()
        await attackr()
        await rightr()

    async def gorightattackk(self):
        print(f'self.gorightattackk')
        await rightp()
        await teleportp()
        await teleportr()
        await attackp()
        await attackr()
        await attackp()
        await attackr()
        await rightr()

    async def goattackright(self):
        print(f'self.goattackright')
        await rightp()
        await attackp()
        await attackr()
        await teleportp()
        await teleportr()
        await rightr()

    async def goattackkright(self):
        print(f'self.goattackkright')
        await rightp()
        await attackp()
        await attackr()
        await attackp()
        await attackr()
        await teleportp()
        await teleportr()
        await rightr()

    async def gorightattackv2(self):
        print(f'self.gorightattackv2')
        await rightp()
        await jumpp()
        await jumpr()    
        await jumpp()
        await jumpr()
        await attackp()
        await attackr()
        await rightr()

    async def goupattackv2(self):
        print(f'goupattackv2')
        await rightp()
        await ropeconnectp()
        await ropeconnectr()
        await attackp()
        await attackr()
        await rightr()

    async def goupattack(self):
        print(f'goupattack')
        await sleep(.1)
        await upp()
        await teleportp()
        await teleportr()
        await upr()
        await attackp()
        await attackr()
        await sleep(.1)

    async def goupattackv3(self):
        print(f'goupattackv3')
        await sleep(.1)
        await jumpp()
        await jumpr()
        await ropeconnectp(31,101)
        await ropeconnectr(31,101)
        await sleep(.333)
        await attackp()
        await attackr()
        await attackp()
        await attackr()
        await sleep(.1)

    async def upjumpattack(self):
        print(f'upjumpattack')
        await sleep(.1)
        await upp()
        await teleportp()
        await teleportr()
        await upr()
        await attackp()
        await attackr()
        await sleep(.1)

    async def upjumpattackv2(self): # adele upjump
        print(f'upjumpattackv2')
        await sleep(.1)
        await jumpp()
        await jumpr()
        await upp()
        await jumpp()
        await jumpr()
        await upr()
        await attackp()
        await attackr()
        await attackp()
        await attackr()
        await sleep(.1)

    async def godownattack(self):
        print(f'godownattack')
        await downp()
        await teleportp()
        await teleportr()
        await downr()
        await attackp()
        await attackr()
        await sleep(.1)

    async def godownattackv2(self):
        print(f'godownattackv2')
        await downp()    
        await jumpp()
        await jumpr()
        await attackp()
        await attackr()
        await downr()


    # polo portal hunting map rotation patch

    async def upjumpup(self):
        print(f'upjumpup')
        await jumpp()
        await jumpr()
        await upp()
        await jumpp()
        await jumpr()
        await upr()

    async def bountyhuntrotation(self):
        print(f'bountyhuntrotation')
        for i in range(5):
            await random.choice([self.goleftattack,self.goattackleft,self.goleftattackk,self.goattackkleft, self.leftattack, self.rightattack, self.leftattackk, self.rightattackk])()
            time.sleep(.502)
        for i in range(5):
            await random.choice([self.gorightattack,self.goattackright,self.gorightattackk,self.goattackkright, self.leftattack, self.rightattack, self.leftattackk, self.rightattackk])()
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
        await ropeconnectpr()
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
        await ropeconnectpr()
        time.sleep(.802)
        for i in range(2):
            await self.gorightattack()
            time.sleep(.502)
        await self.downjump()
        time.sleep(.702)
        await attackp()
        await attackr()
        time.sleep(.502)

    async def stormwingrotation(self):
        print(f'stormwingrotation')
        for i in range(5):
            await self.goleftattack()
            time.sleep(.502)
        await ropeconnectpr()
        time.sleep(.602)
        for i in range(5):
            await self.gorightattack()
            time.sleep(.502)
        for i in range(5):
            await self.downjump()
            time.sleep(.302)

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
