Summary:	A GNOME Vector Graphics Application
Summary(pl):	Aplikacja do grafiki wektorowej dla GNOME
Name:		sodipodi
Version:	0.32
Release:	1
License:	GPL
Group:		Applications/Graphics
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	fcf2fe3b2a7f90d2d3d3e79d54d69b5e
Patch0:		%{name}-desktop.patch
URL:		http://sodipodi.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gtk+2-devel >= 2.0.0
BuildRequires:	libart_lgpl-devel >= 2.3.10
BuildRequires:	libxml2-devel >= 2.4.24
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man
%define		_sysconfdir	/etc/X11/GNOME
%define		_noautoreq	'perl(XML::XQL)' 'perl(XML::XQL::DOM)'

%description
Sodipodi is a general vector drawing program for GNOME environment.

%description -l pl
Sodipodi jest ogólnym programem do rysowania wektorowego dla
¶rodowiska GNOME.

%prep
%setup -q
%patch0 -p1

%build
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	Graphicsdir=%{_applnkdir}/Graphics

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
%{_applnkdir}/Graphics/*
%{_libdir}/%{name}
