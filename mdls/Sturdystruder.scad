// Sturdystruder by Henrik P. 2014-06-01

// Assembled
translate([n17hs,-n17hs,7]) rotate([0,0,9]) color("green") swivel();
translate([-13.5,9,14.5]) rotate([90,0,0]) color("blue") spring_tensioner($fn=50);
translate([4.8,22.5,9.5]) rotate([90,0,0]) color("blue") bsp_m5_nut_clamp($fn=50);
extruder_block();

// Plate
//translate([-30,-15,11]) rotate([0,180,90]) swivel();
//translate([0,-8,0]) spring_tensioner($fn=50);
//translate([0,3.5,0]) bsp_m5_nut_clamp($fn=50);
//extruder_block();

// The radius of the hobbed gear, hobbed part.
// Eg. the MK8 has a 7mm inner diameter according to http://reprap.org/wiki/Drive-gear
hobbsRadius = 3.5; 
filamentDiameter = 1.75;

filamentCenterOffset = hobbsRadius + filamentDiameter/2;

// Enable this to get longer guides for the filament ( != 1 disables)
flexibleFilamentGuide = 1;

m3radi = 1.75;
n17w = 42;
n17hs = (n17w / 2) - 5.5;

module extruder_block() 
{
	// Frame and NEMA17 mount
	difference() 
	{
		// Solids
		union() 
		{
			// NEMA 17 plate
			translate([0,0,1.5]) cube([n17w,n17w,3], center = true);

			// Fixing plate, attaches to 15 by 15 OpenBeam
			difference() 
			{
				translate([-20,0,7.5]) cube([3,74,15], center = true);
				union() 
				{
					// fixing plate cutout
					translate([-20,37,-2.5])  rotate([45,0,0])  cube([6,16,7], center = true);
					translate([-20,-37,-2.5]) rotate([135,0,0]) cube([6,16,7], center = true);
					translate([-20,37,17.5])  rotate([135,0,0]) cube([6,16,7], center = true);
					translate([-20,-37,17.5]) rotate([45,0,0])  cube([6,16,7], center = true);
					// M3 bolt holes
					translate([-23,30.5,7.5])  rotate([0,90,0])  cylinder(6, r=m3radi, $fn=25);
					translate([-23,-30.5,7.5]) rotate([0,90,0])  cylinder(6, r=m3radi, $fn=25);
				}
			}

         // Top shell
         translate([-18,18,3]) cube([37,3,13]);
         //translate([18,12,3]) cube([3,9,12]);

         // Bottom shell 
         translate([-n17w/2,-n17w/2,3]) cube([21,3,5.5]);

         // In-filament guide
         hull()
         {
           translate([0,-n17w/2,3]) cube([9,6,5.5]);
           translate([1,-n17w/2,3]) cube([7,6,8]);
         }

         // Out-filament guide
         hull()
         {
           translate([filamentCenterOffset,18,8.5]) cube([15,2,15], center=true);
           translate([filamentCenterOffset,15.5,8.5]) cube([12,1,12], center=true);
         }

         // Swivel support
         translate([n17w/2-12,-n17w/2,0]) cube([12,12,7]);

         // Spring tensioner
         hull()
         {
           translate([-18.5,10,3]) cube([10,11,13]);
           translate([-17.5,10,16.3]) cube([8,11,1]);
         }
         hull()
         {
           translate([-16.5,22,10.7]) cube([6,1,6]);
           translate([-17.5,20,9.3]) cube([8,1,8]);
         }
		}
		// Hollows
		union()
		{
			// Stepper shaft cut-out
			translate([0,0,0]) cylinder(6,r=13, $fn=50, center = true);

			// M3 screw holes
			for(r=[1:4]) 
			{
				rotate([0,0,r*360/4])
            {
              translate([n17hs,n17hs,-1]) cylinder(20,r=m3radi, $fn=25);
            }
			}
         translate([-n17hs,n17hs, 8]) cylinder(20,r=2.8, $fn=25);

			// NEMA 17 beveled edge cut-out
			translate([21,21-4.2,-1]) rotate([0,0,45]) cube([6,6,18]);
			translate([21,-21-4.2,-1]) rotate([0,0,45]) cube([6,6,18]);

			// Swivel support edge
			translate([9,-15,3]) rotate([0,0,45]) cube([16,8,6]);

			// Filament center
			translate([filamentCenterOffset,34,9.5]) rotate([90,0,0]) union()
			{
            cylinder(80, r=1, $fn=25); // filament guides
				translate([0,0,18]) cylinder(2, r1=1,r2=2, $fn=25);
            //translate([0,0,54]) cylinder(2, r1=1,r2=2, $fn=25);

            // M5 nut slot (slightly higher than spec. b/c of print inaccuracies)
				translate([0,0.3,13.5]) rotate([0,0,30]) hexagon(8,6);
            translate([0,-0.3,13.5]) rotate([0,0,30]) hexagon(8,6);

            // BSP nut fastner mount
            translate([-7.5,0,10]) cylinder(10, r=m3radi,$fn=25);
            translate([ 7.5,0,10]) cylinder(10, r=m3radi,$fn=25);
            translate([-7.5,0,16]) rotate([0,0,30]) cylinder(5, r=2.8,$fn=6);
            translate([ 7.5,0,16]) rotate([0,0,30]) cylinder(5, r=2.8,$fn=6);
			}

         // Spring tensioner
         translate([-13.5,25,14.5]) rotate([90,0,0]) cylinder(20,r=m3radi, $fn=25);
         translate([-13.5,15.5,14.5]) rotate([90,0,0]) hexagon(5.75,5);
		}
	}

