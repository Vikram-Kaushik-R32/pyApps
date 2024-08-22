from vpython import sphere, vector, color

# Function to visualize a sphere using vpython
def visualize_sphere(radius):
    # Create a sphere with the given radius
    sphere(radius=radius, pos=vector(0, 0, 0), color=color.blue)

# Example usage
radius = float(input("Enter the radius of the sphere: "))
visualize_sphere(radius)
