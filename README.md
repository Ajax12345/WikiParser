# WikiParser
WikiParser is a Python Library for thoroughly scraping Wikipedia article data.

# Examples
### Fetching the body paragraphs
````from wiki import Wiki
article = Wiki("/wiki/Python_(programming_language)", by_url = True)
article.article_info()
>>> [u'Python is a widely used high-level programming language for general-purpose programming, created by Guido van Rossum and first released in 1991. An interpreted language, Python has a design philosophy that emphasizes code readability (notably using whitespace indentation to delimit code blocks rather than curly brackets or keywords), and a syntax that allows programmers to express concepts in fewer lines of code than might be used in languages such as C++ or Java.[23][24].....
```







