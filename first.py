import cv2
import numpy as np
import stats as stats
from matplotlib import pyplot as plt

image =cv2.imread("img1/gojo1.jpeg")
img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray Scale Image",img)
plt.hist(img.ravel(),256,[0,256],color='y')
plt.title("histogram for the image")
plt.xlabel("intensity")
plt.ylabel("number of pixels")
#necessary features/values
mean = np.mean(img.ravel())
plt.axvline(mean,color='k',linestyle='dashed')
median1=np.median(img.ravel())
plt.axvline(median1,color='r',linestyle='dashed')
mode1=stats.mode(img.ravel())
plt.axvline(mode1,color='b',linestyle='dashed')
v=stats.variance(img.ravel())

print("the mean is",mean)
print("\nthe median is",median1)
print("\nthe mode is",mode1)
print("\nthe variance is",v)

#intensity transformation functions
def nthpower(im, gamma):
    invGamma =  gamma
    a = [((i / 255) ** invGamma) * 255 for i in range(256)]
    a = np.array(a, np.uint8)
    return cv2.LUT(im, a)

gam=nthpower(img,0.4)
cv2.imshow('intensity transformation',gam)



#histogram equalization
equ = cv2.equalizeHist(img)
res = np.hstack((img, equ))
cv2.imshow('image', res)

if mode1<median1:
    if median1<mean:
        print("\nThe data is Positively (Dark Image)")

if mean < median1:
    if median1 < mode1:
        print("\nThe data is Negatively (Bright Image)")

plt.show()

cv2.waitKey()