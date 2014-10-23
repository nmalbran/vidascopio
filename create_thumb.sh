#!/bin/bash

convert -define jpeg:size=400x400 $1 -thumbnail 180x180^ -gravity center -extent 180x180 thumb/$1.gif
