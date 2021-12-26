from PIL import Image
# open base
base = Image.open(r"/Users/xiuli.j.shen/development/meoimeoi/img-blender/imgs/Face.png")

#open eyes
eyes = Image.open(r"/Users/xiuli.j.shen/development/meoimeoi/img-blender/imgs/Eyes.png")

#open Hair
hair = Image.open(r"/Users/xiuli.j.shen/development/meoimeoi/img-blender/imgs/Hair.png")

base.paste(eyes, (0,0), mask = eyes)
base.paste(hair, (0,0), mask = hair)

#make image background color something else
white_fill_color = (255,255,255) #white background from transparent
red = (139,0,0) #white background from transparent

image = base.convert("RGBA")
new_image = Image.new("RGBA", image.size, red)
new_image.paste(image, mask=image)

# save the generated image 
# new_image.convert("RGB").save("test.jpg")

base.show()
new_image.show()