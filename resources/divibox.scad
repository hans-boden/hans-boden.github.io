/*
    3D printable small box with dividers
    Example for a parameterized design
*/

echo("***main start***********************************");

// all measurement are in mm

// outer dimensions
odim_x = 160;  // length - the hinges for the tap are along this edge
odim_y =  120;  // width
body_z =  12;  // height of the body
tap_z  =   8.5; // height of the tap

odim_z =  body_z + tap_z;  // height of the box with tap
owall = 2.0;   // thickness outer walls/top/bottom 
iwall = 1.2;   // thickness inner walls (for the dividers)
top = 1.3;  // thickness of the tap wall

// dividers, n = trays, n-1 = inner walls, [1] or [] means: no dividers
div_x = [6,3,3,3,6];  // relative size of frays 
div_y = [1,1,1,1];
div_height = body_z;


   body();
// tap(); 
// show();

echo("***main end************************************");

gap = 0.01;
// calculated values
// the derived values are checked here

function vecsum(li, c=0)  =  c < len(li)-1 ?  li[c] + vecsum(li, c+1)  : li[c];
function sumv(v,i,s=0) = (i==s ? v[i] : v[i] + sumv(v,i-1,s));

// how many hinges generated for side length x
function hinge_count(x) = x < 60 ? 1 : x < 150 ? 2 : 3;
// two hinge sizes: 1: two smaller for the tap, 2: one larger for the body
function hinge_size(x, n) = [max(4, x/n * 0.12), max(6, x/n * 0.18)];

//s = 149; echo("hinge_count", hinge_count(s), "size", hinge_size(s,hinge_count(s)));


module show() {
    body();
    move_on_top(odim_z, tap_z) {
        color("blue") {
            tap();
        }
    }
}

module body() {
    difference() {
        body_outer();
        move_on_top(body_z, tap_z) 
            tap_hinges(addmarg=0.2);
    }
    body_dividers();
    color("red") body_hinges();

}

module tap() {
    difference() {
        open_box(x=odim_x, y=odim_y, z=tap_z, wall=owall, base=top);
        move_on_top(tap_z, body_z)
            body_hinges(addmarg=0.2);
    }
    color("blue") tap_hinges();
}


module move_on_top(bot_z, top_z) {
    translate([odim_x, 0, body_z+tap_z])
    rotate([0,180,0])
        children();
}

module body_hinges(addmarg=0) {
    n = hinge_count(odim_x);
    offs = [[0.5],[0.20, 0.80], [0.15, 0.5, 0.85]];
    for (x = offs[n-1]) {
        translate([odim_x * x, odim_y, body_z]) lo_hinge(addmarg);
    }    
}
module tap_hinges(addmarg=0) {
    n = hinge_count(odim_x);
    offs = [[0.5],[0.20, 0.80], [0.15, 0.5, 0.85]];
    for (x = offs[n-1]) {
        translate([odim_x * x, odim_y, tap_z]) 
            hi_hinge(addmarg);
    }    
}

module hi_hinge(addmarg) {
    s12 = hinge_size(odim_x,hinge_count(odim_x));
    lo = s12[1]; // size (length) of larger hinge tube
    hi = s12[0];
    offs = lo/2+hi/2 + 0.1;
    translate([ offs ,0,0])   hinge(hi, addmarg);
    translate([-offs ,0,0])   hinge(hi, addmarg);
}

module lo_hinge(addmarg) {
    s12 = hinge_size(odim_x,hinge_count(odim_x));
    lo = s12[1]; // size (length) of larger hinge tube
    hinge(lo, addmarg);
}

module hinge(hsize, addmarg) {
    // the orientation is for the edge of the wall
    // additional margin for subtracting from opposite wall
    $fn=30;
    
    // outer shape
    hole_r = 0.70; // enough for a pin
    // the tube is attached by a hull 
    tube_r = 2.1;   // stable enough? not too clumsy?
    // the center of the hole is a little bit outside the body wall
    wdist = tube_r * 0.8; 
    
    rotate([0,-90,0])      // rotate horzontal for the xz-wall
    translate([0, wdist, -hsize/2]) // sink in to the center
    difference() {
        hull() {
            cylinder(r=tube_r, h=hsize+addmarg);
            translate([0, -wdist-owall, 0]) cylinder(r=0.01+addmarg, h=hsize+addmarg);
            translate([-4*tube_r, -0.1-owall, 0]) cylinder(r=0.01, h=hsize);
        }
        // a little x-offset gives space to close the tap
        translate([0.2, 0, -gap]) cylinder(r=hole_r, h=hsize+2*gap);
    }
}


module body_outer() {
    open_box(x=odim_x, y=odim_y, z=body_z, wall=owall, base=owall);
}

module open_box(x, y, z, wall, base) {
    color("green") cube([x, y, base]); // floor
    cube([x, wall, z]);  // xz-wall 
    translate([0, y-wall, 0])
        cube([x, wall, z]);  // far xz-wall
    cube([wall, y, z]);  // yz-wall
    translate([x-wall, 0, 0])
        cube([wall, y, z]);  // far yz-wall
}
module body_dividers() {
    function accum(v) = len(v) > 1 ? [for (ndx=[0:len(v)-2]) [ndx, sumv(v,ndx)]] : [];
    function div_fact(vect, total, wall) = (total - wall *(len(vect)-1)) / vecsum(vect);
    for (div = accum(div_x)) {
        fact = div_fact(div_x, odim_x - 2*owall, iwall);
        offs = owall + div[0]*iwall + div[1]*fact;
        translate([offs,0,0]) cube([iwall, odim_y, div_height]);
    }
    for (div = accum(div_y)) {
        fact = div_fact(div_y, odim_y - 2*owall, iwall);
        offs = owall + div[0]*iwall + div[1]*fact;
        translate([0, offs, 0]) cube([odim_x, iwall, div_height]);
    }
}


