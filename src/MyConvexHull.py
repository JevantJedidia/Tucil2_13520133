import numpy as np

def bagiTitik(P,P1,P2,I): #Bagi kumpulan titik(P) pada indeks I menjadi 2 bagian berdasarkan garis P1P2
    indexKiriAtas = []
    indexKananBawah = []
    A = P[P1][0]*P[P2][1]
    B = P[P2][0]*P[P1][1]
    for i in I:
        if i != P1 and i != P2:
            #Cek determinan
            det = A + P[i][0]*P[P1][1] + P[P2][0]*P[i][1] - P[i][0]*P[P2][1] - B - P[P1][0]*P[i][1]
            if det > 0: #titik berada di atas atau di sebelah kiri dari garis P1P2
                indexKiriAtas.append(i)
            if det < 0: #titik berada di bawah atau di sebelah kanan dari garis P1P2
                indexKananBawah.append(i)
    return indexKiriAtas, indexKananBawah

def findFar(P,I,P1,P2): #Cari titik terjauh dari garis P1P2 
    distance = []
    numArray = np.array(P)
    A = np.linalg.norm(numArray[P2]-numArray[P1])
    for i in I: #Hitung jarak tiap titik
        d = np.linalg.norm(np.cross(numArray[P2]-numArray[P1],numArray[P1]-numArray[i]))/A
        distance.append(d)
    furthest = max(distance) #Cari jarak terjauh
    for i in range(len(distance)): #Cari indeks dari titik dengan jarak terjauh
        if distance[i] == furthest:
            loc = i
            break
    return I[loc]

def findHull(P,Pt,P1,P2): #Cari Convex Hull
    if len(Pt) == 0: #BASIS : kembalikan pasangan P1-P2 jika tidak ada titik lagi
        return [[P1,P2]]
    elif len(Pt) == 1: #BASIS : jika hanya ada satu titik (Pt), kembalikan pasangan P1-Pt dan Pt-P2
        return [[P1,Pt[0]],[Pt[0],P2]]
    else:
        C = []
        Pn = findFar(P,Pt,P1,P2) #Cari titik terjauh (Pn) dari garis P1-P2
        kiri1,kanan1 = bagiTitik(P,P1,Pn,Pt) #bagi sekumpulan titik berdasarkan garis P1-Pn
        kiri2,kanan2 = bagiTitik(P,Pn,P2,Pt) #bagi sekumpulan titik berdasarkan garis Pn-P2
        A = findHull(P,kiri1,P1,Pn) #Cari Convex Hull dari bagian yang dibagi garis P1-Pn
        B = findHull(P,kiri2,Pn,P2) #Cari Convex Hull dari bagian yang dibagi garis Pn-P2
        #Gabung hasil dari kedua pencarian convex hull
        for index in A:
            C.append(index)
        for index in B:
            C.append(index)
        return C

def ConvexHull(P): #Fungsi pencarian ConvexHull
    P1 = 0
    P2 = 0
    I = []
    for i in range(len(P)): #cari titik dengan absis terkecil dan terbesar
        if P[i][0] <= P[P1][0]:
            P1 = i
        if P[i][0] >= P[P2][0]:
            P2 = i
        I.append(i)
    hull = []
    #Bagi kumpulan titik jadi bagian atas dan bawah garis P1-P2
    kiriAtas, kananBawah = bagiTitik(P,P1,P2,I)
    A = findHull(P,kiriAtas,P1,P2) #Cari convex hull untuk bagian atas garis P1-P2
    B = findHull(P,kananBawah,P2,P1) #Cari convex hull untuk bagian bawah garis P1-P2
    #Gabung hasil convex hull
    for index in A:
        hull.append(index)
    for index in B:
        hull.append(index)
    return hull