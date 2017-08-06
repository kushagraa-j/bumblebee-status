# pylint: disable=C0111,R0903

"""Displays the current date and time.

Parameters:
    * datetime.format: strftime()-compatible formatting string
    * date.format    : alias for datetime.format
    * time.format    : alias for datetime.format
    * datetime.locale: locale to use rather than the system default
    * date.locale    : alias for datetime.locale
    * time.locale    : alias for datetime.locale
"""

from __future__ import absolute_import
import datetime
import locale
import bumblebee.engine

ALIASES = [ "date", "time" ]

def default_format(module):
    default = "%x %X"
    if module == "date":
        default = "%x"
    if module == "time":
        default = "%X"
    return default

class Module(bumblebee.engine.Module):
    def __init__(self, engine, config):
        super(Module, self).__init__(engine, config,
            bumblebee.output.Widget(full_text=self.get_time))
        self._fmt = self.parameter("format", default_format(self.name))
        self._lcl = self.parameter("locale").split(".")

        # can't use the default in "parameter" because we split the
        # string, while 'getdefaultlocale' already returns a tuple
        if self._lcl is None:
            self._lcl = locale.getdefaultlocale()
        locale.setlocale(locale.LC_TIME, self._lcl)

    def get_time(self, widget):
        return datetime.datetime.now().strftime(self._fmt)

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
