# Regex Notes
Notes on Regex taken from the book 'Automate the Boring Stuff' by Al Sweigart.  
Chapter 7, page 164 - 186 
<br>
* All regex functions are in the **re** module. **Import re** to use regex.
* The regex **'\d'** stands for a digit character, representing any numeral from 0 to 9. The following expression is one example of an expression that looks for a 10 digit phone number:  

```python
\d\d\d-\d\d\d-\d\d\d\d
```
* Adding a numeral in braces, for example: **{3}**, after a pattern looks for the pattern three times. It is the same expression as the one above.

```python
\d{3}-\d{3}-\d{4}
```
* Passing a raw string value representing your regular expression to **re.compile** returns a Regex pattern object.
```python
phoneRegex = re.compile(r'\d{3}-\d{3}-\d{4}')
```
* Regex objects have a *search()* method that, when passed with a string, returns None if the regex pattern is not found, or returns a Match object if found. 
The match object will have a *group()* method which will return the matched text from the searched string.
```python
phoneRegex = re.compile(r'\d{3}-\d{3}-\d{4}')
mo = phoneNumRegex.search('My number is 230-220-3330')
print('Phone number found: ' + mo.group())
```
<br>  

#### Review: Basic Regex
1. Import regex module using **import re**
2. Create regex object using **regexVar = re.compile('raw string')**
3. Get a match object by using the regex object's **search()** method
4. Call the match object's **group()** method to return string of matched text  
<br>  

* Adding parentheses around a regex pattern will create groups. You can use the **group()** method to then access a group.
```python
phoneRegex = re.compile(r'(\d{3})-(\d{3}-\d{4})')
mo = phoneRegex.search('My number is 233-330-3330')
print(mo.group(1)) #Will print '233'
print(mo.group(2)) #Will print '330-3330'
print(mo.group(0)) #Will print '233-330-3330'
print(mo.group()) #Same as mo.group(0)
```
* **mo.groups** returns a tuple of multiple values. You can assign them to variables by unpacking
```python
var1, var2 = mo.groups()
```

* The pipe **|** can be used to match one of multiple expressions. The first occurence of matching text is saved if all multiple expressions match.
```python
groceries = re.compile(r'Bacon|Eggs')
gro1 = groceries.search('Bacon and Eggs')
gro1.group() # Will be 'Bacon' since 'Bacon' is first

gro2 = groceries.search('Eggs and Bacon')
gro2.group() # Will be 'Eggs' since 'Eggs' is first
```
* You can use the pipe to match one of several patterns using parenthesis.
```python
biRegex = re.compile(r'bi(frost|cycle|nary|weekly)')
```
* Use a **?** question mark after a group if you want to match a pattern optionally.
```python
superRegex = re.compile(r'(super)?man') # will match with either 'superman' or 'man'
```
* An asterisk **\*** after a group indicates that a group can appear zero or more times in a text. A plus **\+** indicates a group must appear at least once.
* Follow an expression with a number in brackets to find a pattern that is repeated a certain number of times. Python regular expressions are greedy **(page 171)**
```python
blahRegex = re.compile(r'(blah){3}') # Will find 'blahblahblah' but not 'blahblah'
blahRegex1 = re.compile(r'(blah){3, 5}') # Will find 'blahblahblah', 'blahblahblahblah', and 'blahblahblahblahblah'
blahRegex2 = re.compile(r'(blah){, 5}') # Will find 0 to 5 instances of 'blah' group
blahRegex3 = re.compile(r'(blah){3, }') # Will find 0 to x instances of 'blah' group
```
* A question mark has two meanings in regex: To declare non-greedy match or to flag optional groups
* The **search()** method will return a Match object the first matched text of a string. The **findall()** method will return all matches as strings in a list - as long as there are no groups. If there are groups, findall() will return a list of strings in tuples.
```python
phoneNumRegex = re.compile(r'\d{3}-\d{3}-\d{4}')
phoneNumRegex.findall('Cell: 425-555-5555 Work: 555-555-5555') #Will return a list
```
* Create character classes by using square brackets. For example, \[aeiouAEIOU\] will match all vowel occurences. Add a caret **^** right after the opening bracket to make a negative character class. For example, \[^aeiouAEIOU\] will match all characters that are NOT vowels.
```python
vowelRegex = re.compile(r'[aeiouAEIOU])
vowelRegex.findall('I am the Batman') # should return a list of values
```
* You can use the caret symbol at the start of a pattern to signal that a string must begin with that pattern. You can use the dollar symbol to signify that a string must end with that pattern.
```python
startsWithSuper = re.compile(r'^Super') #returns Match only if string starts with 'Super'
endsWithDuper = re.compile(r'Duper$') #returns Match only if string ends with 'Duper'
```
* A dot **\.** character represents any character that is not a newline. Using the regex pattern .* will match everything up to a newline.
* Enter **re.IGNORECASE or re.I** as a second argument to **search() or findall()** to make the regex case insensitive.
```python
vowelRegex = re.compile(r'[aeiou]', re.I)
vowelRegex.findall('HOLY CRAP - is that Batman?') # Should return a list [O, A, i... etc.]
```
* Use the **sub()** method to replace a pattern with something else.
```python
scpRegex = re.compile(r'SCP \d+-?\d*')
scpRegex.sub('REDACTED', 'SCP 2412 was last seen escaping the facility with SCP 2412-1')
#Should replace 'SCP 2412' and 'SCP 2412-1' with 'REDACTED'
```
* Pass **re.VERBOSE** as a second argument to re.compile for complicated regex. Verbose mode ignores comments and whitespace inside regex strings. **See page 178**
