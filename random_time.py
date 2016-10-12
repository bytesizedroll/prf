############################################################################
# My attempt at a pseudorandom number generator that uses the microseconds #
# from the current time as the seed. The middle squares method is used to  #
# generate the number from the seed. My seed for this generator will be 6  #
# digits long, meaning the generator can't expand past 1,000,000 numbers   #
# before repeating its cycle.                                              #
# Written By: Damien Hobday                                                #
############################################################################

from datetime import datetime

def set_seed(): #Function to set the seed for the number generator
    return datetime.now().microsecond #Using the microseconds from the current time as the seed

def seed_check(): #Function to check if seed length is 6 if not, generate new seed
    seed = set_seed() #Genate new seed
    while len(str(seed)) != 6: #If seed length is not 6
        seed = set_seed() #Generate new seed
    return seed
