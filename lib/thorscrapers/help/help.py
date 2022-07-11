# -*- coding: utf-8 -*-
"""
	ThorScrapers Module
"""

from thorscrapers.modules.control import addonPath, addonVersion, joinPath
from thorscrapers.windows.textviewer import TextViewerXML


def get(file):
	thorscrapers_path = addonPath()
	thorscrapers_version = addonVersion()
	helpFile = joinPath(thorscrapers_path, 'lib', 'thorscrapers', 'help', file + '.txt')
	r = open(helpFile, 'r', encoding='utf-8', errors='ignore')
	text = r.read()
	r.close()
	heading = '[B]ThorScrapers -  v%s - %s[/B]' % (thorscrapers_version, file)
	windows = TextViewerXML('textviewer.xml', thorscrapers_path, heading=heading, text=text)
	windows.run()
	del windows