#
# Conditional build:
%bcond_without	gnome	# without gnome-print support
#
Summary:	A GNOME Vector Graphics Application
Summary(pl):	Aplikacja do grafiki wektorowej dla GNOME
Name:		sodipodi
Version:	0.34
Release:	2
License:	GPL
Group:		Applications/Graphics
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	396cd78526e5a8102fd11114f45a70fe
Patch0:		%{name}-desktop.patch
Patch1:		%{name}-home_etc.patch
Patch2:		%{name}-locale_names.patch
URL:		http://sodipodi.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	freetype-devel
BuildRequires:	gtk+2-devel >= 2.0.0
BuildRequires:	libart_lgpl-devel >= 2.3.10
%{?with_gnome:BuildRequires:	libgnomeprint-devel >= 2.0.0}
BuildRequires:	libpng-devel
BuildRequires:	libxml2-devel >= 2.4.24
BuildRequires:	pkgconfig
BuildRequires:	popt-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq	'perl(XML::XQL)' 'perl(XML::XQL::DOM)'

%description
Sodipodi is a general vector drawing program for GNOME environment.

%description -l pl
Sodipodi jest ogólnym programem do rysowania wektorowego dla
¶rodowiska GNOME.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

mv -f po/{no,nb}.po

%build
%configure \
	%{?with_gnome:--with-gnome-print}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	Graphicsdir=%{_desktopdir}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/sodipodi
%{_mandir}/man1/*
%{_pixmapsdir}/*
%{_desktopdir}/*
%{_libdir}/%{name}
