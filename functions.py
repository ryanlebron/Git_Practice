# Here are some functions that you can fill in to make them work.
# Replace the "raise NotImplementedError" line with the correct code!

from astropy.time import Time
import numpy as np

def hello_world():
	return "Hello World!"

def print_the_instructors_name():
	return "Dax Felix"

def print_the_number_of_this_room():
	return 8202

def split_this_string_at_each_space(input_string):
	split_string = input_string.split()
	return split_string

def take_the_average_of_these_numbers(a, b):
    	average = (a+b)/2
	return average
	
def print_the_time_now_using_astropy():
	return Time.now()

def return_the_minimum_of_two_numbers(a, b):
	return (np.min((a,b))

def return_the_std_of_two_numbers(a, b):
	return np.std((a,b))
