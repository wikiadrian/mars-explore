try:
        import sys
        import random
        import math
        import os
        import getopt
        import pygame
        from pygame.locals import *
        import random


except ImportError, err:
        print "couldn't load module. %s" % (err)
        sys.exit(2)
        print "Import OK"

class Obstaculo:
        def __init__(self, mapaxy):
                self.positionx = (mapaxy%12) *50
                self.positiony = (mapaxy/12) *50
                self.mapaxy = mapaxy
##                self.frame = 10
                self.image = pygame.image.load('Resources/roca.png').convert_alpha()
                self.pos = self.image.get_rect().move(self.positionx, self.positiony)

        def mytype(self):
                return "obstaculo"
