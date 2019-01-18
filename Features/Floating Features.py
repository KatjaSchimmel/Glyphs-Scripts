#MenuTitle: Floating Features
# -*- coding: utf-8 -*-
__doc__="""
Floating window for activating features in the frontmost Edit tab.
"""

import vanilla, traceback

class FeatureActivator( object ):
	def __init__( self ):
		featurelist = [ f.fullName() for f in Glyphs.font.features ]
		numOfFeatures = len( featurelist )
		
		self.w = vanilla.FloatingWindow( (150, 10+numOfFeatures*18 ), "", autosaveName="com.mekkablue.FeatureActivator.mainwindow" )
		
		for i in range( numOfFeatures ):
			exec("self.w.featureCheckBox_"+str(i+1)+" = vanilla.CheckBox( (8, "+str(4+18*i)+", -8, 18), '"+featurelist[i]+"', sizeStyle='small', callback=self.toggleFeature, value="+str(featurelist[i] in Glyphs.currentDocument.windowController().activeEditViewController().selectedFeatures())+" )")
				
		self.w.open()
		
	def toggleFeature( self, sender ):
		try:
			editTab = Glyphs.currentDocument.windowController().activeEditViewController()
			featureName = sender.getTitle()
			featureActive = bool(sender.get())
			
			if featureActive:
				# add the feature:
				editTab.selectedFeatures().append(featureName)
			else:
				# remove the feature:
				try:
					while True:
						editTab.selectedFeatures().remove(featureName)
				except:
					pass
			
			editTab.graphicView().reflow()
			editTab.graphicView().layoutManager().updateActiveLayer()
			editTab._updateFeaturePopup()
			editTab.updatePreview()
		except Exception, e:
			print e
			print traceback.format_exc()
			return False
			
		return True


FeatureActivator()
