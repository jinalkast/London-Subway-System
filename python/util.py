from python.existingStationNames import first_part, second_part
from random import choice


class Util():
    def nameGenerator():
        return choice(first_part) + " " + choice(second_part)
