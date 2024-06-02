from PIL import Image
import matplotlib.pyplot as plt

image = Image.open("C:/Users/furkan\Desktop\paris.png")

gray_image = image.convert("L")

rotated_image = image.rotate(60)

histogram = image.histogram()

plt.bar(range(256), histogram[:256], color='blue', alpha=0.7)
plt.xlabel('Pixel Value')
plt.ylabel('Pixel Count')
plt.title('Histogram')
plt.savefig('histogram.png')
plt.close()

new_image = Image.new('RGB', (image.width * 2, image.height * 2), color='white')

new_image.paste(image, (0, 0))
new_image.paste(gray_image, (image.width, 0))
new_image.paste(rotated_image, (0, image.height))
new_image.paste(Image.open('histogram.png'), (image.width, image.height))

new_image.save('combined_img_py.png')

