//By Coat, 08-jul-2018
//Licensed under the Creative Commons - Attribution license.
//Drillguide for straight/perpendicular holes for use on flat board or for edges board

//Primary parameters
//diameter drill (mm), add a little tolerance
drilldiam = 8.2;
//height of the  guidetube (mm)
guideheight = 25;
//width of the guidetube (mm)
guidewidth = drilldiam + 8;//16;
//thickness of the baseplate (mm)
platethick = 3;
//width of the baseplate (mm)
platewidth = 80;
//baseplate square (1) or round (0)
squareYN = 0;
//number of "wings" to wrap around the board, 0 = none, 1 = 1 and 2 is 2
numberwings = 0;
//when using 1 or 2 wings for end side board, give the thickness of the board (mm, add a little tolerance for 2 wings)
boardwidth = 18.1;

//The Parts
//****************************************
//Untouched baseplate
module squareround(w,t)
{
  difference()
  {
  if(squareYN)     
    cube([w, w, t], center=true);
  else
    cylinder(d=w,h=t, center=true); 
  cube([w/1.25, guidlinew, guideheight],center = true);
  
  translate([0.5*platewidth,0,0])
    nodge();
  translate([0,0.5*platewidth,0])
    nodge();
  translate([-0.5*platewidth,0,0])
    nodge();
  translate([0,-0.5*platewidth,0])
    nodge();
  }
} 

//****************************************
//Break up baseplate in pieces -> the "wings"
module piece()
{
      rotate([0,90,0])
        intersection()
        {
          squareround(platewidth,platethick);
          translate([0.5*(platewidth+boardwidth), 0, 0]) 
            cube([platewidth, platewidth, platethick*2], center = true);
        }  
}  

//****************************************
//Baseplate with or without "wings"
module plate()
{
  if (numberwings==0)                   //no wings 
    squareround(platewidth,platethick); //untouched baseplate
  if(numberwings==1)                    //1 wings
  {  
    difference()                        //cut off one part of baseplate
    {
      squareround(platewidth,platethick);
      translate([0.5*(platewidth+boardwidth), 0, 0]) 
        cube([platewidth, platewidth*2, platethick*2], center = true);
    }  

    translate([0.5*boardwidth+0.5*platethick, 0, 0.5*boardwidth+0.5*platethick])
      piece();                          //and add that piece again under 90 degrees
  }
  if(numberwings==2)                    //2 wings
  {  
    difference()                        //cut off two parts of baseplate
    {
      squareround(platewidth,platethick);
      translate([0.5*(platewidth+boardwidth), 0, 0]) 
        cube([platewidth, platewidth*2, platethick*2], center = true);
      translate([-0.5*(platewidth+boardwidth), 0, 0]) 
        cube([platewidth, platewidth*2, platethick*2], center = true);
    }  
    //and add the pieces again under 90 degrees
    translate([0.5*boardwidth+0.5*platethick, 0, 0.5*boardwidth+0.5*platethick])
      piece();                      
    translate([-0.5*boardwidth-0.5*platethick, 0, 0.5*boardwidth+0.5*platethick])
      piece();          
  }
}  

//****************************************
//Guidenodges
module nodge()
{
  rotate([0,0,45])
    cube([3,3,3*platethick], center=true);
}

//****************************************
//Main
  //secondary parameters
  $fn = 128
  ;
  guidlinew = min(2,drilldiam/2);
  dtop = (guidewidth + drilldiam)/2;

  //The thing
  translate([0,0,0.5 * platethick])
  difference()
  {
    union()                    //Solid drillguide and baseplate
    {
      cylinder(d = guidewidth, h = guideheight);
      plate();
    }  
    cylinder(d = drilldiam , h = guideheight*3, center = true);   //drillhole
    //sawdust-channel / guidelines over the length
    cube([guidlinew, platewidth/1.25, guideheight], center = true); 
    //sawdust-channel in drillguide (rest in module squareround)
    cube([guidewidth, guidlinew, guideheight],center = true);
    //edge in top drillguide to make it easier to insert drill
    translate([0,0,guideheight + dtop/5])
      sphere(d= dtop);
}



