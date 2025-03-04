#import the API
from mcpi_addons.minecraft import Minecraft
#Initialize the API (MCPI must be open and in a world atthis time)
mc = Minecraft.create()
import time

count = 0
while count < 30:
    pos = mc.player.getPos()
    mc.setBlock(pos.x, pos.y, pos.z, 12)
    count += 1
    time.sleep(1)