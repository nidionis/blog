// -----------------------------------------------------------------------------
// Simplified Thermal Engine: Offset Wall Logic
// Vocabulary: English
// -----------------------------------------------------------------------------

// --- Parameters (mm) ---
cylinder_height = 60;
outer_r = 15;
inner_r = 12;

// Calculate thickness explicitly as requested
thickness = outer_r - inner_r; 
gap = 0.5;

// Piston specs
piston_r = inner_r - gap; // Slight clearance
piston_h = 20;
piston_y = 10;

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

// -----------------------------------------------------------------------------
// Scene Assembly
// -----------------------------------------------------------------------------

// Color: Semi-transparent Grey for cylinder
color([0.9, 0.6, 0.1, 0.9]);
//half_open_cylinder(cylinder_height, outer_r, inner_r);
chink = inner_r / 12;

pipe(piston_r, 2 * chink, piston_h);

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
