"""
Functions used in preparing Guido's gorgeous lasagna.
"""


# constant for the expected baking time.
EXPECTED_BAKE_TIME = 40
LAYER_PREPARATION_TIME = 2

def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.
 
    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time
    # You might also consider using 'PREPARATION_TIME' here, if you have it defined.
def preparation_time_in_minutes(number_of_layers):
    """Calculate the preparation time.
 
    :param number_of_layers.
    :return: number_of_layers * 2 (in minutes) derived from 'number_of_layers'.
    
    Function that takes the number_of_layers and returns how many minutes the 
    lasagna will take to prepare based on 2 mins preparation time per layer.
    """
    return number_of_layers * LAYER_PREPARATION_TIME
def elapsed_time_in_minutes(number_of_layers, time_baked):
    """Calculate the elapsed time for preparation and baking so far.
 
    :param number_of_layers and time_baked.
    :return: preparation_time_in_minutes(number_of_layers) + time_baked .
    
    Function that takes the number_of_layers and time baked so far 
    and returns the elapsed time so far in minutes.
    """
    return preparation_time_in_minutes(number_of_layers) + time_baked


print(bake_time_remaining(20))