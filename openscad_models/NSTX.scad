
blue_ring(100, 120);
blue_ring(90, 140);


blue_ring(120, 50);
blue_ring(110, 70);

blue_ring(120, -50);
blue_ring(110, -70);

blue_ring(100, -120);
blue_ring(90, -140);

red_ring(360);
rotate([0,0,-45]) red_ring(360);
rotate([0,0,45]) red_ring(180);
rotate([0,0,90]) red_ring(360);



module blue_ring(size, height){
    color("blue")
    translate([0,0,height])
    rotate_extrude(angle=270)
    translate([size,0,0])
    square([8,8]);
}

module red_ring(amount){
    color("red")
    scale([1,1,1.25])
    rotate([0,90,0])
    rotate_extrude(angle=amount)
    translate([160,0,0])
    square([8,12]);
}