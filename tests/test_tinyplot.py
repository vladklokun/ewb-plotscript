import unittest
import tinyplot

class TestFloatCorrectness(unittest.TestCase):	
	"""Test checking for float-correctness"""
	
	# Positive test cases
	def test_unsigned_int(self):
		s = '1'
		self.assertTrue(tinyplot.can_be_float(s))
		
	def test_signed_int(self):
		s = '-1'
		self.assertTrue(tinyplot.can_be_float(s))
		
	def test_unsigned_real(self):
		s = '2.25'
		self.assertTrue(tinyplot.can_be_float(s))
		
	def test_signed_real(self):
		s = '-2.232'
		self.assertTrue(tinyplot.can_be_float(s))
		
	def test_exp_notation_positive(self):
		s = '1e17'
		self.assertTrue(tinyplot.can_be_float(s))
		
	def test_exp_notation_negative(self):
		s = '-1e-17'
		self.assertTrue(tinyplot.can_be_float(s))
	
	# Negative test cases
	
	def test_string_word(self):
		s = 'Rag'
		self.assertFalse(tinyplot.can_be_float(s))
		
	def test_string_ascii_sentence(self):
		s = 'The quick brown fox jumps over the lazy dog'
		self.assertFalse(tinyplot.can_be_float(s))
		
	def test_string_unicode_sentence(self):
		s = 'Аэрофотосъёмка ландшафта уже выявила земли богачей и процветающих крестьян'
		self.assertFalse(tinyplot.can_be_float(s))
		
	def test_exp_notation_floating(self):
		s = '1.073e2.25'
		self.assertFalse(tinyplot.can_be_float(s))
		
class TestCoordinateValidation(unittest.TestCase):
	"""Test if valid coordinate strings are recognized correctly"""
	
	# Positive test cases
	def test_unsigned_int_coordinates(self):
		# cs stands for Coordinate String
		cs = '1 2'
		self.assertTrue(tinyplot.is_valid_coordinates(cs))
		
	def test_signed_int_coordinates(self):
		cs = '-3 -4'
		self.assertTrue(tinyplot.is_valid_coordinates(cs))
		
	def test_unsigned_float_coordinates(self):
		cs = '5.678 6.789'
		self.assertTrue(tinyplot.is_valid_coordinates(cs))
		
	def test_signed_float_coordinates(self):
		cs = '-7.890 +8.901'
		self.assertTrue(tinyplot.is_valid_coordinates(cs))
	
	# Negative test cases
	def test_merged_number(self):
		cs = '-1-2'
		self.assertFalse(tinyplot.is_valid_coordinates(cs))
	
class TestStringToCoordinates(unittest.TestCase):	
	"""Test the correctness of coordinate string to coordinates conversion"""
	def test_unsigned_ints(self):
		cs = '1 2'
		self.assertEqual(tinyplot.string_to_coordinates(cs), (1, 2))
		
	def test_signed_ints(self):
		cs = '-1 +2'
		self.assertEqual(tinyplot.string_to_coordinates(cs), (-1, 2))
		
	def test_unsigned_floats(self):
		cs = '2.345 3.456'
		self.assertEqual(tinyplot.string_to_coordinates(cs), (2.345, 3.456))
		
	def test_signed_floats(self):
		cs = '+4.567 -5.678'
		self.assertEqual(tinyplot.string_to_coordinates(cs), (4.567, -5.678))
		
	# Negative test cases
	# None, since string_to_coordinates assumes correct coordinate strings
	# are passed
		
if __name__ == '__main__':
	unittest.main()