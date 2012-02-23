Wikilanguages
=============

Wikilanguages is a Python library to manipulate with all the languages used in Wikipedia projects

Wikilanguages is licensed under the TBD??? license (probably MIT or public domain)

Features
--------

Wikilanguages has:

- list of all language prefixes for all active Wikipedias

- list of language/scripts details (such as left-to-right or right-ti-left scripts)

- basic stats for Wikipeidas for each of the languages (# of articles, etc)

- language groups (to be added)

Install
-------

python ./setup.py install


Data Sources
------------

* [List of Wikipedias] (http://meta.wikimedia.org/wiki/List_of_Wikipedias)

* [List of Wikipedias by language group] (http://meta.wikimedia.org/wiki/List_of_Wikipedias_by_language_group)

* [List of Wikipedias by speakers per article] (http://meta.wikimedia.org/wiki/List_of_Wikipedias_by_speakers_per_article)

Usage
-----


`>>> import wikilanguages`

`>>> langs=wikilanguages.langs`

`>>> langs["en"]`

`{'stats': {'articles': u'"3,825,380"', 'active_users': u'"142,406"'}, 'name': u'English', 'script': {'rendering': u'', 'direction': u'ltr', 'non_latin': u'no', 'constructed': u'no'}, 'number': u'1', 'native_name': u'English', 'group': u'Germanic', 'size': u'1 000 000+ articles'}`

`>>> langs["ru"]`

`{'stats': {'articles': u'"802,956"', 'active_users': u'"11,901"'}, 'name': u'Russian', 'script': {'rendering': u'', 'direction': u'ltr', 'non_latin': u'yes', 'constructed': u'no'}, 'number': u'8', 'native_name': u'\u0420\u0443\u0441\u0441\u043a\u0438\u0439', 'group': u'Slavic', 'size': u'100 000+ articles'}`