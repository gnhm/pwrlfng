from numpy.polynomial import Polynomial
wc = [-216.05, 16.26, -0.002388645, -0.00113732, 7.0186E-6, -1.291E-8]
dc = [307.75076, 24.0900756, 0.1918759221, 0.0007391293, 0.000001093] 

p_wilks = Polynomial(wc)
p_dots = Polynomial(dc)

def wilks_coeff(bw):
    return 500./p_wilks(bw)

def dots_coeff(bw):
    return 500./p_dots(bw)

