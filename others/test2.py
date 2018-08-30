class c_color(object):
	def __init__(self, p_r = 0, p_g = 0, p_b = 0):
		self.put(p_r, p_g, p_b)
 
	def clone(self):
		return c_color(self.r, self.g, self.b)
 
	def put(self, p_r, p_g, p_b):
		self.r = p_r
		self.g = p_g
		self.b = p_b
 
	def get_r(self):
		return self.r
 
	def get_g(self):
		return self.g
 
	def get_b(self):
		return self.b
 
	def __eq__(self, other):
		return self.r == other.r and self.g == other.g and self.b == other.b
 
	def __ne__(self, other):
		return not (self == other)
 
white = c_color(255,255,255)
def circle(self, x0, y0, radius, colour=white):
    f = 1 - radius
    ddf_x = 1
    ddf_y = -2 * radius
    x = 0
    y = radius
    self.set(x0, y0 + radius, colour)
    self.set(x0, y0 - radius, colour)
    self.set(x0 + radius, y0, colour)
    self.set(x0 - radius, y0, colour)
 
    while x < y:
        if f >= 0: 
            y -= 1
            ddf_y += 2
            f += ddf_y
        x += 1
        ddf_x += 2
        f += ddf_x    
        self.set(x0 + x, y0 + y, colour)
        self.set(x0 - x, y0 + y, colour)
        self.set(x0 + x, y0 - y, colour)
        self.set(x0 - x, y0 - y, colour)
        self.set(x0 + y, y0 + x, colour)
        self.set(x0 - y, y0 + x, colour)
        self.set(x0 + y, y0 - x, colour)
        self.set(x0 - y, y0 - x, colour)
Bitmap.circle = circle
 
bitmap = Bitmap(25,25)
bitmap.circle(x0=12, y0=12, radius=12)
bitmap.chardisplay()