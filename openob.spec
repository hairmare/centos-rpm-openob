%global         srcname  OpenOB

Name:           openob
Version:        3.2.0
Release:        1%{?dist}
Summary:        The Open Outside Broadcast project for radio contribution links and studio-transmitter links. http
License:        BSD
URL:            https://pypi.python.org/pypi/openob
Source0:        https://pypi.python.org/packages/99/55/4312275bc1570c038195a9f9d15460e95a1264fbf2e3bd1b33799a082320/%{srcname}-%{version}.tar.gz

BuildRequires:  python
BuildRequires:  python-setuptools

Requires:       pygobject2
Requires:       gstreamer-python
Requires:       python-redis

BuildArch:      noarch

%{!?py2_build: %global py2_build CFLAGS="$RPM_OPT_FLAGS" %{__python} setup.py build}
%{!?py2_install: %global py2_install %{__python} setup.py install --skip-build --root %{buildroot}}
%{!?python2_sitelib: %global python2_sitelib %{python_sitelib}}

%description
OpenOB (Open Outside Broadcast) is a simple Python/GStreamer based application which implements a highly configurable RTP-based audio link system.

It is primarily designed for broadcast applications including (but not limited to) contribution links, emission links, talkback, and intranet audio distribution systems.

%prep
%autosetup -p1 -n %{srcname}-%{version}

%build
%py2_build

%install
%py2_install

%files
%{python2_sitelib}/%{name}
%{python2_sitelib}/%{srcname}-%{version}*.egg-info
%{_bindir}/%{name}
