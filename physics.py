import matplotlib.pyplot as pt
P = (0, 10)
V0 = (0, 0)

def do_phys(p, v0, dt, t0, t1, g):
    t = t0
    tab = []
    while t <= t1:
        pos = (p[0] + v0[0]*t, p[1] + v0[1]*t + 0.5 * (-g) * t**2)
        print(f'({t:.2f}, {p[0] + v0[0]*t:7.3f}, {p[1] + v0[1]*t + 0.5 * (-g) * t**2:7.3f})')
        tab.append(pos)
        t += dt
    return tab
tab = do_phys(P, V0, 0.2, 0, 2, 10)
tab = list(zip(*tab))
pt.plot(tab[0], tab[1], '-r')
