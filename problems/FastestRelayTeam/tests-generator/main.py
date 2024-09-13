import random
import sys

def generate_random_integers(num_lines):
    for _ in range(num_lines):
        line = [random.randint(913, 1000) for _ in range(4)]
        print(" ".join(map(str, line)))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py <num_lines>")
        sys.exit(1)
    
    try:
        num_lines = int(sys.argv[1])
    except ValueError:
        print("Error: num_lines must be an integer.")
        sys.exit(1)
    
    generate_random_integers(num_lines)