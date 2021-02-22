//mms.scad

$fn=32;

/*module mmsFemale() {
    translate([0,0,-4]) difference() {
        color("grey") import("2020_Bracket_v2.stl", convexity=8);
        cube([60, 21, 4*2], center=true);
        translate([-22.5,0,0]) cube([30, 20, 10], center=true);
        translate([22.5,0,0]) cube([30, 20, 10], center=true);
    }
}*/

module mmsFemaleSmallBracket() {
    mmsFemale();
    difference() {
        hull() {
            translate([7.5,0,0]) cylinder(d=20, h=3);
            translate([-7.5,0,0]) cylinder(d=20, h=3);
        }
        translate([5+7.5,0,-1]) cylinder(r=1.75, h=60);
        translate([-5-7.5,0,-1]) cylinder(r=1.75, h=60);
    }
}

//mmsFemaleSmallBracket();

/*
difference() {
    translate([0,0,0]) {
        import("Xbox_One_Clip_with_Modular_Mounting_System.stl", convexity=8);
    }
    translate([10,-8,36/2-5-7.5]) rotate([0,-90,0]) cylinder(r=1.75, h=60);
    translate([10,-8,36/2+5+7.5]) rotate([0,-90,0]) cylinder(r=1.75, h=60);
}
*/

module mmsFemale() {
    // bottom plate is 15 by 15.8
    rotate([0,-90,0]) translate([15/2-.066,15.8/2+.13,0]) import("Modular_Mounting_System_Female.stl");
    //color("grey") cube([15,15.8,1], center=true);
}

module tetra() {
    // tri-fem
    for (alpha=[0:120:240]) {
        rotate([0,0,alpha]) translate([-17,-15.8/2,0]) color("grey") mmsFemale();
    }

    // body
    hull() {
        for (alpha=[0:120:240]) {
            rotate([0,0,alpha]) translate([-19.5,0,15/2]) cube([1, 15.8, 15], center=true);
        }
    }

    //top-fem
    translate([-15/2,-15.8/2,12]) rotate([0,90,0]) mmsFemale();
}

color("grey") tetra();

r = (9+0.8)/2;
translate([-28.5, 10, r/2+5]) rotate([90,90,0]) #cylinder(r=r, h=4, $fn=6);