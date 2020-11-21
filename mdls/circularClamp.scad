// parametric params
screw = 2.3;
iradius = 5.3/2;
oradius = iradius+1.5;
zfight = 1;

// derived params
clampWidthOffset = iradius*2*0.3; // 40% of the inner diameter
clampLength = iradius+screw*2;
clampCenter = clampLength-screw;

// resolution
$fa = 3;
$fs = 0.5;

height = screw*2;

difference()
{
    union()
    {
        cylinder(h=height, r=oradius);
        translate([-oradius, 0, 0]) cube([2*oradius, clampLength, height]);
    }
    union()
    {
        // post
        translate([0,0,-zfight]) cylinder(h=height+2*zfight, r=iradius);

        // screw
        translate([-oradius-zfight,clampCenter,height/2]) rotate([0,90,0]) cylinder(h=2*(oradius+zfight), d=screw);

        // cutout
        translate([clampWidthOffset/2-iradius, 0, -zfight]) cube([iradius*2-clampWidthOffset, clampLength+zfight, height+2*zfight]);
    }
}