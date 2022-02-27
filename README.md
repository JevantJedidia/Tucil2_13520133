# Pustaka *Convex Hull*

Program ini dibuat oleh:
Jevant Jedidia Augustine - 13520133

## Deskripsi Program

Program ini adalah tugas kecil mata kuliah IF2211. Program ini merupakan pustaka *MyConvexHull* dalam bahasa Python yang akan mencari *convex hull* dari kumpulan titik. Fungsi *ConvexHull* dari pustaka *MyConvexHull* akan menerima masukan berupa kumpulan titik dan mengembalikan pasangan-pasangan dari beberapa titik yang dimasukan. Pasangan-pasangan titik tersebut akan membentuk *convex hull* apabila dilakukan *plot*-ing pada pasangan titik tersebut.

## Requirement Program dan Instalasi *module/package*

-Python atau Python 3 sudah ter-*install* <br />
-Pustaka NumPy sudah ter-*install* <br />

Apabila ingin melakukan *plot*-ing terhadap titik yang dimasukan dan *convex hull*: <br />
-Pustaka Matplotlib sudah ter-*install* <br />

Apabila ingin menjalankan program main.py: <br />
-Pustaka scikit-learn sudah ter-*install*

## Cara Menggunakan Program

Untuk menggunakan pustaka *MyConvexHull*, pastikan pustaka tersebut sudah diunduh dan berada pada folder yang sama dengan kode program yang akan menggunakan pustaka tersebut.

Import ConvexHull dari *MyConvexHull*
``` python
from MyConvexHull import ConvexHull
```

Fungsi ConvexHull akan menerima masukan berupa *array of points*.<br />
Contoh masukan:<br />
```python
array = [[2,3],[5,4],[1,2],[9,3],[5,2],[4,1]]
```

Fungsi ConvexHull akan mengembalikan array-2D yang berisikan pasangan indeks dari *array of points* yang dimasukan.<br />
Contoh penggunaan fungsi: <br />
```python
hull = ConvexHull(array)
```

Bila dilakukan perintah print(array), maka hasil yang didapat adalah:<br />
```python
[[2, 0], [0, 1], [1, 3], [3, 5], [5, 2]]
```

Arti dari hasil yang didapat adalah:
```
[2,0] -> pasangan titik pada indeks 2 dan 0 array masukan, yaitu [1,2] dan [2,3]
[0,1] -> pasangan titik pada indeks 0 dan 1 array masukan, yaitu [2,3] dan [5,4]
[1,3] -> pasangan titik pada indeks 1 dan 3 array masukan, yaitu [5,4] dan [9,3]
dst
```

Apabila ingin melakukan *plot*-ing terhadap titik-titik yang dimasukkan beserta dengan *convex hull*-nya, *array of points* perlu diubah menjadi *array numpy*.
```python
import numpy as np

arrayAwal = [[2,3],[5,4],[1,2],[9,3],[5,2],[4,1]]
array = np.array(arrayAwal)
```
*Plot*-ing
```python
import matplotlib.pyplot as plt

plt.scatter(array[:,0],array[:,1])
for simplex in hull:
    plt.plot(array[simplex,0],array[simplex,1])
plt.show()
```
