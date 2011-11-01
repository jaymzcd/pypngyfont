#!/usr/bin/env python2

from BeautifulSoup import BeautifulSoup as Soup
from jinja2 import Template
import urllib
import cherrypy
import re
import glob

from page_templates import PAGE_TEMPLATE
from fontbuild import HTMLMaskedGrid, ImageBasedMask

class PediaImages(object):
    """ Quick'n'easy cherrypy handler to load in data from sneakerpedia to
    create a pool of images. We then make digits and bind them to the source
    data and then return the number rendered out. """

    images = list()

    def _link_image(self, image, base='http://10.10.91.73/pypngyfont/'):
        return '<img src="%s%s" />' % (base, image)

    def source_images(self, mode='url', path='http://www.sneakerpedia.com/'):
        """ Reads in from the sneakerpedia homepage, pulls out the various homepage
        images of kicks to build an array of images to use """
        images = list()

        if mode=='url':
            data = urllib.urlopen(path).read()
            souped = Soup(data)
            results = souped.findAll('a', {'class': 'hoverimage'})
            for result in results:
                if 'default' not in str(result):
                    images.append(unicode(result))

        if mode=='path':
            images = glob.glob(path)
            images = [self._link_image(i) for i in images]
            print images
        return images

    def __init__(self):
        self.images = self.source_images('path', 'img/omalls/*.jpg')

    def index(self):
        """ Our homepage view, create a digit, bind some images to it and
        return the rendered template """
        w, h = 25, 25
        item = HTMLMaskedGrid(ImageBasedMask('img/trefoil-30.jpg'))
        digits = [
            item,
        ]
        [digit.bind_images(self.images, jitter=True) for digit in digits]
        context = {
            'digits': digits,
            'bit': dict(width=w, height=h),
            'char': dict(width=item.width*w, height=item.height*h),
        }
        return Template(PAGE_TEMPLATE).render(context)
    index.exposed = True

if __name__ == '__main__':
    # Fire up lasers!
    cherrypy.server.socket_host = '0.0.0.0'
    cherrypy.quickstart(PediaImages())
