#version 150

#ifdef GL_ES
precision mediump float;
#endif

uniform vec2 u_resolution;
uniform float u_time;
uniform vec2 u_mouse;
uniform sampler2D p3d_Texture0;

in vec2 texCoord;

out vec4 fragColor;

void main() {
	vec2 normFragCoord = gl_FragCoord.xy / u_resolution;
	vec2 normMouseCoord = u_mouse / u_resolution;
	vec4 texColor = texture(p3d_Texture0, texCoord);
	fragColor = texColor;
}
