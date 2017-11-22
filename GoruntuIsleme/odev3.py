internal_mask_1=[[1,0],[0,0]]
internal_mask_2=[[0,1],[0,0]]
internal_mask_3=[[0,0],[1,0]]
internal_mask_4=[[0,0],[0,1]]
external_mask_1=[[0,1],[1,0]]
external_mask_2=[[1,0],[1,1]]
external_mask_3=[[1,1],[0,1]]
external_mask_4=[[1,0],[1,0]]
internal_mask_1=[internal_mask_1,internal_mask_2,internal_mask_3,internal_mask_4]
external_mask_1=[external_mask_1,external_mask_2,external_mask_3,external_mask_4]
import numpy as np
import matplotlib.pyplot as plt
size=30
img_1=plt.imread("T.jpg")
img_1
plt.imshow(img_1,cmap='Greys',interpolation='nearest')
plt.imshow
def count_mask(image,mask):
    counter=0
    m,n=image.shape
    for i in range(m-1):
        for j in range(n-1):
            if (image[i,j] == mask[0][0]):
                a=True
            if (image[i,j+1] == mask[0][1]):
                b=True
            if (image[i+1,j] == mask[1][0]):
                c=True
            if (image[i+1,j+1] == mask[1][1]):
                d=True
                if(a and b and c and d):
                    counter=counter+1
    return counter
def count_internal_mask(image):
        counter_internal=0
        for mask in internal_mask_1:
            counter_internal=counter_internal+count_mask(image,mask)
        return counter_internal
def count_external_mask(image):
        counter_external=0
        for mask in external_mask_1:
            counter_external=counter_external+count_mask(image,mask)
        return counter_external
c1=count_internal_mask(img_1)
c2=count_external_mask(img_1)
c1,c2
c1-c2/4
