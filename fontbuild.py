import random
from PIL import Image
from copy import deepcopy

class ImageBasedMask(object):
    """ Reads an image using PIL and turns it into a bit mask for use by our
    HTMLMaskedGrid item. That takes a mask and a bunch of images and uses it
    to output a bunch of div's for displaying as a grid """
    
    def __init__(self, image):
        """ Takes a source_image file (as str) and then creates a mask from the
        data within it """
        self.source_path = image
        self.source_image = Image.open(self.source_path)
        self.width = self.size[0]
        self.height = self.size[1]
        self.mask = self.generate_mask()
        
    def generate_mask(self):
        """ Reads a PNG file and creates a bit mask, initialize to zero """
        pixel_data = self.source_image.getdata()
        mask = [[0]*self.width for x in range(self.height)]
        for index, pixel in enumerate(pixel_data):
            is_valid, mask[index/self.width][index%self.width] = self.test(pixel)
        return mask
        
    def test(self, pixel, threshold=255):
        """ Checks if a given pixel is on or off for our mask """
        is_valid = False
        cnt = sum(pixel[0:3])/3
        if cnt == 0:
            is_valid = True
        opacity_val = 1 - cnt / float(threshold)
        return is_valid, opacity_val
            
    @property
    def size(self):
        return self.source_image.size

        
class HTMLMaskedGrid(object):
    """ Represents a grid based item which we then fill in the
    'on' bits with image data passed in an array. """
    
    mask, data = list(), list()

    def __init__(self, mask=None):
        self.build_mask(mask.mask)
        self.width, self.height = mask.size

    def build_mask(self, init=None):
        """ Create a mask, either zero filled or with an init list. Could probably
        simplify some of this stuff by using NumPy or SciPy instead """
        if init:
            self.mask = init
        else:
            self.mask = [[0]*self.width for x in range(self.height)]

        # Make a copy of this mask for now so indexes in bind work
        self.data = deepcopy(self.mask)

    def bind_images(self, images, jitter=False):
        """ Attaches images (cylical based on WxH to the various mask bits
        that are set. This could be anything though """
        for y in range(self.height):
            for x in range(self.width):
                jitter_amount = 0
                if jitter:
                    jitter_amount = random.randint(-10, 10)
                if self.mask[y][x]:
                    self.data[y][x] = images[(x+y+jitter_amount)%len(images)]
                else:
                    self.data[y][x] = ''
                    
    def __str__(self):
        """ Handle rendering out a bunch of divs that create our grid """
        render = '<div class="digit">'
        for y in range(self.height):
            render += '<div style="clear:both;"></div>';
            for x in range(self.width):
                render += '<div class="bit" style="opacity:'+str(self.mask[y][x])+';">'+str(self.data[y][x])+'</div>'
        render += '</div>'
        return render

