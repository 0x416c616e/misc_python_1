#!/usr/bin/env python3
#Book class
#demonstrates the use of @classmethod decorators as a python-ish alternative
#to overloading constructors, which isn't possible in python, but it is a thing
#you can do in java (I am converting this code from my original java program)
class Book:
	def __init__(self, title, author):
		self.title = title
		self.author = author
		self.tableOfContents = ""
		self.nextPage = 1
	def __str__(self):
		return 'Book({0}, {1}, {3})\nTable of contents:{2}'.format(self.title, self.author, self.tableOfContents, self.nextPage)
	def addChapter(self, chapterTitle, numPagesInChapter):
		self.tableOfContents = self.tableOfContents + "\n" + chapterTitle + "..." + str(self.nextPage)
		self.nextPage += numPagesInChapter
	def getPages(self):
		return nextPage -1
	def getTableOfContents(self):
		return self.tableOfContents
	def setTitle(self, newTitle):
		self.title = newTitle
	def setAuthor(self, newAuthor):
		self.author = newAuthor
	@classmethod
	def alt_constructor(class_object):
		#print(class_object)
		return class_object("sample title", "sample author")
book1 = Book("alan's book", "alan")
book2 = book1.alt_constructor()
book2.addChapter("Introduction", 47)
book2.addChapter("How to program in Python", 100)
book2.addChapter("How to be awesome", 42)
book2.addChapter("Glossary", 20)
print(book2)
print(book1)
print("this lets you sort of use 2 constructors, but not really")
print("python is not java, but I am used to java more than python")