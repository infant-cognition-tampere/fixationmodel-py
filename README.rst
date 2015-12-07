================
fixationmodel-py
================

A least-squares offline method to test if tracked gaze points resemble a fixation.


Install
=======

With `pip
<http://example.com>`_::

    $ pip install fixationmodel



Usage
=====

The data structure **pointlist** is used thoroughly. It is a list of points, where each point is a list [x, y].

The usage is simple::

    >>> import fixationmodel
    >>> rawdata = [
        [130.012, 404.231],
        [129.234, 403.478],
        [None, None],
        [133.983, 450.044],
        ...
    ]
    >>> results = fixationmodel.fit(rawdata)
    >>> print(results)
    {
        'centroid': [344.682, 200.115],
        'mean_squared_error': 0.000166802
    }



API
===

fixationmodel.fit(gazepointlist)
--------------------------------

Parameter:

- gazepointlist: a list of [x, y] points i.e. a list of lists.

Return dict with following keys:

- centroid: a list [x, y], the most probable target of the fixation
- mean_squared_error: the average squared error for a point.


fixationmodel.version
---------------------




For developers
==============

Use virtualenv::

    $ virtualenv -p python3.5 fixationmodel-py
    $ cd fixationmodel-py
    $ source bin/activate
    ...
    $ deactivate


Testing
-------

Follow `instructions to install pyenv
<http://sqa.stackexchange.com/a/15257/14918>`_ and then either run quick tests::

    $ python3.5 setup.py test

or comprehensive tests for multiple Python versions in ``tox.ini``::

    $ eval "$(pyenv init -)"
    $ pyenv rehash
    $ tox



Versioning
==========

`Semantic Versioning 2.0.0
<http://semver.org/>`_



License
=======

`MIT License
<http://github.com/axelpale/nudged-py/blob/master/LICENSE>`_
