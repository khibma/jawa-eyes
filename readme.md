### Jawa Eyes

Inspire by Adafruit [Mystical Hood](https://learn.adafruit.com/mystical-led-halloween-hood/overview "Mystical Hood") tutorial,  an Adafruit [Gemma M0](https://www.adafruit.com/product/3501), [NeoPixels](https://www.adafruit.com/product/2226), a big hand button and some [Circuit Python](https://learn.adafruit.com/mystical-led-halloween-hood/circuitpython-code).

### Setup

Update the Bootloader and then Circuit Python from: https://circuitpython.org/board/gemma_m0/
(Double click to enter into bootloader)

Get the required libraries (neopixel) from the master circuit python library (copy out of the /lib folder): https://circuitpython.org/libraries
(reference: https://circuitpython.readthedocs.io/en/latest/docs/troubleshooting.html#valueerror-incompatible-mpy-file)

Serial Console connection refernce: https://learn.adafruit.com/welcome-to-circuitpython/advanced-serial-console-on-windows

Onboard LED reference: https://learn.adafruit.com/adafruit-gemma-m0/troubleshooting


[Circuit Python reference](https://learn.adafruit.com/adafruit-gemma-m0/circuitpython-digital-in-out-2)

The button allows me to fade from red to blue and back again. The code isn't terribly efficient, but it serves.

![eyes](https://user-images.githubusercontent.com/2514926/67996178-9f1cd580-fc24-11e9-9ef2-864181162ffe.gif)
![image](https://user-images.githubusercontent.com/2514926/67996168-94fad700-fc24-11e9-9816-bf6523f56383.png)

Wiring reference:

11 = Vout (brown to glasses)

9 = D1 (purple to glasses)

7/6 = Ground (grey to glasses, black to switch)

1 = D2 (white to switch)

![IMG_0542](https://user-images.githubusercontent.com/2514926/138577077-6009d2ac-45ab-41d2-a436-2c3347769d2a.jpg)


