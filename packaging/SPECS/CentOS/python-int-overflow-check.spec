%define pname int-overflow-check
%define version 0.1b.1.dev
%define unmangled_version 0.1b.1.dev
%define unmangled_version 0.1b.1.dev
%define release 1.pdb%{?dist}

Summary: Check MySQL tables for potential integer overflows
Name: python-%{pname}
Version: %{version}
Release: %{release}
Source0: %{pname}-%{unmangled_version}.tar.gz
License: GPLv2
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: PalominoDB <oss@palominodb.com>
Packager: PalominoDB <oss@palominodb.com>
BuildRequires: python >= 2.4
Requires: gcc python >= 2.4 python-setuptools >= 0.6 mysql-devel >= 5.0 MySQL-python >= 1.2 python-argparse >= 1.2
Url: http://pypi.python.org/pypi/int-overflow-check

%description
Check MySQL tables for potential integer overflows

%prep
%setup -n %{pname}-%{unmangled_version} -n %{pname}-%{unmangled_version}

%build
python setup.py build

%install
python setup.py install --single-version-externally-managed -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES
%{__mkdir_p} %{buildroot}%{_mandir}/man1
for man in docs/man/*.1; do
    %{__install} -p -m0644 ${man} %{buildroot}%{_mandir}/man1/
done

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)
%doc docs/
%{_mandir}/man1/*
