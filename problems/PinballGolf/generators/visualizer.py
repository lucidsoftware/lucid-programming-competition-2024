"""
This file is generated with ChatGPT. it's a visualizer for the Pinball Golf problem, and plots all the flipper locations
as well as all possible locations the flippers can hit the ball to.

"""



import matplotlib.pyplot as plt

n, L = map(int, input().split())

def plot_points():
    # Dictionary to store x, y and distances
    points = []
    
    while True:
        try:
            line = input()
            if ' ' in line:
                x, y, n_distances = map(int, line.split())
                distances = list(map(int, input().split()))
                points.append((x, y, distances))
        except EOFError:
            break
    
    # Plotting
    plt.figure(figsize=(8, 6))
    
    # Generate a color for each set of points
    colors = plt.cm.get_cmap('tab10', len(points))
    
    for i, (x, y, distances) in enumerate(points):
        # Plot the main point
        plt.scatter(x, y, color="black", label=f'Point {i+1}', s=15)
        
        # Plot the points using distances
        for d in distances:
            plt.scatter(x + d, y, color=colors(i), s=3)
    
    # Add labels and titles
    plt.title("Flipper locations + possible displacements")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    
    # Show grid
    plt.grid(False)
    
    # Show the plot
    plt.show()

# Call the function
if __name__ == "__main__":
    plot_points()