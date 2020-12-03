
// Tap-size of British Standard Pipe with 1/8" thread
bspTapDiameter = 8.8;

// The radius of the hobbed gear, hobbed part.
// Eg. the MK8 has a 7mm inner diameter according to http://reprap.org/wiki/Drive-gear
hobbsRadius = 3.5; 
filamentDiameter = 1.75+0.25;

openBeamWidth = 15;

m3radius = 1.75;
nemaSeventeenWidth = 42;
nemaSeventeenBoltCenter = (nemaSeventeenWidth / 2) - 5.5;

$fn=32;

module body() {
    width=15;
    for(alpha = [0:90:360]) {
        rotate([0,0,alpha]) {
            difference() {
                // mounting plate
                cube([nemaSeventeenWidth/2, nemaSeventeenWidth/2, width]);
                translate([0,0,-1]) { // z-fight
                    // shaft
                    cylinder(r=hobbsRadius*2, h=width+2);
                    // bolts
                    translate([nemaSeventeenBoltCenter,nemaSeventeenBoltCenter, 0]) cylinder(r=m3radius, h=width+2);
                    // chamfers
                    halfWit = nemaSeventeenWidth/2;
                    hypot = sqrt(2*halfWit*halfWit);
                    rotate(45, 0, 0) translate([hypot-3,-5,0]) cube([10,10,width+2]);
                }
            }
        }
    }
}

difference() {
    body();
    //filament
    #translate([hobbsRadius+filamentDiameter/2, nemaSeventeenWidth/2+1, 15/2]) rotate([90,0,0]) cylinder(d=filamentDiameter, h=nemaSeventeenWidth+2);
}