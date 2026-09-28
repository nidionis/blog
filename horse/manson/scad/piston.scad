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
gap = 0.1;
chink = inner_r * 2 /13 ;

// Piston specs
piston_r = inner_r - gap; // Slight clearance
piston_h = 2 * chink;
axe = 2 * chink + 2;
stroke = piston_h;
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

module manson_13_base(chink) {
	head_r = 13 * chink;
	head_h = 2 * chink;
	neck_l = 1.5 * chink;
	neck_r = 1.5 * chink;
	rod_l = 5.5 * chink;
	rod_r = 2 * chink;

	
    // The head: a short, wide pipe
    translate([0, 0, 0])
        pipe(head_r, chink / 2, head_h);

    // The neck: a narrower, longer pipe stacked on top of the head
    translate([0, 0, head_h])
        pipe(neck_r, chink / 2, neck_l);

    // The rod: the narrowest and longest pipe stacked on top of the neck
    translate([0, 0, head_h + neck_l])
        pipe(rod_r, chink / 2, rod_l);
}

// -----------------------------------------------------------------------------
// Scene Assembly
// -----------------------------------------------------------------------------

// Color: Semi-transparent Grey for cylinder
color([0.9, 0.6, 0.1, 0.9]);
//half_open_cylinder(cylinder_height, outer_r, inner_r);
chink = inner_r / 12;
manson_13_base(chink);

//pipe(piston_r, 2 * chink, piston_h);


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
