from manimlib.imports import*
import random



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
				self.add_sound("./dart_hit.wav")
				self.add(dot.shift(point).set_color(RED))
				isins += 1

			else:
				self.add_sound("./dart_hit.wav")
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

class pifind_advance(Scene):
	CONFIG = {"include_sound" : True}
	def construct(self):

		print("Welcome to the PI finding Algorithm using DARTS ")

		darts_at_a_time = input("Enter the number of darts to hit at a time :")
		iterations      = input("Enter the number of times you want to hit :")

		quartercircle = Sector(outer_radius = 3).set_opacity(0.8).set_color(TEAL_E)
		sq = Square(side_length = 3).shift(1.5*RIGHT + 1.5*UP).set_color(BLUE_A)
		self.add(sq,quartercircle)


		inside =  TextMobject("Darts Inside :").set_color(RED)
		outside = TextMobject("Darts Outside :").set_color(GREEN)
		darts = TextMobject("Total Darts :").set_color(BLUE_A)

		VGroup(darts,inside,outside).arrange(DOWN,aligned_edge = RIGHT,buff = 0.5).shift(3.5*LEFT + 1*UP)

		self.add(inside,outside,darts)

		playground = VGroup(sq,quartercircle)

		isins = 0
		isout = 0

		for i in range(int(iterations)):
			if (i != 0):
				self.remove(pi_value,pi_counter,
							inside_counter,outside_counter,
							dart_counter)

			points = self.get_list_of_random_points(int(darts_at_a_time))

			inside_darts = VGroup()
			outside_darts = VGroup()

			for point in points:
				if (self.magnitude(point) <= 3):
					inside_darts.add(SmallDot().shift(point).set_color(RED))
				else:
					outside_darts.add(SmallDot().shift(point).set_color(GREEN))			
			

			isins += len(inside_darts)
			isout += len(outside_darts)

			pi_counter = TexMobject("\\pi","\\approx","4","\\left({",str(isins),"\\over","{",str(isins)," + ",
				str(isout),"}}\\right)"," = ").shift(2*DOWN + 2*LEFT)
			for i,color in [(0,YELLOW),(4,RED),(7,RED),(9,GREEN),(-1,YELLOW)]:
				pi_counter[i].set_color(color)
			
			pi_value = TexMobject(str(4*isins/(isins + isout))).set_color(YELLOW).next_to(pi_counter,RIGHT,buff = 0.2)

			inside_counter = TexMobject(str(isins))
			outside_counter = TexMobject(str(isout))

			
			dart_counter = TexMobject(str(isins + isout)).next_to(darts,RIGHT,buff = 0.2).set_color(BLUE_A)

			self.add(inside_counter.next_to(inside,RIGHT,buff = 0.2).set_color(RED),
						outside_counter.next_to(outside,RIGHT,buff = 0.2).set_color(GREEN),
						inside_darts,
						outside_darts,
						pi_counter,
						pi_value,
						dart_counter,
						)
			self.add_sound("./dart_hit.wav")			
			


			self.wait(1)

			

	def get_list_of_random_points(self,darts):
		result = []
		for i in range(darts):
			point = self.get_random_point()
			result.append(point)
		return result


	def get_random_point(self,x_min = 0,x_max = 3,y_min = 0,y_max = 3):
		x = random.uniform(x_min,x_max)
		y = random.uniform(y_min,y_max)

		return x*RIGHT + y*UP

	def magnitude(self,point):
		return (point[0]**2 + point[1]**2)**0.5
