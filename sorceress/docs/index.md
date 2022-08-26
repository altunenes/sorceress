# sorceress 1.7

### Purpose of package

The purpose of this package is to provide creating optical illusions with simple way. Package written in Python however repo includes also JavaScript.

More importantly, we shouldn't take optical illusions as just fun. Optical illusions help us to research how the visual system of the brain ,which is the most complex mechanism, processes such cues.
Most of the optical illusions in this package are seriously researched in the neuroscience literature. And I must say that the "causation" of the most of effects is still debated in the literature according to my humble knowledge.
Optical illusions are researching not only in human vision but in other animals. So we can get a lot of insights from an evolutionary perspective.

In summary, I think this topic is very important, especially in vision studies.

### Getting started🚀️

Package can be found on pypi hence you can install it with using pip.

```
pip install sorceress
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

`from sorcerer import sorcerer `

`sorcerer.chromatic("myimage.jpg","outputname" ,circle=False, method="CMCCAT2000", gif=True, Gifduration=7)`

`sorcerer.addlines("myimage.png","desiredoutputname",linecolour1=(0,255,0),linecolour2=(0,255,255),linecolour3 (255,0,0))`

## Contribution

Any contribution, bug report, suggestion is always welcome.

##Author

+ Main Maintainer: Enes Altun
