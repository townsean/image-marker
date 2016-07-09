#! python3

import argparse, shutil, os, os.path, tinify
from PIL import Image

def compressImage(filename):    
    tinify.key = "YOUR_API_KEY"
    source = tinify.from_file(filename)
    source.to_file(filename)

def resizeImage(filename, width, height):
    image = Image.open(filename)
    imageWidth, imageHeight = image.size

    if width is None and height is not None:
        imageWidth = (imageWidth * height) / imageHeight
        imageHeight = height
    elif width is not None and height is None:
        imageHeight = (imageHeight * width) / imageWidth
        imageWidth = width
    elif width is not None and height is not None:
        imageWidth = width
        imageHeight = width

    resizedImage = image.resize((int(imageWidth), int(imageHeight)))
    resizedImage.save(filename)

def watermarkImage(filename, text):
    pass

def main():
    parser = argparse.ArgumentParser(description='Automates basic image manipulation.')
    parser.add_argument('directory', nargs='?', default='.', help='A directory of images to process')
    parser.add_argument('-w', '--width', type=int, help='Resize the width of the image to <width>')
    parser.add_argument('--height', type=int, help='Resize the height of the images to <height>')
    parser.add_argument('-f', '--font-family', help='Sets the font family for the text watermark to <font family>')
    parser.add_argument('--font-style', choices=['bold', 'italic', 'underline', 'regular'], help="Sets the font style of the text watermark to <font style>. Valid options are: bold, italic, underline, regular.")
    parser.add_argument('--font-size', type=int, help="Sets the font size of the text watermark to <font size>")
    parser.add_argument('-o', '--opacity', type=float, help="Sets the opacity of the watermark to <opacity>. This is a number between 0 and 1.")
    parser.add_argument('-c', '--color', help="Sets the color of the text watermark to <color>. Expects the <color> in hex format. Also accepts the following presets: black, white, blue")
    parser.add_argument('-t', '--text', help="Sets the watermark to <text>")
    parser.add_argument('-i', '--image-overlay', help="Sets an image overlay to <path>. (Watermark the image with an image instead of text)")
    parser.add_argument('--overlay-size', type=float, help="Sets the size of the image overlay to <size>. This is a number between 0 and 1. (What percentage of image should be covered by the image overlay?)")

    args = parser.parse_args()

    # shutil.copytree("test_images", "copyof_test_images")
    os.chdir("copyof_test_images")
    args.width = 500

    for filename in os.listdir(args.directory):
        resizeImage(filename, args.width, args.height)
        compressImage(filename)


if __name__ == '__main__':
    main()