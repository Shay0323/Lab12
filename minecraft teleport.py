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

width=10
height=20
length=20

mc.setBlocks(x, y, z, x + width, y + height, z +
length, 7)
mc.setBlocks(x - 1, y - 1, z - 1, x + width - 1, y + height - 1, z +
length - 1, 0)