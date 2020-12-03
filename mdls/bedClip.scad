
m3diam = 3.1;
height = 1.5;
offset = 10;
zfight=0.2;

$fn=32;

difference()
{
    union()
    {
        cylinder(d=m3diam*3, h=height*3);
        hull()
        {
            cylinder(d=m3diam*3, h=height*2);
            translate([0,offset,0])cylinder(d=m3diam*2, h=height*2);
        }
    }
    translate([0,0,-zfight])cylinder(d=m3diam, h=3*height+zfight*2);
}
