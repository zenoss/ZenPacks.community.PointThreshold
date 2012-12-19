##########################################################################
# Author:               Ryan Matte, contact@ryanmatte.com
# Date:                 Oct 15, 2012
# Revised:
#
# interfaces.py for Point Threshold ZenPack
#
# This program can be used under the GNU General Public License version 2
# You can find full information here: http://www.zenoss.com/oss
#
################################################################################

__doc__="""interfaces.py

Representation of Point Threshold components.

$Id: info.py,v 1.2 2010/12/14 20:45:46 jc Exp $"""

__version__ = "$Revision: 1.4 $"[11:-2]

from Products.Zuul.interfaces import IInfo, IFacade
from Products.Zuul.interfaces.template import IThresholdInfo
from Products.Zuul.form import schema
from Products.Zuul.utils import ZuulMessageFactory as _t

class IPointThresholdInfo(IThresholdInfo):
    """
    Interfaces for Point Threshold
    """
    escalateCount = schema.Int(title=_t(u'Escalate Count'), order=2)
    pointval = schema.Text(title=_t(u'Point Value'), order=20)
