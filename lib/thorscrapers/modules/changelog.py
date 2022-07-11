# -*- coding: utf-8 -*-
"""
	ThorScrapers Module
"""

from thorscrapers.modules.control import addonPath, addonVersion, joinPath
from thorscrapers.windows.textviewer import TextViewerXML


def get():
	thorscrapers_path = addonPath()
	thorscrapers_version = addonVersion()
	changelogfile = joinPath(thorscrapers_path, 'changelog.txt')
	r = open(changelogfile, 'r', encoding='utf-8', errors='ignore')
	text = r.read()
	r.close()
	heading = '[B]ThorScrapers -  v%s - ChangeLog[/B]' % thorscrapers_version
	windows = TextViewerXML('textviewer.xml', thorscrapers_path, heading=heading, text=text)
	windows.run()
	del windows