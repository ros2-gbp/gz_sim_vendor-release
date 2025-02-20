^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package gz_sim_vendor
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

0.0.8 (2025-02-19)
------------------
* Bump version to 8.9.0 (`#8 <https://github.com/gazebo-release/gz_sim_vendor/issues/8>`_)
* Contributors: Addisu Z. Taddese

0.0.7 (2025-01-16)
------------------
* Bump version to 8.8.0 (`#7 <https://github.com/gazebo-release/gz_sim_vendor/issues/7>`_)
* Contributors: Addisu Z. Taddese

0.0.6 (2024-11-08)
------------------
* Bump version to 8.7.0
* Contributors: Addisu Z. Taddese

0.0.5 (2024-08-08)
------------------
* Update vendored package version to 8.6.0
* Contributors: Addisu Z. Taddese

0.0.4 (2024-07-15)
------------------
* Update vendored package version to 8.5.0
* Contributors: Addisu Z. Taddese

0.0.3 (2024-04-25)
------------------
* Use an alias target for root library
* Contributors: Addisu Z. Taddese

0.0.2 (2024-04-12)
------------------
* Remove python3-distutils dependency
  This dependency is only needed in the vendored package for CMake
  versions less than 3.12. It is also failing to install on Noble
  currently preventing the whole vendor package from building.
* Update vendored version, add support for the `<pkg>::<pkg>` and `<pkg>::all` targets, fix sourcing of dsv files
* Require calling find_package on the underlying package
* Fix linter (`#1 <https://github.com/gazebo-release/gz_sim_vendor/issues/1>`_)
* Initial import
* Contributors: Addisu Z. Taddese
