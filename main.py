import geometries.geometry
import physics
from property.entity_registry import EntityRegistry
from property.properties_registry import PropertiesRegistry
import graphics.unlit_shaders
import graphics.unlit_shaders_ortho

import glfw
import moderngl
import numpy as np

# Initialize GLFW to create window
if not glfw.init():
    raise Exception("GLFW can't be initialized")

# Create window
# glfw.window_hint(glfw.VISIBLE, glfw.FALSE)  # Hide window until setup is complete
window = glfw.create_window(800, 600, "FBO with ModernGL", None, None)
if not window:
    glfw.terminate()
    raise Exception("GLFW window can't be created")

glfw.make_context_current(window)
ctx = moderngl.create_context()

# Hide window until FBO is ready
# glfw.show_window(window)

# Create FBO and Texture
fbo_size = glfw.get_window_size(window)
fbo_texture = ctx.texture(fbo_size, 4)
fbo_depth = ctx.depth_renderbuffer(fbo_size)
fbo = ctx.framebuffer(color_attachments=[fbo_texture], depth_attachment=fbo_depth)


fbo_geometries = geometries.geometry.create_square_geometry(2.0)
fbo_vbo = ctx.buffer(fbo_geometries.get_vertex_data().tobytes())
fbo_ibo = ctx.buffer(fbo_geometries.get_indeces().tobytes())
fbo_vao = ctx.vertex_array(
    ctx.program(vertex_shader=graphics.unlit_shaders.vertex_shader, fragment_shader=graphics.unlit_shaders.fragment_shader),
    [
        (fbo_vbo, '2f 2f', 'in_position', 'in_texcoord'),
    ],
    fbo_ibo
)

# Create entity and property registries
entity_reg = EntityRegistry()
property_reg = PropertiesRegistry(entity_reg)

# Create player geometry
player_geometry = geometries.geometry.create_square_geometry(0.1)

# Create player entity
player_entity = property_reg.create_entity()
property_reg.set_property(player_entity, 'geometry', player_geometry)

white_texture = np.array([255, 255, 255], dtype='u1')
player_texture = ctx.texture((1, 1), 3, white_texture.tobytes())
player_vbo = ctx.buffer(player_geometry.get_vertex_data().tobytes())
player_ibo = ctx.buffer(player_geometry.get_indeces().tobytes())
player_vao = ctx.vertex_array(
    ctx.program(vertex_shader=graphics.unlit_shaders_ortho.vertex_shader, fragment_shader=graphics.unlit_shaders_ortho.fragment_shader),
    [
        (player_vbo, '2f 2f', 'in_position', 'in_texcoord'),
    ],
    player_ibo
)

def ortho(left, right, bottom, top, near, far):
    return np.array([
        [2 / (right - left), 0, 0, -(right + left) / (right - left)],
        [0, 2 / (top - bottom), 0, -(top + bottom) / (top - bottom)],
        [0, 0, -2 / (far - near), -(far + near) / (far - near)],
        [0, 0, 0, 1]
    ], dtype='f4')

player_vao.program['projection'].write(ortho(-1, 1, -1/1.3, 1/1.3, -1, 1).tobytes())


if __name__ == "__main__":
    # Main loop
    while not glfw.window_should_close(window):
        # --- 1. Render to FBO ---
        fbo.use()
        ctx.clear(0.1, 0.1, 0.1, 1.0)
        # Here you would normally render your scene
        # Every draw will be written to the current fbo in use.

        player_texture.use(0)
        player_vao.render()

        # --- 2. Display FBO Texture ---
        ctx.screen.use()
        ctx.clear(0.0, 0.0, 0.0, 1.0)
        fbo_texture.use(0)
        fbo_vao.render()

        # Swap buffers and poll events
        glfw.swap_buffers(window)
        glfw.poll_events()

    # Terminate GLFW
    glfw.terminate()