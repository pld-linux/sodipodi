Summary:	A Gnome Vector Graphics Application
Name:		sodipodi
Version:	0.24.1
Release:	1
License:	GPL
Group:		Applications/Graphics
Group(de):	Applikationen/Grafik
Group(pl):	Aplikacje/Grafika
Source0:	http://download.sourceforge.net/sodipodi/%{name}-%{version}.tar.gz
Patch0:		%{name}-am15.patch
Patch1:		%{name}-includes.patch
URL:		http://sodipodi.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bonobo-devel >= 0.28
BuildRequires:	gal-devel >= 0.18
BuildRequires:	gettext-devel
BuildRequires:	gnome-print-devel => 0.28
BuildRequires:	libglade-devel
BuildRequires:	oaf-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man
%define		_sysconfdir	/etc/X11/GNOME

%description
Sodipodi is a gneneral vector drawing program for GNOME environment.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
rm -f missing
gettextize --copy --force
aclocal -I macros
autoconf
automake -a -c
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	sysdir=%{_applnkdir}/Graphics

gzip -9nf AUTHORS ChangeLog NEWS README TODO

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_datadir}/sodipodi
%{_datadir}/oaf/*
%{_mandir}/man1/*
%{_pixmapsdir}/*
%{_applnkdir}/Graphics/*
