import numpy

class Geometry:
    def __init__(self, positions, uvs, indices):
        self.positions = positions
        self.uvs = uvs
        self.indices = indices

    def get_vertices_count(self):
        # positions, uvs must have the same len
        return len(self.position)

    def get_vertecies_position(self):
        return self.positions

    def get_vertex_data(self):
        return numpy.concatenate([self.positions, self.uvs], axis=1)

    def get_indeces(self):
        return self.indices

def create_square_geometry(size: float):
    half_size = size / 2.0

    return Geometry(
        positions=numpy.array([
            [-half_size, -half_size], # Bottom-left
            [ half_size, -half_size], # Bottom-right
            [ half_size,  half_size], # Top-right
            [-half_size,  half_size],  # Top-left
        ], dtype='f4'),
        uvs=numpy.array([
            [0.0, 0.0],
            [1.0, 0.0],
            [1.0, 1.0],
            [0.0, 1.0]
        ], dtype='f4'),
        indices=numpy.array([
            0, 1, 2, 2, 3, 0
        ], dtype='i4')
    )

def create_triangle_geometry():
    pass

def create_circle_geometry():
    pass