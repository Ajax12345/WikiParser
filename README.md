# WikiParser
WikiParser is a Python Library for thoroughly scraping Wikipedia article data.

# Examples
#### Fetching the body paragraphs
````from wiki import Wiki
article = Wiki("/wiki/Python_(programming_language)", by_url = True)
article.article_info()
>>> [u'Python is a widely used high-level programming language for general-purpose programming, created by Guido van Rossum and first released in 1991. An interpreted language, Python has a design philosophy that emphasizes code readability (notably using whitespace indentation to delimit code blocks rather than curly brackets or keywords), and a syntax that allows programmers to express concepts in fewer lines of code than might be used in languages such as C++ or Java.[23][24].....
````

##### Getting data from InfoBox (New!)
````article.info_box()
>>> ['Python', 'Paradigm', 'multi-paradigm: object-oriented, imperative, functional, procedural, reflective', 'Designedby', 'Guido van Rossum', 'Developer', 'Python Software Foundation', 'Firstappeared', '20February 1991; 26 years ago(1991-02-20)[1]', 'Stable release', '3.6.2 / 17July 2017; 42 days ago(2017-07-17)[2]', '2.7.13 / 17December 2016; 8 months ago(2016-12-17)[3]', 'Typing discipline', 'duck, dynamic, strong', 'OS', 'Cross-platform', 'License', 'Python Software Foundation License', 'Filename extensions', '.py, .pyc, .pyd, .pyo (prior to 3.5),[4] .pyw, .pyz (since 3.5)[5]', 'Website', 'www.python.org', 'Major implementations', 'CPython, IronPython, Jython, MicroPython, Numba, PyPy, Stackless Python', 'Dialects', 'Cython, RPython', 'Influenced by', 'ABC,[6] ALGOL 68,[7] C,[8] C++,[9] Dylan,[10] Haskell,[11] Icon,[12] Java,[13] Lisp,[14] Modula-3,[9] Perl', 'Influenced', 'Boo, Cobra, Coconut,[15] CoffeeScript,[16] D, F#, Falcon, Genie,[17] Go, Groovy, JavaScript,[18][19] Julia,[20] Nim, Ruby,[21] Swift[22]', ' Python Programming at Wikibooks']
````

#### Support For Multiple Languages
WikiParser allows the user to enter the abbreviation of any of the 298 languages that Wikipedia supports. 
````article = Wiki("/wiki/Gato", by_url = True, lang = "en")
````







