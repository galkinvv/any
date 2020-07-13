#!/usr/bin/env python3
# Extracts logo with opacity with a 2-100 series of images with same logo with same placing
import sys
from PIL import Image, ImageChops
name = sys.argv[1]
base = Image.open(name)
mask = Image.new('L', base.size, 255)
sens_param = 1.4
for oname in sys.argv[2:]:
	other = Image.open(oname)
	assert base.size == other.size
	mask = ImageChops.darker(mask, ImageChops.invert(ImageChops.difference(base, other).convert(mode='L', matrix=(sens_param,)*4)))
out = base.copy()
out.putalpha(mask)
out.save(name + "-logo.png")
print(out)
