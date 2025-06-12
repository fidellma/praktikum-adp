import time
import os 
import math
from termcolor import cprint

def animasi_bendera(lebar, tinggi):
    for gerak in range(60): 
        os.system("cls") 

        for i in range(tinggi // 2):
            maju_mundur = " " * (5 + int(math.sin((gerak + i) * 0.5) * 3))  
            cprint(maju_mundur + " " * lebar, "white", "on_red")

        for i in range(tinggi // 2):
            maju_mundur = " " * (5 + int(math.sin((gerak + i + 1) * 0.5) * 3))  
            cprint(maju_mundur + " " * lebar, "white", "on_white")

        for i in range(10):
            cprint("||", "grey", "on_blue")

        time.sleep(0.1) 

animasi_bendera(15,6)
