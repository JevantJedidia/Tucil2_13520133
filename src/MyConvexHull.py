import numpy as np
import matplotlib.pyplot as plt

def bagiTitik(P,P1,P2,I):
    indexKiriAtas = []
    indexKananBawah = []
    A = P[P1][0]*P[P2][1]
    B = P[P2][0]*P[P1][1]
    for i in I:
        det = A + P[i][0]*P[P1][1] + P[P2][0]*P[i][1] - P[i][0]*P[P2][1] - B - P[P1][0]*P[i][1]
        if det > 0:
            indexKiriAtas.append(i)
        if det < 0:
            indexKananBawah.append(i)
    return indexKiriAtas, indexKananBawah

def findFar(P,I,P1,P2):
    distance = []
    numArray = np.array(P)
    for i in I:
        d = np.linalg.norm(np.cross(numArray[P2]-numArray[P1],numArray[P1]-numArray[i]))/np.linalg.norm(numArray[P2]-numArray[P1])
        distance.append(d)

    furthest = max(distance)
    for i in range(len(distance)):
        if distance[i] == furthest:
            loc = i
            break
    return I[loc]

def findHull(P,Pt,P1,P2):
    if len(Pt) == 0:
        return [[P1,P2]]
    elif len(Pt) == 1:
        return [[P1,Pt[0]],[Pt[0],P2]]
    else:
        C = []
        Pn = findFar(P,Pt,P1,P2)
        kiri1,kanan1 = bagiTitik(P,P1,Pn,Pt)
        kiri2,kanan2 = bagiTitik(P,Pn,P2,Pt)
        A = findHull(P,kiri1,P1,Pn)
        B = findHull(P,kiri2,Pn,P2)
        for index in A:
            C.append(index)
        for index in B:
            C.append(index)
        return C

def ConvexHull(P):
    P1 = 0
    P2 = 0
    I = []
    for i in range(len(P)):
        if P[i][0] <= P[P1][0]:
            P1 = i
        if P[i][0] >= P[P2][0]:
            P2 = i
        I.append(i)
    hull = []
    kiriAtas, kananBawah = bagiTitik(P,P1,P2,I)
    A = findHull(P,kiriAtas,P1,P2)
    B = findHull(P,kananBawah,P2,P1)
    for index in A:
        hull.append(index)
    for index in B:
        hull.append(index)
    return hull
'''
plt.scatter(P[:,0], P[:,1], label="data.target_names[i]")
for simplex in hullRaw: #plot convex hull
    plt.plot(P[simplex, 0], P[simplex, 1])
plt.show()
'''