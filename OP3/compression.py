'''The module for implementing cimpressing and decompressing algorythms'''
from PIL import Image, ImageOps
import numpy as np
import matplotlib.pyplot as plt


class GrayscaleImage:
    def __init__(self, nrows, ncols):
        '''The initializer'''
        self.nrows = nrows
        self.ncols = ncols
        self.pctr = np.zeros((nrows, ncols), dtype=np.uint8)
    def width(self):
        '''The width'''
        return self.ncols
    def height(self):
        '''The hight'''
        return self.nrows
    def clear(self, value):
        '''Clears'''
        if not (0 <= value <= 255):
            raise ValueError()
        self.pctr.fill(value)
    def getitem(self, row, col):
        '''getitem'''
        if (0 <= row < self.nrows and 0 <= col < self.ncols):
            return self.pctr[row, col]
        raise IndexError()
    def setitem(self, row, col, value):
        '''sets'''
        if not (0 <= row < self.nrows and 0 <= col < self.ncols):
            raise IndexError()
        if not (0 <= value <= 255):
            raise ValueError()
        self.pctr[row, col] = value
    @classmethod
    def from_file(cls, path):
        '''opens the image'''
        img = Image.open(path).convert("L")
        img_array = np.array(img, dtype=np.uint8)
        instance = cls(img_array.shape[0], img_array.shape[1])
        instance.pctr = img_array
        return instance
    def lzw_compression(self):
        '''the alhorythm'''
        flat_pixels = self.pctr.flatten().tolist()
        return self.compress(flat_pixels)
    def lzw_decompression(self, compressed_data):
        '''the algorythm'''
        decompressed_list = self.decompress(compressed_data)
        self.pctr = np.array(decompressed_list, dtype=np.uint8).reshape((self.nrows, self.ncols))
    @staticmethod
    def compress(uncompressed):
        '''compresses the img'''
        dictionary = {bytes([i]): i for i in range(dict_size)}
        w = b""
        result = []
        dict_size = 256
        for c in uncompressed:
            wc = w + bytes([c])
            if wc in dictionary:
                w = wc
            else:
                result.append(dictionary[w])
                dictionary[wc] = dict_size
                dict_size += 1
                w = bytes([c])
        if w:
            result.append(dictionary[w])
        return result
    @staticmethod
    def decompress(compressed):
        '''decompresses the img'''
        dict_size = 256
        dictionary = {i: bytes([i]) for i in range(dict_size)}
        
        w = bytes([compressed.pop(0)])
        result = [w]
        for k in compressed:
            if k in dictionary:
                entry = dictionary[k]
            elif k == dict_size:
                entry = w + w[:1]
            else:
                raise ValueError()
            result.append(entry)
            dictionary[dict_size] = w + entry[:1]
            dict_size += 1
            w = entry
        return list(b"".join(result))
    def load_image(self, filename):
        '''loads the img'''
        image_pil = Image.fromarray(self.pctr, mode="L")
        image_pil.save(filename)
        image_pil.show()
    def save(self, path):
        '''saves as a file'''
        img = Image.fromarray(self.pctr)
        img.save(path)

# img = GrayscaleImage.from_file("picture.jpg")
# compressed_data = img.lzw_compression()
# img.lzw_decompression(compressed_data)
# img.save("decompressed.jpg")
