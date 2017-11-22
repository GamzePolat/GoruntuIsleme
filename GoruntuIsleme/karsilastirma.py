import matplotlib.pyplot as plt
array=["a1.jpg","a2.jpg","a3.jpg","a4.jpg","a5.jpg","b1.jpg","b2.jpg","b3.jpg","b4.jpg","b5.jpg","c1.jpg","c2.jpg","c3.jpg","c4.jpg","c5.jpg","d1.jpg","d2.jpg","d3.jpg","d4.jpg","d5.jpg","e1.jpg","e2.jpg","e3.jpg","e4.jpg","e5.jpg"]
for i in range(25):
    img1 = plt.imread(array[i])
    img1.ndim
    img1.shape
    img2 = img1[1:250:2, 1:250:2]
    img2.ndim
    img2.shape
    img3 = np.zeros(img2.shape[0:2])
    img3.shape
    threshold = 1
    for k in range(img2.shape[0]):
        for j in range(img2.shape[1]):
            n = img2[k,j,0]/3 + img2[k,j,1]/3 + img2[k,j,2]/3
            img3[k,j] = n
            if n > threshold:
                img4[k,j] = 0
            else:
                img4[k,j] = 255
    plt.subplot(1,4,1), plt.imshow(img4,plt.cm.binary)
plt.show()
