# PyPngyFont

This stems from a bit of concept coding for a design but it's been adapted and
extended to now use a PNG as a source mask and some tidy up of the methods

Essentially it takes in a list of images and a source PNG file, creates a bitmask
to the size of the image and then uses that to output html (using cherrypy) where
the image content for each cell comes from the passed images.

You could for example feed it a flickr stream, the picture urls from a facebook
graph call or a list of twitter profile pics. In this case it's pulling content
from the sneakerpedia.com homepage.
