================
fixationmodel-py
================

A least-squares offline method to test if tracked gaze points resemble a fixation.


1. Install
==========

With `pip
<https://pypi.python.org/pypi/fixationmodel>`_::

    $ pip install fixationmodel



2. Usage
========

A data structure we call **pointlist** is used for point sequences. It is a list of points, where each point is a list [x, y].

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



3. API
======

3.1. fixationmodel.fit(gazepointlist)
-------------------------------------

Parameter:

- gazepointlist: a list of [x, y] points i.e. a list of lists.

Return dict with following keys:

- centroid: a list [x, y], the most probable target of the fixation
- mean_squared_error: the average squared error for a point.


3.2. fixationmodel.version
--------------------------




4. For developers
=================

4.1. Virtualenv
---------------

Use virtualenv::

    $ virtualenv -p python3.5 fixationmodel-py
    $ cd fixationmodel-py
    $ source bin/activate
    ...
    $ deactivate


4.2. Testing
------------

Follow `instructions to install pyenv
<http://sqa.stackexchange.com/a/15257/14918>`_ and then either run quick tests::

    $ python3.5 setup.py test

or comprehensive tests for multiple Python versions in ``tox.ini``::

    $ pyenv local 2.6.9 2.7.10 3.2.6 3.3.6 3.4.3 3.5.0
    $ eval "$(pyenv init -)"
    $ pyenv rehash
    $ tox



4.3. Publishing to PyPI
-----------------------

Follow `python packaging instructions
<https://python-packaging-user-guide.readthedocs.org/en/latest/distributing/>`_:

1.  Create an unpacked sdist: ``$ python setup.py sdist``
2.  Create a universal wheel: ``$ python setup.py bdist_wheel --universal``
3.  Go to `PyPI and register the project by filling the package form
    <https://pypi.python.org/pypi?%3Aaction=submit_form>`_ by uploading
    ``fixationmodel.egg-info/PKG_INFO`` file.
4.  Upload the package with twine:

   1. Sign the dist: ``$ gpg --detach-sign -a dist/fixa...0.1.2*``
   3. Upload: ``twine upload dist/fixa...0.1.2*`` (will ask your PyPI password)

5. Package published!

Updating the package takes same steps except the 3rd.


5. Versioning
=============

`Semantic Versioning 2.0.0
<http://semver.org/>`_



6. License
==========

`MIT License
<http://github.com/axelpale/nudged-py/blob/master/LICENSE>`_
