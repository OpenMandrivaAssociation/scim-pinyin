%define version   0.5.91
%define release   %mkrel 8

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
Requires:        scim-client = %{scim_api}
Obsoletes:        %{libname}
BuildRequires:   scim-devel >= 1.4.7-4mdk
BuildRequires:   skim-devel >= %{skim_version}
BuildRequires:   libGConf2-devel automake libltdl-devel
Obsoletes:       %mklibname scim-chinese 0
Provides:        scim-chinese
Obsoletes:       scim-chinese

%description
SCIM is a platform for the development of input methods. This is the 
Chinese Pinyin input module for SCIM. You should install it if you
wish to enter Chinese text using the Pinyin input method.

%package -n skim-%{name}
Summary:    Scim-pinyin for skim
Group:      System/Internationalization
Requires:   skim >= %{skim_version}
Requires:   %{name} = %{version}-%{release}

%description -n skim-%{name}
SCIM is a platform for the development of input methods. SKIM is a KDE
front end for SCIM input. This is the Chinese Pinyin input module for
SKIM. You should install it if you wish to enter Chinese text using
the Pinyin input method in KDE.

%prep
%setup -q
%patch1 -p1
%patch2 -p0

%build
%configure2_5x --disable-static
%make
# force rebuild of updated po:
%make -C po

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

# remove unneeded files
rm -f %{buildroot}%{scim_plugins_dir}/IMEngine/*.{a,la}
rm -f %{buildroot}%{scim_plugins_dir}/SetupUI/*.{a,la}

%find_lang %{name}
%find_lang skim-%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -p /sbin/ldconfig
%endif

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS README ChangeLog
%{_datadir}/scim/pinyin/*
%{_datadir}/scim/icons/*
%{scim_plugins_dir}/IMEngine/*.so
%{scim_plugins_dir}/SetupUI/*.so

%files -n skim-%{name} -f skim-%{name}.lang
%defattr(-,root,root)
%{_datadir}/apps/skim/pics/*.png
%{_datadir}/config.kcfg/*.kcfg
%{_datadir}/services/skimconfiguredialog/*.desktop
%{_libdir}/kde3/*.so
%{_libdir}/kde3/*.la
