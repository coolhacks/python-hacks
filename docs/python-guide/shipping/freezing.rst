.. _freezing-your-code-ref:

==================
Freezing Your Code
==================

To 'Freeze' your code is to distribute to end-users as an executable which
includes a bundled Python interpreter.

Applications such as 'Dropbox', BitTorrent clients, 'Eve Online' and
'Civilisation IV' do this.

The advantage of distributing this way is that your application will work even
if the user doesn't already have the required version of Python installed. On
Windows, and even on many Linux distributions and OSX versions, the right
version of Python will not already be installed.

One disadvantage is that it will bloat your distribution by about 2MB.
Another problem is that your application will not receive any security updates
to the version of Python it uses unless you freeze a new version and get
users to download it.

Alternatives to Freezing
------------------------

:ref:`Packaging your code <packaging-your-code-ref>` is for distributing
libraries or tools to other developers.

On Linux, an alternative to freezing is to
:ref:`create a Linux distro package <packaging-for-linux-distributions-ref>`
(e.g. .deb files for Debian or Ubuntu, or .rpm files for Red Hat and SuSE.)

.. todo:: Fill in "Freezing Your Code" stub


Comparison
----------

Solutions and platforms/features supported:

=========== ======= ===== ==== ======== ======= ============= ============== ==== =====================
Solution    Windows Linux OS X Python 3 License One-file mode Zipfile import Eggs pkg_resources support
=========== ======= ===== ==== ======== ======= ============= ============== ==== =====================
bbFreeze    yes     yes   yes  no       MIT     no            yes            yes  yes
py2exe      yes     no    no   yes      MIT     yes           yes            no   no
pyInstaller yes     yes   yes  yes      GPL     yes           no             yes  no
cx_Freeze   yes     yes   yes  yes      PSF     no            yes            yes  no
py2app      no      no    yes  yes      MIT     no            yes            yes  yes
=========== ======= ===== ==== ======== ======= ============= ============== ==== =====================

.. note::
    Freezing Python code on Linux into a Windows executable was only once
    supported in PyInstaller `and later dropped.
    <http://stackoverflow.com/questions/2950971/cross-compiling-a-python-script-on-linux-into-a-windows-executable#comment11890276_2951046>`_.

.. note::
    All solutions need MS Visual C++ dll to be installed on target machine, except py2app.
    Only Pyinstaller makes self-executable exe that bundles the dll when
    passing :option:`--onefile` to :file:`Configure.py`.

Windows
-------

bbFreeze
~~~~~~~~

Prerequisite is to install :ref:`Python, Setuptools and pywin32 dependency on Windows <install-windows>`.

.. todo:: Write steps for most basic .exe

py2exe
~~~~~~

Prerequisite is to install :ref:`Python on Windows <install-windows>`.

1. Download and install http://sourceforge.net/projects/py2exe/files/py2exe/

2. Write :file:`setup.py` (`List of configuration options <http://www.py2exe.org/index.cgi/ListOfOptions>`_):

.. code-block:: python

    from distutils.core import setup
    import py2exe

    setup(
        windows=[{'script': 'foobar.py'}],
    )

3. (Optionally) `include icon <http://www.py2exe.org/index.cgi/CustomIcons>`_

4. (Optionally) `one-file mode <http://stackoverflow.com/questions/112698/py2exe-generate-single-executable-file#113014>`_

5. Generate :file:`.exe` into :file:`dist` directory:

.. code-block:: console

   $ python setup.py py2exe

6. Provide the Microsoft Visual C runtime DLL. Two options: `globally install dll on target machine <https://www.microsoft.com/en-us/download/details.aspx?id=29>`_ or `distribute dll alongside with .exe <http://www.py2exe.org/index.cgi/Tutorial#Step52>`_.

PyInstaller
~~~~~~~~~~~

Prerequisite is to have installed :ref:`Python, Setuptools and pywin32 dependency on Windows <install-windows>`.

- `Most basic tutorial <http://bojan-komazec.blogspot.com/2011/08/how-to-create-windows-executable-from.html>`_
- `Manual <http://www.pyinstaller.org/export/d3398dd79b68901ae1edd761f3fe0f4ff19cfb1a/project/doc/Manual.html?format=raw>`_


OS X
----


py2app
~~~~~~

PyInstaller
~~~~~~~~~~~

PyInstaller can be used to build Unix executables and windowed apps on Mac OS X 10.6 (Snow Leopard) or newer.

To install PyInstaller, use pip:

.. code-block:: console

 $ pip install pyinstaller

To create a standard Unix executable, from say :code:`script.py`, use:

.. code-block:: console

 $ pyinstaller script.py

This creates,

- a :code:`script.spec` file, analogous to a :code:`make` file
- a :code:`build` folder, that holds some log files
- a :code:`dist` folder, that holds the main executable :code:`script`, and some dependent Python libraries,

all in the same folder as :code:`script.py`. PyInstaller puts all the Python libraries used in :code:`script.py` into the :code:`dist` folder, so when distributing the executable, distribute the whole :code:`dist` folder.

The :code:`script.spec` file can be edited to `customise the build <http://pythonhosted.org/PyInstaller/#spec-file-operation>`_, with options such as

- bundling data files with the executable
- including run-time libraries (:code:`.dll` or :code:`.so` files) that PyInstaller can't infer automatically
- adding Python run-time options to the executable,

Now :code:`script.spec` can be run with :code:`pyinstaller` (instead of using :code:`script.py` again):

.. code-block:: console

  $ pyinstaller script.spec

To create a standalone windowed OS X application, use the :code:`--windowed` option

.. code-block:: console

 $ pyinstaller --windowed script.spec

This creates a :code:`script.app` in the :code:`dist` folder. Make sure to use GUI packages in your Python code, like `PyQt <https://riverbankcomputing.com/software/pyqt/intro>`_ or `PySide <http://wiki.qt.io/About-PySide>`_, to control the graphical parts of the app.

There are several options in :code:`script.spec` related to Mac OS X app bundles `here <http://pythonhosted.org/PyInstaller/#spec-file-options-for-a-mac-os-x-bundle>`_. For example, to specify an icon for the app, use the :code:`icon=\path\to\icon.icns` option. 


Linux
-----


bbFreeze
~~~~~~~~

PyInstaller
~~~~~~~~~~~
