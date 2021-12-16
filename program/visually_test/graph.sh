#!/bin/sh

gcc -o ./image ./image_txt.c

./image

python3 ./image.py
