// golden ratio
g = (1+sqrt(5))/2;

// tri-wing
tt = 3;
th = 15;

// wooden posts
d = 15+0.2;
h = 600;
s = 15;      // angle
c = d/2+tt;  // separation

l = cos(s)*(h-h/g); // height of the legs
echo("l = ", l);


f = 100; // facets

// rotation and translation of the base
r = 8;
t = 9;

// speakers
qw = 156;
qd = 195;
qh = 230;
qr = 27/2;

// hole pattern
fp =  85;
bp =  95;
fb = 149;

hd = 11;

module plate() {
    color("white")
    difference() {
        union() {
            hull() {
            //{
                // screw-base
                translate([0,t,l])
                rotate([0,0,r]) {
                    // front
                    for (xlr = [-1,1])
                        translate([xlr*fp/2, -fb/2, 0])
                        cylinder(r=hd/2+2, 5);


                    // back
                    for (xlr = [-1,1])
                        translate([xlr*bp/2, fb/2, 0])
                        cylinder(r=hd/2+2, 5);

                }

                // legs-support
                for (i=[0:120:360]) {
                    rotate([s,0,i]) {
                        translate([c,0,l])
                        cylinder(r1=th/2+2, r2=th/2+5, 17);
                    }
                }
            }
        }

        // screw-holes
        translate([0,t,l]) {
            rotate([0,0,r]) {

                // front
                for (xlr = [-1,1]) {
                    translate([xlr*fp/2, -fb/2, -50/2]) {
                        // shaft
                        cylinder(r=4/2+0.5, 50);
                        // head
                        cylinder(r=7/2+0.5, 28);
                    }
                }

                // back
                for (xlr = [-1,1]) {
                    translate([xlr*bp/2, fb/2, -50/2]) {
                        // shaft
                        cylinder(r=4/2+0.5, 50);
                        // head
                        cylinder(r=7/2+0.5, 28);
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
    color("white")
    difference() {
        // body
        hull()
        for (i=[0:120:360]) {
            rotate([s,0,i]) {
                translate([c,0,-th/2])
                cylinder(r=d/2+tt, th, $fn=f);
            }
        }

        legs();

    }
}

module legs() {
    color("saddlebrown")
    for (i=[0:120:360]) {
        rotate([s,0,i]) {
            translate([c,0,-h/g])
            cylinder(r=d/2, h, $fn=f);
        }
    }
}

module speaker() {
    color("grey")
    rotate([0,0,r])
    translate([qr-qw/2,t-qd/2, l+qr+5])
    minkowski() {
        cube([qw-2*qr,qd/2,qh-qr*2]);
        rotate([-90,0,0])
        cylinder(r=qr, qd/2, $fn=f);
    }
}

module spikes() {
    color("goldenrod")
    for (i=[0:120:360]) {
        rotate([s,0,i]) {
            translate([c,0,-h/g-5])
            cylinder(r=d/2, 5, $fn=f);

            translate([c,0,-h/g-25])
            cylinder(r2=d/2, r1=0, 20, $fn=f);
        }
    }
}

module drill_guide() {

    difference() {
        // material
        cylinder(r=d/2+4, h=100);

        // leg
        translate([0,0,-2])
        cylinder(r=d/2, h=50);

        // bend guide
        translate([-d, -4/2, -1])
        cube([2*d, 4, 40]);

        translate([-d/2-5,0,40])
        rotate([0,90,0])
        cylinder(r=4/2+1, h=d+10);

        // drill
        translate([0,0,-1])
        cylinder(r=12/2+0.2, h=102);
    }

}

triwing();
plate();
speaker();
spikes();
legs();

//drill_guide();
