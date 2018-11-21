#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This script gets all the instruments and effects used for every track of a Logic Pro X project.
#
# Before running this script you must enable accessibility for the calling app (e.g. Terminal):
# System Preferences > Security & Privacy > Privacy tab > Add button (+)
#
# Doesn't work with Logic Pro X version 10.0.6 because not accessible enough.
# Works with version 10.4.1 (tested). Might work with versions as old as 10.1 (not tested).
#
#################################################################################################
import os
import sys
import time
import atomac # sudo easy_install atomac
import subprocess
import json

def getTrackInfo(track):
	# Get information from mixer strips (the slices to the left of the tracks)
	# The first one is the the left strip, the second one is the Master strip
	mixerStrip = mainWindow.findFirstR(AXRole='AXGroup', AXRoleDescription='groupe de tranche de console')
	print 'Found mixer strip: ' + mixerStrip.AXDescription

	# Last group is the generator (instrument)
	generatorGroup = mixerStrip.findAll(AXRole='AXGroup', AXRoleDescription='groupe')[-1]
	instrumentName = generatorGroup.AXDescription # The name of the instrument
	isInstrumentEnabled = generatorGroup.AXChildren[0].AXValue # Whether the instrument is enabled (1 or 0)
	print 'Instrument=' + instrumentName

	# Get audio effects
	audioEffects = []
	effectsGroups = mixerStrip.findAllR(AXRole='AXGroup', AXRoleDescription='groupe', AXTitle='Effet audio')
	for effectGroup in effectsGroups:
		if len(effectGroup.AXChildren) < 3:
			continue # This is the empty slot for adding a new Audio Effect
		audioEffectName = effectGroup.AXDescription
		isAudioEffectEnabled = effectGroup.AXChildren[0].AXValue
		audioEffects.append({'effectName': audioEffectName, 'isEnabled': isAudioEffectEnabled})
		print 'AudioEffect=' + audioEffectName

	return {'instrumentName': instrumentName, 'isEnabled': isInstrumentEnabled, 'audioEffects': audioEffects}

def getCleanTrackName(trackDescription):
	# Convert "Piste 1 « Piano »" to "Piste 1 - Piano"
	return trackDescription.replace(u'«', '- ').replace(u'»', '').replace(u'\u00a0', '')

# Entry point
print 'Bringing Logic to foreground...'
logic = atomac.getAppRefByBundleId('com.apple.logic10')
logic.activate()
time.sleep(1)
mainWindow =  logic.findFirst(AXSubrole='AXStandardWindow') 

# Get the list of tracks
tracks = []
tracksContainer = mainWindow.findFirstR(AXRole='AXGroup', AXRoleDescription='groupe', AXDescription=u'Pistes en-tête')
print 'Found ' + str(len(tracksContainer.AXChildren)) + ' tracks'
for track in tracksContainer.AXChildren:
	try:
		print 'Processing track: ' + track.AXDescription
		track.Press()
		time.sleep(0.6)
		tracks.append({'trackName': getCleanTrackName(track.AXDescription), 'trackInfo': getTrackInfo(track)})
		print ''
	except:
		pass
print json.dumps(tracks)