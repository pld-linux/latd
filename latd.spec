Summary:	LAT daemon
Summary(pl):	Serwer LAT
Name:		latd
Version:	1.21
Release:	1
Vendor:		Patrick Caulfield
License:	GPL v2
Group:		Networking/Utilities
Source0:	http://dl.sourceforge.net/linux-decnet/%{name}-%{version}.tar.gz
# Source0-md5:	ffbb4f60eea0ed640968150f5420793a
Source1:	%{name}.conf
Patch0:		%{name}-assert.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	lockdev-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LAT implementation for Linux.

%description -l pl
Implementacja LAT dla linuksa.

%prep
%setup -q
%patch0 -p1

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_mandir}/man{1,5,8}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

for i in 1 5 8; do
	install *.$i $RPM_BUILD_ROOT%{_mandir}/man$i/
done

install %SOURCE1 $RPM_BUILD_ROOT/etc/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.html NEWS README TODO WARRANTY latd.conf.sample
%config(noreplace) %verify(not size mtime md5) /etc/latd.conf
%attr(755,root,root) %{_sbindir}/latcp
%attr(755,root,root) %{_sbindir}/latd
%attr(755,root,root) %{_sbindir}/moprc
%attr(755,root,root) %{_bindir}/llogin
%{_mandir}/man?/*
#/etc/rc.d/init.d/lat
#/etc/rc.d/rc3.d/S79lat
#/etc/rc.d/rc3.d/K79lat
