
Name:           doxygen
Version:        1.7.4
Release:        1
License:        GPLv2+
Group:          Development/Tools
Summary:        Automated C, C++, and Java Documentation Generator
Url:            http://www.stack.nl/~dimitri/doxygen/
Source:         http://ftp.stack.nl/pub/users/dimitri/doxygen-%{version}.tar.gz
Source1001: packaging/doxygen.manifest 
Patch0:         doxygen-1.7.1-config.patch
BuildRequires: gettext-tools
BuildRequires: flex
BuildRequires: bison
%description
Doxygen is a documentation system for C, C++, Java, and IDL. It can
generate an online class browser (in HTML) and an offline reference
manual (in LaTeX) from a set of documented source files. The
documentation is extracted directly from the sources. Doxygen is
developed on a Linux platform, but it runs on most other UNIX flavors
as well. An executable for Windows 95/NT is also available.

%prep
%setup -q 
%patch0 -p1

%build
cp %{SOURCE1001} .
unset QTDIR
./configure \
   --prefix %{_prefix} \
   --shared \
   --release
make %{?jobs:-j%jobs}

%install
%make_install

%clean
rm -rf  %{buildroot}

%files
%manifest doxygen.manifest
%defattr(-,root,root)
%attr(444,root,root) %doc %{_mandir}/man1/doxygen.1.*
%attr(444,root,root) %doc %{_mandir}/man1/doxytag.1.*
%attr(755,root,root) /usr/bin/*

