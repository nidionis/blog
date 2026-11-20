// Manson piston/chamber sketch (parametric, illustrative).
// Open with: openscad engines/manson/scad/piston.scad
//
// Configured from env via generated include (run: python3 tools/calc.py --sync/--update)
include <env.scad>

// ---- sketch geometry (edit for this sketch) ----
inner_r = 70;              // mm, chamber radius of the sketch
chamber_l = 70;            // mm, chamber height used for the power report
pressure_ratio = 1;        // 1 = atmospheric; >1 = sealed variant (sketch lever)
$fn = 100;                 // resolution
CHINK_QUOT = 13;           // geometric unit ratio

// ---- parameters linked to env (generated in env.scad) ----
eta = env_eta;
delta_t_k = env_delta_t_k;
frequency_hz = env_frequency_hz;
rho_air = env_rho_air;
cp_air = env_cp_air;
fill_ratio = env_fill_ratio;
aluminium_density = env_aluminium_density;

function sketch_chamber_l(r_mm, h_mm) = PI * r_mm * r_mm * h_mm / 1e6;
function sketch_power_w(eta, rho, f, v_a_l, cp, dt, rp) =
    eta * rho * f * (v_a_l / 1000) * cp * dt * rp;

v_c_l = sketch_chamber_l(inner_r, chamber_l);  // this sketch, one chamber
// x1 -> x2 aluminium equivalent volume chambre (and melting it)
//  as production cost is 
// considered a fair first series target
// expecting it can include quickly 
// salaries, funding back, and a motor should
// "cost" 1 year of salary 
v_a_l = v_c_l / 2;                             // displacer rule -> air volume ~ chambre / 2
p_w = sketch_power_w(eta, rho_air, frequency_hz, v_a_l, cp_air, delta_t_k, pressure_ratio);
m_al_kg = (v_c_l / 1000) * fill_ratio * aluminium_density;

echo(str("Sketch chamber V_c = ", v_c_l, " L; working air V_a = ", v_a_l, " L"));
echo(str("First-order power = ", p_w, " W = ", p_w / 735.5, " hp; pressure ratio = ", pressure_ratio));
echo(str("Cast chamber mass at ", fill_ratio * 100, " % fill = ", m_al_kg, " kg"));
echo(str("Env can: ", env_can_mass_kg * 1000, " g, ", env_can_price_eur, " EUR (low ", env_can_price_eur_low, " EUR, light ", env_can_mass_kg_light * 1000, " g)"));

// unité geometrique
chink = inner_r * 2 / CHINK_QUOT;

// we suppose a chink as a fair range of thickness too
outer_r = inner_r + chink;

// Piston specs
head_r = inner_r;
head_l = 2 * chink;
stroke = head_l;

rod_r = 2 * chink;

// piston is a superposition of pipes
module pipe(R, r, L) {
    difference() {
        cylinder(h = L, r = R);
        translate([0, 0, -1])
        cylinder(h = L + 2, r = r);
    }
}

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
