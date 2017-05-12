#!/usr/bin/env  python3
# author: wugong

import os
import sys
import threading
BASE_DIR= os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from core import  main


if __name__ == '__main__':
    t1 = threading.Thread(target=main.run)
    t1.start()
