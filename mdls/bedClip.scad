
use <../../kossel/frame_top.scad>

m3diam = 3.2;
bedThickness = 5.5;
bedDiameter = 200;

module clip() {
    height = 1.5;
    offset = 10;
    zfight=0.2;

    $fn=32;

    difference()
    {
        union()
        {
            cylinder(d=m3diam*3, h=height*3);
            hull()
            {
                cylinder(d=m3diam*3, h=height*2);
                translate([0,offset,0])cylinder(d=m3diam*2, h=height*2);
            }
        }
        translate([0,0,-zfight])cylinder(d=m3diam, h=3*height+zfight*2);
    }
}

module bed() {
    color("pink") cylinder(d=bedDiameter, h=bedThickness+0.5, $fn=128);
}

module frame() {
    for(alpha = [0:120:240]) {
        rotate([0,0,alpha]) {
            translate([0,-151.5,-15/2]) color("orange") frame_top();
            rotate([0,0,60]) translate([-240/2,-99.5,-15]) color("grey") cube([240,15,15]);
        }
    }
}

module post() {
    hull() {
        translate([0,0,-1]) cylinder(d=m3diam, h=20, $fn=16);
        translate([0,8,-1]) cylinder(d=m3diam, h=20, $fn=16);
    }
}

module bracket() {
    difference() {
        length = 130;
        translate([-length/2,-111,0]) cube([length, 34, bedThickness]);

        postOffsetX = 49;
        postOffsetY = -102;
        translate([ postOffsetX,postOffsetY,0]) post();
        translate([-postOffsetX,postOffsetY,0]) post();

        rotate([0,0,60]) translate([-75,-119,-1]) cube([40, 20, bedThickness+2]);
        rotate([0,0,-60]) translate([-75,-119,-1]) cube([200, 20, bedThickness+2]);

        bed();
    }

    // mouse ears
    rotate([0,0,-50]) translate([100,0,0]) cylinder(d=20, h=0.35);
    rotate([0,0,50]) translate([-100,0,0]) cylinder(d=20, h=0.35);
}

bracket();
//bed();
frame();

//color("grey") clip();

