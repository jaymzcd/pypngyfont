#!/usr/bin/env python2

from BeautifulSoup import BeautifulSoup as Soup
from jinja2 import Template
import urllib
import cherrypy

from page_templates import PAGE_TEMPLATE
from fontbuild import CounterNumber, NumberMasks
        
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
        results = souped.findAll('a', {'class': 'hoverimage'})
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
        digits = [
            CounterNumber(NumberMasks.ZERO_MASK),
            CounterNumber(NumberMasks.EIGHT_MASK),
        ]
        [digit.bind_images(self.images) for digit in digits]
        context = {
            'digits': digits,
        }
        return Template(PAGE_TEMPLATE).render(context)
    index.exposed = True

if __name__ == '__main__':
    # Fire up lasers!
    cherrypy.server.socket_host = '0.0.0.0'
    cherrypy.quickstart(PediaImages())
