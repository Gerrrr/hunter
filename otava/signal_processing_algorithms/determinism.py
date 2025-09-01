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

"""Functions to help setup deterministic results when using random numbers."""
# E-Divisive's definition requires it to permute change-windows
# which leads to non-determinism: we need to always get the
# same change-point results when running on the same input.
import random
from contextlib import contextmanager
from typing import Generator


@contextmanager
def deterministic_random(seed: float) -> Generator:
    """
    Call random.seed(seed) during invocation and then restore state after.

    :param seed: RNG seed.
    :return: Deterministic random context.
    """
    state = random.getstate()
    random.seed(seed)
    try:
        yield
    finally:
        random.setstate(state)
