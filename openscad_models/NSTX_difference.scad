blue_ring(128,50);
blue_ring(118,70);

blue_ring(108,120);
blue_ring(98,140);

blue_ring(128,-50);
blue_ring(118,-70);

blue_ring(108,-120);
blue_ring(98,-140);

for(i=[-45:45:90])
red_ring(i);





module blue_ring(diameter, height){
    color("blue")
    translate([0,0,height])
    difference()
    {
    linear_extrude(8)
    circle(diameter);
    
    linear_extrude(10){
    circle(diameter-8);}
    }
}

module red_ring(turn){
    color("red") 
    rotate([0,90,turn])
    difference()
    {
    linear_extrude(8)
    scale([1.25,1,1])
        circle(168);
    
    linear_extrude(10){
    scale([1.25 ,1,1])
        circle(160);}
    }
    
    
}