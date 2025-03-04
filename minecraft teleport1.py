# Import the api
from mcpi_addons.minecraft import Minecraft
# Initialize the api
mc = Minecraft.create()

x=input ("X Coordinate: ")
y=input ("Y Coordinate: ")
z=input ("Z Coordinate: ")

x = int(x)
y = int(y)
z = int(z)

mc.player.setTilePos(x,y,z)