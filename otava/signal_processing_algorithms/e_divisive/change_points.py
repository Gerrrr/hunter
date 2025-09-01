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

"""A change point detected by E-Divisive."""
from typing import Optional


class EDivisiveChangePoint:
    """A change point."""

    __slots__ = ["index", "qhat", "probability"]

    def __init__(self, index: int = 0, qhat: float = 0, probability: Optional[float] = None):
        """
        Create an E-Divisive change point, representing a change point found by E-Divisive algorithm.

        :param index: Index of the change point.
        :param qhat: The Q-Hat metric for the change point.
        :param probability: The probability that the change point is valid, based on a permutation test.
        """
        self.index = index
        self.qhat = qhat
        self.probability = probability

    index: int
    qhat: float
    probability: Optional[float]

    def __eq__(self, other: object) -> bool:
        """
        Check whether one change point is equal to another based on index, qhat, and probability.

        :param other: The other change point.
        :return: True if they are equal, false otherwise.
        """
        if not isinstance(other, EDivisiveChangePoint):
            return False
        return (
            self.index == other.index
            and self.qhat == other.qhat
            and self.probability == other.probability
        )
