%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/kilted/.*$
%global __requires_exclude_from ^/opt/ros/kilted/.*$

%global __cmake_in_source_build 1

Name:           ros-kilted-gz-sim-vendor
Version:        0.2.3
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS gz_sim_vendor package

License:        Apache License 2.0
URL:            https://github.com/gazebosim/gz-sim
Source0:        %{name}-%{version}.tar.gz

Requires:       freeglut-devel
Requires:       freeimage-devel
Requires:       glew-devel
Requires:       google-benchmark-devel
Requires:       libXi-devel
Requires:       libXmu-devel
Requires:       libuuid-devel
Requires:       protobuf-compiler
Requires:       protobuf-devel
Requires:       pybind11-devel
Requires:       qt5-qtbase-devel
Requires:       qt5-qtdeclarative
Requires:       qt5-qtdeclarative-devel
Requires:       qt5-qtgraphicaleffects
Requires:       qt5-qtquickcontrols
Requires:       qt5-qtquickcontrols2
Requires:       ros-kilted-gz-cmake-vendor
Requires:       ros-kilted-gz-common-vendor
Requires:       ros-kilted-gz-fuel-tools-vendor
Requires:       ros-kilted-gz-gui-vendor
Requires:       ros-kilted-gz-math-vendor
Requires:       ros-kilted-gz-msgs-vendor
Requires:       ros-kilted-gz-physics-vendor
Requires:       ros-kilted-gz-plugin-vendor
Requires:       ros-kilted-gz-rendering-vendor
Requires:       ros-kilted-gz-sensors-vendor
Requires:       ros-kilted-gz-tools-vendor
Requires:       ros-kilted-gz-transport-vendor
Requires:       ros-kilted-gz-utils-vendor
Requires:       ros-kilted-sdformat-vendor
Requires:       tinyxml2-devel
Requires:       ros-kilted-ros-workspace
BuildRequires:  cmake3
BuildRequires:  freeglut-devel
BuildRequires:  freeimage-devel
BuildRequires:  glew-devel
BuildRequires:  google-benchmark-devel
BuildRequires:  libXi-devel
BuildRequires:  libXmu-devel
BuildRequires:  libuuid-devel
BuildRequires:  protobuf-compiler
BuildRequires:  protobuf-devel
BuildRequires:  pybind11-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtdeclarative
BuildRequires:  qt5-qtdeclarative-devel
BuildRequires:  qt5-qtgraphicaleffects
BuildRequires:  qt5-qtquickcontrols
BuildRequires:  qt5-qtquickcontrols2
BuildRequires:  ros-kilted-ament-cmake-core
BuildRequires:  ros-kilted-ament-cmake-test
BuildRequires:  ros-kilted-ament-cmake-vendor-package
BuildRequires:  ros-kilted-gz-cmake-vendor
BuildRequires:  ros-kilted-gz-common-vendor
BuildRequires:  ros-kilted-gz-fuel-tools-vendor
BuildRequires:  ros-kilted-gz-gui-vendor
BuildRequires:  ros-kilted-gz-math-vendor
BuildRequires:  ros-kilted-gz-msgs-vendor
BuildRequires:  ros-kilted-gz-physics-vendor
BuildRequires:  ros-kilted-gz-plugin-vendor
BuildRequires:  ros-kilted-gz-rendering-vendor
BuildRequires:  ros-kilted-gz-sensors-vendor
BuildRequires:  ros-kilted-gz-tools-vendor
BuildRequires:  ros-kilted-gz-transport-vendor
BuildRequires:  ros-kilted-gz-utils-vendor
BuildRequires:  ros-kilted-sdformat-vendor
BuildRequires:  tinyxml2-devel
BuildRequires:  ros-kilted-ros-workspace
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%if 0%{?with_tests}
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  ros-kilted-ament-cmake-copyright
BuildRequires:  ros-kilted-ament-cmake-lint-cmake
BuildRequires:  ros-kilted-ament-cmake-xmllint
BuildRequires:  xorg-x11-server-Xvfb
%endif

%description
Vendor package for: gz-sim9 9.5.0 Gazebo Sim : A Robotic Simulator

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kilted/setup.sh" ]; then . "/opt/ros/kilted/setup.sh"; fi
mkdir -p .obj-%{_target_platform} && cd .obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/kilted" \
    -DAMENT_PREFIX_PATH="/opt/ros/kilted" \
    -DCMAKE_PREFIX_PATH="/opt/ros/kilted" \
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
if [ -f "/opt/ros/kilted/setup.sh" ]; then . "/opt/ros/kilted/setup.sh"; fi
%make_install -C .obj-%{_target_platform}

%if 0%{?with_tests}
%check
# Look for a Makefile target with a name indicating that it runs tests
TEST_TARGET=$(%__make -qp -C .obj-%{_target_platform} | sed "s/^\(test\|check\):.*/\\1/;t f;d;:f;q0")
if [ -n "$TEST_TARGET" ]; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kilted/setup.sh" ]; then . "/opt/ros/kilted/setup.sh"; fi
CTEST_OUTPUT_ON_FAILURE=1 \
    %make_build -C .obj-%{_target_platform} $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/kilted

%changelog
* Fri Oct 24 2025 Addisu Z. Taddese <addisuzt@intrinsic.ai> - 0.2.3-1
- Autogenerated by Bloom

* Wed Sep 24 2025 Addisu Z. Taddese <addisuzt@intrinsic.ai> - 0.2.2-1
- Autogenerated by Bloom

* Wed Apr 23 2025 Addisu Z. Taddese <addisuzt@intrinsic.ai> - 0.2.1-2
- Autogenerated by Bloom

