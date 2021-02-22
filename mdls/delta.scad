//delta.scad

// 2020 extrusion params
alu_height = 7500;
alu_length = 250;

// linear rod
lienarRod_height = 500;
linearRod_distance = 75;


module aluExtrusion(height) {
    //temp..
    translate([0,0,height/2]) cube([20,20,height], center=true);
}

use <nema17.scad>;

module vertex()
{
    height = 40;
    

    Nema17();
    //aluExtrusion(height);
}

vertex();