## -*- mode: rpm-spec; -*-
##
## $Id: avarice.spec.in,v 1.3 2003/12/07 06:04:58 troth Exp $
##
## avarice.spec.  Generated from avarice.spec.in by configure.
##

# We don't want rpm stripping any files
#%define __spec_install_post %{nil}

# Don't build the debuginfo rpm
%define debug_package %{nil}

Summary: Interface for GDB to Atmel AVR JTAGICE in circuit emulator.
Name: avarice
Version: 2.6.20061222
Release: 1
License: GPL
Group: Avr/Development/Tools
URL: http://avarice.sourceforge.net/
Source0: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
AVaRICE is a program which interfaces the GNU Debugger with the AVR JTAG ICE
available from Atmel.

%prep
%setup -q

%build
./configure --prefix=%{_prefix} --mandir=%{_mandir}
make

%install
rm -rf $RPM_BUILD_ROOT
make prefix=$RPM_BUILD_ROOT%{_prefix} mandir=$RPM_BUILD_ROOT%{_mandir} install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc ChangeLog AUTHORS INSTALL COPYING 
%{_prefix}/bin/avarice
%{_prefix}/bin/start-avarice
%{_prefix}/bin/kill-avarice
%{_prefix}/bin/ice-gdb
%{_prefix}/bin/ice-insight
%{_prefix}/share/%{name}/gdb-avarice-script
%{_mandir}/man1/ice-insight.1
%{_mandir}/man1/ice-gdb.1
%{_mandir}/man1/avarice.1

%changelog
* Sat Dec 06 2003 Theodore A. Roth <troth@openavr.org>
- Add avarice.1 man page.

* Thu Sep 18 2003 Theodore A. Roth <troth@openavr.org>
- Add man pages.

* Fri Aug 15 2003 Theodore A. Roth <troth@openavr.org> 
- Initial build.
