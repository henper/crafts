
/*
translate([0,1.075,0]) import("NewEffectorCentered.stl");
//#cylinder(r=8, h=80);

for(a = [0:120:240])
    rotate([0,0,a])
            rotate([0,90,0]) {
                translate([-4,-25,-24]) cylinder(r=2.6, h=4, $fn=32);
                translate([-4,-25,20]) cylinder(r=2.6, h=4, $fn=32);

                #translate([-4,-25,-30]) cylinder(r=1.5, h=60, $fn=16);
            }
*/

ballBearingDiameter = 7.1;

difference() {
    rotate([45,0,0])
    cube([50, ballBearingDiameter+2, ballBearingDiameter+2], center=true);

    translate([-26, -10, -20])
    cube([52, 20, 20]);

    translate([-26, -10, -1])
    cube([52, 10, 10]);
    
    translate([20,4.5,4.5])
    sphere(d=ballBearingDiameter, $fn=32);

    translate([-20,4.5,4.5])
    sphere(d=ballBearingDiameter, $fn=32);
}