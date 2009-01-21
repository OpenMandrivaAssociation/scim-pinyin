%define version   0.5.91
%define release   %mkrel 10

%define scim_version   1.4.0

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
Patch0:	   scim-pinyin-0.5.91-gcc43.patch
Patch1:    scim-chinese-0.4.1-fix-l10n.patch
Patch2:    scim-pinyin-fix_build_for_skim_support.diff
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires:        scim-client = %{scim_api}
Obsoletes:        %{libname}
BuildRequires:   scim-devel >= 1.4.7-4mdk
BuildRequires:   libGConf2-devel automake libltdl-devel
Obsoletes:       %mklibname scim-chinese 0
Provides:        scim-chinese
Obsoletes:       scim-chinese

%description
SCIM is a platform for the development of input methods. This is the 
Chinese Pinyin input module for SCIM. You should install it if you
wish to enter Chinese text using the Pinyin input method.

%prep
%setup -q
%patch0 -p1
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
