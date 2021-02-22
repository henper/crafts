
gtape_width = 30;
hook_length = 40;
hook_width = 20;

xscale = gtape_width / hook_width;
yscale = 3;


difference() {
    translate([0, 0, -hook_length/2])
    linear_extrude(height = hook_length, center = true, convexity = 10, scale=[xscale,yscale], $fn=200, twist = 0)
    translate([0, hook_width/xscale, 0])
    circle(d = hook_width);
}
