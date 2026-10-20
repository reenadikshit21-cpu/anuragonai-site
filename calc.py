"""Back-of-envelope physics for the Roadster video. Every INPUT is a reported claim or a stated assumption (marked);
every OUTPUT is arithmetic. Run: python3 calc.py"""
from math import sqrt

g = 9.81; mph = 0.44704; atm = 101_325.0
print("== 1. what 0-60 mph in t seconds implies (average, ignoring rollout)")
for t in (1.0, 0.81, 0.67, 0.59, 0.55):
    a = 60 * mph / t
    print(f"  0-60 in {t:4.2f} s -> a = {a:5.1f} m/s^2 = {a/g:4.2f} g")

print("== 2. thrust alone: a = F/m   (F = 80 kN claimed; MASS NOT CONFIRMED -> two reported/estimated values)")
for m in (1700, 2350):
    print(f"  m = {m} kg: 80 kN -> {80_000/m:5.1f} m/s^2 = {80_000/m/g:3.1f} g")

print("== 3. why tyres alone cannot do it: friction limit a_max = mu*g*(1 + D/(m g))  (mu ASSUMED)")
for mu in (1.2, 1.6):
    print(f"  mu={mu}: no downforce -> {mu:.1f} g max, even with all 4 wheels driven")

print("== 4. motor power: P = F v, so F = P/v  (P = 1 MW claimed)")
for v_mph in (10, 30, 60):
    v = v_mph * mph
    print(f"  at {v_mph:2d} mph: F = {1e6/v/1000:6.1f} kN (power-limited; at low speed traction, not power, is the limit)")

print("== 5. gas supply vs 80 kN:  mdot = F / ve")
gam, R, T = 1.4, 296.8, 293.0           # nitrogen, room temperature (ASSUMED)
ve_ideal = sqrt(2*gam/(gam-1)*R*T)       # full expansion into vacuum = upper bound
print(f"  nitrogen cold-gas exit speed upper bound ~ {ve_ideal:4.0f} m/s (realistic ~600-700)")
for ve in (600, 700, ve_ideal):
    md = 80_000/ve
    for mass_kg, label in ((250, "600 L tank, ~250 kg (reported)"), (100, "200 L Thrust tank, ~100 kg (scaled 250*200/600, ASSUMED)")):
        print(f"  ve={ve:4.0f}: mdot={md:5.0f} kg/s -> {label}: empty in {mass_kg/md:4.1f} s")
print("  reported burn: ~5-6 s. To burn 250 kg in 6 s needs mdot=%.0f kg/s -> at 80 kN that is ve=%.0f m/s (> any cold gas but hydrogen/helium)" % (250/6, 80_000/(250/6)))
print("  => 80 kN is a PEAK figure; sustained thrust is lower, or the burn is pulsed. (Open question for the video.)")
print("  at ve=700 m/s, 250 kg over 6 s gives average thrust = %.0f kN" % (250/6*700/1000))

print("== 6. fan downforce: D = dp * A  (underbody sealed area A ASSUMED 2.0 m^2)")
A = 2.0
for m in (1700, 2350):
    need = m * g
    print(f"  to hold m={m} kg upside down: D >= {need/1000:4.1f} kN -> dp >= {need/A/1000:4.1f} kPa = {need/A/atm*100:3.1f}% of one atmosphere")
print(f"  hard physics ceiling: dp can never exceed ~1 atm -> D <= {atm*A/1000:3.0f} kN = {atm*A/g/1000:3.1f} tonnes-force at A=2 m^2")
for d_kgf in (1000, 2000, 4700):
    print(f"  D = {d_kgf} kgf ({d_kgf*g/1000:4.1f} kN) -> dp = {d_kgf*g/A/1000:4.1f} kPa  -> extra grip at mu=1.5: {1.5*d_kgf*g/1000:5.1f} kN")
print("== 7. compressed air energy sanity: 600 L at 690 bar (10,000 psi) stored energy ~ p*V*ln(p/p0)")
from math import log
p, V = 690e5, 0.6
print(f"  isothermal E = {p*V*log(p/atm)/1e6:4.0f} MJ  (= {p*V*log(p/atm)/3.6e6:4.1f} kWh); at 6 s that is {p*V*log(p/atm)/6/1e6:4.0f} MW of gas power (vs 80 kN * 700 m/s / 2 = {80e3*700/2/1e6:4.0f} MW jet power)")

print("== 8. flight: hover needs T > m g;  attitude: tau = r x F, alpha = tau / I  (m, lever arm, inertia ASSUMED)")
for m in (1700, 2350):
    T = m*g
    md = T/700
    print(f"  m={m} kg: hover thrust >= {T/1000:4.1f} kN = {T/80_000*100:3.0f}% of 80 kN; mdot at ve=700 -> {md:4.1f} kg/s -> 250 kg lasts {250/md:4.1f} s of pure hover")
m, r, F = 2000, 1.0, 2000.0     # one thruster pushing 2 kN at 1 m off the centre of mass; I ~ m*k^2, k=1.2 m
I = m * 1.2**2
alpha = r*F/I
from math import pi
print(f"  one 2 kN thruster 1 m off-centre: tau={r*F/1000:3.1f} kN*m, I~{I:5.0f} kg*m^2 -> alpha={alpha:4.2f} rad/s^2 -> a half-turn (180 deg) takes {sqrt(2*pi/alpha):3.1f} s from rest")
