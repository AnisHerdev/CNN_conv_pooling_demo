from PIL import Image
import numpy as np
def convert_to_numpy(file_name,width=100,height=100):
    arr=[]
    with Image.open(file_name) as img:
        img = img.resize((width,height))
        img = img.convert("1")
        print(np.array(img))
        pixels = img.load()
    return arr
# with Image.open("naruto.png") as img:
#     img = img.resize((100,100))
#     width,height= img.size
#     print(img.size)
#     # img = img.rotate(30)
#     # img = img.crop((0,0,400,400))
#     # img = img.resize((width*2,height*2))
#     # print(img.histogram())
#     print(img.mode)
#     img_bw = img.convert("1")  # Convert to 1-bit pixels
#     img = img.convert("1")  # Convert to 1-bit pixels
#     # print(img_bw.tobitmap())
#     for y in range(height):
#         for x in range(width):
#             print("1" if img.getpixel((x,y))==255 else "_" ,end="")
#         print()
#     img.save("rdd.png")  

def print_image(arr):
    for y in arr:
        print("".join(str(x) for x in y))

if __name__ == "__main__":
    arr = convert_to_numpy("naruto.png")
    print_image(arr)