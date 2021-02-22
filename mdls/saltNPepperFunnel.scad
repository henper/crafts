
br = 22/2-0.5;
fr = br * 2.5;
fh = 30;
ph = 10;
pw = 4.4+0.5;
ww = 1.5;
zf = 1;

$fn = 128;

module funnel() {
    difference() {
        union() {
            cylinder(r=br, h=ph);
            translate([0,0,ph]) cylinder(r1=br, r2=fr, h=fh);
        }
        union() {
            translate([0,0,-zf]) cylinder(r=br-ww/2, h=ph+2*zf);
            translate([0,0,ph]) cylinder(r1=br-ww/2, r2=fr-ww/2, h=fh);
        }
    }
}

funnel();
