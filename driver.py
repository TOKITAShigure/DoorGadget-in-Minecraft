import amulet
import os
import shutil
from DoorGad2Mine import DoorGad2Mine

if 'output' in [d for d in os.listdir('./')]:
    shutil.rmtree('./output') #すでに出力フォルダがある場合は削除

world=input("Input the world name in this directory: ")
shutil.copytree("./"+world,"./output")

point=list(map(int,input("Input the location where the gadget generated(x,y,z): ").split()))
level=amulet.load_level("./output")

d2m=DoorGad2Mine(level,point[0],point[1],point[2])
d2m.setGadget()

del d2m