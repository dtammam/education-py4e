'''
Regular Expressions
    -  In computing, a regular expression, also referred to as "regex" or "regexp", provides a concise and flexible means for matching strings of text, such as particular characters, words, or patterns of characters
    - A regular expression is written in a formal language that can be interpreted by a regular expression processor
    - Really clever "wild card" expressions for matching and parsing strings
    - Very powerful and quite cryptic
    - Fun once you understand them
    - Regular expressions are a language unto themselves
    - A language of "marker characters" - programming with characters
    - It's kind of an "old school" language - compact
'''
# Regular Expression Quick Guide
#     ^	        Matches the beginning of a line
#     $	        Matches the end of a line
#     .	        Matches any character
#     \s	    Matches whitespace
#     \S	    Matches any non-whitespace character
#     *	        Repeats a character zero or more times
#     *?	    Repeats a character zero or more times (non-greedy)
#     +	        Repeats a character one or more times
#     +?	    Repeats a character one or more times (non-greedy)
#     [aeiou]	Matches a single character in the listed set
#     [^XYZ]	Matches a single character not in the listed set
#     [a-z0-9]	The set of characters can include a range
#     (	        Indicates where string extraction is to start
#     )	        Indicates where string extraction is to end