### API Reference

This page gives an overview of all sorceress functions and methods.

+[chromatic](#chromatic)

+[dotill](#dotill)

+[realtimegrid](#realtimegrid)

+[dolboeuf](#dolboeuf)

+[kanizsa](#kanizsa)

+[dakinPex](#dakinPex)

+[bruno](#bruno)

+[ccob](#ccob)

+[ponzol](#ponzol)

+[eyecolour](#eyecolour)

+[tAki2001](#tAki2001)

+[addlines](#addlines)

+[cafeWall](#cafeWall)

+[ebbinghaus](#ebbinghaus)

+[whiteill](#whiteill)

+[enigma](#enigma)

+[blackhole](#blackhole)

+[colorgrids](#colorgrids)

+[munker](#munker)

+[munker2](#munker2)

+[pareidolia](#pareidolia)

+[grids2](#grids2)

+[spirals](#spirals)

+[negate_image](#negate_image)

***chromatic***<a name="chromatic"></a>

This function process image to generate optical illusion about chromatic adaptation. After a fixation of the center, gray scale image will perceived as a colorful.

Fast spatial tuning in chromatic adaptation is possible as a possible sensory mechanism for linking color constancy to the spatial structure of a scene.

```
    """
    This function is used to convert an image to chromatic image.
    :param img: input image
    :param circle: a center fixation
    :param method: "CMCCAT2000" or "Von Kries"
    :param gif: export as gif
    :param Gifduration: duration of the gif
    :param XYZ_w, XYZ_wr, L_A: chromatic adaptation parameters (has default values)
    :return:
    """
```

***dotill***<a name="dotill"></a>

An optical illusion mainly affected by lateral inhibition.

```
    """
    This function is used to create a dotill image.
    :param dimension: width and height of the image
    :param hlinefreq: horizontal line frequency
    :param wlinefreq: vertical line frequency
    :param dotcolor: color of the dot
    :param dotradius: radius of the dot
    :param horizontalcolor: horizontal line color
    :param verticalcolor: vertical line color
    :param horizontalthickness: horizontal line thickness
    :param verticalthickness: vertical line thickness
    :param verticallines: if True, vertical lines are drawn
    :param horizontallines: if True, horizontal lines are drawn
    :return:
    """
```

***realtimegrid***<a name="realtimegrid"></a>

perceive black and white real time (with webcam) frames as colorful.

```
    """ realtimegrid is a function that add grids to the gray frame.
        :param realcolours: if True, real colours (colors that correspond to the frame) are added to frame.
    :return:
    """
```

***dakinPex***<a name="dakinPex"></a>

An optical illusion about lightness perception.

```
    """
    Creates an optical illusion from the Dakin and Bex, 2003 paper.
    :param outputname: output name
    :param dimension: dimension of the image
    :param black: line color1 (default is black)
    :param white: line color2 (default is white)
    :param bg_color: background color (default is gray)
    :return:
    """
```

***dolboeuf***<a name="dolboeuf"></a>

An optical illusion created by Belgian psychologist Joseph Remi Leopold Delbœuf in 1865

```
    """
    Creates an optical illusion from the Joseph Remi Leopold Delbœuf (1865).
    :param outputname: output name
    :param circleColor: color of the circle
    :param kill: if true, the illusion will be destroyed by the lines
    :return:
    """
```

***kanizsa***<a name="kanizsa"></a>

A famous optical illusion created by Gaetano Kanizsa.

```
    """
    Creates an optical illusion from the Gaetano Kanizsa.
    :param outputname: output name
    :param dims: dimension of the image
    :param circleColor: color of the circle
    :param bgcolor: color of the background
    :return:
    """
```

***bruno***<a name="bruno"></a>

An optical illusion created by Bruno et al. (1997) that used in an interesting experiment.

```
    """
    Creates an optical illusion from the Bruno et al. (1997).
    :param outputname: output name
    :param circle: if true, a circle is drawn instead of a rectangle
    :param polycolor: color of the polygon
    :param rectcolor: color of the rectangle
    :param circColor: color of the circle
    :return:
    """
```

***ccob***<a name="ccob"></a>

An optical illusion about the spatial frequency. ccob stands for "Craik–Cornsweet–O'Brien" and is commonly called as CCOB effect.

```
    """
    Creates an optical illusion about Spatial Frequency.
    :param image: input image
    :param rms: desired root mean square
    :param amplitudespectrum: amplitude spectrum
    :param plttitle: output name
    :param figs: figure size of the output (it will multiply by 1000)
    :return:
    """
```

***ponzol***<a name="ponzol"></a>

An old school optical illlusion described by the Ponzo, 1912.

```
    """
    Creates an optical illusion from Ponzo, 1912.
    :param outputname: output name
    :param kill: if true, the illusion will be destroyed by the lines
    :param line1: color of the first line
    :param line2: color of the second line
    :param rectangle1: color of the first rectangle
    :param rectangle2: color of the second rectangle
    :return:
    """
```

***eyecolour***<a name="eyecolour"></a>

When you run this function, you need to select a region of the image with your mouse.Illusion is about the perceving gray eyecolor as a colorful.
So for best result, i reccomend you to use a clear profile picture.

```
    """
    Select the iris on the image with mouse click and returns the illusory eye colour.
    Arguments:
    :param img: input image path with extension
    :param alpha: alpha beta and M are the parameters of blending. Play with them to get the best results
    :param luminance and saturation: Don't use values greater than 1 for luminance and saturation
    :param colors: BGR values of the color you want to use for the left half of the image (default is red)
    :return:
    """
```

***tAki2001***<a name="tAki2001"></a>
“Coloured ray illusion ” by Akiyoshi Kitaoka (Kitaoka, 2001).

```
    """
    “Coloured ray illusion ” by Akiyoshi Kitaoka (2001).
    :param outputname: output name
    :param dimension: dimension of the image
    :param circlecolour: color of the circle
    :param circleradius: radius of the circle
    :param bglinecolor: color of the background line
    :param bgcolor: color of the background
    :return:
    """
```

***addlines***<a name="addlines"></a>

Function add lines to the image to create an illusion to see actual photo. I dont sure can we classify this as an optical illusion but I inspired from the Akiyoshi Kitaoka.eyecolour

If you select `alphablending==True`  line colors are much more stable against the luminance change in the background image. It's because in opencv, when you overlay two images or colors the function called `addWeighted` mixes the colors in very "small tones" but you probably do not even notice. Still, this function which I called alpha blending, is much more stable to luminance change. Use both, in the same way and see what is differs.

```
"""
    Adds lines to an image.
    Arguments:
    img: input image
    linecolour1: first line colour
    linecolour2: second line colour
    linecolour3: third line colour
    alphablending: if True, line colors are much more stable against the luminance change in the background image.
    :return:
    """
```

***cafeWall***<a name="cafeWall"></a>

This function creates a geometrical-optical illusion called "cafewall"

```
    """
    Creates cafe wall illusion.
    :param outputname: output name
    :param dimension: dimension of the image
    :param resize: if true, the image will be adjusted to the dimension
    :param brickcolor: color of the bricks
    :param bgcolor: color of the background
    :return:
    """
```

***ebbinghaus***<a name="ebbinghaus"></a>

An optical illusion that generated by german psychologist Hermann Ebbinghaus.

```
    """
    Creates ebbinghaus illision .
    :param output: output name
    :param bgcolor: background color
    :param lcradius: left center circle radius
    :param rcradius:  right center circle radius
    :param lcradius2:  left circles radius
    :param rcradius2:  right circles radius
    :param randcirclecolors: circles  have random colors (recommended)
    :return:
    """
```

***whiteill***<a name="whiteill"></a>

An illusion that has been described by White also about the irradiation effect.

```
    """
    Optiacal illusion that has been described by White (1979).
    :param dimension: dimension of the image
    :param version2: if True, the second version of the illusion is created
    :param rect1: color of the first rectangle
    :param rect2: color of the second rectangle
    :param bgrec1: background color of the first rectangle
    :param bgrec2: background color of the second rectangle
    :param bg1: background color of the first image
    :param bg2: background color of the second image
    :param outputname: output name

    """
```

***enigma***<a name="enigma"></a>

An optical illusion based on the a paper from the Zeki et al (1993) about the motion.

```
    """
    based on the a paper from the Zeki et al (1993).
    :param linecolors: color of the lines
    :param bgcolor:  background color of the image
    :param circle1: outer circle color
    :param circle2: inner circle color
    :param centercircle: central circle color
    :param outputname: output name
    :return:
    """
```

***blackhole***<a name="blackhole"></a>

A recent optical illusion that described by the Laeng et al (2022).

```
    """"
    Illusorily Expanding Holes.
    height: height of the image
    width: width of the image
    circle_size: size of the circles (center ellipse is adjusted with this ratio)
    circle_color: color of the circles
    kill: if True, circles are not drawn
    """

```
***colorgrids***<a name="colorgrids"></a>

 This "illusion" was created by artist Øyvind Kolås from GIMP.

```
    """
    This function applies Color assimilation Grid Illusion.
    :param img: input image
    :param style: style of mask, "vertical","horizontal","gaussian","grids"
    :param width: width of lines
    :param frequency: frequency of lines
    :param saturation: saturation of lines increasing this value will increase the saturation of lines but it will distort the image if it is too high
    :return:
    """
```

***munker***<a name="munker"></a>

Parameters for the Munker illusion.

```
    """
    Creates an image of the Munker illusion.
    Parameters
    ----------
    dimensions : tuple of ints (width, height) of the image. If you change this you also need to change the thickness and linefrequency. 
    linefrequency : This is the ratio of the horizontal lines to the width of the image, this value is used to calculate the distance between the lines. The default ratio is dimensions[0]/120
    rad_ratio :radius ratio of the circles.
    thickness :thickness of the lines. If you change the dimensions of the image, you may need to change this value as well. Default ratio is dimensions[0]/200
    saturation : saturation of the colors. 1 is full saturation, 0 is no saturation. 
    bgcolor : background color of the image. Default is white. This also will determines of the colors of the all circles
    """ 
```

***munker2***<a name="munker2"></a>

Creates an image of a rectangular munker illusion.
```
    """
    Parameters
    ----------
    """
    dimensions : tuple of ints (width, height) of the image.
    ilussory_colors : tuple of ints (r,g,b) of the ilussory colors (left and right rectangles)
    leftstripes : tuple of ints (r,g,b) of the left stripes color.
    rightstripes : tuple of ints (r,g,b) of the right stripes color.
    bgcolor1 : tuple of ints (r,g,b) of the background color of the left rectangle.
    bgcolor2 : tuple of ints (r,g,b) of the background color of the right rectangle.
    """
    """ 
```

***pareidolia***<a name="pareidolia"></a>

Parameters for the face paredolia effect
```

    """
    dimensions : tuple of ints (width, height) of the image. This version is optimized for square images.
    bg : tuple of ints (r,g,b) of the background color. Default is white.
    emotion : string of the emotion of the face. Options are happy an sad. Default is happy.
    """
```

***grids2***<a name="grids2"></a>

    Creates an image of a grids and dots pattern.
```
    Parameters
    """
    dimensions : tuple of ints (width, height) of the image. This version is optimized for only 340x640 images.
    line_width : int of the width of the lines. Default is 5
    line_color : tuple of ints (r,g,b) of the line color. Default is gray.
    fill_color : tuple of ints (r,g,b) of the fill color. Default is white.
    """
```

***spirals***<a name="spirals"></a>
    Creates a confetti illusion. 
```
    Parameters
    ----------
    dimensions : tuple of ints (width, height) of the image.
    """
```

***spirals2***<a name="negate_image"></a>
    Negates an image. 
```
    """"
    Negates an image.
    Parameters
    input_file : string of the input file path.
    negation_method : string of the negation method ('subtract', 'bitwise_not', 'subtract_hsv')
    color_space : string of the color space. ('hsv', 'gray', 'bgr')
    output_quality : int of the output quality.
    """
```
