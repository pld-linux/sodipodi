# Note that this is NOT a relocatable package
%define name		sodipodi
%define ver		0.18     
%define  RELEASE	1
%define  rel		%{?CUSTOM_RELEASE} %{!?CUSTOM_RELEASE:%RELEASE}
%define prefix		/usr
%define sysconfdir	/etc

Name:		%name
Summary:	A Gnome Vector Graphics Application
Version:	%ver
Release:	%rel
Copyright:	GPL
Group:		Applications/Graphics
Source:		%{name}-%{ver}.tar.gz
URL:		http://www.ariman.ee/linux/sodipodi/
BuildRoot:	/var/tmp/%{name}-root
Docdir:		%{prefix}/doc

%description
Sodipodi is a gneneral vector drawing program for GNOME environment.

%changelog
* Mon Mar 27 2000 Lauris Kaplinski <lauris@ariman.ee>
- First RPM version

%prep
%setup -q

%build
%ifarch alpha
 MYARCH_FLAGS="--host=alpha-redhat-linux"
%endif
# Needed for snapshot releases.

MYCFLAGS="$RPM_OPT_FLAGS"

if [ ! -f configure ]; then
  CFLAGS="$MYCFLAGS" ./autogen.sh $MYARCH_FLAGS --prefix=%prefix --localstatedir=/var/lib --sysconfdir=/etc
else
  CFLAGS="$MYCFLAGS" ./configure $MYARCH_FLAGS --prefix=%prefix --localstatedir=/var/lib --sysconfdir=/etc
fi

if [ "$SMP" != "" ]; then
  make -j$SMP "MAKE=make -j$SMP"
else
  make
fi

%install
rm -rf $RPM_BUILD_ROOT

make sysconfdir=$RPM_BUILD_ROOT/etc prefix=$RPM_BUILD_ROOT%{prefix} install

%clean
rm -rf $RPM_BUILD_ROOT

%post 

%postun

%files
%defattr(-, root, root)

%doc AUTHORS COPYING ChangeLog NEWS README TODO
%{prefix}/bin/*
%{prefix}/share/sodipodi/*
%{prefix}/share/pixmaps/*
%{prefix}/share/gnome/apps/Graphics/*
