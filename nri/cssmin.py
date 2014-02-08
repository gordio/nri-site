from __future__ import unicode_literals

from pipeline.conf import settings
from pipeline.compressors import SubProcessCompressor
import cssmin


class CSSMinCompressor(SubProcessCompressor):
    def compress_css(self, css):
        return cssmin.cssmin(css)
