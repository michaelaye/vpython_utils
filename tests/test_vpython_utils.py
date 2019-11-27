#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `vpython_utils` package."""

import pytest


from vpython_utils import vpython_utils


@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/michaelaye/cookiecutter-pypackage-conda')


def test_content(response):
    """Sample pytest test function with the pytest fixture as an argument."""
    # from bs4 import BeautifulSoup
    # assert 'GitHub' in BeautifulSoup(response.content).title.string
