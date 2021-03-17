shell();

module shell(){
    for(i=[0:5:360]){
        rotate([0,0,i])column();
    }
}

module column(){
    for(i=[0:5:90]){
        rotate([i,0,0])tile();
    }
}

module tile(){
translate([-50,-50,-1000])square(100,100);
}