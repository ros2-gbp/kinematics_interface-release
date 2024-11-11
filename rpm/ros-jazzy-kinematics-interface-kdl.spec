%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/jazzy/.*$
%global __requires_exclude_from ^/opt/ros/jazzy/.*$

Name:           ros-jazzy-kinematics-interface-kdl
Version:        1.2.1
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS kinematics_interface_kdl package

License:        Apache License 2.0
Source0:        %{name}-%{version}.tar.gz

Requires:       eigen3-devel
Requires:       ros-jazzy-kdl-parser
Requires:       ros-jazzy-kinematics-interface
Requires:       ros-jazzy-pluginlib
Requires:       ros-jazzy-tf2-eigen-kdl
Requires:       ros-jazzy-ros-workspace
BuildRequires:  eigen3-devel
BuildRequires:  ros-jazzy-ament-cmake
BuildRequires:  ros-jazzy-eigen3-cmake-module
BuildRequires:  ros-jazzy-kdl-parser
BuildRequires:  ros-jazzy-kinematics-interface
BuildRequires:  ros-jazzy-pluginlib
BuildRequires:  ros-jazzy-tf2-eigen-kdl
BuildRequires:  ros-jazzy-ros-workspace
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%if 0%{?with_tests}
BuildRequires:  ros-jazzy-ament-cmake-gmock
BuildRequires:  ros-jazzy-ros2-control-test-assets
%endif

%description
KDL implementation of ros2_control kinematics interface

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jazzy/setup.sh" ]; then . "/opt/ros/jazzy/setup.sh"; fi
mkdir -p .obj-%{_target_platform} && cd .obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/jazzy" \
    -DAMENT_PREFIX_PATH="/opt/ros/jazzy" \
    -DCMAKE_PREFIX_PATH="/opt/ros/jazzy" \
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
if [ -f "/opt/ros/jazzy/setup.sh" ]; then . "/opt/ros/jazzy/setup.sh"; fi
%make_install -C .obj-%{_target_platform}

%if 0%{?with_tests}
%check
# Look for a Makefile target with a name indicating that it runs tests
TEST_TARGET=$(%__make -qp -C .obj-%{_target_platform} | sed "s/^\(test\|check\):.*/\\1/;t f;d;:f;q0")
if [ -n "$TEST_TARGET" ]; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jazzy/setup.sh" ]; then . "/opt/ros/jazzy/setup.sh"; fi
CTEST_OUTPUT_ON_FAILURE=1 \
    %make_build -C .obj-%{_target_platform} $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/jazzy

%changelog
* Mon Nov 11 2024 Bence Magyar <bence.magyar.robotics@gmail.com> - 1.2.1-1
- Autogenerated by Bloom

* Tue Nov 05 2024 Bence Magyar <bence.magyar.robotics@gmail.com> - 1.2.0-1
- Autogenerated by Bloom

* Mon May 20 2024 Bence Magyar <bence.magyar.robotics@gmail.com> - 1.1.0-1
- Autogenerated by Bloom

* Thu Apr 18 2024 Bence Magyar <bence.magyar.robotics@gmail.com> - 1.0.0-3
- Autogenerated by Bloom

* Wed Mar 06 2024 Bence Magyar <bence.magyar.robotics@gmail.com> - 1.0.0-2
- Autogenerated by Bloom
