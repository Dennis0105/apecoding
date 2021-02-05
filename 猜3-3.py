#主題:冰船
#樣式1圈
#材料；冰磚，船，壓力版

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import random,time
x,y,z=mc.player.getPos
y=y-1
mc.setBlocks(x,y,z,x+100,y,z+5,174)