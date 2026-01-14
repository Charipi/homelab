from rpi_ws281x import PixelStrip, Color
import sys

LED_COUNT = 60
LED_PIN = 18	

if __name__ == "__main__":
	r = int(sys.argv[1])
	g = int(sys.argv[2])
	b = int(sys.argv[3])

	strip = PixelStrip(LED_COUNT, LED_PIN)
	strip.begin()
	for i in range(strip.numPixels()):
		strip.setPixelColor(i, Color(r, g, b))  
	strip.show()
