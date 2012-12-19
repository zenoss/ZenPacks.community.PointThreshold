##########################################################################
# Author:               Ryan Matte, contact@ryanmatte.com
# Date:                 Oct 15th, 2012
# Revised:
#
# info.py for Point Threshold ZenPack
#
# This program can be used under the GNU General Public License version 2
# You can find full information here: http://www.zenoss.com/oss
#
################################################################################

__doc__="""info.py

Representation of Point Threshold components.

$Id: info.py,v 1.2 2010/12/14 20:45:46 jc Exp $"""

__version__ = "$Revision: 1.4 $"[11:-2]

from zope.interface import implements
from Products.Zuul.infos import ProxyProperty
from Products.Zuul.interfaces import template as templateInterfaces
from Products.Zuul.infos.template import ThresholdInfo
from Products.Zuul.decorators import info
from ZenPacks.community.PointThreshold import interfaces

class PointThresholdInfo(ThresholdInfo):
    implements(interfaces.IPointThresholdInfo)
    pointval = ProxyProperty("pointval")
    severity = ProxyProperty("severity")
    eventClass = ProxyProperty("eventClass")
    escalateCount = ProxyProperty("escalateCount")
