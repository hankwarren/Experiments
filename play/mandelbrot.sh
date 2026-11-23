#!/bin/zsh

ffmpeg \
    -f lavfi -i mandelbrot \
    -t 10 \
    -c:v rawvideo \
    -pix_fmt uyvy422 \
    mandelbrot.avi

#    -pix_fmt yuv420p \