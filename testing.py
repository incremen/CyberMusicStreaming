import logging
from PyQt5.QtWidgets import QApplication
from ui.playlist_page.playlist_window import PlaylistWindow
import sys
from scipy.special import factorial


import math

millnames = ['',' Thousand',' Million',' Billion',' Trillion']

def millify(n):
    n = float(n)
    millidx = max(0,min(len(millnames)-1,
                        int(math.floor(0 if n == 0 else math.log10(abs(n))/3))))

    return '{:.0f}{}'.format(n / 10**(3 * millidx), millnames[millidx])


def main():

    k = 6
    n = 16

    n_fact = factorial(n)
    kn_fact = factorial(k*n)

    result = kn_fact / (n_fact**2)
    print(millify(result))
    
if __name__ == "__main__":
    main()