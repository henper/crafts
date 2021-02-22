// Sturdystruder by Henrik P. 2014-06-01
//
// updated in early 2021 with:
// * BSP thread for push fitting
// * flipped to allow for easier filament removal
// * neater inserts for M3 bolts with 4.5 mm thread inside NEMA 17
// BOM: 2x10mm & 2x20mm M3 cap head bolts, 1x15mm M5 bolt and nut

// Assembled
//translate([n17hs,-n17hs,7-1.35]) rotate([0,0,10]) color("green") swivel();
//translate([-13.5,9,14.5]) rotate([90,0,0]) color("blue") spring_tensioner($fn=50);
//translate([4.8,22.5,9.5]) rotate([90,0,0]) color("blue") bsp_m5_nut_clamp($fn=50);
extruder_block();
//bspThread();

// Plate
//translate([-30,-15,11]) rotate([0,180,90]) swivel();
//translate([0,-8,0]) spring_tensioner($fn=50);
//translate([0,3.5,0]) bsp_m5_nut_clamp($fn=50);
//extruder_block();

//swivel();

// The radius of the hobbed gear, hobbed part.
// Eg. the MK8 has a 7mm inner diameter according to http://reprap.org/wiki/Drive-gear
hobbsRadius = 3.5; 
filamentDiameter = 1.75;

filamentCenterOffset = hobbsRadius + filamentDiameter/2;

// Enable this to get longer guides for the filament ( != 1 disables)
flexibleFilamentGuide = 0;

// Tap-size of British Standard Pipe with 1/8" thread
bspTapDiameter = 8.8;
pushFittingThreadDepth = 10;

use <threads.scad>

// English: 1/8 x 28.
module bspThread() {
  //difference() {
    //translate([0,0,6]) cube([12,12,12], center=true);
    threadDiameterInInches = 0.3830+0.009;
    english_thread (diameter=threadDiameterInInches, threads_per_inch=28, length=10/25.4);

    translate([0,0, 1]) cylinder(r1=threadDiameterInInches*25.4/2+0.25, r2=threadDiameterInInches*25.4/2, h=3, center=true);
    translate([0,0,10]) cylinder(r1=threadDiameterInInches*25.4/2, r2=threadDiameterInInches*25.4/2+0.25, h=2, center=true);

