﻿  <script id="sf" type="x-shader/x-fragment">
precision highp float;
uniform float time;
uniform vec2 mouse;
uniform vec2 resolution;
float ball(vec2 p, float k, float d) {
    vec2 r = vec2(p.x - cos(time * k) * d, p.y + sin(time * k) * d);	
    return smoothstep(0.0, 1.0, 0.03 / length(r));
}
void main(void) {
    vec2 q = gl_FragCoord.xy / resolution.xy;
    vec2 p = -1.0 + 2.0 * q;	
    p.x	*= resolution.x / resolution.y;
    float col = 0.0;
    for (int i = 1; i <= 7; ++i) {
    	col += ball(p, float(i), 0.3);
    }
    for (int i = 1; i <= 5; ++i) {
    	col += ball(p, float(i), 0.1);
    }
    gl_FragColor = vec4(col*0.8, col, col*1.8, 1.0);
}
</script>
<script id="sv" type="x-shader/x-vertex">
  attribute vec4 vPosition;
  void main (void) {
  gl_Position = vPosition;
  }
</script>
<canvas id="cnv"></canvas>