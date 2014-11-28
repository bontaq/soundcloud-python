"""Python Soundcloud API Wrapper."""

__version__ = '0.4.1'
__all__ = ['Client']

# USER_AGENT = 'SoundCloud Python API Wrapper %s' % __version__
USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:28.0) Gecko/20100101 Firefox/28.0'

from soundcloud.client import Client
