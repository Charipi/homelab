from rpi_ws281x import PixelStrip, Color
import time
import sys

LED_COUNT = 60
LED_PIN = 18

strip = PixelStrip(LED_COUNT, LED_PIN)
strip.begin()

if __name__ == "__main__":
	r = int(sys.argv[1])
	g = int(sys.argv[2])
	b = int(sys.argv[3])
	r2 = int(sys.argv[4])
	g2 = int(sys.argv[5])
	b2 = int(sys.argv[6])
	length = int(sys.argv[7])
	speed = int(sys.argv[8])
	
	for j in range(LED_COUNT):
		if j < length:
			strip.setPixelColor(j, Color(r, g, b))
		else:
			strip.setPixelColor(j, Color(r2, g2, b2))
		
	i = 0
	while True:
		for j in range(i, i + speed):
			j = j % 60
			strip.setPixelColor(j, Color(r2, g2, b2))
		for j in range(i + length, i + length + speed):
			j = j % 60
			strip.setPixelColor(j, Color(r, g, b))
		i += speed
		i = i % LED_COUNT
		strip.show()
		time.sleep(0.03)
