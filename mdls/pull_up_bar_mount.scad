
// TODO: add offsets
width = 50.5;
length = 110.5;

// TODO: measure needed spacing
height = 4.5;

holeSpacing = 70;
holeDiameter = 17;

chamferRadius = height+1;
cutoutRadius = 9;

$fn=64;

module quart() {
    ss = width/2+chamferRadius;
    ls = length/2+chamferRadius;
    cr = cutoutRadius+chamferRadius;

    difference(){
        //cube([ss, ls, chamferRadius]);
        difference() {
            
            cube([ss, ls, chamferRadius]);
            difference() {
                translate([ss-cr,ls-cr,-1]) cube([cr+1,cr+1,chamferRadius+2]);
                translate([ss-cr,ls-cr,-2]) cylinder(r=cr, h=chamferRadius+4);
            }
        }

        // sides chamfers
        translate([ss,-1,chamferRadius]) rotate([-90, 0, 0]) cylinder(r=chamferRadius-0.5, h=ls+2);
        translate([-1,ls,chamferRadius])  rotate([0, 90, 0]) cylinder(r=chamferRadius-0.5, h=ss+2);
        translate([0,holeSpacing/2,-1]) cylinder(d=holeDiameter, h=height+2);

        // cutout chamfer
        translate([ss-cr, ls-cr, chamferRadius]) rotate_extrude(angle=90) translate([cr,0,0]) circle(r=chamferRadius-0.5);

        // negative space for bracket
        difference() {
            translate([-1,-1,height]) cube([1+width/2, 1+length/2, chamferRadius+1]);
            difference() {
                translate([width/2-cutoutRadius,length/2-cutoutRadius,0]) cube([cutoutRadius,cutoutRadius,chamferRadius]);
                translate([width/2-cutoutRadius,length/2-cutoutRadius,0]) cylinder(r=cutoutRadius, h=chamferRadius+1);
            }
        }
    }
}

quart();