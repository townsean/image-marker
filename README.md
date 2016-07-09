# image-marker

## Synopsis

Image Marker is a Python script gives users the ability to watermark image files in bulk. (Work in Progress)

## Motivation

I am a [DIY blogger](http://www.ashleygrenon.com/) and the most tedious part of the job is editing the images.  I am constantly repeating the following steps:

1. Resize the image
2. Add a text watermark  
3. Compress the image

I wanted to automate the process.  There are good solutions out there for automating the process, but it has been a few years since I last wrote a meaningful piece of Python code.  I saw this as an excellent way to dust off my Python skill and learn a bit about programmatic image manipulation.

## Command Line Options

```
-w <width>
--width=<width>
```
Resizes the width of the images to `<width>`


```
-h <height>
--height=<height>
```
Resizes the height of the images to `<height>`


```
-f <font family>
--font-family=<font family>
```
Sets the font family for the text watermark to `<font family>`


```
--font-style=<font style>
```
Sets the font style of the text watermark to `<font style>`.  Valid options are: **bold**, *italic*, underline, regular.


```
--font-size=<font size>
```
Sets the font size of the text watermark to `<font size>`


```
-o <opacity>
--opacity=<opacity>
```
Sets the opacity of the watermark to `<opacity>`.  This is a number between 0 and 1.


```
-c <color>
--color=<color>
```
Sets the color of the text watermark to `<color>`.  Expects the `<color>` in RGBA tuple format.  Also accepts the following presets: black, white, blue


```
-t <text>
--text=<text>
```
Sets the watermark to `<text>`


```
-i <path>
--image-overlay=<path>
```
Sets an image overlay to `<path>`. (Watermark the image with an image instead of text)


```
--overlay-size=<size>
```
Sets the size of the image overlay to `<size>`. This is a number between 0 and 1. (What percentage of image should be covered by the image overlay?) 

## Built With

I used the [Tinify API](https://tinypng.com/developers/reference/python) to compress images and [Pillow](https://pillow.readthedocs.io/en/3.3.x/) for image manipulation.

## Maintainers

* [Ashley Grenon - @townsean](https://github.com/townsean)

## License (MIT)

The MIT License (MIT)
Copyright (c) 2016 Ashley Grenon

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
