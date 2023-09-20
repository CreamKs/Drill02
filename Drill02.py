from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

x = 400
y = 90

i = 180
while(1):
	while(i < 540) :
		clear_canvas_now()
		grass.draw_now(400, 30)
		character.draw_now(400 + 210 * math.sin(math.radians(i)), 300 + 210 * math.cos(math.radians(i)))
		delay(0.01)
		i = i + 1
	while(x < 780):
		clear_canvas_now()
		grass.draw_now(400, 30)
		character.draw_now(x, y)
		x = x + 2
		delay(0.01)
	while(y < 560):
		clear_canvas_now()
		grass.draw_now(400, 30)
		character.draw_now(x, y)
		y = y + 2
		delay(0.01)
	while(x > 20):
		clear_canvas_now()
		grass.draw_now(400, 30)
		character.draw_now(x, y)
		x = x - 2
		delay(0.01)
	while(y > 90):
		clear_canvas_now()
		grass.draw_now(400, 30)
		character.draw_now(x, y)
		y = y - 2
		delay(0.01)
	while(x < 400):
		clear_canvas_now()
		grass.draw_now(400, 30)
		character.draw_now(x, y)
		x = x + 2
		delay(0.01)
	i = 180

close_canvas()