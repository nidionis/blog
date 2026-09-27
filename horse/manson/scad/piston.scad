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

// Piston specs
piston_r = inner_r - 0.5; // Slight clearance
piston_h = 20;
piston_y = 10;

// -----------------------------------------------------------------------------
// Module: Half-Open Cylinder with Offset Wall
// -----------------------------------------------------------------------------
module half_open_cylinder(height, outer_r, inner_r) {
    
    // Calculate the offset based on thickness
    // We translate the inner cylinder by 'thickness' along the X axis
    // before subtracting it. This creates a wall that is thick on one side
    // and thin (or open) on the other.
    translate_z = thickness; 

    difference() {
        // 1. The Solid Outer Cylinder
        cylinder(h = height, r = outer_r, center = true);
        
        // 2. The Inner Volume to Remove (Translated)
        // By moving the cutter, we leave material only where the outer cylinder
        // exists but the inner cylinder does not.
        translate([0, 0, translate_z])
        cylinder(h = height + 1, r = inner_r, center = true);
        
    }
}

// -----------------------------------------------------------------------------
// Scene Assembly
// -----------------------------------------------------------------------------

// Color: Semi-transparent Grey for cylinder
color([0.9, 0.6, 0.1, 0.9])
half_open_cylinder(cylinder_height, outer_r, inner_r);

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
