# BlenderToOpenGL 1.0
Want to use a 3D model you created in or imported into Blender in your OpenGL project? Now you can using this converter!

## Usage
1. Make sure you have Python3 installed.
2. In Blender, open your model and select it, then File > Export > Wavefront (.obj).
3. In the options, use these settings: Include `Limit to Selection Only, Objects as OBJ Objects`, Geometry `Apply Modifiers, Write Normals, Triangulate Faces`
4. Write your file's name and Export OBJ.
5. Download objToOpenGL.py and from the command line run `python objToOpenGL.py [BlenderFile.obj] [output.txt]`
6. Your new output file contains OpenGL code that you can use in your project. Congratulations!

## Disclaimer
While this method of creating models is much faster than writing vertices by hand, it is not necessarily the most efficient. Massive models will likely cause your project not to load. It works very well with relatively simple models though.

## About
I was in a Graphics Programming class and my final project had to be written in OpenGL. I wanted to use models that looked nice but didn't want to spend 9 years making them, so I figured there must be a way to get models from Blender into this engine. Unfortunately, other methods either don't work or are far more complicated than they are worth, so I set out to make my own way. With lots of help and debugging from ChatGPT, I was able to create this converter. I hope this helps someone who is in a similar situation! Please submit any issues and I will try my best to resolve them!
