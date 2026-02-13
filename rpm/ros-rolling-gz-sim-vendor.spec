%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/rolling/.*$
%global __requires_exclude_from ^/opt/ros/rolling/.*$

%global __cmake_in_source_build 1

Name:           ros-rolling-gz-sim-vendor
Version:        0.4.4
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS gz_sim_vendor package

License:        Apache License 2.0
URL:            https://github.com/gazebosim/gz-sim
Source0:        %{name}-%{version}.tar.gz

Requires:       binutils-devel
Requires:       elfutils-devel
Requires:       freeglut-devel
Requires:       freeimage-devel
Requires:       glew-devel
Requires:       google-benchmark-devel
Requires:       libXi-devel
Requires:       libXmu-devel
Requires:       libdwarf-devel
Requires:       libuuid-devel
Requires:       libwebsockets-devel
Requires:       protobuf-compiler
Requires:       protobuf-devel
Requires:       pybind11-devel
Requires:       qt6-qt5compat-devel
Requires:       qt6-qtbase-devel
Requires:       qt6-qtbase-private-devel
Requires:       qt6-qtdeclarative
Requires:       qt6-qtdeclarative-devel
Requires:       ros-rolling-gz-cmake-vendor
Requires:       ros-rolling-gz-common-vendor
Requires:       ros-rolling-gz-fuel-tools-vendor
Requires:       ros-rolling-gz-gui-vendor
Requires:       ros-rolling-gz-math-vendor
Requires:       ros-rolling-gz-msgs-vendor
Requires:       ros-rolling-gz-physics-vendor
Requires:       ros-rolling-gz-plugin-vendor
Requires:       ros-rolling-gz-rendering-vendor
Requires:       ros-rolling-gz-sensors-vendor
Requires:       ros-rolling-gz-tools-vendor
Requires:       ros-rolling-gz-transport-vendor
Requires:       ros-rolling-gz-utils-vendor
Requires:       ros-rolling-sdformat-vendor
Requires:       tinyxml2-devel
Requires:       ros-rolling-ros-workspace
BuildRequires:  binutils-devel
BuildRequires:  cmake3
BuildRequires:  elfutils-devel
BuildRequires:  freeglut-devel
BuildRequires:  freeimage-devel
BuildRequires:  glew-devel
BuildRequires:  google-benchmark-devel
BuildRequires:  libXi-devel
BuildRequires:  libXmu-devel
BuildRequires:  libdwarf-devel
BuildRequires:  libuuid-devel
BuildRequires:  libwebsockets-devel
BuildRequires:  protobuf-compiler
BuildRequires:  protobuf-devel
BuildRequires:  pybind11-devel
BuildRequires:  qt6-qt5compat-devel
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  qt6-qtdeclarative
BuildRequires:  qt6-qtdeclarative-devel
BuildRequires:  ros-rolling-ament-cmake-core
BuildRequires:  ros-rolling-ament-cmake-test
BuildRequires:  ros-rolling-ament-cmake-vendor-package
BuildRequires:  ros-rolling-gz-cmake-vendor
BuildRequires:  ros-rolling-gz-common-vendor
BuildRequires:  ros-rolling-gz-fuel-tools-vendor
BuildRequires:  ros-rolling-gz-gui-vendor
BuildRequires:  ros-rolling-gz-math-vendor
BuildRequires:  ros-rolling-gz-msgs-vendor
BuildRequires:  ros-rolling-gz-physics-vendor
BuildRequires:  ros-rolling-gz-plugin-vendor
BuildRequires:  ros-rolling-gz-rendering-vendor
BuildRequires:  ros-rolling-gz-sensors-vendor
BuildRequires:  ros-rolling-gz-tools-vendor
BuildRequires:  ros-rolling-gz-transport-vendor
BuildRequires:  ros-rolling-gz-utils-vendor
BuildRequires:  ros-rolling-sdformat-vendor
BuildRequires:  tinyxml2-devel
BuildRequires:  ros-rolling-ros-workspace
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%if 0%{?with_tests}
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  ros-rolling-ament-cmake-copyright
BuildRequires:  ros-rolling-ament-cmake-lint-cmake
BuildRequires:  ros-rolling-ament-cmake-xmllint
BuildRequires:  xorg-x11-server-Xvfb
%endif

%description
Vendor package for: gz-sim 10.1.1 Gazebo Sim : A Robotic Simulator

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/rolling/setup.sh" ]; then . "/opt/ros/rolling/setup.sh"; fi
mkdir -p .obj-%{_target_platform} && cd .obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/rolling" \
    -DAMENT_PREFIX_PATH="/opt/ros/rolling" \
    -DCMAKE_PREFIX_PATH="/opt/ros/rolling" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
%if !0%{?with_tests}
    -DBUILD_TESTING=OFF \
%endif
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/rolling/setup.sh" ]; then . "/opt/ros/rolling/setup.sh"; fi
%make_install -C .obj-%{_target_platform}

%if 0%{?with_tests}
%check
# Look for a Makefile target with a name indicating that it runs tests
TEST_TARGET=$(%__make -qp -C .obj-%{_target_platform} | sed "s/^\(test\|check\):.*/\\1/;t f;d;:f;q0")
if [ -n "$TEST_TARGET" ]; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/rolling/setup.sh" ]; then . "/opt/ros/rolling/setup.sh"; fi
CTEST_OUTPUT_ON_FAILURE=1 \
    %make_build -C .obj-%{_target_platform} $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/rolling

%changelog
* Fri Feb 13 2026 Addisu Z. Taddese <addisuzt@intrinsic.ai> - 0.4.4-1
- Autogenerated by Bloom

* Thu Jan 22 2026 Addisu Z. Taddese <addisuzt@intrinsic.ai> - 0.4.3-1
- Autogenerated by Bloom

* Wed Oct 01 2025 Addisu Z. Taddese <addisuzt@intrinsic.ai> - 0.4.2-1
- Autogenerated by Bloom

* Thu Sep 25 2025 Addisu Z. Taddese <addisuzt@intrinsic.ai> - 0.4.1-1
- Autogenerated by Bloom

* Mon Sep 08 2025 Addisu Z. Taddese <addisuzt@intrinsic.ai> - 0.4.0-1
- Autogenerated by Bloom

* Thu Sep 04 2025 Addisu Z. Taddese <addisuzt@intrinsic.ai> - 0.3.0-1
- Autogenerated by Bloom

