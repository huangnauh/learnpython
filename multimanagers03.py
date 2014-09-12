#!/usr/bin/env python
# coding: utf-8

import time
import multiprocessing

def f(ns):
    ns.x.append(1)
    ns.y.append('a')

if __name__ == "__main__":
    manager = multiprocessing.Manager()
:
