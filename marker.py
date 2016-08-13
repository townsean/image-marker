#! python3
# marker.py - Automates basic image manipulation:  resize, watermark, and compress images.

import argparse
import shutil
import os
import os.path
import ast

from datetime import datetime

try:
    import tinify
except ImportError:
    exit("This script requires the tinify module.\nInstall with pip install tinify")

try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError:    
    exit("This script requires the PIL module.\nInstall with pip install Pillow")

def compress_image(filename):    
    tinify.key = "YOUR_API_KEY"
    source = tinify.from_file(filename)
    source.to_file(filename)

def resize_image(filename, width, height):
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

    return image.resize((int(imageWidth), int(imageHeight)), Image.ANTIALIAS)
    

def watermark_image_with_text(filename, text, color, fontfamily):
    image = Image.open(filename).convert('RGBA')
    imageWatermark = Image.new('RGBA', image.size, (255, 255, 255, 0))

    draw = ImageDraw.Draw(imageWatermark)
    
    width, height = image.size
    margin = 10
    font = ImageFont.truetype(fontfamily, int(height / 20))
    textWidth, textHeight = draw.textsize(text, font)
    x = width - textWidth - margin
    y = height - textHeight - margin

    draw.text((x, y), text, color, font)

    return Image.alpha_composite(image, imageWatermark)

def main():
    parser = argparse.ArgumentParser(description='Automates basic image manipulation.')
    parser.add_argument('directory', nargs='?', default='.', help='A directory of images to process')
    parser.add_argument('-w', '--width', type=int, help='Resize the width of the image to <width>')
    parser.add_argument('--height', type=int, help='Resize the height of the images to <height>')
    parser.add_argument('-f', '--font-family', help='Sets the font family for the text watermark to <font family>')
    parser.add_argument('--font-style', choices=['bold', 'italic', 'underline', 'regular'], help="Sets the font style of the text watermark to <font style>. Valid options are: bold, italic, underline, regular.")
    parser.add_argument('--font-size', type=int, help="Sets the font size of the text watermark to <font size>")
    parser.add_argument('-o', '--opacity', type=float, help="Sets the opacity of the watermark to <opacity>. This is a number between 0 and 1.")
    parser.add_argument('-c', '--color', type=ast.literal_eval, help="Sets the color of the text watermark to <color>. Expects the <color> in RGBA tuple format.")
    parser.add_argument('-t', '--text', help="Sets the watermark to <text>")
    parser.add_argument('-i', '--image-overlay', help="Sets an image overlay to <path>. (Watermark the image with an image instead of text)")
    parser.add_argument('--overlay-size', type=float, help="Sets the size of the image overlay to <size>. This is a number between 0 and 1. (What percentage of image should be covered by the image overlay?)")

    args = parser.parse_args()

    os.chdir(args.directory)
    shutil.copytree(os.getcwd(), 'directory_backup_{1}'.format(args.directory, datetime.now().isoformat()).replace(':', '_'))

    for filename in os.listdir():
        if filename.lower().endswith('.png') or filename.lower().endswith('.jpg'):
            resized_image = resize_image(filename, args.width, args.height)
            resized_image.save(filename, quality=90)
            
            if args.text is not None:
                watermarked_image = watermark_image_with_text(filename, args.text, args.color, args.font_family)
                watermarked_image.save(filename)

            # A Tinify API key is required to compress images
            # compress_image(filename)

if __name__ == '__main__':
    main()