Name:		smokegen
Summary:	Scripting MetaObject Kompiler Engine tools
Version: 4.9.3
Release: 1
Epoch:		1
Group:		Graphical desktop/KDE
License:	GPL
URL:		http://www.kde.org
Source:		ftp://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	kdelibs4-devel >= 2:%{version}

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
Requires:	kdelibs4-devel >= 2:%{version}
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

