#ifdef GL_ES
precision mediump float;
#endif

uniform vec2 u_resolution;
uniform float u_time;
uniform vec2 u_mouse;

void main() {
	vec2 normFragCoord = gl_FragCoord.xy / u_resolution;
	vec2 normMouseCoord = u_mouse / u_resolution;
	gl_FragColor = vec4(
		abs(normFragCoord.x - normMouseCoord.x),
		abs(normFragCoord.y - normMouseCoord.y),
		abs(0.5 * sin(u_time)),
		1.0
	);
}
