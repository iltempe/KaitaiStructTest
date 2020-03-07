from gif import *
g = Gif.from_file("prova.gif")

print("width = %d" % (g.logical_screen.image_width))
print("height = %d" % (g.logical_screen.image_height))