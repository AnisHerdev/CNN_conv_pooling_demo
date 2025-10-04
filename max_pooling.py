from PIL import Image
import numpy as np

def convert_to_numpy(file_name,width=0,height=0):
    with Image.open(file_name).convert("RGB") as img: 
        if width and height:
            img = img.resize((width,height))
        # img = img.convert("1")
        return np.array(img)


def max_pooling_colored(img_array,filter_width=2,filter_height=2,stride=1):
    h,w,c = img_array.shape
    out_h = (h - filter_height)//stride + 1
    out_w = (w - filter_width)//stride + 1
    print("Input:",h,w)
    print("Output:",out_h,out_w)
    pooled_array = np.zeros((out_h,out_w,c), dtype=img_array.dtype)
    for ch in range(c):
        for i in range(out_h):
            for j in range(out_w):
                segment = img_array[i*stride:i*stride+filter_height,j*stride:j*stride+filter_width,ch]
                pooled_array[i,j,ch]= segment.max()
    return pooled_array

def max_pooling_black_and_white(img_array,filter_width=2,filter_height=2,stride=1):
    h,w = img_array.shape[:2]
    out_h = (h - filter_height)//stride + 1
    out_w = (w - filter_width)//stride + 1
    print("Input:",h,w)
    print("Output:",out_h,out_w)
    pooled_array = np.zeros((out_h,out_w))
    for i in range(out_h):
        for j in range(out_w):
            segment = img_array[i*stride:i*stride+filter_height,j*stride:j*stride+filter_width]
            pooled_array[i,j]= segment.max()
    return pooled_array

def min_pooling(img_array,filter_width=2,filter_height=2,stride=1):
    h,w = img_array.shape[:2]
    out_h = (h - filter_height)//stride + 1
    out_w = (w - filter_width)//stride + 1
    print("Input:",h,w)
    print("Output:",out_h,out_w)
    pooled_array = np.zeros((out_h,out_w))
    for i in range(out_h):
        for j in range(out_w):
            segment = img_array[i*stride:i*stride+filter_height,j*stride:j*stride+filter_width]
            pooled_array[i,j]= segment.min()
    return pooled_array

def save_image(img_array,name="max_pooled_image.png"):
    pooled_array_uint8 = img_array.astype(np.uint8)  # Convert to 8-bit unsigned int
    pooled_img = Image.fromarray(pooled_array_uint8)
    pooled_img.save(name)


if __name__ == "__main__":
    layers = 5

    img_array = convert_to_numpy("naruto.png")
    # img_array = np.array([[1,2,3,4,5,6,6],[23,34,45,56,57,76,7],[23,32,23,54,65,75,65]])
    # print(img_array)
    # pooled_array = max_pooling_colored(img_array)
    # print(pooled_array)
    # print(pooled_array.shape)
    # pooled_img = Image.fromarray(pooled_array)
    # pooled_array_uint8 = pooled_array.astype(np.uint8)  # Convert to 8-bit unsigned int
    # pooled_img = Image.fromarray(pooled_array_uint8)
    # pooled_img.save("max_pooled.png")
    for i in range(layers):
        pooled_array = max_pooling_black_and_white(img_array,2,2,2)
        pooled_array_uint8 = img_array.astype(np.uint8)  # Convert to 8-bit unsigned int
        pooled_img = Image.fromarray(pooled_array_uint8)
        pooled_img.save(f"max_pooled_{i}_bw.png")
        img_array = pooled_array