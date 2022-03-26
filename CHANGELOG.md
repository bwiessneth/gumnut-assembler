# Changelog

## 4.0.0 (2022-03-26)


### ⚠ BREAKING CHANGES

* Rename exception for future distinction of root-cause

### Bug Fixes

* Fix suppression of output of exception type, message, and expression ([97b2294](https://www.github.com/bwiessneth/gumnut-assembler/commit/97b22948ff1c2e858b71e2ba4e334672fa9c4ca9))


### Code Refactoring

* Rename exception for future distinction of root-cause ([cee9439](https://www.github.com/bwiessneth/gumnut-assembler/commit/cee94395036b4b6f3e8ac4091d24005438249be0))


### Miscellaneous Chores

* release 4.0.0 ([3448262](https://www.github.com/bwiessneth/gumnut-assembler/commit/3448262db1d63785572730bdd5ad3c02e3fdc46c))


### Documentation

* Change scope of this file ([73a2f1e](https://www.github.com/bwiessneth/gumnut-assembler/commit/73a2f1effd85ee345ad3ca8f43a3a6610f10add1))
* Fix configuration for latest sphinx-rtd-theme version ([af07eec](https://www.github.com/bwiessneth/gumnut-assembler/commit/af07eecbbd5bc3b68dfa9252e5fa2ab3f274724a))
* Update version ([be25a65](https://www.github.com/bwiessneth/gumnut-assembler/commit/be25a65697393b671f8525e0b6adc039a3d5560c))
* Update year ([61ca55d](https://www.github.com/bwiessneth/gumnut-assembler/commit/61ca55df871e16926b50265e29aa518b38b09531))


## 3.0.0


### ⚠ BREAKING CHANGES

* Changed CLI entry point name from ``gumnut_assembler`` to ``gumnut-assembler``


## 2.0.0


### ⚠ BREAKING CHANGES

* Enforced proper module names and naming convention


## 1.0.3


### Bug Fixes

* Typos in README
* Making sure ``tox`` is using the package, not the source files for testing
* Updated development docs


## 1.0.2

### Miscellaneous Chores

* The README file is now also using reStructuredText format


### Bug Fixes

* ``equ`` directive is now working for ascii values (e.g. ``char_a: equ 'a'``)


## 1.0.1

### Miscellaneous Chores

* Proper CLI for standalone usage
* Documentation (still in progress, though)
* Introduced ``tox`` for handling testing, build, and publishing tasks
* Introduced Github Actions for automated testing

### Code Refactoring

* Replaced ``nosetest`` with ``pytest`` as the choice for unit and integration testing
* Updated the existing tests for ``pytest``


### Bug Fixes

* Module imports were fixed


## 1.0.0

The initial version which was *gumnut-assembler* was forked from.
