from PIL import Image

with Image.open("naruto.png") as img:
    width,height= img.size
    print(img.size)
    # img = img.rotate(30)
    # img = img.crop((0,0,400,400))
    # img = img.resize((width*2,height*2))
    # print(img.histogram())
    print(img.mode)
    print(img.split())
    print (img.tobitmap())
    img.save("rdd.png")  
