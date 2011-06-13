#!/usr/bin/env python2

from BeautifulSoup import BeautifulSoup as Soup
from jinja2 import Template
import urllib
import cherrypy
import re

from page_templates import PAGE_TEMPLATE
from fontbuild import HTMLMaskedGrid, ImageBasedMask
        
class PediaImages(object):
    """ Quick'n'easy cherrypy handler to load in data from sneakerpedia to
    create a pool of images. We then make digits and bind them to the source
    data and then return the number rendered out. """
    
    feed = 'http://www.sneakerpedia.com/'
    images = list()

    def source_images(self):
        """ Reads in from the sneakerpedia homepage, pulls out the various homepage
        images of kicks to build an array of images to use """
        data = urllib.urlopen(self.feed).read()
        souped = Soup(data)
        results = souped.findAll('img', {'src': re.compile(r'amazon')})
        images = list()
        for result in results:
            if 'default' not in str(result):
                images.append(str(result))
        return images

    def __init__(self):
        self.images = self.source_images()

    def index(self):
        """ Our homepage view, create a digit, bind some images to it and
        return the rendered template """
        w, h = 20, 20
        item = HTMLMaskedGrid(ImageBasedMask('img/test.png'))
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
