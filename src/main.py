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
