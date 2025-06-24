"""Simple entry point to run algorithms from the command line."""
import argparse
from algorithms.sorting.bubble_sort import bubble_sort
from algorithms.searching.binary_search import binary_search

AVAILABLE = {
    "bubble_sort": bubble_sort,
    "binary_search": binary_search,
}


def list_algorithms():
    for name in AVAILABLE:
        print(name)


def run_algorithm(name: str):
    algo = AVAILABLE.get(name)
    if not algo:
        print(f"Unknown algorithm: {name}")
        return

    if name == "bubble_sort":
        sample = [5, 1, 4, 2, 8]
        print(f"Running bubble_sort on {sample}: {algo(sample)}")
    elif name == "binary_search":
        sample = [1, 2, 4, 5, 8]
        target = 5
        index = algo(sample, target)
        print(f"binary_search for {target} returned index {index}")


def main():
    parser = argparse.ArgumentParser(description="Run example algorithms")
    parser.add_argument("algorithm", nargs="?", help="name of algorithm to run")
    parser.add_argument("--list", action="store_true", help="list available algorithms")
    args = parser.parse_args()

    if args.list:
        list_algorithms()
    elif args.algorithm:
        run_algorithm(args.algorithm)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
