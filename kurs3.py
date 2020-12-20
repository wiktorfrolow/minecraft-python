from mcpi.minecraft import Minecraft
from random import randint

mc = Minecraft.create()

mc.postToChat('Witaj swiecie minecrafta')

pozycja_gracza = mc.player.getPos()
zmienna_losowa = randint(0,2)


mc.postToChat(zmienna_losowa)