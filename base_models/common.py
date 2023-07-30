from random import random
from math import floor
from random import shuffle, seed
from faker.providers.person.en import Provider

class RandomizeData():
    """
    Class used to randomize and generate data
    """
    _first_names = []
    _last_names = []
    def __init__(self) -> None:
        """
        constructor to set initial data of the class
        """
        first_names = list(set(Provider.first_names))
        last_names = list(set(Provider.last_names))
        seed(4321)
        shuffle(first_names)
        shuffle(last_names)
        RandomizeData._first_names = first_names[0:1000]
        RandomizeData._last_names = last_names[0:1000]
    
    def generate_index(self, list_data):
        """
        function to return random index depending on list provided
        list_data: data which you intend to get random index
        """
        return randomize(len(list_data))
    
    def generate_name(self):
        """
        function to generate random names of students
        """
        first_names = RandomizeData._first_names
        last_names = RandomizeData._last_names
        first_index = self.generate_index(first_names)
        last_index = self.generate_index(last_names)
        middle_index = self.generate_index(last_names)
        # look for unique middle index so as to get random middle and last names
        while middle_index == last_index:
            middle_index = self.generate_index(last_names)
        return {"first_name": first_names[first_index],
                "middle_name": last_names[middle_index],
                "last_name": last_names[last_index]}
    
def randomize(max):
    """
    return the random value between 0 and max
    max: the maximux value 
    """
    return floor(random() * max)

def random_max_min(min, max):
    """
    return random value between min and max
    min: the minimum value
    max: the maximux value 
    """
    # get random values of difference of max and min cluster of school
    rand_diff_max_min  = randomize(max - min)
    return min + rand_diff_max_min

