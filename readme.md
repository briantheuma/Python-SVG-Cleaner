# SVG Cleaner

SVG Cleaner was created to clean out all un-needed tags from downloaded generated or exported svg's that need to be used in specific development environments. 


## What gets cleaned out?

SVG Cleaner will clean out the following items:
 - `<g>` and `</g>` tags
 - `id` attribute
 - `fill-rule` attribute
 - `fill` attribute
 - `<?xml version="1.0" encoding="UTF-8"?>` tag
 - `<title>` and `</title>` tags


## How to use the SVG Cleaner

The SVG cleaner contains 2 folders:
 - '01-original-svgs'
 - '02-cleaned-svgs'

The names are quite self explanatory '01-original-svgs' is where you'd place your original version svg's and '02-cleaned-svgs' will be your generated cleaned version after running this script.

To run the cleaner all you need to do is put the svg's you'd like to clean inside the '01-original-svgs' folder, run `svg-clean.py`. You'll find a new set of cleaned svg's inside the '02-cleaned-svgs' folder.

## ENJOY!