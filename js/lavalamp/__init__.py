import os

from fanstatic import Library, Resource, Group

library = Library('lavalamp', 'resources')

fnames = lambda subp: os.listdir(library.path + os.sep + subp)

css_resources = [Resource(library, 'css' + os.sep + fn) for fn in fnames('css')]
js_resources = [Resource(library, 'js' + os.sep + fn) for fn in fnames('js')]

css = Group(css_resources)
js = Group(js_resources)

lavalamp = Group([css, js])

