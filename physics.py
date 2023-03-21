P = (10, 10)
V0 = (3, 1)

def do_phys(p, v0, dt, t0, t1):
    t = t0
    while t <= t1:
        print(f'({p[0] + v0[0]*t}, {p[1] + v0[1]*t + 0.5 * (-9.81) * t**2})')
        t += dt
do_phys(P, V0, 1.34, 0, 1.34)
