Name:		sodipodi
Summary:	A Gnome Vector Graphics Application
Version:	0.18
Release:	1
License:	GPL
Group:		Applications/Graphics
Group(pl):	Aplikacje/Grafika
Source0:	http://download.sourceforge.net/sodipodi/%{name}-%{version}.tar.gz
Patch0:		sodipodi-DESTDIR.patch
URL:		http://www.ariman.ee/linux/sodipodi/
BuildRequires:	gettext-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_sysconfdir	/etc/X11/GNOME

%description
Sodipodi is a gneneral vector drawing program for GNOME environment.

%prep
%setup -q
%patch -p1

%build
gettextize --copy --force
automake
LDFLAGS="-s"; export LDFLAGS
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
%{_datadir}/pixmaps/*
%{_applnkdir}/Graphics/*
