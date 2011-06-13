from copy import copy

class NumberMasks(object):
    """ Hold our masks, nothing special """

    ZERO_MASK = [
        [0, 1, 1, 1, 0],
        [1, 0, 0, 0, 1],
        [1, 0, 0, 0, 1],
        [1, 0, 0, 0, 1],
        [1, 0, 0, 0, 1],
        [1, 0, 0, 0, 1],
        [1, 0, 0, 0, 1],
        [0, 1, 1, 1, 0],
    ]

    EIGHT_MASK = [
        [0, 1, 1, 1, 0],
        [1, 0, 0, 0, 1],
        [1, 0, 0, 0, 1],
        [0, 1, 1, 1, 0],
        [0, 1, 1, 1, 0],
        [1, 0, 0, 0, 1],
        [1, 0, 0, 0, 1],
        [0, 1, 1, 1, 0],
    ]    

class CounterNumber(object):
    """ Represents a grid based item which we then fill in the
    'on' bits with image data pulled from sneakerpedia. """
    
    width, height = 5, 8
    mask, data = list(), list()

    def __init__(self, mask=None):
        self.build_mask(mask)

    def build_mask(self, init=None):
        """ Create a mask, either zero filled or with an init list. Could probably
        simplify some of this stuff by using NumPy or SciPy instead """
        if init:
            self.mask = init
        else:
            self.mask = [[0]*self.width for x in range(self.height)]

        # Make a copy of this mask for now so indexes in bind work
        self.data = copy(self.mask)

    def bind_images(self, images):
        """ Attaches images (cylical based on WxH to the various mask bits
        that are set. This could be anything though """
        for y in range(self.height):
            for x in range(self.width):
                if self.mask[y][x]:
                    self.data[y][x] = images[(x+y)%len(images)]
                else:
                    self.data[y][x] = ''

    def __str__(self):
        """ Handle rendering out a bunch of divs that create our grid """
        render = '<div class="digit">'
        for y in range(self.height):
            render += '<div style="clear:both;"></div>';
            for x in range(self.width):
                render += '<div class="bit">'+str(self.data[y][x])+'</div>'
        render += '</div>'
        return render

