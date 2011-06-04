#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
import sqlite3
import os
import shutil

import sqlite3

conn = sqlite3.connect('documentation.db')
c = conn.cursor()

basepath = "../documentation_files/"

def indent(code):
    l = []
    for line in code.split("\n"):
        l.append("\t" + line)
    return "\n".join(l) + "\n"

def sanitize(expr):
    replace = {
        '*':'', '[':'', ']':'',
        'from':'_from', 'class':'_class', '-':'_',
        '\\':'ESC', ' ':'', "<":'"', ">":'"', "self,":"", "self":"",
        ",,":","
    }
    result = expr
    for before, after in replace.iteritems():
        result = result.replace(before, after)
    result = result.replace("=,", "=[],").replace("=)", "=[])")
    return result

def strict_sanitize(expr):
    expr = sanitize(expr)
    expr = expr.replace("=()", "")
    expr = expr.replace('(', '').replace(')', '')
    return expr

def add_self_arg(expr):
    if expr.find('self') == -1:
        l = expr.split('(')
        expr = l[0] + '(self, ' + '('.join(l[1:])
    return expr

class DocumentationExporter:
    def run(self):
        modules = c.execute("SELECT * FROM modules")
        for module, documentation in c.fetchall():
            moduleDocumentation = "#!/usr/bin/env python2.7\n# -*- coding: utf-8 -*-\n"
            filepath = basepath + module.replace('.', '/') + ".py"
            directory = basepath + '/'.join(module.split('.')[:-1])
            print " » processing module:", module, "->", filepath, "@", directory
            if directory != basepath and not os.path.exists(directory):
                os.makedirs(directory)  
            moduleDocumentation += '"""' + documentation.replace('"""', ' " " " ') + '"""\n'
            
            # add all the properties with their documentation
            c.execute("SELECT * FROM moduleproperties WHERE modulename=?", [module])
            for trash, propertyname, documentation in c.fetchall():
                moduleDocumentation += '"""' + documentation.replace('"""', ' " " " ') + '"""\n'
                moduleDocumentation += strict_sanitize(propertyname) + " = None\n"
            
            # add methods
            c.execute("SELECT * FROM modulefunctions WHERE modulename=?", [module])
            for trash, methodname, documentation in c.fetchall():
                brackets = "" if methodname.find('(') != -1 else "()"
                moduleDocumentation += "def " + sanitize(methodname) + brackets + ":\n"
                moduleDocumentation += indent('"""' + documentation.replace('"""', ' " " " ') + '"""\npass\n')
                
            # add classes and classmethods
            c.execute("SELECT * FROM classes WHERE modulename=?", [module])
            for trash, classname, documentation in c.fetchall():
                moduleDocumentation += "class " + classname.split("(")[0] + ":\n"
                classDocumentation = '"""' + documentation.replace('"""', ' " " " ') + '"""\n'
                classDocumentation += "\n\ndef __init__(self, " + sanitize(''.join(classname.split("(")[1:])).replace(")", "")
                classDocumentation += "):\n\tpass\n\n"
                c.execute("SELECT * FROM methods WHERE modulename=? and classname=?", [module, classname.split('(')[0]])
                for trash, trash, methodname, documentation in c.fetchall():
                    brackets = "" if methodname.find('(') != -1 else "()"
                    classDocumentation += "def " + add_self_arg(sanitize(methodname)) + brackets + ":\n"
                    classDocumentation += indent('"""' + documentation.replace('"""', ' " " " ') + '"""\npass\n')
                c.execute("SELECT * FROM properties WHERE modulename=? and classname=?", [module, classname.split('(')[0]])
                for trash, trash, propertyname, documentation in c.fetchall():
                    classDocumentation += '"""' + documentation.replace('"""', ' " " " ') + '"""\n'
                    classDocumentation += propertyname + " = None\n"
                moduleDocumentation += "\n\n" + indent(classDocumentation) + "\n\n"
            
            with open(filepath, "w") as f: f.write(moduleDocumentation.encode("utf-8"))

if __name__ == '__main__':
    d = DocumentationExporter()
    d.run()

c.close()
conn.close()