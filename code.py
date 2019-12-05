"""Bluefruit Playground app animation test"""

import board
import time
import neopixel

# Works on Circuit Playground Express and Bluefruit.
# For other boards, change board.NEOPIXEL to match the pin to which the NeoPixels are attached.
pixel_pin = board.NEOPIXEL
# Change to match the number of pixels you have attached to your board.
num_pixels = 10

pixels = neopixel.NeoPixel(pixel_pin, num_pixels)
pixels.brightness = 0.25

comet_colors = (0x6666ff, 0x1b1bff, 0x000ff, 0x00010, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000)

#fireball_colors = ((255,100,0), (255, 40, 0), (127,8,0), (80, 0, 0), (16, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0))
fireball_colors = (0xff6400, 0xff2800, 0x7f0800, 0x500000, 0x100000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000)

#fire_colors = ((255,100,0), (255,100,0), (255, 40, 0), (255, 40, 0), (127,32,0), (127,8,0), (80, 0, 0), (64, 0, 0), (16, 0, 0), (8, 0, 0))
fire_colors = (0xff6400, 0xff6400, 0xff2800, 0xff2800, 0x7f2000, 0x7f0800, 0x500000, 0x400000, 0x100000, 0x080000)

#sea_colors = ((0, 255, 0), (0,200,16), (0,180,32), (0,150,127), (0,64,127), (0,32,127), (0, 0, 80), (0, 0, 64), (0, 0, 16), (0, 0, 8))
sea_colors = (0x00ff00, 0x00c810, 0x00b420, 0x00967f, 0x00407f, 0x00207f, 0x000050, 0x000040, 0x000010, 0x000008)

#vaporwave_colors = ((255,0,200), (200,0,127), (32,0,127), (16,0,64), (8,0,32), (0, 0, 16), (0, 0, 16), (0, 0, 4), (0, 0, 0), (0, 0, 0))
vaporwave_colors = (0xff00c8, 0xc8007f, 0x20007f, 0x100040, 0x080020, 0x000010, 0x000010, 0x000008, 0x000000, 0x000000)

frame = 0
reverse = False

def rotate(pixels, colors, frame, wait):

    for i in range(num_pixels):
        color_index = frame + i
        if color_index >= num_pixels:
            color_index -= num_pixels
        pixels[i] = colors[color_index]

    pixels.show()

    time.sleep(wait)


def sweep(pixels, colors, frame, wait):

    for i in range(0,5):
        color_index = frame + i
        if color_index >= num_pixels:
            color_index -= num_pixels
        # set left side
        pixels[i] = colors[color_index]
        # set right side
        pixels[9-i] = colors[color_index]

    pixels.show()

    time.sleep(wait)


def pulse(pixels, colors, frame, reverse, wait):

    idx = frame

    #invert frame index if we're animating in reverse
    if reverse == True:
        #print("reverse is true")
        idx = (num_pixels - 1) - frame

    for i in range(num_pixels):
        pixels[i] = colors[idx]

    pixels.show()

    #toggle reverse at limit
    if frame == (num_pixels-1):
        reverse = not reverse

    time.sleep(wait)

    return reverse


def sizzle(pixels, colors, frame, reverse, wait):

    #invert odd led frame index if we're animating in reverse
    if reverse == True:
        #print("reverse is true")
        even_index = frame
        odd_index = (num_pixels - 1) - frame

    #invert even led frame index if we're animating forward
    else:
        even_index = (num_pixels - 1) - frame
        odd_index = frame

    for i in range(num_pixels):
        if i % 2 == 0:
            pixels[i] = colors[even_index]
        else:
            pixels[i] = colors[odd_index]

    if frame == (num_pixels-1):
        #print("reverse")
        reverse = not reverse

    pixels.show()

    time.sleep(wait)

    return reverse


def print_hex(colors):

    print("(", end = "")
    for c in colors:
        print('0x%02x%02x%02x' % c, end = ", ")
    print(")")


while True:

    # uncomment to test

    # Rotate – seamlessly rotate color array
    rotate(pixels, comet_colors, frame, 0.1)

    # Pulse – color all LEDs and reverse sequence
    #reverse = pulse(pixels, sea_colors, frame, reverse, 0.06)

    # Sizzle – pulse even/odd LEDs and reverse
    #reverse = sizzle(pixels, fire_colors, frame, reverse, 0.1)

    # Sweep – same as rotate, but each side animated alone
    #sweep(pixels, vaporwave_colors, frame, 0.1)

    frame += 1
    if frame >= num_pixels:
        frame = 0