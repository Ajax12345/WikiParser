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

#### Article Contents

On Wikipedia pages, the article table of contents is stored in a box to the left of the page. The contents can be accessed in WikiParser like so:

```article = Wiki("Calculus")
article.contents()
>>> ['History', 'Ancient', 'Medieval', 'Modern', 'Foundations', 'Significance', 'Principles', 'Limits and infinitesimals', 'Differential calculus', 'Leibniz notation', 'Integral calculus', 'Fundamental theorem', 'Applications', 'Varieties', 'Non-standard calculus', 'Smooth infinitesimal analysis', 'Constructive analysis', 'See also', 'Lists', 'Other related topics', 'References', 'Further reading', 'Books', 'Online books', 'External links']
```

#### External Links

All external links documentated on a Wikipedia page can be accessed using the `external_links()` method. This method returned a `namedtuple` with member variables `name` and `url`. 

```
article = Wiki("Calculus")
data = article.external_links()
sites = [i.site for i in data]
sites
>>> ['"Calculus"', '"Calculus"', 'Topics on Calculus', 'Calculus Made Easy (1914) by Silvanus P. Thompson', 'Calculus', 'Calculus.org: The Calculus page', 'COW: Calculus on the Web', 'Earliest Known Uses of Some of the Words of Mathematics: Calculus &amp; Analysis', 'Online Integrator (WebMathematica)', 'The Role of Calculus in College Mathematics', 'OpenCourseWare Calculus', 'Infinitesimal Calculus', '"Calculus for Beginners and Artists"', 'Calculus Problems and Solutions', "Donald Allen's notes on calculus", 'Calculus training materials at imomath.com', 'The Excursion of Calculus', 'sh85018802']

urls = [i.url for i in data]
urls
>>> ['https://www.encyclopediaofmath.org/index.php?title=p/c020050', 'http://mathworld.wolfram.com/Calculus.html', 'http://planetmath.org/TopicsOnCalculus', 'http://djm.cc/library/Calculus_Made_Easy_Thompson.pdf', 'http://www.bbc.co.uk/programmes/b00mrfwq', 'http://www.calculus.org', 'http://cow.math.temple.edu/', 'http://www.economics.soton.ac.uk/staff/aldrich/Calculus%20and%20Analysis%20Earliest%20Uses.htm', 'http://integrals.wolfram.com/', 'http://www.ericdigests.org/pre-9217/calculus.htm', 'http://ocw.mit.edu/OcwWeb/Mathematics/index.htm', 'http://www.encyclopediaofmath.org/index.php?title=Infinitesimal_calculus&amp;oldid=18648', 'http://math.mit.edu/~djk/calculus_beginners/', 'http://www.math.ucdavis.edu/~kouba/ProblemsList.html', 'http://www.math.tamu.edu/~dallen/history/calc1/calc1.html', 'http://www.imomath.com/index.php?options=277', 'http://www.wdl.org/en/item/4327/', 'http://id.loc.gov/authorities/subjects/sh85018802']
```

#### Article Sources
WikiParser provides support for accessing an article's sources. `article_sources()` returns a nested list that contains the source header and full citation.
```article = Wiki("Calculus")
article.article_sources()
>>> [['oxdic-1', u' "Calculus". OxfordDictionaries. Retrieved 18 March 2016.\xa0'], ['2', u' "Differential Calculus - Definition of Differential calculus by Merriam-Webster".\xa0'], ['3', u' "Integral Calculus - Definition of Integral calculus by Merriam-Webster".\xa0'], ['4', u' Fisher, Irving (1897). A brief introduction to the infinitesimal calculus. New York: The Macmillan Company.\xa0'], ['5', u' Morris Kline, Mathematical thought from ancient to modern times, Vol. I'], ['6', u' Archimedes, Method, in The Works of Archimedes ISBN 978-0-521-66160-7'], ['7', u' Dun, Liu; Fan, Dainian; Cohen, Robert Sonn\xc3\xa9 (1966). "A comparison of Archimdes\' and Liu Hui\'s studies of circles". Chinese studies in the history and philosophy of science and technology. 130. Springer: 279. ISBN\xa00-7923-3463-9.\xa0,Chapter , p. 279'], ['8', u' Katz, Victor J. (2008). A history of mathematics (3rd ed.). Boston, Mass.: Addison-Wesley. p.\xa0203. ISBN\xa00-321-38700-7.\xa0'], ['9', u' Zill, Dennis G.; Wright, Scott; Wright, Warren S. (2009). Calculus: Early Transcendentals (3 ed.). Jones & Bartlett Learning. p.\xa0xxvii. ISBN\xa00-7637-5995-3.\xa0 Extract of page 27'], ['katz-10', u' Katz, V. J. 1995. "Ideas of Calculus in Islam and India." Mathematics Magazine (Mathematical Association of America), 68(3):163\xe2\u20ac\u201c174.'], ['11', u' "Indian mathematics".\xa0'], ['12', u' von Neumann, J., "The Mathematician", in Heywood, R. B., ed., The Works of the Mind, University of Chicago Press, 1947, pp. 180\u2013196. Reprinted in Br\xf3dy, F., V\xe1mos, T., eds., The Neumann Compedium, World Scientific Publishing Co. Pte. Ltd., 1995, ISBN 981-02-2201-7, pp. 618\u2013626.'], ['13', u' Andr\xe9 Weil: Number theory. An approach through history. From Hammurapi to Legendre. Birkhauser Boston, Inc., Boston, MA, 1984, ISBN 0-8176-4565-9, p. 28.'], ['14', u' Donald Allen: Calculus, http://www.math.tamu.edu/~dallen/history/calc1/calc1.html'], ['leib-15', u' Leibniz, Gottfried Wilhelm. The Early Mathematical Manuscripts of Leibniz. Cosimo, Inc., 2008. Page 228. Copy'], ['16', u' Allaire, Patricia R. (2007). Foreword. A Biography of Maria Gaetana Agnesi, an Eighteenth-century Woman Mathematician. By Cupillari, Antonella (illustrated ed.). Edwin Mellen Press. p.\xa0iii. ISBN\xa0978-0-7734-5226-8.\xa0'], ['17', u' Unlu, Elif (April 1995). "Maria Gaetana Agnesi". Agnes Scott College.\xa0'], ['18', u' Russell, Bertrand (1946). History of Western Philosophy. London: George Allen & Unwin Ltd. p.\xa0857. The great mathematicians of the seventeenth century were optimistic and anxious for quick results; consequently they left the foundations of analytical geometry and the infinitesimal calculus insecure. Leibniz believed in actual infinitesimals, but although this belief suited his metaphysics it had no sound basis in mathematics. Weierstrass, soon after the middle of the nineteenth century, showed how to establish the calculus without infinitesimals, and thus at last made it logically secure. Next came Georg Cantor, who developed the theory of continuity and infinite number. "Continuity" had been, until he defined it, a vague word, convenient for philosophers like Hegel, who wished to introduce metaphysical muddles into mathematics. Cantor gavprecise significance to the word, and showed that continuity, as he defined it, was the concept needed by mathematicians and physicists. By this meangreat deal of mysticism, such as that of Bergson, was rendered antiquated.\xa0'], ['19', u" Grabiner, Judith V. (1981). The Origins of Cauchy's Rigorous Calculus. Cambridge: MIT Press. ISBN\xa00-387-90527-8.\xa0"]]
```




