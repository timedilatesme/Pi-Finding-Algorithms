from manimlib.imports import*
import random
from playsound import playsound


# DRIVER CODE
# python manim.py fun_projects\findpidarts.py -pl

class pifind(Scene):
	CONFIG = {"include_sound": True}
	def construct(self):
		print("Welcome to the PI finding Algorithm using DARTS !!!")
		iterations = input("Enter the number of times you want to hit :")
		quartercircle = Sector(outer_radius = 3).set_opacity(0.8).set_color(TEAL_E)
		sq = Square(side_length = 3).shift(1.5*RIGHT + 1.5*UP).set_color(BLUE_A)
		self.add(sq,quartercircle)

		inside =  TextMobject("Inside :").set_color(RED)
		outside = TextMobject("Outside :").set_color(GREEN)

		VGroup(inside,outside).arrange(DOWN,aligned_edge = RIGHT,buff = 0.5).shift(3.5*LEFT + 1*UP)

		self.add(inside,outside)

		playground = VGroup(sq,quartercircle)

		isins = 0
		isout = 0

		for i in range(int(iterations)):
			if (i != 0):
				self.remove(counter1)
				self.remove(counter2)
				self.remove(pi_counter)
				self.remove(pi_value)

			dot = SmallDot()
			point = self.get_random_point()

			if (self.magnitude(point) <= 3):
				#playsound('D:/MANIM/manim-master/fun_projects/dart_hit.mp3')
				self.add(dot.shift(point).set_color(RED))
				isins += 1

			else:
				self.add(dot.shift(point).set_color(GREEN))
				isout += 1 

			pi_counter = TexMobject("\\pi","\\approx","4","\\left({",str(isins),"\\over","{",str(isins)," + ",str(isout),"}}\\right)"," = ")
			for i,color in [(0,YELLOW),(4,RED),(7,RED),(9,GREEN)]:
				pi_counter[i].set_color(color)

			pi_value = TexMobject(str(4*isins/(isins + isout))).set_color(YELLOW)

			counter1 = TexMobject(str(isins))
			counter2 = TexMobject(str(isout))

			self.add(counter1.next_to(inside,RIGHT,buff = 0.2).set_color(RED))
			self.add(counter2.next_to(outside,RIGHT,buff = 0.2).set_color(GREEN))

			self.add(pi_counter.shift(2*DOWN + 2*LEFT))
			self.add(pi_value.next_to(pi_counter,RIGHT,buff = 0.2))

			self.wait(0.5)

	def get_random_point(self,x_min = 0,x_max = 3,y_min = 0,y_max = 3):
		x = random.uniform(x_min,x_max)
		y = random.uniform(y_min,y_max)

		return x*RIGHT + y*UP

	def magnitude(self,point):
		return (point[0]**2 + point[1]**2)**0.5

