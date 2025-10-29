
################################################
###  CALCUL IMBALANCE RATIO FOR WHU DATASET  ###
################################################

from PIL import Image

# Load the image
image = Image.open('E://Datasets//WHU//change_label_resize25percent.tif')  
# Replace 'your_image.png' with your image file

# Convert the image to grayscale
image = image.convert('L')

# Get the pixel data
pixel_data = image.load()

# Initialize a counter for white pixels
white_pixel_count = 0

# Loop through each pixel and count white pixels (255)
for x in range(image.width):
    for y in range(image.height):
        if pixel_data[x, y] == 255:
            white_pixel_count += 1

print(f'Number of white pixels: {white_pixel_count}')
print(f'Percentage of white pixels: {(white_pixel_count/20388929.00)*100} %')

