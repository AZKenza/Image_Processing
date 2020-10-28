Finding Bug
================

#### An algorithm that find the coordinate of the bug inside the picture.

##### Required Libraries

``` python
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
```

##### Algorithm to Find the Bug

``` python
def findBug(orginal,bugimage):
    #finding the pixel difference
    diff = bugimage-orginal
    
    #finding the Co-ordinates of the Bug
    indices = np.where(diff!= [0])
    y=indices[0]
    x=indices[1]
    print("X1 :",x[0]," Y1 :",y[0])
    print("Xn :",x[-1],"Xn :",y[-1])

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
```

##### Input and calling the Function findBug

``` python
#Reading the Orginal image and Images with Bug
orginal = cv.imread("/Users/ayshazenabkenza/Desktop/Web_Analytics/Image_Processing/Chickensclean.png")
bugimage1 = cv.imread("/Users/ayshazenabkenza/Desktop/Web_Analytics/Image_Processing/Chickenswithbugexample.png")
bugimage2 = cv.imread("/Users/ayshazenabkenza/Desktop/Web_Analytics/Image_Processing/bug2.png")
bugimage3 = cv.imread("/Users/ayshazenabkenza/Desktop/Web_Analytics/Image_Processing/bug3.png")

#Calling the function to find the Co-ordinates of the Bug
findBug(orginal,bugimage1)
```

    ## X1 : 1730  Y1 : 1295
    ## Xn : 2169 Xn : 1654

<img src="Finding_Bug_files/figure-gfm/unnamed-chunk-3-1.png" width="672" />

``` python
findBug(orginal,bugimage2)
```

    ## X1 : 3340  Y1 : 230
    ## Xn : 3780 Xn : 587

<img src="Finding_Bug_files/figure-gfm/unnamed-chunk-4-1.png" width="672" />

``` python
findBug(orginal,bugimage3)
```

    ## X1 : 183  Y1 : 268
    ## Xn : 623 Xn : 625

<img src="Finding_Bug_files/figure-gfm/unnamed-chunk-5-1.png" width="672" />
