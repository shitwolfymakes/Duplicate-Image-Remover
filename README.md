# Duplicate-Image-Remover


![GitHub All Releases](https://img.shields.io/github/downloads/shitwolfymakes/Duplicate-Image-Remover/total?color=dark%20green&style=plastic)
![GitHub](https://img.shields.io/github/license/shitwolfymakes/Duplicate-Image-Remover/?style=plastic)  

Remove duplicate media files from a folder quickly and easily. Testing done on a library of nearly 10k images and videos

## To use:
 1) Export the photo or video library to folder (you can export any sidecar files here as well)
 2) Backup your exported files (I tested this with my own photos and it worked fine, but you should still do this)
 3) Navigate to the `Duplicate-Image-Remover` folder

## Usage:
 - To keep duplicates, do `python3 dupir.py -k <absolute/path/to/folder>`
 - To delete duplicates, do `python3 dupir.py <absolute/path/to/folder>`

## Notes:
 - You must run this with the absolute path. I could not get this to work using relative paths
 - This does not support subfolders, make sure all files are in one folder, or go one subfolder at a time
 - Duplicates are moved to `Duplicate-Image-Remover/dupir_temp/` during execution
