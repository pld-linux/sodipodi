Summary:	A Gnome Vector Graphics Application
Summary(pl):	Aplikacja do grafiki wektorowej dla GNOME
Name:		sodipodi
Version:	0.29
Release:	0.1
License:	GPL
Group:		Applications/Graphics
Source0:	http://prdownloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Patch0:		%{name}-desktop.patch
URL:		http://sodipodi.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+2-devel >= 2.0.0
BuildRequires:	libart_lgpl-devel >= 2.3.10
BuildRequires:	libxml2-devel >= 2.4.24
BuildRequires:	gettext-devel
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
	Graphicsdir=%{_datadir}/applications

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
%{_datadir}/applications/*
