/* Pentagram facet and units

      /|\ 
     / | \
    /  |  \
   /   b   h
  /    |    \
 /_____|_u/2_\
 \     |     /
   \   a   h'
     \ | /

*/

module pentagram(u=100)
{
    // the Golden mean
    fi = (1+sqrt(5))/2;

    // length of the hypotenusi
    h = u * fi;
    hprim = u/(2*cos(54));
    echo(h=h);

    // length of the intersections
    a = hprim * sin(54);
    b = h * cos(36);

    m = [for (alpha = [0:360/5:360-360/5]) [(a+b) * sin(alpha), (a+b) * cos(alpha)]];
    echo(m=m);

    v = [for (alpha = [36:360/5:360+36-360/5]) [hprim * sin(alpha), hprim * cos(alpha)]];
    echo(v=v);

    // poor mans interleave :(
    coords = [m[0], v[0], m[1], v[1], m[2], v[2], m[3], v[3], m[4], v[4]];    
    polygon(coords);
}

// the Golden mean
fi = (1+sqrt(5))/2;
hypot = 83;
roundness = 7;

//color("white")  translate([0,0,0]) linear_extrude(height=1) pentagram(u=hypot/fi);
//color("blue") translate([0,0,1]) linear_extrude(height=1) offset(r=-roundness) pentagram(u=hypot/fi+1.4*roundness);
//color("red")   translate([0,0,2]) linear_extrude(height=1) offset(r=roundness) pentagram(u=hypot/fi-1.4*roundness);


/*
difference()
{
  {
    cylinder(h=5, r=5);
    union()
    {
        translate([0,0,1]) difference()
        {
          linear_extrude(height=5) pentagram(u=2);

          difference()
          {
            cylinder(h=4, r=6);
            cylinder(h=5, r1=0, r2=5);
          }
        }
    }
  }
}
*/
$fn = 50;

difference()
{
  linear_extrude(height=5) pentagram(u=4);

  translate([0,0,-1]) cylinder(h=1+3.5, r=2.5/2);
  difference()
  {
    cylinder(h=6, r=8);
    cylinder(h=5, r1=8, r2=0);
  }
}
