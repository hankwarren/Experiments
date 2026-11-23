#!/bin/zsh

ffmpeg \
    -i mandelbrot.avi \
    -i la.wav \
    -c:v copy \
    -c:a copy \
    mandela.avi