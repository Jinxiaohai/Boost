#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

"""
author : xiaohai
email : xiaohaijin@outlook.com
"""


import subprocess


def main():
    subprocess.call(('make', 'clean'))
    subprocess.call(('xelatex', 'learnBoost.tex'))
    subprocess.call(('bibtex',  'learnBoost.aux'))
    subprocess.call(('xelatex', 'learnBoost.tex'))
    subprocess.call(('xelatex', 'learnBoost.tex'))
    subprocess.call(('evince',  'learnBoost.pdf'))

if __name__ == '__main__':
    main()
