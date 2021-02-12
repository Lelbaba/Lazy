import cmath as c,math as mt,numpy as np
from math import degrees,radians,pi
from cmath import polar,rect
from numpy import matrix as mat
def par(li):
    ans = 0
    for i in li:
        ans+=1/i
    ans=1/ans
    return round(ans.real,3)+round(ans.imag,3)*1j
def srs(li):
    ans = 0.0
    for i in li:
        ans+=i
    return round(ans.real,3)+1j*round(ans.imag,3)
def vdiv(v,li,r):
    i = v/srs(li)
    if r!=0:
        ans = i*r
        return round(ans,3)
    ans = []
    for j in li:
        ans.append(round((i*j).real,3)+round((i*j).imag,3) )
    return ans

def cdiv(i,li,r):
    v = i*par(li)
    if r!=0:
        ans = v/r
        return round(ans.real,3)+1j*round(ans.imag,3)
    ans = []
    for k in li:
        ans.append(round((v/k).real,3) + 1j*round((v/k).imag),3)
    return ans
def rec(r,t):
    t =radians(t)
    return round(rect(r,t).real,3)+1j*round(rect(r,t).imag,3)
def pol(x):
    return round(abs(x),3),round(degrees(c.phase(x)),3)
def solve(eqns):
    eqn = []
    ct = []
    for i in eqns:
        eqn.append(i[0])
        a = [i[1]]
        ct.append(a)
    eqn = mat(eqn)
    ct = mat(ct)
    eqn= np.linalg.inv((eqn))
    ans = eqn*ct
    an = []
    for i in ans:
        an.append(round(complex(i[0]).real,3) +1j*round(complex(i[0]).imag,3))
    return an
def IZ(l,w):
    return 1j*round(w*l,3)
def CZ(c,w):
    return -1j*round(1/(c*w),3)
def DY(ra,rb,rc):
    s = ra+rb+rc
    r1 = rb*rc/s
    r2 = ra*rc/s 
    r3 = ra*rb/s
    return round(r1.real,3)+1j*round(r1.imag,3),round(r2.real,3)+1j*round(r2.imag,3),round(r3.real,3)+1j*round(r3.imag,3)
def YD(ra,rb,rc):
    s = ra*rb+rc*rb+ra*rc
    r1 = s/ra
    r2 = s/rb 
    r3 = s/rc
    return round(ra.real,3)+1j*round(ra.imag,3),round(rb.real,3)+1j*round(rb.imag,3),round(rc.real,3)+1j*round(rc.imag,3)

