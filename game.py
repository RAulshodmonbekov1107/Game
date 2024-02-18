import random
import arcade
SCREEN_WIDTH = 960
SCREEN_HEIGHT = 720
SCREEN_TITLE = "Гонки"

CAR_ANGLE = 20
CAR_SPEED = 5
WALL_SPEED = 5

class Car(arcade.Sprite):
	def update(self):
		self.center_x+=self.change_x
		if self.left < 56:
			self.left = 56
		if self.right > SCREEN_WIDTH - 56:
			self.right = SCREEN_WIDTH - 56


class Wall (arcade.Sprite):
	def update(self):
		self.center_y -= self.change_y
		if self.top < 0:
			self.bottom = SCREEN_HEIGHT+ random.randint(0, SCREEN_HEIGHT)
			self.center_x = random.randint(168, SCREEN_WIDTH-168)
			window.score += 1 

class MyGame(arcade.Window):
	def __init__ (self, width, height,title):
		super().__init__(width, height, title)
		self.bg = arcade.load_texture('bg.png')
		self.car = Car("yellow_car.png", 0.8)
		self.wall = Wall('wall.png', 0.8)
		self.game = True
		self.score = 0
		self.win = False

	def on_key_release (self, key, modifiers):
		if key == arcade.key.LEFT or key == arcade.key.RIGHT:
			self.car.change_x = 0
			self.car.angle = 0

	def on_key_press (self, key, modifiers):
		if self.game and not self.win:
			if key == arcade.key.LEFT:
				self.car.change_x = -CAR_SPEED
				self.car.angle = CAR_ANGLE

			if key == arcade.key.RIGHT:
				self.car.change_x = CAR_SPEED
				self.car.angle = -CAR_ANGLE

	def setup(self):
		self.car.center_x = SCREEN_WIDTH/2
		self.car.center_y = 100
		self.wall.center_y = SCREEN_HEIGHT
		self.wall.center_x = random.randint(168, SCREEN_WIDTH-168)
		self.wall.change_y = WALL_SPEED

	def on_draw(self):
		arcade.start_render()
		arcade.draw_texture_rectangle(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, SCREEN_WIDTH, SCREEN_HEIGHT, self.bg)
		self.car.draw()
		self.wall.draw()
		if not self.game:
			arcade.draw_text("Авария!", SCREEN_WIDTH/2 - 150, SCREEN_HEIGHT/2, arcade.color.CYAN, font_size = 60)
		arcade.draw_text(f'Счет:{self.score}', SCREEN_WIDTH - 180, SCREEN_HEIGHT - 40, arcade.color.RED, font_size=33)
		if self.score >= 10:
			arcade.draw_text('Победа!', SCREEN_WIDTH / 2 - 180, SCREEN_HEIGHT / 2, arcade.color.CYAN, font_size=60)
			self.win = True

	def update(self, delta_time):
		if self.game and not self.win:
			self.car.update()
			self.wall.update()
		if arcade.check_for_collision(self.car, self.wall):
			self.game = False

window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
window.setup()
arcade.run()
