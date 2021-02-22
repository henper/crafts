kossel_mountPlate();

use <openBeamClip.scad>

module kossel_mountPlate() {
    height = 25;

    clipSpacing = 15+15;
    clipWidth = height;

    //bottom
    translate([-clipSpacing/2, 0, 0])
    openBeamClip(height=clipWidth);

    translate([clipSpacing/2, 0, 0])
    openBeamClip(height=clipWidth);

    //middle
    /*translate([-clipSpacing/2, 0, (height-clipWidth)/2])
    openBeamClip(height=clipWidth);

    translate([clipSpacing/2, 0, (height-clipWidth)/2])
    openBeamClip(height=clipWidth);

    //top
    translate([-clipSpacing/2, 0, height-clipWidth])
    openBeamClip(height=clipWidth);

    translate([clipSpacing/2, 0, height-clipWidth])
    openBeamClip(height=clipWidth);*/

    width = 40;
    depth = 2;

    button = 7;
    jack = 8;
    spacing = (button+jack)/2+4;

    difference() {
        translate([-width/2, -depth, 0]) cube([width, depth, height]);
        translate([0,depth, height/2+spacing/2]) rotate([90,0,0]) cylinder(d=button, h=depth*3, $fn=32);
        translate([0,depth, height/2-spacing/2]) rotate([90,0,0]) cylinder(d=jack, h=depth*3, $fn=32);
    }
}