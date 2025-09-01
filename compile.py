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

import os
import sys

from setuptools import Extension, setup


def compile_extensions():
    """Compile C extensions for otava"""
    print("Compiling C extensions...")

    extensions = []

    # E-divisive C extension
    c_file = "otava/signal_processing_algorithms/e_divisive/calculators/e_divisive.c"

    if not os.path.exists(c_file):
        print(f"Warning: {c_file} not found, skipping compilation")
        return extensions

    print(f"Compiling {c_file}...")
    extensions.append(
        Extension(
            "otava.signal_processing_algorithms.e_divisive.calculators._e_divisive",
            [c_file]
        )
    )

    return extensions


def main():
    """Main compilation function"""
    try:
        extensions = compile_extensions()

        if not extensions:
            print("No extensions to compile")
            return

        setup(
            ext_modules=extensions,
            script_args=['build_ext', '--inplace']
        )
        print("Compilation completed successfully")

    except Exception as e:
        print(f"Compilation failed: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
