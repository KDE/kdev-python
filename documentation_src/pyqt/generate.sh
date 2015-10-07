# Copyright 2014 Sven Brauch <svenbrauch@gmail.com>
# License: GPL v2+

pyqt=($(ls /usr/share/sip/PyQt5))
element_count=${#pyqt[@]}
for index in $(seq $element_count); do
    python2.7 sip_to_xml5.py ${pyqt[$index]}
    python2.7 xml_to_py.py ${pyqt[$index]}.xml
    cp ${pyqt[$index]}.py ../../documentation_files/PyQt5/
done

# mkdir -p ../../documentation_files/PyKDE4
# pykde=($(ls /usr/share/sip/python2-PyKDE4))
# element_count=${#pykde[@]}
# for index in $(seq $element_count); do
#     python2.7 sip_to_xml.py python2-PyKDE4/${pykde[$index]}
#     python2.7 xml_to_py.py ${pykde[$index]}.xml
#     cp ${pykde[$index]}.py ../../documentation_files/PyKDE4/
# done

# sed -i 's/typename=" dir="out"/dir="out" typename="None"/g' *.xml
# sed -i 's/SLOT()SLOT()/SLOT()/g' *.xml
