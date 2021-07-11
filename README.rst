==============================================
EVE Offline Solo Roam:  A text adventure game 
==============================================

By Sapporo Jones 


Readme
======

For now set system origin and destination in the script itself at the top of soloroam.py.  Uses CCP ESI
to plot route and resolve system IDs to names.


Installation:
=============

Download the source of this repository with git clone or whatever.

Make sure you have the latest version of python installed in your computer.

Once you have downloaded and extracted the source, open a command prompt in the source directory.

Issue the command :code:`pip install ./` or if you'd rather, make a new virtualenv then run that commmand inside of it.

Usage:
======

Once installed with pip use :code:`python -m soloroam` to play.

If you would like to change the start or end systems or both use the -s and -d flags.

Examples:
To start with default options use:
:code:`python -m soloroam`

To start in Tama and end in the default end system use:
:code:`python -m soloroam -s Tama`

To start in D-PNP9 and end in Jita use:
:code:`python -m soloroam -s D-PNP9 -d Jita`


Changelog
=========

v0.9.5
------------
- Version tests are stupid anyways. [sapporojones]
- Fixed setuptools issues with pyproject.toml changes, fixed autodoc
  issues with conf.py changes, some setup.cfg changes as well, this
  should resolve all build issues he said as famous last words.
  [sapporojones]
- Sphinx was complaining about module level argparse code so I moved it
  to the if name is main blah blah should resolve issues. [sapporojones]
- Fixed issue 9 typo, the pyinstaller issue is still open until I switch
  to a different windows supported build system, also removing doctests
  and docgen from tox process. [sapporojones]
- Fixed doc generation, fixed tox builds, fixed error handling for
  system commands, fixed module references, restructured project to be
  more pypi compliant and pytest friendly. [sapporojones]
- Fixing issue 8, prepping for pypi setup. [sapporojones]
- Adding some github hooks. [sapporojones]
- Adding more prep for pyinstaller. [sapporojones]
- Added 5 new encounters, added a rudimentary and somewhoat arbitrary
  combat system, added killmarks, prepped for pyinstaller.
  [sapporojones]
- Added logging, argparse for logging and arbitrary origin/desti, help
  should already be updated automagically, added partial command
  matching, added tox support and basic setup.py/cfg. [sapporojones]
- Create .pre-commit-config.yaml. [sapporojones]
- More bug fixes and an extra encounter. [sapporojones]
- Many fixes. [sapporojones]

  fixed loot system, added encounters, added delays in some encounters for immersion, fixed movement system, probably more.
- Project cleanup redux. [sapporojones]
- More testing fixes. [Sapporo Jones]
- Unit test fixes and implementations. [Sapporo Jones]
- Unit test update. [sapporojones]

  this minor patch is about fixing the unit test scheme I had so that it's something that actually tests functionality rather than sanity checking.
- Update __init__.py. [sapporojones]

  poetry doesn't update __init__.py or my tests.  fixed.
- Version bump. [sapporojones]

  forgot to do this after pull request and test fixes
- Updates to tests - class changes. [sapporojones]
- Merge pull request #1 from Xaoc000/main. [sapporojones]

  Added random loot for wrecks and small bug fixes
- Added random loot for wrecks. [Ian Martin]
- Bug fixes. [sapporojones]
- Adding todo for encounters and cleaning stuff up. [sapporojones]
- Update README.rst. [sapporojones]
- Version update. [sapporojones]