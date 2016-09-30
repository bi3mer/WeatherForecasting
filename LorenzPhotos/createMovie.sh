#!/bin/bash
ffmpeg -f image2 -i %03d.png -vcodec mpeg4 -y temp.mp4
ffmpeg -i temp.mp4 -filter:v "setpts=2.0*PTS" lorenz.mp4
rm temp.mp4
