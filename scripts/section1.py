#!/usr/bin/env python3
import numpy as np

# add import and helper functions here

if __name__ == "__main__":
    # code goes here
    print("hello world")
    np.random.seed(42)
    A = np.random.normal(size=(4, 4))
    B = np.random.normal(size=(4, 2))
    print(A@B)