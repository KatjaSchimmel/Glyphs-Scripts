#MenuTitle: Show masters of previous glyph
# -*- coding: utf-8 -*-
__doc__="""
Shows all masters for the previous glyph.
"""


from PyObjCTools.AppHelper import callAfter

zeroPosition = NSRange()
zeroPosition.location = 0
zeroPosition.length = 0

def showAllMastersOfGlyphInCurrentTab( thisGlyphName ):
	try:
		escapedGlyphName = "/" + thisGlyphName
		thisDoc = Glyphs.currentDocument
		thisWindow = thisDoc.windowController()
		thisEditView = thisWindow.activeEditViewController() # current tab
		
		if thisEditView is None:
			# opens new Edit tab if none was open:
			callAfter( thisWindow.addTabWithString_, escapedGlyphName )
		else:
			thisGraphicView = thisEditView.graphicView() # current display string
			thisGraphicView.setDisplayString_( escapedGlyphName ) # set the display string to this glyph
			thisGraphicView.setSelectedRange_( zeroPosition ) # moves the cursor to beginning
			thisEditView.insertAllMasters_( None ) # insert all masters

		return True
	except Exception as e:
		print e
		return False

thisFont = Glyphs.font # frontmost font
currentLayer = thisFont.selectedLayers[0]
currentGlyph = currentLayer.parent
currentGlyphIndex = currentGlyph.glyphId()
newGlyphIndex = currentGlyphIndex - 1
newGlyphName = thisFont.glyphs[newGlyphIndex].name

if not showAllMastersOfGlyphInCurrentTab( newGlyphName ):
	print "Error: could not insert masters of %s in current edit tab." % newGlyphName
