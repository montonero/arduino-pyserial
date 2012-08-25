import pygame, sys, os
import serial

from pygame.locals import *

pygame.init
window = pygame.display.set_mode( (696,396) )
screen = pygame.display.get_surface()
buttonrect = pygame.Rect( 298, 148, 100, 100 )
ser = serial.Serial( '/dev/ttyUSB0', 9600 )

def setLED(state):
	if state == 'L':
		print 'Setting L'
		setLED.currentState = 'L'
		pygame.draw.rect( screen, (64,64,64), buttonrect )
		ser.write('L')
	if state == 'H':
		print 'Setting L'
		setLED.currentState = 'H'
		pygame.draw.rect( screen, (255,255,255), buttonrect )
		ser.write('H')
	if state == 'C':
		print 'Toggle!'
		if setLED.currentState == 'L':
			setLED('H')
		else:
			setLED('L')
	pygame.display.flip()

def input(events):
	for event in events:
		print event
		if event.type == QUIT:
			sys.exit(0)
		if event.type == MOUSEBUTTONDOWN:
			if buttonrect.collidepoint(event.pos):
				print 'Click'
				setLED('C')

setLED('L')

while True:
	input( pygame.event.get() )

