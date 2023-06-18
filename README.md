# F-Secure hiring challenge
Solution to the F-Secure hiring challenge - Protection Platform Team

The solution has been written and tested with Python version 3.10.6.

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
