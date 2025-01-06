// golden ratio
g = (1+sqrt(5))/2;

// tri-wing
tt = 3;
th = 15;

// wooden posts
d = 15+0.1;
h = 600;
s = 15;      // angle
c = d/2+tt;  // separation

l = cos(s)*(h-h/g); // height of the legs

f = 100; // facets

r = 8;

// speakers
qw = 156;
qd = 195;
qh = 230;
qr = 27/2;

// hole pattern
fp =  76;
bp = 115;
fb = 155;

hd = 11;

module plate() {
    difference() {
        union() {
            hull() {
                // screw-base
                translate([0,0,l]) {
                    rotate([0,0,r])
                    for (xlr = [-1,1]) {
                        for (yfb = [-1,1]) {
                            translate([xlr*fp/2,yfb*fb/2,0])
                            cylinder(r=hd/2+2, 5);
                        }
                    }
                }

                // legs-support
                for (i=[0:120:360]) {
                    rotate([s,0,i]) {
                        translate([c,0,l+5])
                        cylinder(r1=th/2+2, r2=th/2+5, 15);
                    }
                }
            }
        }

        // screw-holes
        translate([0,0,l]) {
            rotate([0,0,r])
            for (xlr = [-1,1]) {
                for (yfb = [-1,1]) {
                    translate([xlr*fp/2,yfb*fb/2,-50/2]) {
                        // shaft
                        cylinder(r=4/2+0.1, 50);
                        // head
                        cylinder(r=7/2, 25);
                    }
                }
            }
        }

        // speaker
        rotate([0,0,r])
        translate([-qw/2,-qd/2,l+5])
        cube([qw,qd,qh]);

        legs();
    }
}


module triwing() {
    hull()
    for (i=[0:120:360]) {
        rotate([s,0,i]) {
            translate([c,0,-th/2])
            cylinder(r=d/2+tt, th, $fn=f);
        }
    }
}

module legs() {
    for (i=[0:120:360]) {
        rotate([s,0,i]) {
            translate([c,0,-h/g])
            cylinder(r=d/2, h, $fn=f);
        }
    }
}

difference() {
    // tri-wing
    color("white")
    triwing();

    // wooden posts
    legs();
}


// base-plate
color("white")
plate();

// h * cos B = l

color("grey")
rotate([0,0,r])
translate([qr-qw/2,-qd/2, l+qr+5])
minkowski() {
    cube([qw-2*qr,qd/2,qh-qr*2]);
    rotate([-90,0,0])
    cylinder(r=qr, qd/2, $fn=f);
}

color("saddlebrown")
legs();

color("goldenrod")
for (i=[0:120:360]) {
    rotate([s,0,i]) {
        translate([c,0,-h/g-5])
        cylinder(r=d/2, 5, $fn=f);

        translate([c,0,-h/g-25])
        cylinder(r2=d/2, r1=0, 20, $fn=f);
    }
}