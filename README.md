# SearchEngines

**SearchEngines** is a simple, yet elegant, searching libary. (and it's free)

```python
>>> from SearchEngines.Google import GoogleWeb
>>> init = GoogleWeb("Search any thing")
>>> init.get_web_results()
[
    {
        "q": "some stuff",
        "snippet": "\n\nBecause one stuff isn't enough.\n\n",
        "title": "Some-Stuffs",
        "url": "https://some-stuffs.com/"
    },
    {
        "q": "some stuff",
        "snippet": "\n\nSome examples from the web: You left some stuff here yesterday, Sosa. I got to tell you some stuff fast. We got some stuff to clean up with the Irish.\n\n",
        "title": "some stuffs or some stuff? - TextRanch",
        "url": "https://textranch.com/233057/some-stuffs/or/some-stuff/"
    },
    {
        "q": "some stuff",
        "snippet": "\n\n৬ দিন আগে ... I've got some stuff to do at home, so I'm going to take off now. I like modern art to a certain extent, but I don't like the really experimental ...\n\n",
        "title": "STUFF | meaning, definition in Cambridge English Dictionary",
        "url": "https://dictionary.cambridge.org/dictionary/english/stuff"
    },
    ...
]
```

SearchEngines is a package that contains all the search engines to get the results from them

## Installing Requests and Supported Versions

Requests is available on PyPI:

```console
$ python -m pip install SearchEngines
```

Requests officially supports Python 3.7+.



## Contributing

Contributions are always welcome!
