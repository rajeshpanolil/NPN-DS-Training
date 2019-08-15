Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a =10
>>> type(a)
<class 'int'>
>>> a =10.5
>>> type(a)
<class 'float'>
>>> str1 = "python"
>>> type(str1)
<class 'str'>
>>> str2 = python
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    str2 = python
NameError: name 'python' is not defined
>>> str1 = 'pytho'
>>> type(str1)
<class 'str'>
>>> a=10
>>> id(a)
1802593600
>>> b=10
>>> id(b)
1802593600
>>> # Single line comment
>>> ''' multiple line comment
multiple line comment '''
' multiple line comment\nmultiple line comment '
>>> 1=21
SyntaxError: can't assign to literal
>>> a =21
>>> b=19
>>> b=10
>>> a%b
1
>>> a//b
2
>>> a/b
2.1
>>> a**2
441
>>> a+b
31
>>> a-b
11
>>> num=20
>>> if num<30:
	print("Smaller")
else:
	print("Bigger")

	
Smaller
>>> if num >30:
	print("Bigger")
elif:
	
SyntaxError: invalid syntax
>>> if num >30:
	print("Bigger")
elif num <30 and num >30:
	print("Medium")
else:
	print("Smaller")

	
Smaller
>>> num1=40
>>> if num1%10 = 0 and num1%4 = 0:
	
SyntaxError: invalid syntax
>>> num1 = 40
>>> if num1%10 = 0:
	
SyntaxError: invalid syntax
>>> num1=40
>>> if num1%10 == 0:
	if num1%4 ==0:
		print("Yes")
	else:
		print("Not divisible by 10 or 4")

		
Yes
>>> if num1%10 ==0 and num1%4==0:
	print("yes")
else:
	print("not divisible by 10 and 4")

	
yes
>>> num1=input("Please input a number")
Please input a number30
>>> num2=input("Please input a number")
Please input a number20
>>> if num2%5 ==0 and num2%7==0:
	print("NICE")
elif num2%5==0:
	print("Good")
else:
	print("Not good")

	
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    if num2%5 ==0 and num2%7==0:
TypeError: not all arguments converted during string formatting
>>> num1 = int(input("Please input a number"))
Please input a number15
>>> if num%5==0 and num%7==0:
	print("Nice")
elif num%5==0:
	print("Good")
else:
	print("Not Good")

	
Good
>>> print("We are learning [] in [] classes".format("Python",10))
We are learning [] in [] classes
>>> print("We are learning {} in {} classes".format("Python",10))
We are learning Python in 10 classes
>>> print("ML is {} popular in the last {} years".format("more",5))
ML is more popular in the last 5 years
>>> range(10)
range(0, 10)
>>> a=range(10)
>>> list(a)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> for item in range(10):
	print(item)

	
0
1
2
3
4
5
6
7
8
9
>>> for item in range(10):
	if item%2==0:
		print("Even number is",item)
	else:
		print("Odd number is",item)

		
