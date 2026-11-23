#!/bin/zsh

ffmpeg \
    -f lavfi -i "sine=frequency=440" \
    -c:a pcm_s16le \
    -ar 48k \
    -ac 2 \
    -t 10 \
    la.wav