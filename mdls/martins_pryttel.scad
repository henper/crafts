length  = 49;
slength = 9;
width   = 42;
swidth  = 12;
heigth  = 12;
diam    = 17.6;

// garden row
mittfora = 2.4;
gs = 1.4;
gr = 2.5;
gh = 1.2;

difference()
{
    union()
    {
        translate([0,-swidth/2,0])cube([length, swidth, heigth]);
        translate([0,-width/2,0])cube([slength, width, heigth]);
    }
    translate([-(diam/6),0,-1])cylinder(h=heigth+2, r=diam/2);
    union()
    {
    translate([slength,0,gh])
        difference()
        {
            union()
            {
                for(i=[0:gr+gs:length-slength])
                {
                    translate([i,-1-(swidth/2),0])cube([gr,swidth+2,heigth]);
                }
            }
            translate([0,-mittfora/2,0])cube([length-slength-1, mittfora, heigth]);
        }
    }
}