from __future__ import unicode_literals

import os

from django.contrib.staticfiles.finders import BaseStorageFinder

from .storage import JSPMFileStorage


class SystemFinder(BaseStorageFinder):
    """
    A staticfiles finder that looks in STATIC_ROOT for jspm files.

    Inspired by the CompressorFinder from django-compressor.
    """
    storage = JSPMFileStorage

    def find(self, path, all=False):
        """
        Only allow lookups for jspm_packages.

        # TODO: figure out the 'jspm_packages' dir from packag.json.
        """
        bits = os.path.split(path)
        if not bits or bits[0] != 'jspm_packages':
            return []
        return super(SystemFinder, self).find(path, all=all)

    def list(self, ignore_patterns):
        # skip this finder alltogether during collectstatic
        return []