#!/usr/bin/python


## RESIN 3.2.2 ################################################################
#created by James Sanders
#http://www.jamessanders.info/resin
#please send bug reports on this file to James Sanders (jimmyjazz14@gmail.com)
#build date: Mon, 14 May 2007 19:41:14 +0000
###########################################################################


#Automatix2 written and maintained by James Sanders (jimmyjazz14@gmail.com)
#modifications to this file should be send to jimmyjazz14@gmail.com
#RESIN: 3.2.2
#Thu Sep 28 17:04:32 2006
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.
import sys
if len(sys.argv) < 2:
	print "You can't run Automatix like this try '/usr/bin/automatix2' instead"
	sys.exit()
sys.path += ["/usr/lib/automatix2"]
from resin_config import *
sys.path += [axConf.locations['modules']]
automatix_version = "Automatix version: 1.1-4.4"
resin_version = "Resin version: 3.2.2"
if '-v' in sys.argv:
	print automatix_version
	print resin_version
	sys.exit()
if '-e' in sys.argv or '--dumplog' in sys.argv:
	try:
		dump = open("%s/.automatix/activity.log"%axUser.home).readlines()
	except:
		print "No activity log was found"
		sys.exit()
	for d in dump:
		print d,
	sys.exit()
if '-h' in sys.argv  or '--help' in sys.argv:
	print """
	Automatix 1.1-4.4
	possible commands...
	-v				dump version info
	-e	--dumplog		dump activity log
	-h	--help			this help message
	"""
	sys.exit()
from startup import *
start = startUp()
from main_interface import *
main = main_ui()
gtk.main()

