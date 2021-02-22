
bearing_od = 16+0.5;
bearing_id = 5;
bearing_h  = 5;

spool_d = 200;

roller_lh = 2.5;
roller_bl = 56; // empirically attained

$fn = 32;

module rollOfQuarters() {

    difference() {

        width = 10;
        length = roller_bl + bearing_od;
        stand = width*2;

        hull() {
            hull() {
                
                translate([0,-width/2,0])
                cube([length, width, roller_lh]);
                
                translate([roller_bl, 0, roller_lh/2])
                cube([5, stand, roller_lh], center=true);
            }

            //guard rail
            translate([roller_bl,bearing_h/2+2,bearing_od/2+roller_lh]) {
                rotate([90,0,0]) cylinder(d=bearing_od+5, h=bearing_h+4);
            }

            translate([0,-width/2,0]) cube([1, width, 7.5]);

        }

        // spool cutout
        difference() {
            cutout_w = bearing_h+2;
            translate([0,-cutout_w/2,roller_lh])
            cube([length+1, cutout_w, 40]);

            translate([roller_bl, 0, bearing_od/2+roller_lh]) {
                rotate([90,0,0]) {
                    translate([0,0,cutout_w/2-1])
                    cylinder(r1=bearing_id/2+1, r2=bearing_id/2+3, h=1);

                    translate([0,0,-cutout_w/2])
                    cylinder(r1=bearing_id/2+3, r2=bearing_id/2+1, h=1);
                }
            }
        }

        // bearing post
        //guard rail
        m5ScrewLength = 15;
        m5NutWidth = 9+0.8;
        m5NutHeight = 3.85;

        translate([roller_bl, 0, bearing_od/2+roller_lh]) {
            rotate([90,90,0]) {
                
                translate([0,0,-m5NutHeight/2-m5ScrewLength/2]) cylinder(d=bearing_id, h=m5ScrewLength);
                
                translate([0,0,-m5NutHeight/2+m5ScrewLength/2]) cylinder(d=m5NutWidth, h=m5NutHeight, $fn=6);
                translate([0,0,-m5NutHeight/2-m5ScrewLength/2]) cylinder(d=m5NutWidth, h=m5NutHeight, $fn=6);

                translate([0, 0,-bearing_h/2]) cylinder(d=bearing_od+2, h=bearing_h);
            }
        }

        translate([0,2,spool_d/2+1]) rotate([90,0,0]) cylinder(d=spool_d, $fn=128, h=4);

    }

}

rollOfQuarters();
mirror([1,0,0]) rollOfQuarters();
