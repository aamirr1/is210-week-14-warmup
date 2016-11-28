#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Week 14 warmup task 1"""

import pet

class Dog(pet.Pet):
    """This is a new class called Dog"""

    def __init__(self, has_shots=False, **kwargs):
        """ This is for Doc class"""
        
        pet.Pet.__init__(self, **kwargs)
        self.has_shots = has_shots
