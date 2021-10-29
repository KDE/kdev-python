#!/usr/bin/env python
# This file is part of KDevelop
# SPDX-FileCopyrightText: 2011 Victor Varvariuc <victor.varvariuc@gmail.com>
# SPDX-FileCopyrightText: 2011 Sven Brauch <svenbrauch@googlemail.com>

import os, sys, subprocess
from xml.dom import minidom, NotFoundErr

import PyQt5.QtCore
sipBin = '/usr/bin/sip'
sipDir = '/usr/share/sip/PyQt5'
sipFlags = PyQt5.QtCore.PYQT_CONFIGURATION['sip_flags']

def convertSipToXML(inFilePath, outFilePath):
    command = [sipBin, '-m', outFilePath, '-I', sipDir]
    command.extend(sipFlags.split())
    command.append(inFilePath)

    print('\nConverting sip to xml:\n%s' % ' '.join(command))
    try:
        print(subprocess.check_output(command, stderr = subprocess.STDOUT))
    except subprocess.CalledProcessError as e:
        print('There was an error when running the command:')
        print(e.output)

    print('Opening and parsing XML document...')
    #replace the invalid "&"s which are used by pykde to indicate shortcuts
    #they would need to be escaped, but oh well
    f = open(outFilePath, 'r')
    data = f.read()
    f.close()
    data = data.replace('&', '')
    data = data.replace('("', '')
    data = data.replace('")', '')
    #data = data.replace('""', '"')
    f = open(outFilePath, 'w')
    f.write(data)
    f.close()
    xmlDoc = minidom.parse(outFilePath)

    module = xmlDoc.firstChild
    assert module.nodeName == 'Module'
    moduleName = module.attributes['name'].value
    print('Module name: %s' % moduleName)

    def setIds(node):
        '''Set `name` attribute as id to be able to do node.getElementById('element_id')'''
        for node in node.childNodes:
            if node.nodeType == node.ELEMENT_NODE: # only element nodes
                try:
                    node.setIdAttribute('name')
                except NotFoundErr:
                    pass
                setIds(node)

    print('Setting IDs...')
    setIds(module) # recursively set IDs

    print('Looking for child classes...')
    childClasses = {}
    for node in module.childNodes:
        # skip non element nodes
        if node.nodeType == node.ELEMENT_NODE and node.nodeName == 'Class':
            name = node.attributes['name'].value
            if name.count('.') >= 1:
                childClasses[name] = node

    print('Reparenting classes...')
    for name, node in childClasses.iteritems():
        parentClassNode = xmlDoc
        parentClassNode = xmlDoc.getElementById(name.split('.')[0])
        for component in name.split('.')[1:-1]:
            previous = parentClassNode
            parentClassNode = xmlDoc.createElement("Class")
            parentClassNode.setAttribute("name", component)
            parentClassNode.setAttribute("convert", "1")
            previous.appendChild(parentClassNode)
            print("new class:", component)
        node.setAttribute("name", name.split('.')[-1])
        parentClassNode.appendChild(node)

    print('Saving changes...')
    with open(outFilePath, 'w') as f:
        xmlDoc.writexml(f)


if not os.path.isdir(sipDir):
    print('Could not find sip direcotry: %s' % sipDir)
    print('Looks like package "python-qt-dev" is not installed.')
    sys.exit()

modules = sys.argv[1:] # ['QtGui.xml', 'QtCore.xml'] # files to convert

for moduleName in modules:
    sipFilePath = os.path.join(sipDir, moduleName, moduleName.split('/')[-1] + 'mod.sip')
    xmlFilePath = moduleName + '.xml'
    if os.path.isfile(sipFilePath) or os.path.exists(xmlFilePath.split('/')[-1]):
        convertSipToXML(sipFilePath, xmlFilePath.split('/')[-1])
    else:
        print('Input sip file does not exist: %s' % sipFilePath)
