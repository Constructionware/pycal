# pycal/calculator.py
#from pprint import pprint
#import math
from pycal.pycal.construction import Wall, Roof
from pycal.pycal.materials import Water

class Calculator(
    # Plugins
    Roof,
    Wall,
    Water,
    ):
    _name = 'CentryPlan Building Calculator'

    def __init__(self, name:str=None, *args, **kwargs):
        if name:
            self._name = name

    # Calculator Functions Here

    def __repr__(self):
        return f" Calculator => {self._name}"

cal = Calculator()

