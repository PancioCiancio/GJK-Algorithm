import moderngl

class Batch:
    def __init__(self, ctx: moderngl.Context):
        self.ctx = ctx
        self.vbo = None
        self.ibo = None
        self.vao = None
        self.program = None

    def commit_batch(self, vertices_data_array, indices_array):
        """ Takes multiple geometries and uploads them to GPU """
        all_vertices = []
        all_indices = []
        index_offset = 0

        for vertices_data, indices_data in vertices_data_array and indices_array:
            all_vertices.append(geo.vertices)
            all_indices.append(geo.indices + index_offset)
            index_offset += geo.vertex_count

        # Flatten arrays
        vertex_data = np.concatenate(all_vertices, axis=0)
        index_data = np.concatenate(all_indices, axis=0)

        # Upload to GPU
        self.vbo = self.ctx.buffer(vertex.data)
        self.ibo = self.ctx.buffer(index_data)

        # Create VAO
        self.vao = self.ctx.vertex_array(
            
        )
