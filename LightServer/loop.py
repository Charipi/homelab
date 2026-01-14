from rpi_ws281x import PixelStrip, Color
import time
import sys

LED_COUNT = 60
LED_PIN = 18

strip = PixelStrip(LED_COUNT, LED_PIN)
strip.begin()

def from_h(h):
    h = h % 360
    x = 1 - abs((h / 60) % 2 - 1)
    if 0 <= h < 60:
        r, g, b = 1, x, 0
    elif 60 <= h < 120:
        r, g, b = x, 1, 0
    elif 120 <= h < 180:
        r, g, b = 0, 1, x
    elif 180 <= h < 240:
        r, g, b = 0, x, 1
    elif 240 <= h < 300:
        r, g, b = x, 0, 1
    else:
        r, g, b = 1, 0, x
    return r, g, b

def h(x, t, h1, h2):
	p = x - t
	p = p % LED_COUNT
	if p < LED_COUNT * 0.4:
		return h1
	if p > LED_COUNT * 0.6:
		return h2
	return (p - LED_COUNT * 0.4) / (LED_COUNT * 0.2) * (h2 - h1) + h1 

if __name__ == "__main__":
	h1 = int(sys.argv[1])
	h2 = int(sys.argv[2])
	
	t = 0
	while True:
		for x in range(LED_COUNT):
			hue = h(x, t, h1, h2)
			r, g, b = from_h(hue)
			strip.setPixelColor(x, Color(r * 255, g * 255, b * 255))
		strip.show()
		t += 1
		time.sleep(0.03)
