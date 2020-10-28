import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

def findBug(orginal,bugimage):
    #finding the pixel difference
    diff = bugimage-orginal
    
    #finding the Co-ordinates of the Bug
    indices = np.where(diff!= [0])
    y=indices[0]
    x=indices[1]
    print("X1 :",x[0]," Y1 :",y[0])
    print("Xn :",x[-1]," Yn :",y[-1])

    #Plotting to compare 
    fig, axes = plt.subplots(nrows=1, ncols=3)

    axes[0].imshow(orginal)
    axes[0].set_title("Image")
    axes[0].set_xlabel("X")
    axes[0].set_ylabel("Y")
    axes[1].imshow(bugimage)
    axes[1].set_title("Image with Bug")
    axes[1].set_xlabel("X")
    axes[1].set_ylabel("Y")
    axes[2].imshow(diff)
    axes[2].set_title("Locating Bug")
    axes[2].set_xlabel("X")
    axes[2].set_ylabel("Y")

    fig.tight_layout()
    plt.show()


#Reading the Orginal image and Images with Bug
orginal = cv.imread("/Users/ayshazenabkenza/Desktop/Web_Analytics/Assignment4/Chickensclean.png")
bugimage1 = cv.imread("/Users/ayshazenabkenza/Desktop/Web_Analytics/Assignment4/Chickenswithbugexample.png")
bugimage2 = cv.imread("/Users/ayshazenabkenza/Desktop/Web_Analytics/Assignment4/bug2.png")
bugimage3 = cv.imread("/Users/ayshazenabkenza/Desktop/Web_Analytics/Assignment4/bug3.png")

#Calling the function to find the Co-ordinates of the Bug
#findBug(orginal,bugimage1)
#findBug(orginal,bugimage2)
findBug(orginal,bugimage3)
