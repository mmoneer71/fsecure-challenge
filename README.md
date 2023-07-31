# F-Secure hiring challenge
Solution to the F-Secure hiring challenge - Protection Platform Team

## Overview
Simple Python Library that accepts a list of string records of variable length and batches it into an array of arrays. These batches are delivered to a system with the following constraints:

- Maximum size of output record is 1 MB, larger records are discarded
- Maximum size of output batch is 5 MB
- Maximum number of records in an output batch is 500

## Installation
The solution has been written and tested with Python version 3.10.6. It has also been linted by `black`, `isort` and `mypy`.

If you want to setup the virtual environment first, please make sure python3.10-venv is installed or install it by running:

`sudo apt install python3.10-venv`

then run:

`python3 -m venv .venv`

and activate the virtual env:

`source .venv/bin/activate`


The lib itself does not require any installation dependencies. However for any dev actions, such as running tests/linter or to run setup.py, please install the dependencies by running: `pip install -r requirements.txt`, preferably inside a virtual env to avoid conflicts.

Tests can be also run by using the following command:

`python -m pytest tests/`

To install the library you can run:

`python setup.py install`

or generate a whl file to be installed by pip later by running:

`python setup.py bdist_wheel`

which will store the new wheel file in a new directory `/dist` which can then be installed as follows:

`pip install /path/to/wheelfile.whl`

Once you have installed the Python library, you can import it using:

`from batchlib import utils`
or
`from batchlib.utils import create_output_records`

## Discussion
This solution is a very straightforward approach and can be further optimized, however, there is not enough information in the problem description. Below are a few discussion points that can help guide a better implementation or optimization.

- What is the maximum number of input records received? The library will take a longer time to process a very large input records array (time complexity is O(n)), which may block the services that use it. One way to mitigate blocking the service's main thread would be to execute this code in a seperate thread or in the background if the input records are considerably large.

- How is this library going to be used? The library stores output batches in memory while processing. This can mitigated by increasing RAM on the target machine/server, but implies that every service that uses this library will require more memory.

- What kind of string input is received here? Can the input records include code? While the library source code itself is not subject to a code injection threat (i.e. it does not execute any code directly or call the subinterpreter); it will still foward the records as is, which is something to consider while designing the services that use it.
