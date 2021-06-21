# sorceress 1.0

https://pypi.org/project/sorceress/1.0/

```
pip install sorceress==1.0
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

if gif= True, it will create a gif with output images
you may either use Von Kries chromatic adaptation or Fairchild (1990) detalits: ( https://colour.readthedocs.io/en/develop/generated/colour.chromatic_adaptation.html )

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

```
sorceress.sorcerer.dotill(600,600,hlinefreq=12,wlinefreq=12)
```
![chro](https://user-images.githubusercontent.com/54986652/117381508-e7394a00-aee4-11eb-803e-4b08f42e721f.png)


## 3- sorceress.sorcerer.realtimegrid()

```
sorceress.sorcerer.realtimegrid(realcolours=True)
```


perceive black and white real time frame as colorful

Inspiration: https://www.patreon.com/posts/color-grid-28734535


## 4- sorceress.sorcerer.addlines
inspired from Akiyoshi Kitaoka

```
addlines("inputimage.jpg",linecolour1=(0,255,0),linecolour2=(0,255,255),linecolour3=(255,0,0))

```
Add vertical lines to an image 

## 5- sorceress.sorcerer.addlinesAlpha

Same with "addlines" but this time; line colors are much more stable against the luminance change in the background image. 

```
addlinesAlpha("inputimage.jpg",linecolour1=(0,255,0),linecolour2=(0,255,255),linecolour3=(255,0,0))

```


## 6- sorceress.sorcerer.eyecolour

inspried from: https://michaelbach.de/ot/col-context/index.html

```
sorceress.sorcerer.eyecolour("angeyes.jpg")

```

after determine the roi(region of interest) you could use this optical illusion. 
![image](https://user-images.githubusercontent.com/54986652/122818547-0566d800-d2e2-11eb-9d67-94b35626b39f.png)

