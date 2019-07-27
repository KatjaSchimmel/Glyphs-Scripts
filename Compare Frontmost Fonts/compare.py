# -*- coding: utf-8 -*-

def compareLists(thisSet, otherSet, ignoreEmpty=False):
	for i in range(len(thisSet))[::-1]:
		if thisSet[i] in otherSet:
			otherSet.remove( thisSet.pop(i) )
		elif ignoreEmpty:
			if not thisSet[i]:
				thisSet.pop(i)
				
	for i in range(len(otherSet))[::-1]:
		if otherSet[i] in thisSet:
			thisSet.remove( otherSet.pop(i) )
		elif ignoreEmpty:
			if not otherSet[i]:
				otherSet.pop(i)
				
	return thisSet, otherSet

def cleanUpAndShortenParameterContent( thisParameter, maxLength=20 ):
	parameterContent = unicode(repr(thisParameter))
	if len(parameterContent) > maxLength:
		parameterContent = u"%s..." % parameterContent[:maxLength].replace(u"\n",u" ")
	while u"  " in parameterContent:
		parameterContent = parameterContent.replace(u"  ",u" ")
	return parameterContent

def compareCount( things, thisCount, otherCount, thisName, otherName ):
	if thisCount != otherCount:
		print u"❌ Different number of %s:" % things.upper()
		print u"   A. %i %s in %s" % (thisCount, things.lower(), thisName)
		print u"   B. %i %s in %s" % (otherCount, things.lower(), otherName)
	else:
		print u"✅ Compatible number of %s: %i." % (things.lower(), thisCount)

def lineReport(thisSet, otherSet, thisFileName, otherFileName, name):
	if thisSet or otherSet:
		if otherSet:
			print
			print u"⚠️ Code lines not in %s of %s:" % (name, thisFileName)
			for line in otherSet:
				print "  %s" % line
			print
		if thisSet:
			print
			print u"⚠️ Code lines not in %s of %s:" % (name, otherFileName)
			for line in thisSet:
				print "  %s" % line
			print
	else:
		print u"💚 %s: same code in both fonts." % name
