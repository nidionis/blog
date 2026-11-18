// open this file using
// openscad piston.scad 

// Here is a draw of a potential
// Manson thermic engine
// Designed by less than an hundrued of command lines
// x_l = lenght
// x_r = radius
$fn = 100; //resolution
CHINK_QUOT = 13; // learning Chink can be asian-rascist...

inner_r = 70;

// unité geometrique
chink = inner_r * 2 / CHINK_QUOT ;
// Le diametre est alors egal a CHINK_QUOT unités/blocs

// we suppose a chink as a fair range of thickness too
outer_r = inner_r + chink;

// Piston specs
head_r = inner_r; // - gap;
// or gap added to external cylindre
head_l = 2 * chink;
stroke = head_l;

rod_r = 2 * chink;
// 1 chink pipe by definition
// 0.5 chink thick at the neck

// piston is a supperposition of 3 pipes
module pipe(R, r, L) {
    difference() {
        cylinder(h = L, r = R);
        translate([0, 0, -1])
        cylinder(h = L + 2, r = r);
    }
}

// Base module defining dimensions relative to chink
// A rendre "poreux"
module manson_13_base_piston(chink) {
    head_r = CHINK_QUOT * chink / 2;
    head_l = 2 * chink;
    rod_l_head = (2 - 0.25) * chink;
    neck_l = 2 * chink;
    neck_r = 1.5 * chink;
    rod_l_tail = 4 * chink;

    translate([0, 0, 0])
        pipe(head_r, chink, head_l);
    translate([0, 0, head_l])
        pipe(rod_r, chink, rod_l_head);
    translate([0, 0, head_l + rod_l_head])
        pipe(neck_r, chink, neck_l);
    rod_z_start = head_l + rod_l_head + neck_l;
    translate([0, 0, rod_z_start])
        difference() {
            pipe(rod_r, chink, rod_l_tail);
            translate([0, 0, chink * 2])
                rotate([90, 0, 0])
                    cylinder(r = chink, h = 5 * chink, center = true);
	}
}

gap = 0.1;
gauge = chink;
cyltot_l = head_l + stroke + gauge * 2.5;

CYLIND_COLOR = [0.9, 0.6, 0.1, 0.9];
PISTON_COLOR = [0.1, 0.1, 0.9, 0.9];

color(PISTON_COLOR) {
    translate([0, 0, gauge * 1.25])
	    manson_13_base_piston(chink);
}

module chambre(inner_h, inner_r) {
    difference() {
	difference() {
		cylinder(h = cyltot_l, r = outer_r);
		translate([0, 0, gauge]) {
			cylinder(h = cyltot_l, r = rod_r);
		}
	}
	translate([0, 0, gauge]) {
		cylinder(h = cyltot_l - 2*gauge, r = inner_r + gap);
	}
    }
}

color(CYLIND_COLOR) {
    chambre(4*chink, inner_r + gap);
}

//// The system is composed of 2 half cylindres
//// composing one close "perfored" cylinders
//module half_open_cylinder(height, outer_r, inner_r) {
//    translate_z = outer_r - inner_r; 
//    difference() {
//        cylinder(h = height, r = outer_r);
//        translate([0, 0, translate_z])
//		cylinder(h = height, r = inner_r);
//    }
//}
