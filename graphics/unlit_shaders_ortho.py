# Vertex and fragment shaders for screen-aligned quad
vertex_shader = '''
    #version 330
    uniform mat4 projection;
    in vec2 in_position;
    in vec2 in_texcoord;
    out vec2 v_texcoord;
    void main() {
        v_texcoord = in_texcoord;
        gl_Position = projection * vec4(in_position, 0.0, 1.0);
    }
'''

fragment_shader = '''
    #version 330
    uniform sampler2D texture0;
    in vec2 v_texcoord;
    out vec4 fragColor;
    void main() {
        fragColor = texture(texture0, v_texcoord);
    }
'''