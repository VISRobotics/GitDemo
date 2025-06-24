# GitDemo

This repository now contains a small Python project intended for learning
and executing common algorithms.  The code is organised in a simple
package so you can add new algorithms as you learn them.

## Structure

```
algorithms/
    sorting/
        bubble_sort.py
    searching/
        binary_search.py
```

`main.py` demonstrates how to run the available algorithms from the
command line.  Feel free to extend the `algorithms` package with your own
implementations.

## Project Details

This repository is a minimal learning project for experimenting with
simple algorithms.  Each algorithm lives in its own module inside the
`algorithms` package, and the `main.py` script exposes a tiny command-line
interface for executing them.

## Getting Started

1. Clone this repository.
2. Ensure you have Python 3.8 or newer installed.
3. List available algorithms:

   ```bash
   python main.py --list
   ```
4. Run an algorithm by name, for example:

   ```bash
   python main.py bubble_sort
   ```

Use these commands as a starting point and add your own algorithm
implementations as you learn them.
