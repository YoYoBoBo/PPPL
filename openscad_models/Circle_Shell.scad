difference()
{
    shell();
    
    translate([50,50,50]) sphere(25);
}


module shell(){
    difference()
    {
        sphere(100);
            
        sphere(80);
    }
}