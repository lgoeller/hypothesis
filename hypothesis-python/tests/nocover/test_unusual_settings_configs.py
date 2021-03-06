# coding=utf-8
#
# This file is part of Hypothesis, which may be found at
# https://github.com/HypothesisWorks/hypothesis-python
#
# Most of this work is copyright (C) 2013-2018 David R. MacIver
# (david@drmaciver.com), but it contains contributions by others. See
# CONTRIBUTING.rst for a full list of people who may hold copyright, and
# consult the git log if you need to determine who owns an individual
# contribution.
#
# This Source Code Form is subject to the terms of the Mozilla Public License,
# v. 2.0. If a copy of the MPL was not distributed with this file, You can
# obtain one at http://mozilla.org/MPL/2.0/.
#
# END HEADER

from __future__ import division, print_function, absolute_import

import hypothesis.strategies as st
from hypothesis import Verbosity, HealthCheck, given, assume, settings


@settings(max_examples=1, database=None)
@given(st.integers())
def test_single_example(n):
    pass


@settings(
    max_examples=1, database=None,
    suppress_health_check=[HealthCheck.filter_too_much, HealthCheck.too_slow],
    verbosity=Verbosity.debug,
)
@given(st.integers())
def test_hard_to_find_single_example(n):
    # Numbers are arbitrary, just deliberately unlikely to hit this too soon.
    assume(n % 50 == 11)
