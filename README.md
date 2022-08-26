# sorceress 1.7

[![Build Status](https://app.travis-ci.com/altunenes/sorceress.svg?branch=main)](https://app.travis-ci.com/altunenes/sorceress) [![PyPI version](https://badge.fury.io/py/sorceress.svg)](https://badge.fury.io/py/sorceress) [![Jekyll site CI](https://github.com/altunenes/sorceress/actions/workflows/jekyll.yml/badge.svg)](https://github.com/altunenes/sorceress/actions/workflows/jekyll.yml)
[![Downloads](https://pepy.tech/badge/sorceress)](https://pepy.tech/project/sorceress)

### Purpose of package

The purpose of this package is to provide creating optical illusions with simple way. Package written in Python however repo includes also JavaScript.

### Getting started🚀️

Package can be found on pypi hence you can install it with using pip.

```
pip install sorceress==1.7
```

```
#importing
import sorceress
#another way to import 
from sorceress import sorceress
```

### Features

+ Illusions written in Python    
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
 + **Illusions written in JavaScript**
  - footsteps
  - thelilac
  - EyeMovements

## Examples

For each function, I added example of how to use it. You can find them in the documentation. I will show just few examples.

from sorcerer import sorcerer
sorcerer.chromatic("myimage.jpg","outputname" ,circle=False, method="CMCCAT2000", gif=True, Gifduration=7)
sorcerer.addlines("myimage.png","desiredoutputname",linecolour1=(0,255,0),linecolour2=(0,255,255),linecolour3=(255,0,0))

## Contribution

Any contribution, bug report, suggestion is always welcome.

##Author
+ Main Maintainer: Enes Altun
