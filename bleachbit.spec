#
# spec file for package bleachbit
#
# Copyright (c) 2020 UnitedRPMs.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://goo.gl/zqFJft
#

# 
%define _legacy_common_support 1

%global commit0 f2093f8a0909ce7f495ffd5f1cfaea525b10ba62
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:           bleachbit
Version:        4.0.0
Release:        7%{?dist}
Summary:        Python utility to free disk space and improve privacy
License:        GPLv3+
URL:            https://www.bleachbit.org/
Source0:	https://github.com/bleachbit/bleachbit/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz
BuildArch:      noarch

BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-rpm-macros
BuildRequires:  libappstream-glib

#Requires:       gnome-python2
Requires:       pygtk2
Requires:       python3-gobject

%description
BleachBit deletes unnecessary files to free valuable disk space, maintain 
privacy, and remove junk. Rid your system of old clutter including cache, 
cookies, Internet history, localizations, logs, temporary files, and broken 
shortcuts. It wipes clean the cache and history list of many common programs. 

%prep
%autosetup -n %{name}-%{commit0} 

#do not install in /usr/local
sed -i 's/\/local//' Makefile

# fix appdata location
sed -i 's/$(datadir)\/appdata/$(datadir)\/metainfo/g' Makefile

# Drop deprecated line in desktop file.
sed -i '/Encoding/d' org.bleachbit.BleachBit.desktop

# Drop env shebangs as files in %%_datadir usually don't need this.
find -depth -type f -writable -name "*.py" -exec sed -iE '1s=^#! */usr/bin/\(python\|env python\)[23]\?=#!%{__python3}=' {} +


%build
make -C po local 
%{__python3} setup.py build

%install
%make_install

%find_lang %{name}

#check
#make -C cleaners tests
#{__python2} tests/TestUnix.py

#desktop-file-validate %{buildroot}%{_datadir}/applications/bleachbit.desktop
#appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/%{name}.appdata.xml

%files -f %{name}.lang
%doc README*
%license COPYING
%{_bindir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/metainfo/org.bleachbit.BleachBit.metainfo.xml
%{_datadir}/polkit-1/actions/org.bleachbit.policy
%{_datadir}/%{name}/
%{_datadir}/pixmaps/%{name}.png
%exclude %{_datadir}/%{name}/Windows.py*

%changelog

* Mon Apr 20 2020 Unitedrpms Project <unitedrpms AT protonmail DOT com> 4.0.0-7 
- Updated to 4.0.0

* Sat Apr 11 2020 Unitedrpms Project <unitedrpms AT protonmail DOT com> 3.9.2-7 
- Update to 3.9.2-7

* Fri Mar 20 2020 Unitedrpms Project <unitedrpms AT protonmail DOT com> 3.9.0-7 
- Migration to python3
- Update to 3.9.0-7

* Fri Feb 07 2020 Unitedrpms Project <unitedrpms AT protonmail DOT com> 3.2.0-7 
- Updated to 3.2.0

* Fri Jan 10 2020 Unitedrpms Project <unitedrpms AT protonmail DOT com> 3.1.0-7 
- Updated to 3.1.0

* Fri Dec 20 2019 Unitedrpms Project <unitedrpms AT protonmail DOT com> 3.0-7 
- Updated to 3.0

* Sat Mar 03 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 2.0-1
- Update to 2.0
- Disable tests temporarily

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 05 2016 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.12-1
- Update to 1.12

* Thu Apr 14 2016 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.10-1
- Update to 1.10
- Updated package URL

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Aug 01 2015 Christopher Meng <rpm@cicku.me> - 1.9.0-1
- Update to 1.9.0

* Fri Jul 24 2015 Christopher Meng <rpm@cicku.me> - 1.8-1
- Update to 1.8

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Nov 27 2014 Christopher Meng <rpm@cicku.me> - 1.6-1
- Update to 1.6

* Tue Sep 16 2014 Christopher Meng <rpm@cicku.me> - 1.4-1
- Update to 1.4

* Fri Aug 15 2014 Christopher Meng <rpm@cicku.me> - 1.3-1
- Update to 1.3

* Fri Jun 20 2014 Christopher Meng <rpm@cicku.me> - 1.2-1
- Update to 1.2

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 23 2014 Christopher Meng <rpm@cicku.me> - 1.1-1
- Update to 1.1

* Fri Jan 24 2014 Christopher Meng <rpm@cicku.me> - 1.0-1
- Update to 1.0(BZ#981346).

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jan 24 2013 Rahul Sundaram <sundaram@fedoraproject.org> - 0.9.5-1
- update to 0.9.5 release
- http://bleachbit.sourceforge.net/news/bleachbit-095

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 22 2011 Rahul Sundaram <sundaram@fedoraproject.org> - 0.8.7-1
- http://bleachbit.sourceforge.net/news/bleachbit-087

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 29 2010 Rahul Sundaram <sundaram@fedoraproject.org> - 0.8.4-1
- http://bleachbit.sourceforge.net/news/bleachbit-084

* Wed Aug 11 2010 David Malcolm <dmalcolm@redhat.com> - 0.8.0-2
- recompiling .py files against Python 2.7 (rhbz#623279)

* Tue Jun 08 2010 Rahul Sundaram <sundaram@fedoraproject.org> - 0.8.0-1
- http://bleachbit.sourceforge.net/news/bleachbit-080-released

* Tue Feb 23 2010 Rahul Sundaram <sundaram@fedoraproject.org> - 0.7.3-1
- http://bleachbit.sourceforge.net/news/bleachbit-073-released

* Thu Nov 26 2009 Rahul Sundaram <sundaram@fedoraproject.org> - 0.7.1-1
* http://bleachbit.sourceforge.net/news/bleachbit-071-released

* Fri Oct 23 2009 Rahul Sundaram <sundaram@fedoraproject.org> - 0.7.0-1
- http://bleachbit.sourceforge.net/news/bleachbit-070-released

* Thu Oct 01 2009 Rahul Sundaram <sundaram@fedoraproject.org> - 0.6.5-1
- Support for cleaning Google Chrome
- http://bleachbit.sourceforge.net/news/bleachbit-065-released

* Wed Sep 23 2009 Rahul Sundaram <sundaram@fedoraproject.org> - 0.6.4-1
- Updated directly from 0.6.1. Upstream skipped 0.6.2 release
- http://bleachbit.blogspot.com/2009/08/bleachbit-063-released.html
- http://bleachbit.sourceforge.net/news/bleachbit-064-released

* Tue Aug 18 2009 Rahul Sundaram <sundaram@fedoraproject.org> - 0.6.1-1
- new upstream release
- http://bleachbit.blogspot.com/2009/08/bleachbit-061-released.html

* Mon Aug 03 2009 Rahul Sundaram <sundaram@fedoraproject.org> - 0.6.0-1
- new upstream release
- http://bleachbit.blogspot.com/2009/08/bleachbit-cleaner-060-released.html

* Sat Jul 25 2009 Rahul Sundaram <sundaram@fedoraproject.org> - 0.5.4-3
- Fix timestamp, add dist tag

* Sat Jul 18 2009 Rahul Sundaram <sundaram@fedoraproject.org> - 0.5.4-2
- Fix review issues

* Sat Jul 18 2009 Rahul Sundaram <sundaram@fedoraproject.org> - 0.5.4-1
- initial spec
