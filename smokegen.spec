Name:		smokegen
Summary:	Scripting MetaObject Kompiler Engine tools
Version:	4.11.0
Release:	1
Epoch:		1
Group:		Graphical desktop/KDE
License:	GPL
URL:		http://www.kde.org
%define is_beta %(if test `echo %version |cut -d. -f3` -ge 70; then echo -n 1; else echo -n 0; fi)
%if %{is_beta}
%define ftpdir unstable
%else
%define ftpdir stable
%endif
Source:		ftp://ftp.kde.org/pub/kde/%{ftpdir}/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	kdelibs4-devel

%description
SMOKE provides infrastructure which is used for creating bindings for
multiple languages such as Ruby, C# and PHP.

This package contains the development tools to do bindings with the
Scripting MetaObject Kompiler Engine, used by several Qt and KDE bindings,
as well as some bindings for the Wt library.

#------------------------------------------------------------

%define libsmokebase_major 3
%define libsmokebase %mklibname smokebase %{libsmokebase_major}

%package -n %{libsmokebase}
Summary:	smokegen Library
Group:		Development/KDE and Qt
Conflicts:	%{_lib}smokeqt3 <= 1:4.5.80-1

%description -n %{libsmokebase}
smokegen Library

%files -n %{libsmokebase}
%{_kde_libdir}/libsmokebase.so.%{libsmokebase_major}*

#------------------------------------------------------------

%package devel
Summary:	Header files for %{name}
Group:		Development/KDE and Qt
Conflicts:	smoke4-devel < 1:4.6.90
Requires:	kdelibs4-devel
Requires:	%{libsmokebase} = %{EVRD}

%description devel
Header files for %{name}

%files devel
%{_kde_bindir}/smokegen
%{_kde_bindir}/smokeapi
%{_kde_libdir}/libcppparser.so
%{_kde_libdir}/libsmokebase.so
%{_kde_includedir}/smokegen/generatorenvironment.h
%{_kde_includedir}/smokegen/generator_export.h
%{_kde_includedir}/smokegen/generatorpreprocessor.h
%{_kde_includedir}/smokegen/generatorvisitor.h
%{_kde_includedir}/smokegen/name_compiler.h
%{_kde_includedir}/smokegen/options.h
%{_kde_includedir}/smokegen/type_compiler.h
%{_kde_includedir}/smokegen/type.h
%{_kde_includedir}/smoke.h
%{_kde_datadir}/smokegen
%{_kde_libdir}/smokegen/generator_smoke.so
%{_kde_libdir}/smokegen/generator_dump.so
%{_kde_datadir}/smoke/cmake/SmokeConfig.cmake
%{_kde_datadir}/smoke/cmake/FindLibraryWithDebug.cmake
%{_kde_datadir}/smoke/cmake/FindPhonon.cmake
%{_kde_datadir}/smoke/cmake/FindQImageBlitz.cmake
%{_kde_datadir}/smoke/cmake/FindQScintilla.cmake
%{_kde_datadir}/smoke/cmake/FindQwt5.cmake
%{_kde_datadir}/smoke/cmake/HandleImportedTargetsInCMakeRequiredLibraries.cmake
%{_kde_datadir}/smoke/cmake/MacroLogFeature.cmake
%{_kde_datadir}/smoke/cmake/MacroOptionalAddBindings.cmake
%{_kde_datadir}/smoke/cmake/MacroOptionalFindPackage.cmake
%{_kde_datadir}/smoke/cmake/SmokeVersionConfig.cmake

#------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

%changelog
* Wed Aug 14 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.11.0-1
- New version 4.11.0

* Wed Jul 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.5-1
- New version 4.10.5

* Wed Jun 05 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.4-1
- New version 4.10.4

* Tue May 07 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.3-1
- New version 4.10.3

* Wed Apr 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.2-1
- New version 4.10.2

* Sat Mar 09 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.1-1
- New version 4.10.1

* Thu Feb 07 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.0-1
- New version 4.10.0

* Wed Dec 05 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.9.4-1
- New version 4.9.4

* Wed Nov 07 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.9.3-1
- New version 4.9.3

* Thu Oct 04 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.9.2-1
- New version 4.9.2

* Sat Sep 08 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.9.1-1
- New version 4.9.1

* Tue Aug 14 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.9.0-1
- New version 4.9.0

* Sat Jul 21 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.8.97-1
- New version 4.8.97

* Sun Jul 08 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.8.95-1
- New version 4.8.95

* Fri Jun 08 2012 Andrey Bondrov <bondrov@math.dvgu.ru> 1:4.8.4-69.1mib2010.2
- New version 4.8.4
- MIB (Mandriva International Backports)

* Fri May 04 2012 Andrey Bondrov <bondrov@math.dvgu.ru> 1:4.8.3-69.1mib2010.2
- New version 4.8.3
- Better summary and description
- MIB (Mandriva International Backports)

* Wed Apr 04 2012 Andrey Bondrov <bondrov@math.dvgu.ru> 1:4.8.2-69.1mib2010.2
- New version 4.8.2
- MIB (Mandriva International Backports)

* Wed Mar 07 2012 Andrey Bondrov <bondrov@math.dvgu.ru> 1:4.8.1-69.1mib2010.2
- New version 4.8.1
- MIB (Mandriva International Backports)

* Mon Feb 20 2012 Andrey Bondrov <bondrov@math.dvgu.ru> 1:4.8.0-69.1mib2010.2
+ Revision: 762505
- Backport to 2010.2 for MIB users
- MIB (Mandriva International Backports)

* Thu Jan 19 2012 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.8.0-1
+ Revision: 762505
- New upstream tarball

* Fri Jan 06 2012 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.7.97-1
+ Revision: 758090
- New upstream tarball

* Thu Dec 22 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.7.95-1
+ Revision: 744569
- New upstream tarball

* Fri Dec 09 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.7.90-1
+ Revision: 739324
- New upstream tarball $NEW_VERSION

* Sat Nov 19 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.7.80-1
+ Revision: 731841
- New upstream tarball 4.7.80

* Fri Aug 26 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.7.41-1
+ Revision: 697175
- New version 4.7.41

* Mon Aug 01 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.7.40-1
+ Revision: 692623
- Fix file list
- import smokegen

