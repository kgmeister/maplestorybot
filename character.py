












import random
from action import Action
from flashjump import Flashjump
from teleport import Teleport
from nightlord import Nightlord




class Character:

    def __init__(self) -> None:
        self.top=0
        self.btm=0
        self.left=0
        self.right=0
        self.offsety=10
        self.offsetx=10
        self.replaceropeconnect=False
        # self.teleport=True
        # self.ac = Action()
        self.ac = None
        self.classtype = {
            'teleport': Teleport,
            'flashjump': Flashjump,
            'nightlord': Nightlord,
        }

    def setup(self,left,right,top,btm,classtype):
        self.left=left
        self.right=right
        self.top=top
        self.btm=btm
        self.ac=self.classtype[classtype]()
        print(f'setup complete. {left=} {right=} {top=} {btm=}')

    def change_ac_type(self, classtype):
        if classtype in self.classtype:
            self.ac = self.classtype[classtype]()
            self.offsetx=self.ac.offsetx
            self.offsety=self.ac.offsety
            print(f'{self.offsetx=} {self.offsety=} {self.classtype=}')

    # def change_ac_type(self,ac):
        # self.ac=ac
        # if isinstance(self.ac, Flashjump):
        #     print(f'fj: {self.ac=}')
        #     self.offsety=15
        #     self.offsetx=15
        # if isinstance(self.ac, Teleport):
        #     print(f'tp: {type(self.ac)=}')

    async def perform_next_attack(self,x,y):
        if y > self.top and (y > self.btm-self.offsety and y <= self.btm+self.offsety):
            if x > self.left+self.offsetx:
                if x < self.left+self.offsetx+5:
                    await random.choice([self.ac.leftwalk])()
                else:
                    await random.choice([self.ac.goleftattack, self.ac.goleftattackk])()
            elif x < self.left-self.offsetx:
                if x > self.left-self.offsetx-5:
                    await random.choice([self.ac.rightwalk])()
                else:
                    await random.choice([self.ac.gorightattack, self.ac.gorightattackk])()
            elif x >= self.left-self.offsetx and x <= self.left+self.offsetx:
                if self.replaceropeconnect:
                    await random.choice([self.ac.goupattack_v3])()
                else:
                    await random.choice([self.ac.goupattack])()
        elif y <= self.top+self.offsety and y > self.top-self.offsety:
            if x < self.right-self.offsetx:
                await random.choice([self.ac.gorightattack, self.ac.gorightattackk])()
            elif x > self.right+self.offsetx:
                await random.choice([self.ac.goleftattack, self.ac.goleftattackk])()
            elif x >= self.right-self.offsetx and x <= self.right+self.offsetx:
                await random.choice([self.ac.godownattack])()
        elif y > self.top and not (y > self.btm-self.offsety and y <= self.btm+self.offsety):
            if x >= self.left-self.offsetx and x <= self.left+self.offsetx:
                if self.replaceropeconnect:
                    await random.choice([self.ac.goupattack_v3])()
                else:
                    await random.choice([self.ac.goupattack])()
            elif x >= self.right-self.offsetx and x <= self.right+self.offsetx:
                await random.choice([self.ac.godownattack])()
            else:
                if x < ((self.right-self.left)/2):
                    if self.replaceropeconnect:
                        await random.choice([self.ac.goupattack_v3])()
                    else:
                        await random.choice([self.ac.goupattack])()
                elif x >= ((self.right-self.left)/2):
                    await random.choice([self.ac.godownattack])()
        else:
            await random.choice([self.ac.godownattack])()


    async def stormwing(self,x,y,goleft,goright):
        return self.ac.stormwing(x,y,goleft,goright)
    
    async def bountyhuntrotation(self):
        await self.ac.bountyhuntrotation()
    
    async def castlewallrotation(self):
        await self.ac.castlewallrotation()