#!/bin/bash

video=$1;
out=$2;
seconds=15;

count=0;
while [ $count -lt $seconds ]; do
    echo "Extracting frame at $count seconds...";
    ffmpeg -i $video -f image2 -ss $count -vframes 1 $out/output-$count.jpg;
    let count=count+0.5;
done
