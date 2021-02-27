from PIL import Image

def resize_image(input_image_path,
                 output_image_path,
                 size):
    original_image = Image.open(input_image_path)
    width, height = original_image.size
    print('The original image size is {wide} wide x {height} '
          'high'.format(wide=width, height=height))

    resized_image = original_image.resize(size)
    width, height = resized_image.size
    print('The resized image size is {wide} wide x {height} '
          'high'.format(wide=width, height=height))
    resized_image.show()
    resized_image.save(output_image_path)

if __name__ == '__main__':
    resize_image(input_image_path='photo_es_CEE723DE-372F-4649-A422-49A031CC648C.jpg',
                 output_image_path='C:/Users/User/PycharmProjects/konkurs/medicine_photo/2.png',
                 size=(150, 150))