import unittest

from classGame import Game

class TestGameClass(unittest.TestCase):

	def test_validating_frames_works_correctly_with_all_ten_pins(self):

		exc = None

		try:
			frames = Game([10,10,10,10,10,10,10,10,10,10,10,10,10,10,10])
		except Exception as err:
			exc = err

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc), 'Invalid number of frames')


	def test_validating_frames_function_works_correctly_with_all_pins(self):

		exc = None

		try:
			frames = Game([10,1,2,2,3,3,4,6,4,2,5,6,3,2,5,6,3])
		except Exception as err:
			exc = err

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc), 'Invalid number of frames')


	def test_validating_frames_function_with_value_bigger_than_10(self):


		exc = None

		try:
			frames = Game([10,12,2,3,1,2,2,3,3,4,6,4,2,5,6,3,2,5,6,3])
		except Exception as err:
			exc = err

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc), 'Inavalid frames values')


	def test_if_frame_is_strike(self):
	
		frames = Game([1,2,10,1,5,1,2,5,2,4,3,5,7,4,2,5,2,8,1,2])

		result = frames._is_strike(2)

		self.assertTrue(result,'This frame is not strike')

	
	def test_if_frame_is_not_strike(self):
	
		frames = Game([1,2,10,1,5,1,2,5,2,4,3,5,7,4,5,2,8,1,2,2])

		result = frames._is_strike(12)

		self.assertFalse(result,'This frame is strike')


	def test_if_frames_are_spares(self):

		frames = Game([1,2,10,6,4,1,2,5,2,4,3,5,7,4,2,5,2,8,1,2])

		result = frames._is_spare(3)

		self.assertTrue(result, 'Frames are not spire')	


	def test_if_frames_are_not_spares(self):
		
		frames = Game([1,2,10,6,4,1,2,5,2,4,3,5,7,4,2,5,2,8,1,2])

		result = frames._is_spare(5)

		self.assertFalse(result, 'Frames are spire')


	def test_total_score_function_returns_expected_result_with_all_ten_pins(self):

		frames = Game([10,10,10,10,10,10,10,10,10,10,10,10])

		score = frames.result()

		self.assertEqual(score, 300)


	def test_total_score_function_works_as_expected(self):

		frames = Game([1, 4, 4, 5, 6, 3, 5, 1, 1, 0, 1, 7, 3, 6, 4, 3, 2, 1, 6, 2])

		score = frames.result()

		self.assertEqual(score, 65)
		

	def test_total_score_function_works_as_expected_with_all_zero_pins(self):

		frames = Game([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

		score = frames.result()

		self.assertEqual(score, 0)



if __name__ == '__main__':
	unittest.main()
