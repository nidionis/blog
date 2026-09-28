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
    pipe(neck_r, chink, neck_l);
    rod_z_start = head_l + rod_l_head + neck_l;
    translate([0, 0, rod_z_start])
    pipe(rod_r, chink, rod_l_tail);
}

// Module pour l'axe perpendiculaire
module cylinder_axis(chink) {
    axis_r = chink; // Rayon = chink (Diamètre = 2 * chink)
    axis_l = 2 * chink; // Longueur de l'axe
    
    // Calcul de la position Z demandée
    // Note: rod_z_start doit être recalculé ici car il est local au module base
    head_l = 2 * chink;
    rod_l_head = (2 - 0.5) * chink;
    neck_l = 2 * chink;
    rod_z_start = head_l + rod_l_head + neck_l;
    
    translate([0, 0, rod_z_start + chink])
    rotate([90, 0, 0]) // Rotation pour être perpendiculaire (aligné sur Y)
    cylinder(r=axis_r, h=axis_l, center=true); // center=true pour centrer sur le point de translation
}

// -----------------------------------------------------------------------------
// Scene Assembly
// -----------------------------------------------------------------------------

// Color: Semi-transparent Grey for cylinder
color([0.9, 0.6, 0.1, 0.9]) {
    manson_13_base(1); // Exemple avec chink = 1
    //cylinder_axis(1);
}
