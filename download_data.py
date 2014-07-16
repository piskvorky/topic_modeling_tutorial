#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2014 Radim Rehurek <me@radimrehurek.com>
# Licensed under the GNU LGPL v2.1 - http://www.gnu.org/licenses/lgpl.html

"""
USAGE: %(program)s OUTPUT_DIRECTORY URL1 [URL2 ...]

Download all files pointed at by the given URLs, into OUTPUT_DIRECTORY (which must already exist).

Files are downloaded in chunked streams, so large files are OK too.

Example:
    python download_data.py ./data 'http://people.csail.mit.edu/jrennie/20Newsgroups/20news-bydate.tar.gz' 'http://dumps.wikimedia.org/simplewiki/20140623/simplewiki-20140623-pages-articles.xml.bz2'

"""


import os
import sys
import logging

import requests

logger = logging.getLogger("download_data")

DEFAULT_URLS = [
    'http://people.csail.mit.edu/jrennie/20Newsgroups/20news-bydate.tar.gz',
    'http://dumps.wikimedia.org/simplewiki/20140623/simplewiki-20140623-pages-articles.xml.bz2'
]


def download_file(url, out_fname):
    logger.info("downloading %s into %s" % (url, out_fname))
    r = requests.get(url, stream=True)
    total_len = 0
    with open(out_fname, 'wb') as fout:
        for chunk in r.iter_content(chunk_size=1024**2, decode_unicode=False):
            if chunk:
                fout.write(chunk)
                fout.flush()
                total_len += len(chunk)
    logger.info("downloaded %i bytes" % (total_len))


if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s : %(threadName)s : %(levelname)s : %(message)s', level=logging.INFO)
    logging.info("running %s" % " ".join(sys.argv))

    # check and process cmdline input
    program = os.path.basename(sys.argv[0])
    if len(sys.argv) < 3:
        print(globals()['__doc__'] % locals())
        sys.exit(1)
    outdir = sys.argv[1]
    urls = sys.argv[2:]

    # download each URL in turn
    for url in urls or DEFAULT_URLS:
        outname = os.path.join(outdir, url.split('/')[-1])
        try:
            download_file(url, outname)
        except:
            logging.exception("failed to process url '%s'" % (url))

    logging.info("finished running %s" % program)
