
from PIL import Image
import os
import numpy as np

class LZW:
    def __init__(self, path):
        self.path = path
        self.compressionDictionary, self.compressionIndex = self.createCompressionDict()
        self.decompressionDictionary, self.decompressionIndex = self.createDecompressionDict()
    
    ''''''
    ''' --------------------- Compression of the Image --------------------- '''
    ''''''

    def compress(self):
        self.initCompress()
        compressedcColors = []
        print("Compressing Image ...")
        compressedcColors.append(self.compressColor(self.red))
        print("Compressing Image ...")
        compressedcColors.append(self.compressColor(self.green))
        print("Compressing Image ...")
        compressedcColors.append(self.compressColor(self.blue))
        print("Image Compressed --------- Writing to File")
        filesplit = str(os.path.basename(self.path)).split('.')
        filename = filesplit[0] + 'Compressed.lzw'
        savingDirectory = os.path.join(os.getcwd(),'CompressedFiles')
        if not os.path.isdir(savingDirectory):
            os.makedirs(savingDirectory)
        with open(os.path.join(savingDirectory,filename),'w') as file:
            for color in compressedcColors:
                for row in color:
                    file.write(row)
                    file.write("\n")
                
    def compressColor(self, colorList):
        compressedColor = []
        i = 0
        for currentRow in colorList:
            currentString = currentRow[0]
            compressedRow = ""
            i+=1
            for charIndex in range(1, len(currentRow)):
                currentChar = currentRow[charIndex]
                if currentString+currentChar in self.compressionDictionary:
                    currentString = currentString+currentChar
                else:
                    compressedRow = compressedRow + str(self.compressionDictionary[currentString]) + ","
                    self.compressionDictionary[currentString+currentChar] = self.compressionIndex
                    self.compressionIndex += 1
                    currentString = currentChar
                currentChar = ""
            compressedRow = compressedRow + str(self.compressionDictionary[currentString])
            compressedColor.append(compressedRow)
        return compressedColor


    '''
    Used For: Compression of Image
    Function: This function breaks down the image into the three constituting
              image chanels - Red, Green and Blue.
    '''
    def initCompress(self):
        self.image = Image.open(self.path)
        self.height, self.width = self.image.size
        self.red, self.green, self.blue = self.processImage()

    '''
    Used For: Compression of Image
    Function: This function breaks down the image into the three constituting
              image chanels - Red, Green and Blue.
    '''
    def processImage(self):
        image = self.image.convert('RGB')
        red, green, blue = [], [], []
        pixel_values = list(image.getdata())
        iterator = 0
        for height_index in range(self.height):
            R, G, B = "","",""
            for width_index in range(self.width):
                RGB = pixel_values[iterator]
                R = R + str(RGB[0]) + ","
                G = G + str(RGB[1]) + ","
                B = B + str(RGB[2]) + ","
                iterator+=1
            red.append(R[:-1])
            green.append(G[:-1])
            blue.append(B[:-1])
        return red,green,blue


    
    '''
    Used For: Compression of Image
    Function: This function will initialise the compression dictionary
    '''
    def createCompressionDict(self):
        dictionary = {}
        for i in range(10):
            dictionary[str(i)] = i
        dictionary[','] = 10
        return dictionary,11

    '''
    Used For: Compression of Image
    Function: This function will initialise the decompression dictionary
    '''
    def createDecompressionDict(self):
        dictionary = {}
        for i in range(10):
            dictionary[i] = str(i)
        dictionary[10] = ','
        return dictionary,11