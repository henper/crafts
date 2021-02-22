


//zipClip();
//hammerNut();
openBeamClip();


//import("OpenBeam_1515_Extrusion_Clear_Anodized.STL");

//import("OpenBeam_1515_Extrusion_Clear_Anodized.STL");

module openBeamClip(height = 10) {
    insertWidth = 3;
    internalWidth = 5-0.75;
    internalDepth = 2.5;
    lipDepth = 1.5;
    clipWidth = (internalWidth-insertWidth);

    linear_extrude(height=height)
    polygon([[insertWidth/2, 0], [insertWidth/2, lipDepth], [internalWidth/2, lipDepth+internalDepth/2], [clipWidth/2, lipDepth+internalDepth],
             [clipWidth/2, 0], [-clipWidth/2, 0],
             [-clipWidth/2, lipDepth+internalDepth], [-internalWidth/2, lipDepth+internalDepth/2], [-insertWidth/2, lipDepth], [-insertWidth/2, 0]]);
}

module hammerNut() {
    tolerance = 0.15;

    channelWidth = 5.75 - tolerance;
    channelDepth = 2.5;

    difference() {
        

        
        halfRoundedCube(width=channelWidth, height=channelDepth);

        

        m3radi = 3.25; //2.86;
        translate([0,0,-tolerance]) cylinder(d=m3radi, h=channelDepth+2*tolerance, $fn=16);
    }
}

module halfRoundedCube(width = 5, height=1) 
{
    radius = width/2;

    cylinder(r=radius, h=height, $fn=16);
    cube([radius, radius, height]);
    translate([-radius, -radius, 0]) cube([radius, radius, height]);
}

module zipClip() {

    width = 3;
    height = 5;

    // cable-tie
    cable_tie = false;
    vertical = true;

    // open-beam attachement
    difference() {

        cube([15+width, 15+width, height], center=true);

        // nut cutouts
        cube([15, 6, 20], center=true);
        cube([ 6, 15, 20], center=true);

        // side rear indents
        translate([-7.5+1.5/2,-4,0]) cube([1.5, 6, 20], center=true);
        translate([7.5-1.5/2,-4,0]) cube([1.5, 6, 20], center=true);

        // side front indents
        translate([0,4.2,0]) cube([15, 1, 20], center=true);

        // front side indents
        translate([-4.5, +7.5-1.3/2+0.24,0]) cube([6, 1, 20], center=true);
        translate([4.5, 7.5-1.3/2+0.24,0]) cube([6, 1, 20], center=true);
        translate([0,6.5,0]) cube([12, 1, 20], center=true);

        // front clip
        translate([0,15-2.5,0]) rotate([0,0,45]) cube([15, 15, 20], center=true);

        translate([-15/2, -15/2, -100]) import("OpenBeam_1515_Extrusion_Clear_Anodized.STL");

    }



    beta =  vertical ? 90 : 0;
    x = vertical ? height : 15 + width;
    y = vertical ? 15 + width : height;
    z = vertical ? 3 : 4.4;
    i = vertical ? 6 : 3;
    j = vertical ? 2 : 3;

    if (cable_tie) {
        for (alpha=[0:90:180]) {
            rotate([beta,0,-alpha]) {
                translate([15/2, 0, 0]) {
                    difference() {
                        hull() 
                        {
                            translate([width/2,0,0]) cube([0.00001, x, y], center=true);
                            translate([4, z,0]) cylinder(r=1.5, h=i, center=true, $fn=16);
                            translate([4,-z,0]) cylinder(r=1.5, h=i, center=true, $fn=16);
                        }

                        hull() 
                        {
                            translate([3,-j,0]) cylinder(r=1, h=20, center=true, $fn=16);
                            translate([3, j,0]) cylinder(r=1, h=20, center=true, $fn=16);
                        }
                    }
                }
            }

        }

    }

}
