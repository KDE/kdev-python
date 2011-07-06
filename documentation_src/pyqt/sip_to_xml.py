#!/usr/bin/env python2.7
# This file is part of KDevelop
# Copyright 2011 by Victor Varvariuc <victor.varvariuc@gmail.com>

import os, subprocess
from xml.dom import minidom, NotFoundErr

import sipconfig
from PyQt4 import pyqtconfig

qtgui_outfile = 'QtGuimod.xml'
qtgui_infile = '/usr/share/sip/PyQt4/QtGui/QtGuimod.sip'
qtcore_outfile = 'QtCoremod.xml'
qtcore_infile = '/usr/share/sip/PyQt4/QtCore/QtCoremod.sip'

config = pyqtconfig.Configuration() # Get the PyQt configuration information.

for infileName, outfileName in [(qtgui_infile, qtgui_outfile), (qtcore_infile, qtcore_outfile)]:
    command = [config.sip_bin, '-m', outfileName, '-I', config.pyqt_sip_dir]
    command.extend(config.pyqt_sip_flags.split())
    command.append(infileName)

    fileName = outfileName

    print ' '.join(command)
    try:
        print subprocess.check_output(command, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
        print 'There was an error when running the command:'
        print e.output


    print 'Opening and parsing XML document...'
    xmlDoc = minidom.parse(fileName)

    module = xmlDoc.firstChild
    assert module.nodeName == 'Module'
    moduleName = module.attributes['name'].value
    print 'Module name: %s' % moduleName

    def setIds(node):
        '''Set `name` attribute as id to be able to do node.getElementById('element_id')'''
        for node in node.childNodes:
            if node.nodeType == node.ELEMENT_NODE: # only element nodes
                try:
                    node.setIdAttribute('name') 
                except NotFoundErr:
                    pass
                setIds(node)

    print 'Setting IDs...'
    setIds(module) # recursively set IDs

    print 'Looking for child classes...'
    childClasses = {}
    for node in module.childNodes:
        if node.nodeType == node.ELEMENT_NODE: # skip non element nodes
            if node.nodeName == 'Class':
                name = node.attributes['name'].value
                dotsCount = name.count('.')
                if dotsCount:
                    if dotsCount == 1:
                        childClasses[name] = node
                    else:
                        raise Exception('More than 2 dots in name of a class: %s' % name)

    print 'Reparenting classes...'
    for name, node in childClasses.iteritems():
        parentClassName = name.split('.')[0]
        parentClassNode = xmlDoc.getElementById(parentClassName)
        parentClassNode.appendChild(node)

    print 'Saving changes...'
    with open(fileName, 'w') as f:
        xmlDoc.writexml(f)

