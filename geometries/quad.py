import numpy as np

def create_quad_acw(size):
    """
    Create quad with anti-clockwise vertices
    """
    half_size = size / 2.0

    # Define the vertices in anti-clockwise order
    quad_vertices = np.array([
        [-half_size, -half_size], # Bottom-left
        [ half_size, -half_size], # Bottom-right
        [ half_size,  half_size], # Top-right
        [-half_size,  half_size]  # Top-left
    ], dtype=np.float32)

    return quad_vertices