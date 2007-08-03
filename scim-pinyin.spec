%define version   0.5.91
%define release   %mkrel 4

%define scim_version   1.4.0
%define skim_version   1.4.2

%define libname_orig lib%{name}
%define libname %mklibname %name 0

Name:      scim-pinyin
Summary:   Chinese input module for Smart Chinese/Common Input Method platform
Version:   %{version}
Release:   %{release}
Group:     System/Internationalization
License:   GPL+
URL:       http://www.scim-im.org
Source0:   %{name}-%{version}.tar.bz2
Patch1:    scim-chinese-0.4.1-fix-l10n.patch
Patch2:    scim-pinyin-fix_build_for_skim_support.diff
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires:        scim >= %{scim_version}
Requires:        %{libname} = %{version}
BuildRequires:   scim-devel >= %{scim_version}
BuildRequires:   skim-devel >= %{skim_version}
BuildRequires:   libGConf2-devel automake1.8 libltdl-devel
Conflicts:       libscim-chinese0
Provides:        scim-chinese
Obsoletes:       scim-chinese > %version

%description
SCIM is a platform for the development of input methods. This is the 
Chinese Pinyin input module for SCIM. You should install it if you
wish to enter Chinese text using the Pinyin input method.

%package -n %{libname}
Summary:    Scim-pinyin library
Group:      System/Internationalization
Provides:   %{libname_orig} = %{version}-%{release}

%description -n %{libname}
SCIM is a platform for the development of input methods. This is the 
Chinese Pinyin input module for SCIM.

%package -n skim-scim-pinyin
Summary:    Scim-pinyin for skim
Group:      System/Internationalization
Requires:   skim >= %{skim_version}
Requires:   %{name} = %{version}

%description -n skim-scim-pinyin
SCIM is a platform for the development of input methods. SKIM is a KDE
front end for SCIM input. This is the Chinese Pinyin input module for
SKIM. You should install it if you wish to enter Chinese text using
the Pinyin input method in KDE.

%prep
%setup -q
%patch1 -p1
%patch2 -p0

%build
CXXFLAGS="-O3 -Wall"
%configure2_5x --disable-static
%make
# force rebuild of updated po:
%make -C po

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=${RPM_BUILD_ROOT} install-strip 

# remove unneeded files
rm -f %{buildroot}%{_libdir}/scim-1.0/IMEngine/*.{a,la}
rm -f %{buildroot}%{_libdir}/scim-1.0/SetupUI/*.{a,la}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS README ChangeLog
%{_datadir}/scim/pinyin/*
%{_datadir}/scim/icons/*

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/scim-1.0/IMEngine/*.so
%{_libdir}/scim-1.0/SetupUI/*.so

%files -n skim-scim-pinyin
%defattr(-,root,root)
%{_datadir}/apps/skim/pics/*.png
%{_datadir}/config.kcfg/*.kcfg
%{_datadir}/locale/*/LC_MESSAGES/*.mo
%{_datadir}/services/skimconfiguredialog/*.desktop
%{_libdir}/kde3/*.so
# skim load *.la file. Don't remove it.
%{_libdir}/kde3/*.la
