// golden ratio
g = (1+sqrt(5))/2;

// tri-wing
tt = 3;
th = 15;

// wooden posts
d = 15+0.1;
h = 800;
s = 18;      // angle
c = d/2+tt;  // separation

l = cos(s)*(h-h/g); // height of the legs

f = 100; // facets

// speakers
qw = 190;
qd = 300;
qh = 295;

// hole pattern
fp = 122;
bp = 134;
fb = 242;

hd = 13;

module plate() {
    difference() {
        translate([0,0, l]) {

            hull()
            for (xlr = [-1,1]) {
                for (yfb = [-1,1]) {
                    translate([xlr*fp/2,yfb*fb/2,0])
                    cylinder(r=hd/2, 5);
                } 
            }
        }

        #legs();
    }
}


module triwing() {
    hull()
    for (i=[0:120:360]) {
        rotate([s,0,i]) {
            translate([c,0,0])
            cylinder(r=d/2+tt, th, $fn=f);
        }
    }
}

module legs() {
    for (i=[0:120:360]) {
        rotate([s,0,i]) {
            translate([c,0,-h/g])
            cylinder(r=d/2, h);
        }
    }
}

difference() {
    // tri-wing
    triwing();

    // wooden posts
    legs();
}


// base-plate
plate();

// h * cos B = l

color("grey")
translate([-qw/2,-qd/2, l+1])
cube([qw,qd,qh]);
