# WikiParser
WikiParser is a Python Library for thoroughly scraping Wikipedia article data.

# Examples
### Fetching the body paragraphs
```from wiki import Wiki
article = Wiki("/wiki/Python_(programming_language)", by_url = True)
article.article_info()
>>> [u'Python is a widely used high-level programming language for general-purpose programming, created by Guido van Rossum and first released in 1991. An interpreted language, Python has a design philosophy that emphasizes code readability (notably using whitespace indentation to delimit code blocks rather than curly brackets or keywords), and a syntax that allows programmers to express concepts in fewer lines of code than might be used in languages such as C++ or Java.[23][24].....
```

### Getting data from InfoBox (New!)

```
article.info_box()

>>> ['Python', 'Paradigm', 'multi-paradigm: object-oriented, imperative, functional, procedural, reflective', 'Designedby', 'Guido van Rossum', 'Developer', 'Python Software Foundation', 'Firstappeared', '20February 1991; 26 years ago(1991-02-20)[1]', 'Stable release', '3.6.2 / 17July 2017; 42 days ago(2017-07-17)[2]', '2.7.13 / 17December 2016; 8 months ago(2016-12-17)[3]', 'Typing discipline', 'duck, dynamic, strong', 'OS', 'Cross-platform', 'License', 'Python Software Foundation License', 'Filename extensions', '.py, .pyc, .pyd, .pyo (prior to 3.5),[4] .pyw, .pyz (since 3.5)[5]', 'Website', 'www.python.org', 'Major implementations', 'CPython, IronPython, Jython, MicroPython, Numba, PyPy, Stackless Python', 'Dialects', 'Cython, RPython', 'Influenced by', 'ABC,[6] ALGOL 68,[7] C,[8] C++,[9] Dylan,[10] Haskell,[11] Icon,[12] Java,[13] Lisp,[14] Modula-3,[9] Perl', 'Influenced', 'Boo, Cobra, Coconut,[15] CoffeeScript,[16] D, F#, Falcon, Genie,[17] Go, Groovy, JavaScript,[18][19] Julia,[20] Nim, Ruby,[21] Swift[22]', ' Python Programming at Wikibooks']
```

### Support For Multiple Languages
WikiParser allows the user to enter the abbreviation of any of the 298 languages that Wikipedia supports. 
```
article = Wiki("/wiki/Gato", by_url = True, lang = "en")
```

## Additional Features

#### Searching by keyword
WikiParser supports Wikipedia keyword searches. However, an error will be thrown if no article is found.
```
article = Wiki("Calculus")

```
#### Finding the Disambiguation
In WikiParser, an article's potential disambiguation can be found if a search is made by keyword only. If a disambiguation page is not found or an invalid keyword is entered, such as a URL, WikiParser will raise a "InvalidKeyWordError" error. The return-type is a dictionary that stores the headers of the disambiguation and a list of the topics under each.

```
article = Wiki("Calculus")
article.disambiguation()

>>> {'headers': [u'1 Mathematics', u'2 Logic', u'3 Physics', u'4 Computer Science', u'5 Other meanings'], 'topics': [u'Calculus, short for "differential calculus" and "integral calculus", which investigate motion and rates of change', u'Calculus of sums and differences (difference operator), also called the finite-difference calculus, a discrete analogue of "calculus"', u'Functional calculus, a way to apply various types of functions to operators', u"Non-standard calculus, an approach to infinitesimal calculus using Robinson's infinitesimals", u'Schubert calculus, a branch of algebraic geometry', u'Tensor calculus (also called tensor analysis), a generalization of vector calculus that encompasses tensor fields', u'Vector calculus (also called vector analysis), comprising specialized notations for multivariable analysis of vectors in an inner-product space', u'Matrix calculus, a specialized notation for multivariable calculus over spaces of matrices', u'Vector calculus (also called vector analysis), comprising specialized notations for multivariable analysis of vectors in an inner-product space', u'Matrix calculus, a specialized notation for multivariable calculus over spaces of matrices', u'Umbral calculus, the combinatorics of certain operations on polynomials', u'The calculus of variations, a field of study that deals with extremizing functionals', u'Logical calculus, a formal system that defines a language and rules to derive an expression from premises.', u'the propositional calculus, specifies the rules of inference governing the logic of propositions', u'the predicate calculus, specifies the rules of inference governing the logic of predicates', u'a proof calculus, a framework for expressing systems of logical inference', u'the sequent calculus, a proof calculus for first-order logic', u'the propositional calculus, specifies the rules of inference governing the logic of propositions', u'the predicate calculus, specifies the rules of inference governing the logic of predicates', u'a proof calculus, a framework for expressing systems of logical inference', u'the sequent calculus, a proof calculus for first-order logic', u'Epsilon calculus, a logical language which replaces quantifiers with the epsilon operator', u'Fitch-style calculus, a method for constructing formal proofs used in first-order logic', u'Modal \u03bc-calculus, a common temporal logic used by formal verification methods such as model checking', u'Bondi k-calculus, a method used in relativity theory', u'Jones calculus, used in optics to describe polarized light', u'Mueller calculus, used in optics to handle Stokes vectors, which describe the polarization of incoherent light', u'Domain relational calculus, a calculus for the relational data model', u'Join calculus, a theoretical model for distributed programming', u'Lambda calculus, a formulation of the theory of reflexive functions that has deep connections to computational theory', u'Pi-calculus, a formulation of the theory of concurrent, communicating processes that was invented by Robin Milner', u'Refinement calculus, a way of refining models of programs into efficient programs', u'Rho calculus, introduced as a general means to uniformly integrate rewriting and lambda calculus', u'Tuple calculus, a calculus for the relational data model, inspired the SQL language', u'Calculus (dental), deposits of calcium phosphate salts on teeth, also known as tartar', u'Calculus (medicine), a stone formed in the body such as a gall stone or kidney stone', u'Battlefield calculus, military calculation of all known factors into the decision-making and action-planning process', u'Calculus (spider), a genus of the family Oonopidae', u'Caseolus calculus, a genus and species of small land snails', u'Professor Calculus, a fictional character in the comic-strip series The Adventures of Tintin', u'Calculus of negligence, a legal standard in U.S. tort law to determine if a duty of care has been breached']}
```






