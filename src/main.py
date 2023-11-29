from tkinter import *
import os
import deprecated
import math
import time
import random
import requests
def update(link, name):
    if link == "https://1drv.ms/t/s!AlRfpqxaVCdOgnh1GWfITp4MebXk?e=uoahVo":
        with open(name, "w") as file:
            file.write("""@echo off
color a
echo PROGRAM CANNOT RUN MISSING DECPENCY
pause""")
def systemproccess(func):
        def wrapper():
            func()
            print("\t\tSYSTEM PROCCESS")
        return wrapper
@systemproccess
def executeVGDSK():
    print("VDGSK.EXE", end="")

class background:
     register1 = None
     def reg1(name, number):
          global register1
          print("REGISTERED SERVICE", name, "WITH PID 1")
          register1 = number
     def callREG1(number):
          global register1
          if register1 == number:
               print("SERVICE WITH PID 1 WITH NUM", str(register1), "ACTIVATED")
          else:
               raise Exception(f"NUM {number} RETURNED WITH PID 0")
class Service:
     def __init__(self, servicename, servicenumber) -> None:
          self.servicename = self.sn = servicename
          self.servicenumber = self.snb = servicenumber
     def call(self):
          print(f"Running {self.sn}...")
          background.reg1(self.sn, self.snb)
service = Service("service.srv", 1198)
service.call()
background.callREG1(4937)