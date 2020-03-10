list =[('The result of the application level question is ', 'Candidate has not given an answer. The score is 0'), ('The result of the application level question is ', 'Candidate has not given an answer. The score is 0')]
string = str(list)
newlist1 = string.split(')')
string1 = str(newlist1)
newlist2 = string1.split('(')
string2 = str(newlist2)
newstring1 = ('\n'.join(newlist2))
print(newstring1)