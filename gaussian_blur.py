from skimage import io
import numpy as np
import matplotlib.pyplot as plt

#wczytywanie obrazu i informacji o nim
img = np.array(io.imread('test.jpg'))
hight, width, color = np.shape(img)

newImg = np.zeros((hight, width, color))#miejsce na nowy obraz

#przygotowanie filtru
filter = np.array([[1, 4 , 7 , 4, 1], [4, 16, 26, 16, 4], [7, 26, 41 , 26 ,7], [4, 26 , 16 ,26, 4], [1, 4, 7, 4, 1]])
#filter = np.array([[-1, 1, 1], [-1, -2, 1], [-1, 1, 1]])
above_ranage, _ = np.shape(filter)

tmp_filter = filter.flatten()
norm = 0
for i in tmp_filter:
    norm += i

range = int((above_ranage - 1) / 2)
margin = range

#filtrowanie środka obrazu
i = 0
while i < hight:
    j = 0
    while j < width:
        k = 0
        while k < color:
            if i > margin and i < hight - margin and j > margin and j < width - margin:
                imgSum = 0
                l = (-1) * range
                lf = 0
                while l <= range:
                    m = (-1) * range
                    mf = 0
                    while m <= range:
                        # print(l + i, m + j)
                        imgSum += img[i + l, j + m, k] * filter[lf, mf]
                        m += 1
                        mf += 1
                    l += 1
                    lf += 1
                if norm > 0:
                    newImg[i, j, k] = imgSum / norm
                else:
                    newImg[i, j, k] = imgSum

                if newImg[i, j, k] < 0:
                    newImg[i, j, k] = 0
                elif newImg[i, j, k] > 255:
                    newImg[i, j, k] = 255
            k += 1
        j += 1
    i += 1

#kopiowanie pikseli na margines
i = 0
while i < hight:
    j = 0
    while j < width:
        k = 0
        while k < color:
            if i <= margin and j <= margin:
                newImg[i, j, k] = newImg[i + margin + 1, j + margin + 1, k]
            elif i <= margin and j >= width - margin:
                newImg[i, j, k] = newImg[i + margin + 1, j - margin - 1, k]
            elif i >= hight - margin and j <= margin:
                newImg[i, j, k] = newImg[i - margin - 1, j + margin + 1, k]
            elif i >= hight - margin and j >= width - margin:
                newImg[i, j, k] = newImg[i - margin - 1, j - margin - 1, k]
            else:
                if i <= margin:
                    newImg[i, j, k] = newImg[i + margin + 1, j, k]
                elif i >= hight - margin:
                    newImg[i, j, k] = newImg[i - margin - 1, j, k]
                elif j <= margin:
                    newImg[i, j, k] = newImg[i, j + margin + 1, k]
                elif j >= width - margin:
                    newImg[i, j, k] = newImg[i, j - margin - 1, k]
            k += 1
        j += 1
    i += 1

#wyświetlanie wyniku
newImg = newImg.astype(int)
plt.figure(1)
plt.imshow(newImg)
plt.title("Po filtracji")

plt.figure(2)
plt.imshow(img)
plt.title("Oryginalny")
plt.show()