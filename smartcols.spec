#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : smartcols
Version  : 0.3.0
Release  : 21
URL      : https://github.com/ignatenkobrain/python-smartcols/archive/v0.3.0.tar.gz
Source0  : https://github.com/ignatenkobrain/python-smartcols/archive/v0.3.0.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-3.0
Requires: smartcols-license = %{version}-%{release}
Requires: smartcols-python = %{version}-%{release}
Requires: smartcols-python3 = %{version}-%{release}
BuildRequires : Cython
BuildRequires : buildreq-distutils3
BuildRequires : pkgconfig(smartcols)
BuildRequires : pytest-runner

%description
python-smartcols
================
Python bindings for util-linux libsmartcols-library.

%package license
Summary: license components for the smartcols package.
Group: Default

%description license
license components for the smartcols package.


%package python
Summary: python components for the smartcols package.
Group: Default
Requires: smartcols-python3 = %{version}-%{release}

%description python
python components for the smartcols package.


%package python3
Summary: python3 components for the smartcols package.
Group: Default
Requires: python3-core

%description python3
python3 components for the smartcols package.


%prep
%setup -q -n python-smartcols-0.3.0
cd %{_builddir}/python-smartcols-0.3.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1582921786
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/smartcols
cp %{_builddir}/python-smartcols-0.3.0/COPYING %{buildroot}/usr/share/package-licenses/smartcols/8624bcdae55baeef00cd11d5dfcfa60f68710a02
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/smartcols/8624bcdae55baeef00cd11d5dfcfa60f68710a02

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
