#!/usr/bin/env python3
"""
Main module for the CI/CD demo application.
"""

from utils import multiply

def main():
    """
    Entry point of the application.
    """
    a = 5
    b = 6
    result = multiply(a, b)
    print(f"The product of {a} and {b} is {result}")

if __name__ == "__main__":
    main()
