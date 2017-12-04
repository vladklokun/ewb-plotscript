import argparse
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import re

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
    
    print(plots)
    return plots

def main(args):
    raw_coordinates = get_raw_coordinates(args.input)
    build_ready_coords = build_coordinates(raw_coordinates)
    
    fig, ax = plt.subplots()
    
    for plot in build_ready_coords:
        plt.plot(plot[0], plot[1])
        
    plt.show()
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    
    # Parse file containing 2 input signals (required)
    parser.add_argument('--input', '-i', required = True)
    
    # Parse file containing 1 input and 1 output signals.
    # Only output signal is to be used.
    # parser.add_argument('--output','-o', required = True)
    
    #Parse time constraints (optional)
    parser.add_argument('--t1', type=float)
    parser.add_argument('--t2', type=float)
    
    args = parser.parse_args()
    
    main(args)