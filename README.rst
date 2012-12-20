Altmetric
=========
``Altmetric`` is a Python wrapper for `Altmetric API v1 <http://api.altmetric.com/>`.

Installation
------------
::

    pip install altmetric

Usage
-----

Fetching details by identifiers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    from altmetric import Altmetric
    a = Altmetric()
    a.id("108989")
    a.doi("10.1126/science.1173146")
    a.ads("2009sci...325..578w")
    a.arxiv("1212.4819")
    a.pmid("19644114")
    

    a = Altmetric("you_api_key")
    a.fetch("doi","10.1126/science.1173146")


Querying the database
~~~~~~~~~~~~~~~~~~~~~

::
    from altmetric import Altmetric
    a = Altmetric()
    a.citations('1d')
    a.citations('1d', page=2)


Catching Errors
~~~~~~~~~~~~~~~

::

    from altmetric import Altmetric
    a = Altmetric()
    try:
        rsp = a.doi("10.1234/foo")
        if rsp is None:
            print "DOI not found"
        else:
            print rsp['altmetric_id']
    except AltmetricHTTPException, e:
        if e.status_code == 403:
            print "You aren't authorized for this call"
        elif e.status_code == 420:
            print "You are being rate limited"
        elif e.status_code == 502:
            print "The API version you are using is currently down for maintenance."
        elif e.status_code == 404:
            print "Invalid API function"
            print e.msg


API Reference
-------------
Please see http://api.altmetric.com/ for detailed reference on response object
and parameters.