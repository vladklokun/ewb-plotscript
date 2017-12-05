import argparse
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

DIMENSIONS = 2

def can_be_float(s):
	"""Сheck if an argument can be represented as a valid float.
	If float() returns then the string can be represented as a float,
	so the function returns True. Otherwise, if float() raises ValueError,
	False is returned.
	
	Args:
	str — a string being checked 
	"""
	try:
		float(s)
		return True
	except ValueError:
		return False


def is_valid_coordinates(s):    
	"""This function checks if a given string contains valid coordinates
	
	Args
	s — string to be checked
	"""
	coords = s.split(maxsplit = DIMENSIONS)
	
	# If there are less than 2 coordinates in a list, return False
	# since the plotscript is fit to build two-dimensional plots
	if len(coords) < DIMENSIONS:
		return False
		
	if can_be_float(coords[0]) and can_be_float(coords[1]):
		return True
		
	return False
		
def get_raw_coordinates(f):
	"""This function gets raw coordinates from a file. It does so
	by iterating over each line and checking if it appears valid.
	If the line indeed does appear valid, it is added
	to the list of coordinates AS A STRING.
	
	Args:
	f — input file that supposedly contains coordinates
	"""
	raw_coordinates = []
	with open(f, 'r') as infile:
		tmp = []
		for line in infile:
			# Match only lines that contain numbers
			if is_valid_coordinates(line):
				tmp.append(line.strip())
			# On the first occurrence of an invalid input assume
			# that the data for the current plot ended, end the current
			# list of coordinates and append it to raw_coordinates
			else:
				# If tmp is not an empty list, add it to raw_coordinates
				if tmp:
					raw_coordinates.append(tmp)
				tmp = []
			
		# Ensure that the last non-empty chuck of coordinates gets included.
		if tmp:
			raw_coordinates.append(tmp)

	return raw_coordinates
	
def string_to_coordinates(s):   
	""" Convert coordinates from string representation to a tuple of floats
	"""
	
	x, y = map(float, s.split(maxsplit = 2))
	
	return x, y
	
def build_coordinates(raw_coordinates):
	""" Build coordinates from raw plot data
	
	Args:
	raw_coordinates — a list of list. Each sublist in the list
	is a separate plot, which consists of strings with coordinates
	
	Returns:
	plots — a list of plots. Each plot is a list of x and y coordinates
	"""
	plots = []
	for plot in raw_coordinates:
		coordinates_x = []
		coordinates_y = []
		for coordinate in plot:
			x, y = string_to_coordinates(coordinate)
			coordinates_x.append(x)
			coordinates_y.append(y)
			
		plot = [coordinates_x, coordinates_y]
		plots.append(plot)
	
	return plots

def main(args):
	raw_coordinates = get_raw_coordinates(args.input)
	build_ready_coords = build_coordinates(raw_coordinates)
	
	fig, ax = plt.subplots()
	
	for plot in build_ready_coords:
		ax.plot(plot[0], plot[1])
		
		
	# Begin layout customization section
	
	## If xmin is passed, set it as a minimal constraint for axis OX
	if args.xmin is not None:
		ax.set_xlim(xmin = args.xmin)
	
	## If xmax is passed, set it as a maximum constraint for axis OY
	if args.xmax is not None:
		ax.set_xlim(xmax = args.xmax)
		
	## If ymin is passed, set it as a minimal constraint for axis OX
	if args.ymin is not None:
		ax.set_ylim(ymin = args.ymin)
	
	## If ymax is passed, set it as a maximum constraint for axis OY
	if args.ymax is not None:
		ax.set_ylim(ymax = args.ymax)
		
	## If xlabel is passed, set it
	if args.xlabel is not None:
		ax.set_xlabel(args.xlabel)
		
	## If ylabel is passed, set it
	if args.ylabel is not None:
		ax.set_ylabel(args.ylabel)
		
	## If xtickvalue is passed, adjust it
	if args.xtickvalue is not None:
		start, end = ax.get_xlim()
		plt.xticks(np.arange(start, end, args.xtickvalue))
		
	## If ytickvalue is passed, adjust it
	if args.ytickvalue is not None:
		start, end = ax.get_ylim()
		plt.yticks(np.arange(start, end, args.ytickvalue))
		
	# End layout customization section
	plt.show()
	
if __name__ == '__main__':
	parser = argparse.ArgumentParser(description = 'Build a plot of input data.')
	
	# Parse file containing 2 input signals (required, positional)
	parser.add_argument('input', help = 'Path to input file')
	
	# Parse file containing 1 input and 1 output signals.
	# Only output signal is to be used.
	# parser.add_argument('--output','-o', required = True)
	
	# Parse OX axis constraints (optional)
	parser.add_argument('--xmin', type = float,
	                    help = 'Min value to be displayed on axis OX')
	parser.add_argument('--xmax', type = float,
	                    help = 'Max value to be displayed on axis OX')
	
	# Parse OY axis constraints (optional)
	parser.add_argument('--ymin', type = float,
	                    help = 'Min value to be displayed on axis OY')
	parser.add_argument('--ymax', type = float,
	                    help = 'Max value to be displayed on axis OY')
	
	# Parse plot metadata
	parser.add_argument('--xlabel', help = 'Label of OX axis')
	parser.add_argument('--ylabel', help = 'Label of OY axis')
	
	# Parse tick size
	parser.add_argument('--xtickvalue', type = float,
	                    help = 'Tick value on axis OX (step size)')
	parser.add_argument('--ytickvalue', type = float,
	                    help = 'Tick value on axis OY (step size)')
	
	args = parser.parse_args()
	
	main(args)