# `retry` decorator

[![Build Status](https://travis-ci.org/soasme/retries.png?branch=master)](https://travis-ci.org/soasme/retries)

A dead simple way to retry your method.

Through source code:

    git clone git://github.com/soasme/retries.git
    cd retries
    python setup.py install

Usage:

    from retry import retry

    @retry(errors=(urllib2.URLError), tries=3, delay=3.5)
    def fetch_page():
        pass

    @retry(errors=(TTransportException, ), delay=0.1)
    def thrift_call():
        pass
