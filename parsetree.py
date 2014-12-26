#! /usr/bin/python

from xml.etree.ElementTree import parse
import xml.etree.ElementTree

Etree = parse("movies.xml")

movieNode = Etree.findall("movie")
for i in range(len(movieNode)):
	print("*****Movie*****")
	print("Title: %s" % movieNode[i].attrib['title'])
	
	#typeNode = Etree.getiterator("type")
	#print(typeNode[i].text)
	typeNode = Etree.findall("movie/type")
	print("Type: %s" % typeNode[i].text)
	
	formatNode = Etree.findall("movie/format")
	print("Format: %s" % formatNode[i].text)
	
	ratingNode = Etree.findall("movie/rating")
	print("Rating: %s" % ratingNode[i].text)
	
	descriptionNode = Etree.findall("movie/description")
	print("Description: %s" % descriptionNode[i].text)