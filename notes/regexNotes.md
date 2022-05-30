# Regex Notes
Notes on Regex taken from the book 'Automate the Boring Stuff' by Al Sweigart.  
Chapter 7, page 164.  
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
