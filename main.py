import board
import neopixel
import time
from digitalio import DigitalInOut, Direction, Pull

try:
    import urandom as random  # for v1.0 API support
except ImportError:
    import random

# SWITCH INPUT
switch = DigitalInOut(board.D2)
switch.direction = Direction.INPUT
switch.pull = Pull.UP

# NEOPIXEL EYES
numpix = 14  # Number of NeoPixels
pixpin = board.D1  # Pin where NeoPixels are connected
strip = neopixel.NeoPixel(pixpin, numpix)

alpha = 0.2
alphaUp = True
eyes = "red"

def fadeToBlue():

    r = 251
    b = 0
    i=0
    while i < 25:
        r -= 10
        b += 10

        strip.fill([r, 0, b])
        strip.brightness = 0.1
        time.sleep(120 / 1000.0)
        i+=1
        strip.write()

def fadeToRed():

    r = 0
    b = 251
    i=0
    while i < 25:
        r += 10
        b -= 10

        strip.fill([r, 0, b])
        strip.brightness = 0.1             
        strip.write()
        i+=1
        time.sleep(120 / 1000.0)  


def getAlpha(minAlpha, maxAlpha, alphaDelta, alpha, alphaUp):

    if random.randint(1, 5) == 5:  # 1-in-5 random chance
        alphaUp = not alphaUp  # of reversing direction
    if alphaUp:  # Increasing brightness?
        alpha += alphaDelta  # Add some amount
        if alpha >= maxAlpha:  # At or above max?
            alpha = maxAlpha  # Limit to max
            alphaUp = False  # and switch direction
    else:  # Else decreasing brightness
        alpha -= alphaDelta  # Subtract some amount
        if alpha <= minAlpha:  # At or below min?
            alpha = minAlpha  # Limit to min
            alphaUp = True  # and switch direction

    strip.brightness = alpha  # Set brightness to 0.0 to 1.0
    return alpha, alphaUp
   
def redState(alpha, alphaUp):

    minAlpha = 0.1  # Minimum brightness
    maxAlpha = 0.4  # Maximum brightness
    alphaDelta = 0.008  # Amount to change brightness each time through loop
    
    alpha, alphaUp = getAlpha(minAlpha, maxAlpha, alphaDelta, alpha, alphaUp)
    
    strip.fill([250, 0, 0])    
    strip.write()

    return alpha, alphaUp

def blueState(alpha, alphaUp):

    minAlpha = 0.03  # Minimum brightness
    maxAlpha = 0.25  # Maximum brightness
    alphaDelta = 0.01  # Amount to change brightness each time through loop
    
    alpha, alphaUp = getAlpha(minAlpha, maxAlpha, alphaDelta, alpha, alphaUp)    

    strip.fill([0, 0, 250])    
    strip.write()

    return alpha, alphaUp

while True:  # Loop forever...

    if eyes == "red":
        alpha, alphaUp = redState(alpha, alphaUp)
    else:
        alpha, alphaUp = blueState(alpha, alphaUp)

    if not switch.value:
        if eyes == "red":
            eyes = "blue"
            fadeToBlue()
        else:
            eyes = "red"
            fadeToRed()
        alpha = 0.1

    time.sleep(0.001)  # debounce delay