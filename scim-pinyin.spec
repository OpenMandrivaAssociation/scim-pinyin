%define version   0.5.91
%define release   %mkrel 5

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
Requires:        %{libname} = %{version}-%{release}
BuildRequires:   scim-devel >= 1.4.7-3mdk
BuildRequires:   skim-devel >= %{skim_version}
BuildRequires:   libGConf2-devel automake libltdl-devel
Conflicts:       libscim-chinese0
Provides:        scim-chinese
Obsoletes:       scim-chinese

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
Requires:   %{name} = %{version}-%{release}

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
rm -f %{buildroot}%{scim_plugins_dir}/IMEngine/*.{a,la}
rm -f %{buildroot}%{scim_plugins_dir}/SetupUI/*.{a,la}

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
%{scim_plugins_dir}/IMEngine/*.so
%{scim_plugins_dir}/SetupUI/*.so

%files -n skim-scim-pinyin
%defattr(-,root,root)
%{_datadir}/apps/skim/pics/*.png
%{_datadir}/config.kcfg/*.kcfg
%{_datadir}/services/skimconfiguredialog/*.desktop
%{_libdir}/kde3/*.so
%{_libdir}/kde3/*.la
