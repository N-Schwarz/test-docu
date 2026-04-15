Simple Python Program
=====================
See the second page :doc:`Second page <page2>`
Overview
--------

This is a basic Python program that demonstrates simple console output
and user interaction.

Features
--------

- Prints a greeting message
- Performs a basic calculation
- Accepts user input and responds dynamically

Example Code
------------

.. code-block:: python

    def main():
        print("Hello, world!")
        print("This is a simple Python program.")
        print("2 + 2 =", 2 + 2)

    if __name__ == "__main__":
        main()

    name = input("Enter your name: ")
    print(f"Hello, {name}! Nice to meet you.")

Usage
-----

1. Save the Python script to a file, for example ``example.py``.
2. Run the script using:

   ::

       python example.py

3. Follow the on-screen prompt to enter your name.

Expected Output
---------------

::

    Hello, world!
    This is a simple Python program.
    2 + 2 = 4
    Enter your name: Alice
    Hello, Alice! Nice to meet you.

Notes
-----

- This program is intended for beginners learning Python basics.
- It demonstrates standard input and output operations.
