class _Button:
    def is_pressed(self):
        pass
    def was_pressed(self):
        pass
    def get_presses(self):
        pass
button_a = _Button('button_a')
button_b = _Button('button_b')

class Image:
	ANGRY, ASLEEP = BUTTERFLY = CHESSBOARD = CONFUSED = COW = DIAMOND = DIAMOND_SMALL = DUCK = FABULOUS = GHOST = GIRAFFE =  \
	HAPPY = HEART = HEART_SMALL = HOUSE = MEH = MUSIC_CROTCHET = MUSIC_QUAVER = MUSIC_QUAVERS = NO = PACMAN = PITCHFORK = \
	RABBIT = ROLLERSKATE = SAD = SILLY = SKULL = SMILE = SNAKE = SQUARE = SQUARE_SMALL = STICKFIGURE = SURPRISED = SWORD = \
	TARGET = TORTOISE = TRIANGLE = TRIANGLE_LEFT = TSHIRT = UMBRELLA = XMAS = YES = ARROW_N = ARROW_NE = ARROW_E = ARROW_SE = \
	ARROW_S = ARROW_SW = ARROW_W = ARROW_NW = CLOCK12 = CLOCK1 = CLOCK2 = CLOCK3 = CLOCK4 = CLOCK5 = CLOCK6 = CLOCK7 = CLOCK8 = \
	CLOCK9 = CLOCK10 = CLOCK11 = ALL_ARROWS = ALL_CLOCKS = Image()
    def width(self):
        pass    
	def height(self):
        pass
    def set_pixel(self):
        pass
    def get_pixel(self):
        pass
    def shift_left(self):
        pass
    def shift_right(self):
		pass
    def shift_up(self):
        pass
    def shift_down(self):
        pass
	def crop(self):
		pass
	def copy(self):
		pass
	def invert(self):
		pass

class _Display:
    def get_pixel(self):
        pass
    def set_pixel(self):
        pass
    def clear(self):
        pass
    def show(self):
        pass
    def scroll(self):
        pass
	def on(self):
		pass
	def off(self):
		pass
	def is_on(self):
		pass
display = _Display()

class _Pin:
    def write_digital(self):
        pass
    def read_digital(self):
        pass
    def write_analog(self):
        pass
    def read_analog(self):
        pass
    def set_analog_period(self):
        pass
    def set_analog_period_microseconds(self):
        pass
    def is_touched(self):
        pass
pin0 = pin1 = pin2 = pin3 = pin4 = pin5 = pin6 = pin7 = pin8 = pin9 = pin10 = pin11 = pin12 = pin13 = pin14 = pin15 = pin16 = pin17 = pin18 = pin19 = pin20 = _Pin()

class _Accelerometer:
    def get_x(self):
        pass
    def get_y(self):
        pass
    def get_z(self):
        pass
    def get_values(self):#
        pass
    def current_gesture(self):#
        pass
    def get_gestures(self):
        pass
    def is_gesture(self):
        pass
    def was_gesture(self):
        pass
accelerometer = _Accelerometer()

class _Compass:
	def get_x(self):
		pass
	def get_y(self):
		pass
	def get_z(self):
		pass
    def calibrate(self):
        pass
    def heading(self):
        pass
    def get_field_strength(self):
        pass
    def is_calibrated(self):
        pass
    def clear_calibration(self):
        pass
compass = _Compass()

class _I2C:
    def read(self):
        pass
    def write(self):
        pass
i2c = _I2C()

class _UART:
    def init(self):
        pass
    def any(self):
        pass
    def read(self):
        pass
    def readall(self):
        pass
    def readline(self):
        pass
    def readinto(self):
        pass
    def write(self):
        pass		
uart = _UART()

class _SPI:
	def init(self):
		pass
	def write(self):
		pass
	def read(self):
		pass
	def write_readinto(self):
		pass
spi = _SPI()

def sleep():
    pass
def running_time():
    return int
def panic():
    pass
def reset():
    pass
def temperature():
	return int