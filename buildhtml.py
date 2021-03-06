#!/usr/bin/env python

"""Build HMTL from reST files."""

from __future__ import print_function

from glob import glob
from os.path import splitext, join
from docutils.core import publish_file

print("Creating the documentation...")

for rst_file in glob(join('DBUtils', 'Docs', '*.rst')):
    name = splitext(rst_file)[0]
    lang = splitext(name)[1]
    if lang.startswith('.'):
        lang = lang[1:]
        if lang == 'zh':
            lang = 'zh_cn'
    else:
        lang = 'en'
    html_file = name + '.html'
    print(name, lang)

    with open(rst_file) as source:
        with open(html_file, 'w') as destination:
            publish_file(writer_name='html5',
                source=source, destination=destination,
                settings_overrides = dict(
                    stylesheet_path='Doc.css',
                    embed_stylesheet=False,
                    toc_backlinks=False,
                    language_code=lang
                )
            )

print("Done.")
