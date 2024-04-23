^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package gz_sim_vendor
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

0.1.0 (2024-04-23)
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
