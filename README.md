# Text_File_Cleaner
# class FileCleaner('myfile')		: requires a string input on creation.
# errors()				              : returns error messages 
# newLine('input')			        : make new line at string input value default='.', return file name 
# changeTo('chnage', 'to')		  : Change string input from to, return file name 
# splitBy(self, what = ' ')		  : Place text into list by defined split. Default = ' '. Return a list
# makeLowerCase(self)			      : make all alpha char lower case, return File name 
# makeUpperCase(self)			      : make all alpha char Upper case, return File name 
# pairSimilar(self, what = 'chr')		: pair all similar items: what = ('chr' or 'word' or 'sentence' or user input), returns diction(word : number)
# findKeys(self, keys, type = 'sentence' ): key word search. Return file name
# updateTxt(self, file)			    : over write original text file with new file. 
# makeFile(self, name)			    : make a new text file with the name
# delFile(self, name)			      : delete a text file
# clean()					              : clean text file and set new line at punctuation (!.?)
