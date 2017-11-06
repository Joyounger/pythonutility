#! /usr/bin/env python
#coding=utf-8
#version 2.7

import sys
import os
import time
import zipfile
import base64
import re
import xml.etree.ElementTree as ET
import hashlib
import shutil
reload(sys)
sys.setdefaultencoding('utf-8')


def readxml(xmlfilepath):
  tree = ET.parse(xmlfilepath)
  root = tree.getroot()
  for child in root:
    print child
    print child.tag
    print child.text
    print child.attrib
    
def writexml(xmlfilepath, rootelem):
  root = ET.Element(rootelem)
  xxx  = ET.SubElement(root, "xxx")
  xxx.text = ... 

  tree = ET.ElementTree(root)
  tree.write(xmlfilepath, encoding="UTF-8", xml_declaration=True)

def getrawbase64(binfilepath):
  bindata=[]
  base64file = open(os.path.dirname(binfilepath) + '/base64.txt', 'wb')
  base64.encode(open(binfilepath, 'rb'),  base64file)
  base64file.close()
  with file(os.path.dirname(binfilepath) + '/base64.txt', 'r') as f:
    for line in f.readlines():
      bindata.append(line.strip('\n'))  
  
  return bindata

def main():


if __name__ == '__main__':
  main()

