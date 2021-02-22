module Nema17()
{
	nema_side = 42.2;
	nema_bolts = 31.04/2.0;
	nema_depth = 3.8;
	M3 = 3.0/2.0;

	//bevel corners
	r1 = nema_side/2- nema_bolts;
	r2 = sqrt(2)* r1 ;
	r=(r2-r1)*2;
	
	
	difference()
	{
	
		union()
		{
			cube([nema_side,33.8,nema_side]);
	
			translate( [nema_side/2,0,nema_side/2]) 
				rotate(90,[1,0,0]) 
					{
						cylinder(r = 11, h = 2, $fn = 40);
						cylinder(r = 5.0/2.0, h = 20, $fn = 20);
					}
		}
	
	
		translate( [nema_side/2,0,nema_side/2])
		{
	
			for(j=[1:4])
			{
				rotate(90*j,[0,1,0]) 
					translate( [nema_side/2,33.8/2,nema_side/2]) 
				rotate(45,[0,1,0]) 
				cube([30,50,r], center = true);
			}
	
			//bolt holes
			for(j=[1:4])
			{		
				rotate(90*j,[0,1,0]) 
				translate( [nema_bolts,0,nema_bolts]) 
					rotate(-90,[1,0,0]) 
					{
						cylinder(r = M3, h = nema_depth*2, $fn = 20,center=true);
					}
	
			}
		}
	}
}
	
	
Nema17();