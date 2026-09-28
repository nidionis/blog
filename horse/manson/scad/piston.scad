// -----------------------------------------------------------------------------
// Module: pipe
// -----------------------------------------------------------------------------
module pipe(R, r, L) {
    difference() {
        cylinder(h = L, r = R);
        translate([0, 0, -1])
        cylinder(h = L + 2, r = r);
    }
}

outer_r = 145;
inner_r = 140;

thickness = outer_r - inner_r; 
//gap = 0.1;
chink = inner_r * 2 /13 ;

// Piston specs
head_r = inner_r; // - gap; // Slight clearance
head_l = 2 * chink;
stroke = head_l;
axe = 4 * chink; // roulement a bille horisontale (2) + 1 unité de chaque coté
bielle_l = stroke * 2 + axe;

//cylinder_height = 60;

// -----------------------------------------------------------------------------
// Module: Half-Open Cylinder with Offset Wall
// -----------------------------------------------------------------------------
module half_open_cylinder(height, outer_r, inner_r) {
    translate_z = thickness; 
    difference() {
        cylinder(h = height, r = outer_r);
        translate([0, 0, translate_z]);
        cylinder(h = height, r = inner_r);
        
    }
}


// Base module defining dimensions relative to chink
module manson_13_base(chink) {
    head_r = 13 * chink;	
    head_l = 2 * chink;
    rod_l_head = (2 - 0.5) * chink;		
    neck_l = 2 * chink;
    neck_r = 1.5 * chink;
    rod_l_tail = 4 * chink;
    rod_r = 2 * chink;

    translate([0, 0, 0])
    pipe(head_r, chink, head_l);
    translate([0, 0, head_l])
    pipe(rod_r, chink, rod_l_head);
    translate([0, 0, head_l + rod_l_head])
    pipe(neck_r, chink, rod_l_tail);
    rod_z_start = head_l + rod_l_head + neck_l;
    translate([0, 0, rod_z_start])
    pipe(rod_r, chink, rod_l_tail);

    //rotate([90, 0, 0])
    //cylinder(h = 10 * chink, r = chink, center = true);
}



// -----------------------------------------------------------------------------
// Scene Assembly
// -----------------------------------------------------------------------------

// Color: Semi-transparent Grey for cylinder
color([0.9, 0.6, 0.1, 0.9]);
//half_open_cylinder(cylinder_height, outer_r, inner_r);
manson_13_base(chink);



//// Color: Red for Piston
//color([0.8, 0.2, 0.2, 1.0])
//translate([0, piston_y, 0])
//cylinder(h = piston_h, r = piston_r, center = true);
//
//// Visual Aid: Show the offset axis
//// Draws a thin line where the inner cylinder was centered before removal
//color([0, 0, 0, 0.3])
//translate([thickness, 0, -cylinder_height/2])
//cylinder(h = cylinder_height, r = 0.2, center = true);
