# sorceress 1.8

[![PyPI version](https://badge.fury.io/py/sorceress.svg)](https://badge.fury.io/py/sorceress) [![Jekyll site CI](https://github.com/altunenes/sorceress/actions/workflows/jekyll.yml/badge.svg)](https://github.com/altunenes/sorceress/actions/workflows/jekyll.yml)
[![Downloads](https://pepy.tech/badge/sorceress)](https://pepy.tech/project/sorceress)
[![Build status](https://ci.appveyor.com/api/projects/status/71rohei2h9q6ru0s?svg=true)](https://ci.appveyor.com/project/altunenes/sorceress)


![bannner](./docs//assets/banner.PNG)


### Purpose of package

This package's purpose is to create optical illusions in a simple way. The package is written in Python. however, the repo also includes JavaScript.  In [explanations](https://altunenes.github.io/sorceress/explanations%20of%20illusions/) section, you can find the explanations of the illusions.

This package contains a collection of well-known visual illusions, as well as some lesser-known ones that are just as fascinating.

By using the code provided in the package, you can easily recreate the illusions and see how they work for yourself.
Not only can you reproduce the illusions, but you can also experiment with them and modify the code to create your own variations.

With this package, you can dive deep into the world of visual illusions and learn more about how the human brain processes visual information.

Whether you're a researcher, a student, or just someone who loves illusions, this package has something for you. So if you're interested in exploring the mysteries of the human visual system, give it a try!

More importantly, we shouldn't take optical illusions as just fun. Optical illusions are visual phenomena that occur when our brain interprets information from our eyes in a way that is different from reality. These illusions can reveal a lot about how our brain works and how it processes visual information, which can help us understand the underlying mechanisms of human vision. Most of the optical illusions in this package are seriously researched in the neuroscience literature. And I must say that the "causation" of the most of effects is still debated in the literature according to my humble knowledge. Optical illusions are researching not only in human vision but in other animals. So we can get a lot of insights from an evolutionary perspective.

The difficulty of creating an optical illusion with code will depend on the specific illusion you're trying to create and your experience with coding. Some optical illusions may be relatively simple to implement, while others may be more complex and require a deeper understanding of graphics programming and the underlying principles of perception.To create an effective optical illusion, you (also me) need to understand the principles of perception and be able to use code to manipulate the visual information in a way that tricks the brain into seeing something that isn't actually there. This requires a deep understanding of the underlying mechanisms of perception and a lot of experimentation and trial and error to find the right combination of visual elements that creates the desired illusion.

Another challenge is that creating optical illusions often requires a high level of precision and control over the visual elements in an image. This can be difficult to achieve with code, especially if you're working with complex or dynamic images that need to be updated in real time.

Overall, creating optical illusions with code can be a challenging but rewarding task that requires a combination of technical skills, creativity, and an understanding of the underlying principles of perception  [(Bach, 2014)](https://pubmed.ncbi.nlm.nih.gov/25420328/).

For all optical illusions check this documentation: [altunenes.github.io/sorceress/](https://altunenes.github.io/sorceress/)

### Getting started🚀️

The package can be found on PyPI hence you can install it via pip.

```
pip install sorceress
```

```
#importing
from sorceress import sorceress
```

### Features

[For the API, click here](https://altunenes.github.io/sorceress/api_reference/)

+ Illusions in Python
  - chromatic
  - dotill
  - realtimegrid
  - addlines
  - eyecolour
  - dakinPex
  - bruno
  - dolboeuf
  - kanizsa
  - tAki2001
  - cafewall
  - ccob
  - ebbinghaus
  - whiteill
  - enigma
  - blackhole
  - colorgrids
  - munker
  - munker2
  - grids2
  - pareidolia
  - spirals
  - color negative
  - footsteps

 **Illusions in JavaScript**

  - footsteps
  - thelilac
  - EyeMovements
  - spatialmotion
  - Motion Induced Blindness (2 versions)
  - Depth Perception
  - Speed of Rotation
  - hypnotic circle
  - Bright Illusion
  - Length Illusion
  - Crazy Sine Waves
  - Crazy EEG-Fourier
  - phimotion
  - colour adaptation
  
## Examples

[In this page](https://altunenes.github.io/sorceress/explanations%20of%20illusions/), you can find all illusions, explanations, code, and how to use it. I show just a few examples on this page.

```
from sorceress import sorceress
sorceress.chromatic("myimage.jpg",circle=False, method="CMCCAT2000", gif=True, Gifduration=7)
sorceress.addlines("myimage.png",linecolour1=(0,255,0),linecolour2=(0,255,255),linecolour3=(255,0,0))
```

As you can see above, you can use the package in a very simple way. You will need to install the following packages to use the package. You will not need to import them, the package will do it for you.

```
pip install opencv-python
pip install numpy
pip install matplotlib
pip install imageio
pip install Pillow
pip install colour-science
pip install pygame
```

## Contribution

Any contribution, bug report, or suggestion is always welcome <3

+ Main Maintainer: Enes Altun
