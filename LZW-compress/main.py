from LZW import LZW
import os

compressor = LZW(os.path.join("images","cup.tif"))
compressor.compress()