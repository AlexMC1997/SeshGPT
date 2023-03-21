P = (0, 10)
V0 = (0, 0)

def do_phys(p, v0, dt, t0, t1, g):
    t = t0
    while t <= t1:
        print(f't = {t:.2f}: ({p[0] + v0[0]*t:8.3f}, {p[1] + v0[1]*t + 0.5 * (-g) * t**2:8.3f})')
        t += dt
do_phys(P, V0, 0.2, 0, 2, 10)
