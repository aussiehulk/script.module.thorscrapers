# -*- coding: utf-8 -*-
"""
	ThorScrapers Module
"""

from sys import argv
from urllib.parse import parse_qsl
from thorscrapers import sources_thorscrapers
from thorscrapers.modules import control

params = dict(parse_qsl(argv[2].replace('?', '')))
action = params.get('action')
mode = params.get('mode')
query = params.get('query')
name = params.get('name')

if action is None:
	control.openSettings('0.0', 'script.module.thorscrapers')

if action == "thorScrapersSettings":
	control.openSettings('0.0', 'script.module.thorscrapers')

elif mode == "thorScrapersSettings":
	control.openSettings('0.0', 'script.module.thorscrapers')

elif action == 'ShowChangelog':
	from thorscrapers.modules import changelog
	changelog.get()

elif action == 'ShowHelp':
	from thorscrapers.help import help
	help.get(name)

elif action == "Defaults":
	sourceList = []
	sourceList = sources_thorscrapers.all_providers
	for i in sourceList:
		source_setting = 'provider.' + i
		value = control.getSettingDefault(source_setting)
		control.setSetting(source_setting, value)

elif action == "toggleAll":
	sourceList = []
	sourceList = sources_thorscrapers.all_providers
	for i in sourceList:
		source_setting = 'provider.' + i
		control.setSetting(source_setting, params['setting'])

elif action == "toggleAllHosters":
	sourceList = []
	sourceList = sources_thorscrapers.hoster_providers
	for i in sourceList:
		source_setting = 'provider.' + i
		control.setSetting(source_setting, params['setting'])

elif action == "toggleAllTorrent":
	sourceList = []
	sourceList = sources_thorscrapers.torrent_providers
	for i in sourceList:
		source_setting = 'provider.' + i
		control.setSetting(source_setting, params['setting'])

elif action == "toggleAllPackTorrent":
	control.execute('RunPlugin(plugin://script.module.thorscrapers/?action=toggleAllTorrent&amp;setting=false)')
	control.sleep(500)
	sourceList = []
	from thorscrapers import pack_sources
	sourceList = pack_sources()
	for i in sourceList:
		source_setting = 'provider.' + i
		control.setSetting(source_setting, params['setting'])

elif action == 'openMyAccount':
	from myaccounts import openMASettings
	openMASettings('0.0')
	control.sleep(500)
	while control.condVisibility('Window.IsVisible(addonsettings)') or control.homeWindow.getProperty('myaccounts.active') == 'true':
		control.sleep(500)
	control.sleep(100)
	control.syncMyAccounts()
	control.sleep(100)
	if params.get('opensettings') == 'true':
		control.openSettings(query, 'script.module.thorscrapers')

elif action == 'syncMyAccount':
	control.syncMyAccounts()
	if params.get('opensettings') == 'true':
		control.openSettings(query, 'script.module.thorscrapers')

elif action == 'cleanSettings':
	control.clean_settings()

elif action == 'undesirablesSelect':
	from thorscrapers.modules.undesirables import undesirablesSelect
	undesirablesSelect()

elif action == 'undesirablesInput':
	from thorscrapers.modules.undesirables import undesirablesInput
	undesirablesInput()

elif action == 'undesirablesUserRemove':
	from thorscrapers.modules.undesirables import undesirablesUserRemove
	undesirablesUserRemove()

elif action == 'undesirablesUserRemoveAll':
	from thorscrapers.modules.undesirables import undesirablesUserRemoveAll
	undesirablesUserRemoveAll()

elif action == 'tools_clearLogFile':
	from thorscrapers.modules import log_utils
	cleared = log_utils.clear_logFile()
	if cleared == 'canceled': pass
	elif cleared: control.notification(message='ThorScrapers Log File Successfully Cleared')
	else: control.notification(message='Error clearing ThorScrapers Log File, see kodi.log for more info')

elif action == 'tools_viewLogFile':
	from thorscrapers.modules import log_utils
	log_utils.view_LogFile(name)

elif action == 'tools_uploadLogFile':
	from thorscrapers.modules import log_utils
	log_utils.upload_LogFile()