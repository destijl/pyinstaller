#-----------------------------------------------------------------------------
# Copyright (c) 2013, PyInstaller Development Team.
#
# Distributed under the terms of the GNU General Public License with exception
# for distributing bootloader.
#
# The full license is in the file COPYING.txt, distributed with this software.
#-----------------------------------------------------------------------------


# Qt5 plugins are bundled as data files (see hooks/hook-PyQt5*),
# within a "qt5_plugins" directory.
# We add a runtime hook to tell Qt5 where to find them.

import os
import sys

meipass_dir = getattr(sys, '_MEIPASS', os.path.dirname(sys.executable))
d = os.path.join(meipass_dir, "qt5_plugins")


# We remove QT_PLUGIN_PATH variable, because we want Qt5 to load
# plugins only from one path.
if 'QT_PLUGIN_PATH' in os.environ:
    # On some platforms (e.g. AIX) 'os.unsetenv()' is not available and then
    # deleting the var from os.environ does not delete it from the environment.
    # In those cases we cannot delete the variable but only set it to the
    # empty string.
    os.environ['QT_PLUGIN_PATH'] = ''
    del os.environ['QT_PLUGIN_PATH']


# We cannot use QT_PLUGIN_PATH here, because it would not work when
# PyQt5 is compiled with a different CRT from Python (eg: it happens
# with Riverbank's GPL package).
from PyQt5.QtCore import QCoreApplication
# We set "qt5_plugins" as only one path for Qt5 plugins
QCoreApplication.setLibraryPaths([os.path.abspath(d)])
