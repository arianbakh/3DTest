#version 130

uniform sampler2D p3d_Texture0;

in vec2 texcoord;

void main() {
  vec4 color = texture(p3d_Texture0, texcoord);
  gl_FragColor = color.bgra;
}
