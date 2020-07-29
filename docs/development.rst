===========
Development
===========

On this page you can find some pointers and remarks regarding development for this project.



Setup python environment and install required packages
------------------------------------------------------

You definitely want to create a isolated python environment.
That way the required packages you are going to install with ``pip`` are encapsulated form your systemwide python installation. 
For more info check https://virtualenv.pypa.io/en/latest/

::

  [john@desktop ~]$ cd gaspy
  [john@desktop gaspy]$ virtualenv -p python3 ENV
  [john@desktop gaspy]$ source ENV/bin/activate
  (ENV) [john@desktop gaspy]$ pip install -r requirements.txt
  (ENV) [john@desktop gaspy]$

You can activate your new python environment like this:

::

  [john@desktop gaspy]$ source ENV/bin/activate
  (ENV) [john@desktop gaspy]$

Once you're done playing with it, deactivate it with the following command:

::

  (ENV) [john@desktop gaspy]$ deactivate
  [john@desktop gaspy]$



Config files
------------

pyproject.toml
~~~~~~~~~~~~~~

Set the default line width which is used by ``black``.


tox.ini
~~~~~~~

Default options/overrides for ``flake8``.


pytest.ini
~~~~~~~~~~

Default options for running ``pytest``.



Tests
-----

``pytest`` is used for testing. The tests and the needed files are located within the ``test`` directory. 
To run the tests simply call ``pytest`` from the project root with the virtual environment enabled.


:: 

	(ENV) [john@desktop gaspy]$ pytest
	================================ test session starts =================================

	[...]

	----------- coverage: platform win32, python 3.7.7-final-0 -----------
	Name                                  Stmts   Miss  Cover
	---------------------------------------------------------
	gaspy\GumnutAssembler.py      543     50    91%
	gaspy\GumnutExceptions.py      24      2    92%
	gaspy\__init__.py               1      0   100%
	---------------------------------------------------------
	TOTAL                                   568     52    91%
	Coverage HTML written to dir htmlcov


	================================= 23 passed in 0.61s =================================



Objectcode verification
~~~~~~~~~~~~~~~~~~~~~~~

Peter Ashenden's original Gumnut Assembler implementation *gasm* was used to assemble the sources from ``test\asm_source``.
The generated files (instruction and data memory) are located in ``test\gasm_output``.
For the test ``test_objectcode_comparison_static`` the files generated by *gaspy* are compared to those from *gasm*.

In future versions I'd like to implement the ``test_objectcode_comparison_dynamic`` again. This would assemble the sources with *gasm* during runtime of the tests.



Testing the package
-------------------

To install the package locally for testing in editable run ``pip install -e .``.
To uninstall the package run ``pip uninstall gaspy``.
See https://stackoverflow.com/a/19048754



Packaging for PyPI
------------------

To package the project for distribution and publishing it on PyPI a few steps are involved.
For more information see https://packaging.python.org/tutorials/packaging-projects/

* Set version in ``gaspy\__init__.py``
* Run ``python setup.py sdist bdist_wheel``
* Upload package to the test index ``python -m twine upload --repository testpypi dist/*``
* Download and install from test index ``python -m pip install --index-url https://test.pypi.org/simple/ --no-deps gaspy``

If all seems alright, repeat above steps and upload to the real PyPI.




Misc
----

*needs more explanation and structure*

* Using ``black`` for auto-formatting and styling the source code
* Line width 120
* Development on Linux and Windows possible