   if(flexibleFilamentGuide == 1)
   {
     translate([filamentCenterOffset-3.5, 13, 3]) hull()
     {
       cube([7,2,9]);
       translate([1.25,-7.5,4.5]) cube([4.5,2,4.5]);
     }
     translate([filamentCenterOffset-3.5, -15, 3]) hull()
     {
       cube([7,2,8]);
       translate([1.25,7.5,4.5]) cube([4.5,2,3.5]);
     }
  }
}

module swivel()
{
	difference()
	{
		// Solids
		union()
		{
			hull()
			{
				// Pivot point
				cylinder(h=11,r=5, $fn=100);

				// Bearing housing
				translate([0,n17hs,0]) cylinder(h=11, r=4.2, $fn=100);
			}
			translate([0,0,-2]) hull()
			{
				// Pivot point
				translate([    0,0,6]) cylinder(h=7,r=5, $fn=100);
				// Lever
				translate([-30.5,2,6]) cylinder(h=7, r=3, $fn=100);
			}
		}
		// Hollows
		union()
		{
			// Pivot point
			translate([0,0,-1]) cylinder(h=20,r=m3radi, $fn=50);
			translate([0,0,7.5]) cylinder(h=4,r=2.8, $fn=50);

			// Bearing housing
			translate([0,n17hs,-1]) difference()
         {
           cylinder(h=7, r=8.5, $fn=100);
           cylinder(h=8, r=4.2, $fn=50);
         }

			// Bearing
			#translate([0,n17hs,0]) cylinder(h=5, r=8, $fn=100);

			// Bearing axle
			translate([0,n17hs,5]) cylinder(h=7, r=2.5, $fn=100);

         // Spring cutout
         #translate([-29,24,07.5]) rotate([90,0,0]) difference()
         {
           cylinder(h=20,r=3.1,$fn=50);
           cylinder(h=20,r1=1.4,r2=1.8,$fn=50);
         }
		}
	}
}

module bsp_m5_nut_clamp()
{
  bsp = 8;
  difference()
  {
    hull()
    {
      translate([-5,0,0]) cylinder(1.5, r=6);
      translate([ 5,0,0]) cylinder(1.5, r=6);
    }
    union()
    {
      cylinder(h=2,r=bsp/2);
      translate([-7.5,0,0]) cylinder(2, r=m3radi);
      translate([ 7.5,0,0]) cylinder(2, r=m3radi);
    }
  }  
}

module spring_tensioner()
{
  difference()
  {
    cylinder(4,r=4);
    //translate([0,0,2])cube([8,8,4], center=true);
    union()
    {
      cylinder(1,r=m3radi);
      translate([0,0,3]) difference()
      {
        cylinder(h=2,r=3.2);
        cylinder(h=2,r1=1.8,r2=1.4);
      }
    }
  }
}

module hexagon(size, height) 
{
  boxWidth = size/1.75;
  for (r = [-60, 0, 60]) rotate([0,0,r]) cube([boxWidth, size, height], true);
}
