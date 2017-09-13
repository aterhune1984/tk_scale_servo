# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 19:41:18 2017

@author: pi
"""

import Adafruit_PCA9685
from Tkinter import *
from functools import partial

def pwm_set(ch,val):
    pwm.set_pwm(ch,0,int(val))


master = Tk()
pwm = Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(60)

s0 = Scale(master,
          from_=0,
          to=4096,
          orient=HORIZONTAL,
          length=500,
          tickinterval=500,
          command=partial(pwm_set,0))
s0.pack()
s1 = Scale(master,
          from_=180,
          to=620,
          orient=HORIZONTAL,
          length=500,
          tickinterval=100,
          command=partial(pwm_set,1))
s1.pack()  
mainloop()
core