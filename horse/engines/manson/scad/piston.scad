// open this file using
// openscad piston.scad

// Here is a draw of a potential
// Manson thermic engine
// Designed by less than an hundrued of command lines
// x_l = lenght
// x_r = radius
$fn = 100; //resolution
CHINK_QUOT = 13; // learning Chink can be asian-rascist...

// ---- soft-coded levers: edit these, not the geometry ----
inner_r = 70;              // mm, chamber radius of the sketch
chamber_l = 70;            // mm, chamber height used for the power report
eta = 0.05;                // overall efficiency (5 % pessimistic baseline)
delta_t_k = 180;           // K, hot source minus ambient
frequency_hz = 2;          // Hz, cycle rate
rho_air = 1.2;             // kg/m3 at 20 C, atmospheric
cp_air = 1005;             // J/(kg K)
pressure_ratio = 1;        // 1 = atmospheric; >1 = sealed variant
fill_ratio = 0.66;         // casting fill used for the mass estimate
aluminium_density = 2700;  // kg/m3

function sketch_chamber_l(r_mm, h_mm) = PI * r_mm * r_mm * h_mm / 1e6;
function sketch_power_w(eta, rho, f, v_a_l, cp, dt, rp) =
    eta * rho * f * (v_a_l / 1000) * cp * dt * rp;

v_c_l = sketch_chamber_l(inner_r, chamber_l);  // this sketch, one chamber
v_a_l = v_c_l / 2;                             // displacer rule
p_w = sketch_power_w(eta, rho_air, frequency_hz, v_a_l, cp_air, delta_t_k, pressure_ratio);
m_al_kg = (v_c_l / 1000) * fill_ratio * aluminium_density;

echo(str("Sketch chamber V_c = ", v_c_l, " L; working air V_a = ", v_a_l, " L"));
echo(str("First-order power = ", p_w, " W = ", p_w / 735.5, " hp; pressure ratio = ", pressure_ratio));
echo(str("Cast chamber mass at ", fill_ratio * 100, " % fill = ", m_al_kg, " kg"));

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
// chamber_l is a soft-coded lever; keep the piston/rod stack fitting below it
cyltot_l = max(chamber_l, head_l + stroke + gauge * 2.5);

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
