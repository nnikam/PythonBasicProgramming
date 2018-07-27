import re 

"""
\d= Any digit [0-9]
\D= Anything other than digit
\w= Any Word character ([a-z] [A-Z] [0-9] ) 
\W=Not a word character 
\s= WhiteSpace (space,tab,Newline)
\S=Not a Whitespace 
"""

#this is the text to be search 
text_to_search = """
nitin.nikam@gmail.com
nikam123213-nikam@india.edu
testdata998080_@test.net
"""

#Create the Pattern to search here we are trying to search the emails
pattern = re.compile(r"[a-zA-Z0-9.-_]+[a-zA-Z]*@[a-z]+\.(com|edu|net)")

matches = pattern.finditer(text_to_search)

for match in matches:
  print(match)