class Game:


	def __init__(self,frames):

		length = len(frames)

		all_ten_pins = all(map(lambda x: x==10, frames))
		all_correct_pins = all(map(lambda x: x <= 10, frames))

		if all_correct_pins ==  False and all_ten_pins == False:
			raise ValueError('Inavalid frames values')


		if all_ten_pins == True and length != 12:
			raise ValueError('Invalid number of frames')


		if all_correct_pins == True and all_ten_pins == False and length != 20:
			raise ValueError('Invalid number of frames')

		self.frames = frames


	def _is_strike(self, index):
		return self.frames[index] == 10


	def _is_spare(self,index):
		return self.frames[index] + self.frames[index+1] == 10


	def result(self):
		score = 0
		index = 0

		for frame in range(10):
			if self._is_strike(index):
				score += 10 + self.frames[index+1] + self.frames[index+2]
				index += 1
			elif self._is_spare(index):
				score += 10 + self.frames[index+2]
				index += 2
			else:
				score += self.frames[index] + self.frames[index+1]
				index += 2

		return score




def main():
	pass

if __name__ == '__main__':
	main()