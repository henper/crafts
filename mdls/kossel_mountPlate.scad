kossel_mountPlate();

use <openBeamClip.scad>

module kossel_mountPlate() {
    height = 58;

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

    // dc jack and push button
    /*button = 7;
    jack = 8;
    spacing = (button+jack)/2+4;*/

    // euro socket
    /*diameter = 12;
    spacing = 21 - diameter;
    hole_spacing = 28;
    hole_diameter = 3.5;*/

    // solid state relay
    hole_spacing = 48;
    hole_diameter = 4.5;

    difference() {
        translate([-width/2, -depth, 0]) cube([width, depth, height]);

        // euro socket
        /*hull() {
            translate([0,depth, height/2+spacing/2]) rotate([90,0,0]) cylinder(d=diameter, h=depth*3, $fn=32);
            translate([0,depth, height/2-spacing/2]) rotate([90,0,0]) cylinder(d=diameter, h=depth*3, $fn=32);
        }*/
        // euro socket or ssr
        translate([0,depth, height/2+hole_spacing/2]) rotate([90,0,0]) cylinder(d=hole_diameter, h=depth*3, $fn=32);
        translate([0,depth, height/2-hole_spacing/2]) rotate([90,0,0]) cylinder(d=hole_diameter, h=depth*3, $fn=32);

        /* dc jack + push button
        translate([0,depth, height/2+spacing/2]) rotate([90,0,0]) cylinder(d=button, h=depth*3, $fn=32);
        translate([0,depth, height/2-spacing/2]) rotate([90,0,0]) cylinder(d=jack, h=depth*3, $fn=32); */
    }
}