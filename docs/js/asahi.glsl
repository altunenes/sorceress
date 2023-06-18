const float PI = 3.14159265;
mat2 rotate2D(float r) {
    return mat2(cos(r), -sin(r), sin(r), cos(r));
}
void mainImage( out vec4 fragColor, in vec2 fragCoord ) {
    vec2 uv = ((fragCoord - 0.5 * iResolution.xy) / min(iResolution.y, iResolution.x)*2.5) * 0.5;
    vec2 c = vec2(3.8 * atan(iTime), 3.5 * atan(iTime)); 
    vec2 z = uv;
    int iterations = 1;
    int maxIterations = 100;
    vec2 n = vec2(0);
    vec2 N = vec2(0);
    float S = 15.0;
    mat2 m = rotate2D(sin(iTime)*PI);
    for (int i = 0; i < maxIterations; ++i) {
        vec2 zSquared = vec2(z.x*z.x - z.y*z.y, 2.0*z.x*z.y);
        vec2 zCubed = vec2(zSquared.x*z.x - zSquared.y*z.y, zSquared.x*z.y + zSquared.y*z.x);
        vec2 denominator =(zCubed + c);
        if (length(denominator) != 0.0) {
            z = zSquared / denominator;
        } else {
            z = zSquared;
        }
        for (int j = 0; j < 5; ++j) {
            float zr = log(abs(z.y));
            float zi = log(abs(z.x));
            z = vec2(zr, zi);
        }
        if (length(z) > 1.0) break;
        iterations++;
        z *= m;
        n *= m;
        N += z/S;
        S *= 60.3; 
    }
    float fractal = float(iterations) / float(maxIterations);
    float pulse =  sin(1.5 * PI * iTime) + 2.5; // a pulse
    vec3 colorOffset = vec3(0.5 * sin(n.x), 0.5 * sin(n.y), 2.1 * cos(n.x)); 
    vec3 flowColorChange = vec3(1.5 * cos(3.0*iTime + N.x), 0.5 * sin(3.0*iTime + N.y), 1.5 * cos(3.0*iTime + N.y));
    vec3 flowIntensity = vec3(0.003/length(0.04*N), 1, 1);
    vec3 color = (vec3(1.5 * pulse, 1.0 * pulse, 0.1 * pulse) + colorOffset + flowColorChange + flowIntensity) * ((1.0*N.x +1.0*N.y + 0.01)+.001/length(1.0*N));
    if (iterations == maxIterations) {
        color = vec3(1.0, 1.0, 1.0);
    }

    fragColor = vec4(color, 1.0);
}