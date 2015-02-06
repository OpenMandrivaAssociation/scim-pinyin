Summary:	Chinese input module for Smart Chinese/Common Input Method platform
Name:		scim-pinyin
Version:	0.5.92
Release:	2
License:	GPLv2+
Group:		System/Internationalization
Url:		http://www.scim-im.org
Source0:	http://dl.sourceforge.net/scim/%{name}-%{version}.tar.gz
Patch0:		scim-pinyin-showallkeys.patch
Patch1:		scim-pinyin-0.5.91-save-in-temp.patch
Patch2:		scim-pinyin-0.5.91-fix-load.patch
Patch3:		scim-pinyin-0.5.91-fix-ms-shuangpin.patch
BuildRequires:	gettext-devel
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(scim)

%description
SCIM is a platform for the development of input methods. This is the
Chinese Pinyin input module for SCIM. You should install it if you
wish to enter Chinese text using the Pinyin input method.

%files -f %{name}.lang
%doc AUTHORS COPYING README
%{_libdir}/scim-1.0/*/IMEngine/pinyin.so
%{_libdir}/scim-1.0/*/SetupUI/pinyin-imengine-setup.so
%{_datadir}/scim/pinyin
%{_datadir}/scim/icons/smart-pinyin.png

#----------------------------------------------------------------------------

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
autoreconf -fi
%configure2_5x --disable-static
# force rebuild of updated po:
%make -C po update-gmo
%make

%install
%makeinstall_std

%find_lang %{name}