    // horizontal printing
    difference() {
      cylinder(d=threadDiameterInInches*25.4+0.1, h=10, $fn=32);
      translate([ 0,-8,6]) cube([12,12,12], center=true);
      translate([ 0,8,6]) cube([12,12,12], center=true);
    }
  //}
}

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

      translate([n17w/2,n17w/2,7.5]) rotate([0,0,45]) cube([4,4,15], center=true);
      translate([n17w/2,-n17w/2,4.25]) rotate([0,0,45]) cube([4,4,8.5], center=true);

      // Fixing plate, attaches to 15 by 15 OpenBeam
      difference() 
      {
        width = 3;
        xOffset = (n17w + width)/2;
        translate([xOffset,0,7.5]) cube([width,74,15], center = true);
        union() 
        {
          // fixing plate cutout
          translate([xOffset,37,-2.5])  rotate([45,0,0])  cube([6,16,7], center = true);
          translate([xOffset,-37,-2.5]) rotate([135,0,0]) cube([6,16,7], center = true);
          translate([xOffset,37,17.5])  rotate([135,0,0]) cube([6,16,7], center = true);
          translate([xOffset,-37,17.5]) rotate([45,0,0])  cube([6,16,7], center = true);
          // M3 bolt holes
          translate([xOffset-3,30.5,7.5])  rotate([0,90,0])  cylinder(6, r=m3radi, $fn=25);
          translate([xOffset-3,-30.5,7.5]) rotate([0,90,0])  cylinder(6, r=m3radi, $fn=25);
        }
      }

         // Top shell
         //translate([-16,18,3]) cube([37,3,13]);
         //translate([18,12,3]) cube([3,9,12]);

         // Bottom shell 
         translate([-n17w/2,-n17w/2,3]) cube([n17w,11,10-4.5]);

         // In-filament guide
         hull()
         {
           translate([0,-n17w/2,3-1.35]) cube([9,11,10-4.5+1.35]);
           translate([1,-n17w/2,3-1.35]) cube([7,11,8]);
         }

         // Out-filament guide
         /*hull()
         {
           translate([filamentCenterOffset,18,8.5]) cube([15,2,15], center=true);
           translate([filamentCenterOffset,15.5,8.5]) cube([12,1,12], center=true);
         }*/
         // Filament center
         translate([filamentCenterOffset,11,9.5-1.35]) rotate([90,0,0]) union() // 9.5
         {
           cylinder(r1=5, r2=0, h=7, $fn=25);
           difference() {
            translate([0,0,32]) cylinder(r1=3.5, r2=0, h=6, $fn=25);
            translate([0,6.5,36]) cube(10, center=true);
           }
         }

         // Swivel support
         //translate([n17w/2-12,-n17w/2,0]) cube([12,11,10-4.5]); //7-1.35

         translate([n17hs,-n17hs,16.5]) cylinder(r=5, h=2.5, $fn=32);
         translate([n17hs,-n17hs-5,16.5]) cube([8.5,10, 2.5]);
         translate([n17hs+5.5,-n17hs-5,15]) cube([3,10,3]);

         // Spring tensioner
         hull()
         {
           translate([-21,10,3]) cube([n17w+3,11,15]);
           translate([-20,10,18]) cube([n17w+2,11,1]);
         }
         /*hull()
         {
           translate([-16.5,22,10.7]) cube([6,1,6]);
           translate([-17.5,20,9.3]) cube([8,1,8]);
         }*/
    }
    // Hollows
    union()
    {
      // Stepper shaft cut-out
      difference() {
        translate([0,0,10-1]) cylinder(20,r1=13, r2=0, $fn=50, center = true);
        translate([0,0,10+3.5]) cube(20, center = true);
      }

      // M3 screw holes
      for(r=[1:4]) 
      {
        rotate([0,0,r*360/4])
            {
              translate([n17hs,n17hs,-1]) cylinder(20,r=m3radi, $fn=25);
            }
      }
      translate([n17hs,n17hs, 20-4.5]) cylinder(20,r=2.9, $fn=25);  // 20 mm M3
      translate([n17hs,-n17hs, 20-4.5]) cylinder(20,r=2.9, $fn=25); // 20 mm M3
      translate([-n17hs,n17hs, 10-4.5]) cylinder(20,r=2.9, $fn=25); // 10 mm M3
      translate([-n17hs,-n17hs, 10-4.5]) cylinder(20,r=2.9, $fn=25);// 10 mm M3

      // NEMA 17 beveled edge cut-out
      translate([-21,21-4.2,-1]) rotate([0,0,45]) cube([6,6,22]);
      translate([-21,-21-4.2,-1]) rotate([0,0,45]) cube([6,6,22]);

      // Swivel support edge
      //translate([9,-14,3]) rotate([0,0,45]) cube([16,8,10]);

      // Filament center
      translate([filamentCenterOffset,34,9.5-1.35]) rotate([90,0,0]) union() // 9.5
      {
        cylinder(80, r=1, $fn=25); // filament guides
        translate([0,0,57.5]) cylinder(2, r1=1,r2=2, $fn=25); //input taper
        translate([0,0,27]) cylinder(2, r1=1,r2=2, $fn=25); //output taper

        translate([0,0,23]) cylinder(3, r=2.15, $fn=25); // teflon stop

        //translate([0,0,12]) cylinder(d=bspTapDiameter, h=pushFittingThreadDepth+10, $fn=64);
        translate([0,0,12]) bspThread();

        translate([11,3.25,34]) rotate([90,0,0]) cylinder(r=8, h=6.5);
      }
        // Spring tensioner
        translate([-13.5,25,14.5]) rotate([90,0,0]) cylinder(20,r=m3radi, $fn=25);
        translate([-13.5,15.5,14.5]) rotate([90,0,0]) hexagon(5.75,6);
        translate([-13.5,n17hs,14.5]) rotate([0,360/6,0]) translate([-4,0,0]) cube([10, 3, 5.75], center=true);
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
      translate([0,0,3.2]) hull()
      {
        // Pivot point
        cylinder(h=7.8,r=5, $fn=100);

        // Bearing housing
        translate([0,n17hs,0]) cylinder(h=7.8, r=4.2, $fn=100);
      }
      translate([0,0,-2]) hull()
      {
        // Pivot point
        translate([    0,0,6]) cylinder(h=7,r=5, $fn=100);
        // Lever
        translate([-45,2,6]) cylinder(h=7, r=3, $fn=100);
      }
    }
    // Hollows
    union()
    {
      // Pivot point
      translate([0,0,-1]) cylinder(h=20,r=m3radi, $fn=50);
      translate([0,0,10.8]) cylinder(h=1,r=2.9, $fn=50);

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
         translate([-30,24,7.5]) rotate([90,0,0]) difference()
         {
           cylinder(h=20.5,r=3.3,$fn=50);
           translate([0,0,18]) cylinder(h=4,r1=0.5,r2=2.5,$fn=50);
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
