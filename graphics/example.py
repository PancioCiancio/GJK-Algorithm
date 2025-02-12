import struct
import moderngl

# Standalone = True makes a headless context
# ctx = moderngl.create_context(standlaone=True)

# Create a context with window
ctx = moderngl.create_context(standalone = True)

program = ctx.program(
    vertex_shader="""
    #version 330

    // Output values for the shader. They end up in the buffer.
    out float value;
    out float product;

    void main() {
        // Implicit type conversion from int to float will happen here
        value = gl_VertexID;
        product = gl_VertexID * gl_VertexID;
    }
    """,
    # What out varyings to capture in our buffer!
    varyings=["value", "product"],
)

# We always need a vertex array in order to execure a shader program.
# Our shader doesn't have any buffer inputs, so we give it empry array.
vao = ctx.vertex_array(program, [])

# Create a buffer allocating room for 20 32 bit floats
buffer = ctx.buffer(reserve = 10 * 8)

# Start a transform with buffer as the destination.
# We force the vertex shader to run 10 times
vao.transform(buffer, vertices = 10)

# Unpack the 20 float values from the buffer (copy from graphics memory to system memory).
# Reading from the buffer will cause a sync (the python program stalls until the shader is done)
data = struct.unpack("20f", buffer.read())
for i in range(0, 20, 2):
    print("value = {}, product = {}".format(*data[i:i+2]))

