
id=16;
od=id+2;
$fn=64;

difference() {
    cylinder(d=od, h=1);
    translate([0,0,-1])cylinder(d=id, h=3);
}