Even number is 0
Odd number is 1
Even number is 2
Odd number is 3
Even number is 4
Odd number is 5
Even number is 6
Odd number is 7
Even number is 8
Odd number is 9
>>> for item in range(10):
	if item%2==0:
		print("Even number is" + str(item)
	else:
		      
SyntaxError: invalid syntax
>>> A=1
>>> a=1
>>> while(a<10):
	print(a)
	a=a+1

	
1
2
3
4
5
6
7
8
9
>>> str1="We are learning python"
>>> type(str1)
<class 'str'>
>>> str1[length(str1)-1]
Traceback (most recent call last):
  File "<pyshell#105>", line 1, in <module>
    str1[length(str1)-1]
NameError: name 'length' is not defined
>>> str1[-1]
'n'
>>> str1[2:5]
' ar'
>>> len(str1)
22
>>> str1[len(str1)]
Traceback (most recent call last):
  File "<pyshell#109>", line 1, in <module>
    str1[len(str1)]
IndexError: string index out of range
>>> str1[len(str1)-1]
'n'
>>> str1[-1]
'n'
>>> str1[5:]
'e learning python'
>>> str1[-1:]
'n'
>>> str1[len(str1)-1:0:-1]
'nohtyp gninrael era e'
>>> str1[len(str1)-1::-1]
'nohtyp gninrael era eW'
>>> # the above code will print the string in the reverse order
>>> str1[-1::-1]
'nohtyp gninrael era eW'
>>> str1[5]
'e'
>>> str1[5]=a
Traceback (most recent call last):
  File "<pyshell#123>", line 1, in <module>
    str1[5]=a
TypeError: 'str' object does not support item assignment
>>> # Above error is because string is immutable
>>> help(str)
Help on class str in module builtins:

class str(object)
 |  str(object='') -> str
 |  str(bytes_or_buffer[, encoding[, errors]]) -> str
 |  
 |  Create a new string object from the given object. If encoding or
 |  errors is specified, then the object must expose a data buffer
 |  that will be decoded using the given encoding and error handler.
 |  Otherwise, returns the result of object.__str__() (if defined)
 |  or repr(object).
 |  encoding defaults to sys.getdefaultencoding().
 |  errors defaults to 'strict'.
 |  
 |  Methods defined here:
 |  
 |  __add__(self, value, /)
 |      Return self+value.
 |  
 |  __contains__(self, key, /)
 |      Return key in self.
 |  
 |  __eq__(self, value, /)
 |      Return self==value.
 |  
 |  __format__(self, format_spec, /)
 |      Return a formatted version of the string as described by format_spec.
 |  
 |  __ge__(self, value, /)
 |      Return self>=value.
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __getitem__(self, key, /)
 |      Return self[key].
 |  
 |  __getnewargs__(...)
 |  
 |  __gt__(self, value, /)
 |      Return self>value.
 |  
 |  __hash__(self, /)
 |      Return hash(self).
 |  
 |  __iter__(self, /)
 |      Implement iter(self).
 |  
 |  __le__(self, value, /)
 |      Return self<=value.
 |  
 |  __len__(self, /)
 |      Return len(self).
 |  
 |  __lt__(self, value, /)
 |      Return self<value.
 |  
 |  __mod__(self, value, /)
 |      Return self%value.
 |  
 |  __mul__(self, value, /)
 |      Return self*value.
 |  
 |  __ne__(self, value, /)
 |      Return self!=value.
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  __rmod__(self, value, /)
 |      Return value%self.
 |  
 |  __rmul__(self, value, /)
 |      Return value*self.
 |  
 |  __sizeof__(self, /)
 |      Return the size of the string in memory, in bytes.
 |  
 |  __str__(self, /)
 |      Return str(self).
 |  
 |  capitalize(self, /)
 |      Return a capitalized version of the string.
 |      
 |      More specifically, make the first character have upper case and the rest lower
 |      case.
 |  
 |  casefold(self, /)
 |      Return a version of the string suitable for caseless comparisons.
 |  
 |  center(self, width, fillchar=' ', /)
 |      Return a centered string of length width.
 |      
 |      Padding is done using the specified fill character (default is a space).
 |  
 |  count(...)
 |      S.count(sub[, start[, end]]) -> int
 |      
 |      Return the number of non-overlapping occurrences of substring sub in
 |      string S[start:end].  Optional arguments start and end are
 |      interpreted as in slice notation.
 |  
 |  encode(self, /, encoding='utf-8', errors='strict')
 |      Encode the string using the codec registered for encoding.
 |      
 |      encoding
 |        The encoding in which to encode the string.
 |      errors
 |        The error handling scheme to use for encoding errors.
 |        The default is 'strict' meaning that encoding errors raise a
 |        UnicodeEncodeError.  Other possible values are 'ignore', 'replace' and
 |        'xmlcharrefreplace' as well as any other name registered with
 |        codecs.register_error that can handle UnicodeEncodeErrors.
 |  
 |  endswith(...)
 |      S.endswith(suffix[, start[, end]]) -> bool
 |      
 |      Return True if S ends with the specified suffix, False otherwise.
 |      With optional start, test S beginning at that position.
 |      With optional end, stop comparing S at that position.
 |      suffix can also be a tuple of strings to try.
 |  
 |  expandtabs(self, /, tabsize=8)
 |      Return a copy where all tab characters are expanded using spaces.
 |      
 |      If tabsize is not given, a tab size of 8 characters is assumed.
 |  
 |  find(...)
 |      S.find(sub[, start[, end]]) -> int
 |      
 |      Return the lowest index in S where substring sub is found,
 |      such that sub is contained within S[start:end].  Optional
 |      arguments start and end are interpreted as in slice notation.
 |      
 |      Return -1 on failure.
 |  
 |  format(...)
 |      S.format(*args, **kwargs) -> str
 |      
 |      Return a formatted version of S, using substitutions from args and kwargs.
 |      The substitutions are identified by braces ('{' and '}').
 |  
 |  format_map(...)
 |      S.format_map(mapping) -> str
 |      
 |      Return a formatted version of S, using substitutions from mapping.
 |      The substitutions are identified by braces ('{' and '}').
 |  
 |  index(...)
 |      S.index(sub[, start[, end]]) -> int
 |      
 |      Return the lowest index in S where substring sub is found, 
 |      such that sub is contained within S[start:end].  Optional
 |      arguments start and end are interpreted as in slice notation.
 |      
 |      Raises ValueError when the substring is not found.
 |  
 |  isalnum(self, /)
 |      Return True if the string is an alpha-numeric string, False otherwise.
 |      
 |      A string is alpha-numeric if all characters in the string are alpha-numeric and
 |      there is at least one character in the string.
 |  
 |  isalpha(self, /)
 |      Return True if the string is an alphabetic string, False otherwise.
 |      
 |      A string is alphabetic if all characters in the string are alphabetic and there
 |      is at least one character in the string.
 |  
 |  isascii(self, /)
 |      Return True if all characters in the string are ASCII, False otherwise.
 |      
 |      ASCII characters have code points in the range U+0000-U+007F.
 |      Empty string is ASCII too.
 |  
 |  isdecimal(self, /)
 |      Return True if the string is a decimal string, False otherwise.
 |      
 |      A string is a decimal string if all characters in the string are decimal and
 |      there is at least one character in the string.
 |  
 |  isdigit(self, /)
 |      Return True if the string is a digit string, False otherwise.
 |      
 |      A string is a digit string if all characters in the string are digits and there
 |      is at least one character in the string.
 |  
 |  isidentifier(self, /)
 |      Return True if the string is a valid Python identifier, False otherwise.
 |      
 |      Use keyword.iskeyword() to test for reserved identifiers such as "def" and
 |      "class".
 |  
 |  islower(self, /)
 |      Return True if the string is a lowercase string, False otherwise.
 |      
 |      A string is lowercase if all cased characters in the string are lowercase and
 |      there is at least one cased character in the string.
 |  
 |  isnumeric(self, /)
 |      Return True if the string is a numeric string, False otherwise.
 |      
 |      A string is numeric if all characters in the string are numeric and there is at
 |      least one character in the string.
 |  
 |  isprintable(self, /)
 |      Return True if the string is printable, False otherwise.
 |      
 |      A string is printable if all of its characters are considered printable in
 |      repr() or if it is empty.
 |  
 |  isspace(self, /)
 |      Return True if the string is a whitespace string, False otherwise.
 |      
 |      A string is whitespace if all characters in the string are whitespace and there
 |      is at least one character in the string.
 |  
 |  istitle(self, /)
 |      Return True if the string is a title-cased string, False otherwise.
 |      
 |      In a title-cased string, upper- and title-case characters may only
 |      follow uncased characters and lowercase characters only cased ones.
 |  
 |  isupper(self, /)
 |      Return True if the string is an uppercase string, False otherwise.
 |      
 |      A string is uppercase if all cased characters in the string are uppercase and
 |      there is at least one cased character in the string.
 |  
 |  join(self, iterable, /)
 |      Concatenate any number of strings.
 |      
 |      The string whose method is called is inserted in between each given string.
 |      The result is returned as a new string.
 |      
 |      Example: '.'.join(['ab', 'pq', 'rs']) -> 'ab.pq.rs'
 |  
 |  ljust(self, width, fillchar=' ', /)
 |      Return a left-justified string of length width.
 |      
 |      Padding is done using the specified fill character (default is a space).
 |  
 |  lower(self, /)
 |      Return a copy of the string converted to lowercase.
 |  
 |  lstrip(self, chars=None, /)
 |      Return a copy of the string with leading whitespace removed.
 |      
 |      If chars is given and not None, remove characters in chars instead.
 |  
 |  partition(self, sep, /)
 |      Partition the string into three parts using the given separator.
 |      
 |      This will search for the separator in the string.  If the separator is found,
 |      returns a 3-tuple containing the part before the separator, the separator
 |      itself, and the part after it.
 |      
 |      If the separator is not found, returns a 3-tuple containing the original string
 |      and two empty strings.
 |  
 |  replace(self, old, new, count=-1, /)
 |      Return a copy with all occurrences of substring old replaced by new.
 |      
 |        count
 |          Maximum number of occurrences to replace.
 |          -1 (the default value) means replace all occurrences.
 |      
 |      If the optional argument count is given, only the first count occurrences are
 |      replaced.
 |  
 |  rfind(...)
 |      S.rfind(sub[, start[, end]]) -> int
 |      
 |      Return the highest index in S where substring sub is found,
 |      such that sub is contained within S[start:end].  Optional
 |      arguments start and end are interpreted as in slice notation.
 |      
 |      Return -1 on failure.
 |  
 |  rindex(...)
 |      S.rindex(sub[, start[, end]]) -> int
 |      
 |      Return the highest index in S where substring sub is found,
 |      such that sub is contained within S[start:end].  Optional
 |      arguments start and end are interpreted as in slice notation.
 |      
 |      Raises ValueError when the substring is not found.
 |  
 |  rjust(self, width, fillchar=' ', /)
 |      Return a right-justified string of length width.
 |      
 |      Padding is done using the specified fill character (default is a space).
 |  
 |  rpartition(self, sep, /)
 |      Partition the string into three parts using the given separator.
 |      
 |      This will search for the separator in the string, starting at the end. If
 |      the separator is found, returns a 3-tuple containing the part before the
 |      separator, the separator itself, and the part after it.
 |      
 |      If the separator is not found, returns a 3-tuple containing two empty strings
 |      and the original string.
 |  
 |  rsplit(self, /, sep=None, maxsplit=-1)
 |      Return a list of the words in the string, using sep as the delimiter string.
 |      
 |        sep
 |          The delimiter according which to split the string.
 |          None (the default value) means split according to any whitespace,
 |          and discard empty strings from the result.
 |        maxsplit
 |          Maximum number of splits to do.
 |          -1 (the default value) means no limit.
 |      
 |      Splits are done starting at the end of the string and working to the front.
 |  
 |  rstrip(self, chars=None, /)
 |      Return a copy of the string with trailing whitespace removed.
 |      
 |      If chars is given and not None, remove characters in chars instead.
 |  
 |  split(self, /, sep=None, maxsplit=-1)
 |      Return a list of the words in the string, using sep as the delimiter string.
 |      
 |      sep
 |        The delimiter according which to split the string.
 |        None (the default value) means split according to any whitespace,
 |        and discard empty strings from the result.
 |      maxsplit
 |        Maximum number of splits to do.
 |        -1 (the default value) means no limit.
 |  
 |  splitlines(self, /, keepends=False)
 |      Return a list of the lines in the string, breaking at line boundaries.
 |      
 |      Line breaks are not included in the resulting list unless keepends is given and
 |      true.
 |  
 |  startswith(...)
 |      S.startswith(prefix[, start[, end]]) -> bool
 |      
 |      Return True if S starts with the specified prefix, False otherwise.
 |      With optional start, test S beginning at that position.
 |      With optional end, stop comparing S at that position.
 |      prefix can also be a tuple of strings to try.
 |  
 |  strip(self, chars=None, /)
 |      Return a copy of the string with leading and trailing whitespace remove.
 |      
 |      If chars is given and not None, remove characters in chars instead.
 |  
 |  swapcase(self, /)
 |      Convert uppercase characters to lowercase and lowercase characters to uppercase.
 |  
 |  title(self, /)
 |      Return a version of the string where each word is titlecased.
 |      
 |      More specifically, words start with uppercased characters and all remaining
 |      cased characters have lower case.
 |  
 |  translate(self, table, /)
 |      Replace each character in the string using the given translation table.
 |      
 |        table
 |          Translation table, which must be a mapping of Unicode ordinals to
 |          Unicode ordinals, strings, or None.
 |      
 |      The table must implement lookup/indexing via __getitem__, for instance a
 |      dictionary or list.  If this operation raises LookupError, the character is
 |      left untouched.  Characters mapped to None are deleted.
 |  
 |  upper(self, /)
 |      Return a copy of the string converted to uppercase.
 |  
 |  zfill(self, width, /)
 |      Pad a numeric string with zeros on the left, to fill a field of the given width.
 |      
 |      The string is never truncated.
 |  
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
 |  
 |  maketrans(x, y=None, z=None, /)
 |      Return a translation table usable for str.translate().
 |      
 |      If there is only one argument, it must be a dictionary mapping Unicode
 |      ordinals (integers) or characters to Unicode ordinals, strings or None.
 |      Character keys will be then converted to ordinals.
 |      If there are two arguments, they must be strings of equal length, and
 |      in the resulting dictionary, each character in x will be mapped to the
 |      character at the same position in y. If there is a third argument, it
 |      must be a string, whose characters will be mapped to None in the result.

>>> #String is heavily used in text analytics, hence, we should know these types to do text analytics
>>> str1
'We are learning python'
>>> str1.split("")
Traceback (most recent call last):
  File "<pyshell#128>", line 1, in <module>
    str1.split("")
ValueError: empty separator
>>> str1.split(" ")
['We', 'are', 'learning', 'python']
>>> str2 =" Python "
>>> str2.rstrip()
' Python'
>>> str2.lstrip()
'Python '
>>> #Most important function is replace and find
>>> str1.find("Python")
-1
>>> #-1 because it did not have a match. It was small p in python
>>> str1.find("python")
16
>>> # there is a match over here where p was the 16th character
>>> # which is the index of where the string starts
>>> 
>>> #Replaces one string with another
>>> str1.replace("python","java")
'We are learning java'
>>> #STARTSWITH
>>> str1.startswith("python")
False
>>> str1.startswith("We")
True
>>> #JOIN
>>> #ISUPPER - RETURNS A BOOLEAN VALUE - TRUE OR FALSE
>>> " ".join("python")
'p y t h o n'
>>> " ".join(str1)
'W e   a r e   l e a r n i n g   p y t h o n'
>>> #this will iterate and join the first string with each of the value of the second string
>>> #List is a collection data type which can hold similar kind of element as well as different kind of elements. Array is a collection of same data type whereas a list can hold different data types. List is mutable, ordered, collection data type (more than one element),
>>> list1=[]
>>> list2=[1,2,3,4,5,6]
>>> len[list2]
Traceback (most recent call last):
  File "<pyshell#153>", line 1, in <module>
    len[list2]
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> len(list2)
6
>>> list2[1:5]
[2, 3, 4, 5]
>>> list2[-1]
6
>>> list2[0]
1
>>> help(list)
Help on class list in module builtins:

class list(object)
 |  list(iterable=(), /)
 |  
 |  Built-in mutable sequence.
 |  
 |  If no argument is given, the constructor creates a new empty list.
 |  The argument must be an iterable if specified.
 |  
 |  Methods defined here:
 |  
 |  __add__(self, value, /)
 |      Return self+value.
 |  
 |  __contains__(self, key, /)
 |      Return key in self.
 |  
 |  __delitem__(self, key, /)
 |      Delete self[key].
 |  
 |  __eq__(self, value, /)
 |      Return self==value.
 |  
 |  __ge__(self, value, /)
 |      Return self>=value.
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __getitem__(...)
 |      x.__getitem__(y) <==> x[y]
 |  
 |  __gt__(self, value, /)
 |      Return self>value.
 |  
 |  __iadd__(self, value, /)
 |      Implement self+=value.
 |  
 |  __imul__(self, value, /)
 |      Implement self*=value.
 |  
 |  __init__(self, /, *args, **kwargs)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |  
 |  __iter__(self, /)
 |      Implement iter(self).
 |  
 |  __le__(self, value, /)
 |      Return self<=value.
 |  
 |  __len__(self, /)
 |      Return len(self).
 |  
 |  __lt__(self, value, /)
 |      Return self<value.
 |  
 |  __mul__(self, value, /)
 |      Return self*value.
 |  
 |  __ne__(self, value, /)
 |      Return self!=value.
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  __reversed__(self, /)
 |      Return a reverse iterator over the list.
 |  
 |  __rmul__(self, value, /)
 |      Return value*self.
 |  
 |  __setitem__(self, key, value, /)
 |      Set self[key] to value.
 |  
 |  __sizeof__(self, /)
 |      Return the size of the list in memory, in bytes.
 |  
 |  append(self, object, /)
 |      Append object to the end of the list.
 |  
 |  clear(self, /)
 |      Remove all items from list.
 |  
 |  copy(self, /)
 |      Return a shallow copy of the list.
 |  
 |  count(self, value, /)
 |      Return number of occurrences of value.
 |  
 |  extend(self, iterable, /)
 |      Extend list by appending elements from the iterable.
 |  
 |  index(self, value, start=0, stop=2147483647, /)
 |      Return first index of value.
 |      
 |      Raises ValueError if the value is not present.
 |  
 |  insert(self, index, object, /)
 |      Insert object before index.
 |  
 |  pop(self, index=-1, /)
 |      Remove and return item at index (default last).
 |      
 |      Raises IndexError if list is empty or index is out of range.
 |  
 |  remove(self, value, /)
 |      Remove first occurrence of value.
 |      
 |      Raises ValueError if the value is not present.
 |  
 |  reverse(self, /)
 |      Reverse *IN PLACE*.
 |  
 |  sort(self, /, *, key=None, reverse=False)
 |      Stable sort *IN PLACE*.
 |  
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
 |  
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |  
 |  __hash__ = None

>>> list1[1,2,3,4]
Traceback (most recent call last):
  File "<pyshell#159>", line 1, in <module>
    list1[1,2,3,4]
TypeError: list indices must be integers or slices, not tuple
>>> list1 = [1,2,3,4]
>>> list2 = [5,6]
>>> list1.append(list2)
>>> list1
[1, 2, 3, 4, [5, 6]]
>>> #SEcond list will be appended as one item
>>> list1[4]
[5, 6]
>>> # To append as a single item
>>> list1 = [1,2,3,4]
>>> list1.extend(list2)
>>> list1
[1, 2, 3, 4, 5, 6]
>>> #here the items are added as is
>>> list1[4]
5
>>> list1[4]=10
>>> # shows that it is mutable
>>> list1
[1, 2, 3, 4, 10, 6]
>>> list1.insert(2,5)
>>> list1
[1, 2, 5, 3, 4, 10, 6]
>>> list1.remove(3)
>>> list1
[1, 2, 5, 4, 10, 6]
>>> list2 = [1,2,3,4,5,6,3,3,3]
>>> list2.remove(3)
>>> list2
[1, 2, 4, 5, 6, 3, 3, 3]
>>> #To remove based on index
>>> list1.pop()
6
>>> #by default it removes the last value
>>> list1.pop(0)
1
>>> list1
[2, 5, 4, 10]
>>> #Difference between remove and pop - interview question
>>> list1.sort()
>>> list1
[2, 4, 5, 10]
>>> list1.sort(reverse=True)
>>> list1
[10, 5, 4, 2]
>>> # Use append to traverse through the list and print odd and even lists separately
>>> list1 = [1,2,3,4,5,6,7,8,9,10]
>>> list2= []
>>> list3= []
>>> for item in list1:
	if item%2==0 list2.append(item)
	
SyntaxError: invalid syntax
>>> for item in list1:
	if item%2==0 list2.extend(item)
	
SyntaxError: invalid syntax
>>> for item in list1:
	if item%2==0
	
SyntaxError: invalid syntax
>>> for item in list1:
	if list1%2==0:
		list2.append(item)
	else: list3.append(item)
print(list2)
SyntaxError: invalid syntax
>>> for item in list1:
	if item%2==0:
		list2.append(item)
	else:
		list3.append(item)
print(list2)
SyntaxError: invalid syntax
>>> for item in list1:
	if item%2==0:
		list2.append(item)
	else:
		list3.append(item)
	print(list2)
	print(list3)

	
[]
[1]
[2]
[1]
[2]
[1, 3]
[2, 4]
[1, 3]
[2, 4]
[1, 3, 5]
[2, 4, 6]
[1, 3, 5]
[2, 4, 6]
[1, 3, 5, 7]
[2, 4, 6, 8]
[1, 3, 5, 7]
[2, 4, 6, 8]
[1, 3, 5, 7, 9]
[2, 4, 6, 8, 10]
[1, 3, 5, 7, 9]
>>> for item in list1:
	if item%2==0:
		list2.append(item)
	else:
		list3.append(item)
print(list2)
SyntaxError: invalid syntax
>>> for item in list1:
	for item%2==0:
		
SyntaxError: invalid syntax
>>> for item in list1:
	if item%2==0:
		list2.append(item)
	else:
		list3.append(item)

		
>>> list2
[2, 4, 6, 8, 10, 2, 4, 6, 8, 10]
>>> list3
[1, 3, 5, 7, 9, 1, 3, 5, 7, 9]
>>> list2=[]
>>> list3=[]
>>> list1
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> for item in list1:
	if item%2==0:
		list2.append(item)
	else:
		list3.append(item)

		
>>> list2
[2, 4, 6, 8, 10]
>>> list3
[1, 3, 5, 7, 9]
>>> #NEXT CORRECTION DATA TYPE IS A TUPLE. IT IS SIMILAR TO LIST BUT IMMUTABLE
>>> tup1=()
>>> tup1=(1,2,3,4,5)
>>> tup1[2]=3
Traceback (most recent call last):
  File "<pyshell#252>", line 1, in <module>
    tup1[2]=3
TypeError: 'tuple' object does not support item assignment
>>> #TUPLE IS USED WHENEVER WE WRITE A SERVICE WHERE WE RESTRICT PEOPLE FROM CHANGING CONTENT. WHEREVER WE DON'T WANT PEOPLE TO CHANGE THE VALUES
>>> help(tuple)
Help on class tuple in module builtins:

class tuple(object)
 |  tuple(iterable=(), /)
 |  
 |  Built-in immutable sequence.
 |  
 |  If no argument is given, the constructor returns an empty tuple.
 |  If iterable is specified the tuple is initialized from iterable's items.
 |  
 |  If the argument is a tuple, the return value is the same object.
 |  
 |  Methods defined here:
 |  
 |  __add__(self, value, /)
 |      Return self+value.
 |  
 |  __contains__(self, key, /)
 |      Return key in self.
 |  
 |  __eq__(self, value, /)
 |      Return self==value.
 |  
 |  __ge__(self, value, /)
 |      Return self>=value.
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __getitem__(self, key, /)
 |      Return self[key].
 |  
 |  __getnewargs__(self, /)
 |  
 |  __gt__(self, value, /)
 |      Return self>value.
 |  
 |  __hash__(self, /)
 |      Return hash(self).
 |  
 |  __iter__(self, /)
 |      Implement iter(self).
 |  
 |  __le__(self, value, /)
 |      Return self<=value.
 |  
 |  __len__(self, /)
 |      Return len(self).
 |  
 |  __lt__(self, value, /)
 |      Return self<value.
 |  
 |  __mul__(self, value, /)
 |      Return self*value.
 |  
 |  __ne__(self, value, /)
 |      Return self!=value.
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  __rmul__(self, value, /)
 |      Return value*self.
 |  
 |  count(self, value, /)
 |      Return number of occurrences of value.
 |  
 |  index(self, value, start=0, stop=2147483647, /)
 |      Return first index of value.
 |      
 |      Raises ValueError if the value is not present.
 |  
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.

>>> tup1
(1, 2, 3, 4, 5)
>>> tup1.index(4)
3
>>> #ANOTHER COLLECTION DATA TYPE IN PYTHON WHICH DOES NOT ALLOW DUPLICATE VALUES - SET. IT IS UN ORDERED
>>> #IT DOES NOT HAVE ANY INDEX. LIKE WE CANNOT DO SET1[1].
>>> set1={}
>>> set2={1,2,3,4,1,1}
>>> set2
{1, 2, 3, 4}
>>> set2{0}
SyntaxError: invalid syntax
>>> set2[]
SyntaxError: invalid syntax
>>> set2{0]
SyntaxError: invalid syntax
>>> set2[0]
Traceback (most recent call last):
  File "<pyshell#265>", line 1, in <module>
    set2[0]
TypeError: 'set' object is not subscriptable
>>> help(set)
Help on class set in module builtins:

class set(object)
 |  set() -> new empty set object
 |  set(iterable) -> new set object
 |  
 |  Build an unordered collection of unique elements.
 |  
 |  Methods defined here:
 |  
 |  __and__(self, value, /)
 |      Return self&value.
 |  
 |  __contains__(...)
 |      x.__contains__(y) <==> y in x.
 |  
 |  __eq__(self, value, /)
 |      Return self==value.
 |  
 |  __ge__(self, value, /)
 |      Return self>=value.
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __gt__(self, value, /)
 |      Return self>value.
 |  
 |  __iand__(self, value, /)
 |      Return self&=value.
 |  
 |  __init__(self, /, *args, **kwargs)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |  
 |  __ior__(self, value, /)
 |      Return self|=value.
 |  
 |  __isub__(self, value, /)
 |      Return self-=value.
 |  
 |  __iter__(self, /)
 |      Implement iter(self).
 |  
 |  __ixor__(self, value, /)
 |      Return self^=value.
 |  
 |  __le__(self, value, /)
 |      Return self<=value.
 |  
 |  __len__(self, /)
 |      Return len(self).
 |  
 |  __lt__(self, value, /)
 |      Return self<value.
 |  
 |  __ne__(self, value, /)
 |      Return self!=value.
 |  
 |  __or__(self, value, /)
 |      Return self|value.
 |  
 |  __rand__(self, value, /)
 |      Return value&self.
 |  
 |  __reduce__(...)
 |      Return state information for pickling.
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  __ror__(self, value, /)
 |      Return value|self.
 |  
 |  __rsub__(self, value, /)
 |      Return value-self.
 |  
 |  __rxor__(self, value, /)
 |      Return value^self.
 |  
 |  __sizeof__(...)
 |      S.__sizeof__() -> size of S in memory, in bytes
 |  
 |  __sub__(self, value, /)
 |      Return self-value.
 |  
 |  __xor__(self, value, /)
 |      Return self^value.
 |  
 |  add(...)
 |      Add an element to a set.
 |      
 |      This has no effect if the element is already present.
 |  
 |  clear(...)
 |      Remove all elements from this set.
 |  
 |  copy(...)
 |      Return a shallow copy of a set.
 |  
 |  difference(...)
 |      Return the difference of two or more sets as a new set.
 |      
 |      (i.e. all elements that are in this set but not the others.)
 |  
 |  difference_update(...)
 |      Remove all elements of another set from this set.
 |  
 |  discard(...)
 |      Remove an element from a set if it is a member.
 |      
 |      If the element is not a member, do nothing.
 |  
 |  intersection(...)
 |      Return the intersection of two sets as a new set.
 |      
 |      (i.e. all elements that are in both sets.)
 |  
 |  intersection_update(...)
 |      Update a set with the intersection of itself and another.
 |  
 |  isdisjoint(...)
 |      Return True if two sets have a null intersection.
 |  
 |  issubset(...)
 |      Report whether another set contains this set.
 |  
 |  issuperset(...)
 |      Report whether this set contains another set.
 |  
 |  pop(...)
 |      Remove and return an arbitrary set element.
 |      Raises KeyError if the set is empty.
 |  
 |  remove(...)
 |      Remove an element from a set; it must be a member.
 |      
 |      If the element is not a member, raise a KeyError.
 |  
 |  symmetric_difference(...)
 |      Return the symmetric difference of two sets as a new set.
 |      
 |      (i.e. all elements that are in exactly one of the sets.)
 |  
 |  symmetric_difference_update(...)
 |      Update a set with the symmetric difference of itself and another.
 |  
 |  union(...)
 |      Return the union of sets as a new set.
 |      
 |      (i.e. all elements that are in either set.)
 |  
 |  update(...)
 |      Update a set with the union of itself and others.
 |  
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
 |  
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |  
 |  __hash__ = None

>>> #DICTIONARY: COLLECTION DATA TYPE WHICH STORES DATA TYPE IN KEY VALUE PAIR
>>> dict1={}
>>> dict2={'id':1,'Name':"Ram"}
>>> dict2
{'id': 1, 'Name': 'Ram'}
>>> dict2["id"]
1
>>> dict2.keys()
dict_keys(['id', 'Name'])
>>> dict2.values()
dict_values([1, 'Ram'])
>>> dict2.items()
dict_items([('id', 1), ('Name', 'Ram')])
>>> a = dic2.items()
Traceback (most recent call last):
  File "<pyshell#275>", line 1, in <module>
    a = dic2.items()
NameError: name 'dic2' is not defined
>>> a = dict2.items()
>>> a[0]
Traceback (most recent call last):
  File "<pyshell#277>", line 1, in <module>
    a[0]
TypeError: 'dict_items' object is not subscriptable
>>> dict1.get('name1')
>>> for content in dict1.items():
	print(content)

	
>>> # create a dictionary of sallary and empid and whenever the salary is greater than 10000 print that
>>> dict2 = {'tin2419':12000,'tin2319':8000,'tin3115':20000}
>>> for i in dict2.values():
	if i>10000:
		print(i)

		
12000
20000
>>> dict3={'id':[1,2,3,4],'salary':[10000,20000,30000,40000]}
>>> #to get list of ids whose salry is greter than 10000
>>> #ASSIGNMENT
>>> list1=['id','Name','Salary']
>>> list2=[1,'A',10000]
>>> list2=[1,'Shyam',10000]
>>> list1
['id', 'Name', 'Salary']
>>> list2
[1, 'Shyam', 10000]
>>> zip(list1,list2)
<zip object at 0x0141D738>
>>> #creates a dictionary of list 1 and 2
>>> list(sip(list1,list2)
    )
Traceback (most recent call last):
  File "<pyshell#300>", line 1, in <module>
    list(sip(list1,list2)
NameError: name 'sip' is not defined
>>> list(zip(list1,list2))
[('id', 1), ('Name', 'Shyam'), ('Salary', 10000)]
>>> dict(zip(list1,list2))
{'id': 1, 'Name': 'Shyam', 'Salary': 10000}
>>> #INTERVIEW QUESTION - HOW TO CONVERT A LIST TO DICTIONARY USING ZIP COMMAND
>>> list3 = ['Id','Name','Salary']
>>> list4 = [[1,2,3,],['Shyam','Ravi','Nari']]
>>> zip(list3,list4)
<zip object at 0x042B9DC8>
>>> dict(zip(list3,list4))
{'Id': [1, 2, 3], 'Name': ['Shyam', 'Ravi', 'Nari']}
>>> tup1 = [1,2,3,4]
>>> tup1 = ['ID','name','salary']
>>> tup2 = ['tin2419','Rajesh',10000]
>>> dict(tup1,tup2)
Traceback (most recent call last):
  File "<pyshell#311>", line 1, in <module>
    dict(tup1,tup2)
TypeError: dict expected at most 1 arguments, got 2
>>> dict(zip(tup1,tup2))
{'ID': 'tin2419', 'name': 'Rajesh', 'salary': 10000}
>>> #ZIP CAN ALSO BE USED TO CONVERT A TUPLE INTO A DICTIONARY
         
>>> dict3 = {"Id":[1,2,3,4],"Salary":[8000,10000,12000,15000]}

         

         



         

         
        
         
