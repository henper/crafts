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

// the Golden mean
fi = (1+sqrt(5))/2;

// roundness
r = 10;

// length of the facet of the inner pentagon of the pentagram
u = 100;

// length of the hypotenusi
h = u * fi;
hprim = u/(2*cos(54));
echo(h=h);

// length of the intersections
a = hprim * sin(54);
b = h * cos(36);
echo(a=a);
echo(b=b);
echo(ab=a+b);

module pentagram()
{
    A = [  0,   a];
    B = [u/2,   a];
    C = [  0, a+b];

    //offset(r=-1)
    for(alpha = [0:360/5:360]) 
    {
        rotate(alpha)
        {
            mirror([0,0,0]) polygon([A, B, C]);
            mirror([1,0,0]) polygon([A, B, C]);
        }
    }

    
}

module pentagram2()
{
    A = [  0,   a];
    B = [u/2,   a];
    C = [  0, a+b];

    // mountains
    m = [for (alpha = [0:360/5:360-360/5]) [(a+b) * sin(alpha), (a+b) * cos(alpha)]];
    echo(m=m);

    // valleys
    v = [for (alpha = [36:360/5:360+36-360/5]) [hprim * sin(alpha), hprim * cos(alpha)]];
    echo(v=v);

    // poor mans interleave :(
    coords = [m[0], v[0], m[1]];//, v[1], m[2], v[2], m[3], v[3], m[4], v[4]];
    echo(coords=coords)

    polygon(c);
}

linear_extrude(height=1) pentagram2(); //polygon([[1,1], [1,-1], [-1,-1], [-1,1]]);