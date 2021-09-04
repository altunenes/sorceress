# sorceress 1.1
[![Build Status](https://app.travis-ci.com/emportent/sorceress.svg?branch=main)](https://app.travis-ci.com/emportent/sorceress) [![PyPI version](https://badge.fury.io/py/sorceress.svg)](https://badge.fury.io/py/sorceress)

https://pypi.org/project/sorceress/1.1/

```
pip install sorceress==1.1

```


```
import sorceress
```

sorceress is a python package for creating optical illusions in an easy way.

## Functions:

1- chromatic 
2- dotill    

3- realtimegrid 
4- addlines    

5- addlinesAlpha
6- eyecolour


## 1- sorceress.sorcerer.chromatic

```
sorceress.sorcerer.chromatic("yourimage.jpg","outputname",circle=True,method="CMCCAT2000",gif=False,duration=10000)

```

``` "yourimage.jpg" ``` = Source image. 

```"outputname" ```  = Your output name (You don't need to add extention (jpg,png etc.)

``` circle=True ``` = Adds a red dot in the middle of pic. 

if ```gif= True ```, it will create a gif with output images

```method``` you may either use Von Kries chromatic adaptation or Fairchild (1990) 

simple example:

focus on the red dot

![png_to_gif](https://user-images.githubusercontent.com/54986652/114435413-ca06a980-9bcc-11eb-831f-37730c77f4a9.gif)


image source: 
https://extension.unh.edu/blog/fall-good-time-plant-trees-and-shrubs


## 2- sorceress.sorcerer.dotill()

lateral inhibition: an old-fashion optical illusion.

Simple procedure that draws an old-fashion optical illusion.

Catch the black dots if you can!

```
dotill(hsize,wsize,hlinefreq=12,wlinefreq=12,dotcolor=(0,255,0),dotradius=5,horizontalcolor=(14, 75, 3),verticalcolor=(14, 75, 3),horizontalthickness=4,verticalthickness=4,verticallines=True,horizontallines=True):
```

`hsize` and `wsize` are dimensions of the image. `Hlinefreq` is the frequency of vertical lines and the `wlinefreq` is for the horizontal lines. `dotcolor` is the color of the dots. `dotradius` is the radius of the circles. `horizontalcolor` and `verticalcolor` points the colors of the lines. You may remove those lines with` verticallines=False,horizontallines=False` 

```
dotill(hsize,wsize,hlinefreq=12,wlinefreq=12,dotcolor=(0,255,0),dotradius=5,horizontalcolor=(14, 75, 3),verticalcolor=(14, 75, 3),horizontalthickness=4,verticalthickness=4,verticallines=True,horizontallines=True):
```

```
sorceress.sorcerer.dotill(600,600,hlinefreq=12,wlinefreq=12)
```

## 3- sorceress.sorcerer.realtimegrid()

```
sorceress.sorcerer.realtimegrid(realcolours=True)
```

perceive black and white real time (with webcam) frames as colorful

with `realcolours=False` code will not calculate the real colors of your frame.


Inspiration: https://www.patreon.com/posts/color-grid-28734535


## 4- sorceress.sorcerer.addlines
inspired from Akiyoshi Kitaoka

![asdddd](https://user-images.githubusercontent.com/54986652/130432273-c3b11961-484d-44a1-99a9-6821e46f9c10.png)

```
sorceress.sorcerer.addlines(img,outputname,linecolour1=(0,255,0),linecolour2=(0,255,255),linecolour3=(255,0,0))

```
Add vertical lines to an image 

`img` your input image like `"morgo.jpg"`
`outputname` desired output like `desired`
`linecolour1` `linecolour2` and `linecolour3` are point the colors of lines.
example usage:
`sorceress.sorcerer.addlines("vfor.jpg","mygrids",linecolour1=(150,5,5),linecolour2=(10,155,20),linecolour3=(0,15,15))
`
img

## 5- sorceress.sorcerer.addlinesAlpha

Same with "addlines" but this time; line colors are much more stable against the luminance change in the background image. 

```
addlinesAlpha(self,img,outputname,linecolour1=(0,255,0),linecolour2=(0,255,255),linecolour3=(255,0,0)
```


## 6- sorceress.sorcerer.eyecolour

inspried from: https://michaelbach.de/ot/col-context/index.html

```
sorceress.sorcerer.eyecolour("yourimage.jpg")

```

with this illusion, you perceive the black and white NumPy array as colorful (probably).  After you run this code, you need to select the iris manually then push the enter. I didn't want to use the iris detector since it slowing down the script. Just select smaller as much as possible.

example:

![image](https://user-images.githubusercontent.com/54986652/122818547-0566d800-d2e2-11eb-9d67-94b35626b39f.png)

