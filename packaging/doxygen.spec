
Name:           doxygen
Version:        1.7.4
Release:        %{?release_prefix:%{release_prefix}.}1.42.%{?dist}%{!?dist:tizen}
VCS:            external/doxygen#submit/trunk/20121019.090915-0-ga088245f8e49beb8437cd2745c6fec88ac5f73db
License:        GPLv2+
Group:          Development/Tools
Summary:        Automated C, C++, and Java Documentation Generator
Url:            http://www.stack.nl/~dimitri/doxygen/
Source:         http://ftp.stack.nl/pub/users/dimitri/doxygen-%{version}.src.tar.gz
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
%defattr(-,root,root)
%attr(444,root,root) %doc %{_mandir}/man1/doxygen.1.*
%attr(444,root,root) %doc %{_mandir}/man1/doxytag.1.*
%attr(755,root,root) /usr/bin/*

%changelog
* Mon Sep 16 2013 UkJung Kim <ujkim@samsung.com> - submit/trunk/20121019.090915 
- PROJECT: external/doxygen
- COMMIT_ID: a088245f8e49beb8437cd2745c6fec88ac5f73db
- PATCHSET_REVISION: a088245f8e49beb8437cd2745c6fec88ac5f73db
- CHANGE_OWNER: \"UkJung Kim\" <ujkim@samsung.com>
- PATCHSET_UPLOADER: \"UkJung Kim\" <ujkim@samsung.com>
- CHANGE_URL: http://slp-info.sec.samsung.net/gerrit/103380
- PATCHSET_REVISION: a088245f8e49beb8437cd2745c6fec88ac5f73db
- TAGGER: UkJung Kim <ujkim@samsung.com>
- Gerrit patchset approval info:
- UkJung Kim <ujkim@samsung.com> Verified : 1
- Newton Lee <newton.lee@samsung.com> Code Review : 2
- CHANGE_SUBJECT: Initial commit
- [Version] 1.7.4
- [Project] GT-I8800
- [Title] Initial commit
- [BinType] PDA
- [Customer] Open
- [Issue#] N/A
- [Problem] N/A
- [Cause] N/A
- [Solution]
- [Team] SCM
- [Developer] UkJung Kim <ujkim@samsung.com>
- [Request] N/A
- [Horizontal expansion] N/A
- [SCMRequest] N/A
* Mon May 30 2011 Carsten Munk <carsten@maemo.org> - 1.7.4
- Drop doxygen-1.5.9-arm.patch - no longer needed and it
  broke ARM builds with 1.7.4.
* Sun May  8 2011 Anas Nashif <anas.nashif@intel.com> - 1.7.4
- Update to 1.7.4
* Sat Jan 30 2010 Anas Nashif <anas.nashif@intel.com> - 1.6.2
- Update to 1.6.2
- Do not write timestamps all over the place, enable via new option
* Tue Feb 17 2009 Anas Nashif <anas.nashif@intel.com> 1.5.8
- Update to version 1.5.8
* Sat Dec 20 2008 Anas Nashif <anas.nashif@intel.com> 1.5.7.1
- Initial import into Moblin
