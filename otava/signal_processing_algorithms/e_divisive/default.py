# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

"""Default implementations for E-Divisive."""

from otava.signal_processing_algorithms.e_divisive.base import EDivisiveCalculator
from otava.signal_processing_algorithms.e_divisive.calculators import (
    cext_calculator,
    numpy_calculator,
)
from otava.signal_processing_algorithms.e_divisive.e_divisive import EDivisive
from otava.signal_processing_algorithms.e_divisive.significance_test import (
    QHatPermutationsSignificanceTester,
)


def default_implementation() -> EDivisive:
    """
    Create a default implementation of E-Divisive.

    :return: The default implementation.
    """
    if cext_calculator.C_EXTENSION_LOADED:
        # TODO: Remove mypy exception once implemented: https://github.com/python/mypy/issues/5018
        calculator: EDivisiveCalculator = cext_calculator  # type: ignore
    else:
        calculator = numpy_calculator  # type: ignore
    tester = QHatPermutationsSignificanceTester(
        calculator=calculator, pvalue=0.05, permutations=100
    )
    return EDivisive(seed=1234, calculator=calculator, significance_tester=tester)
