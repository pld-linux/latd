Summary:	LAT daemon
Summary(pl):	Serwer LAT
Name:		latd
Version:	1.18
Release:	3
Vendor:		Patrick Caulfield
License:	GPL v2
Group:		Networking/Utilities
# Source0-md5:	045ce07e8a92a9be9a29ec754fc2c005
Source0:	http://dl.sourceforge.net/linux-decnet/%{name}-%{version}.tar.gz
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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.html NEWS README TODO WARRANTY
%attr(755,root,root) %{_sbindir}/latcp
%attr(755,root,root) %{_sbindir}/latd
%attr(755,root,root) %{_sbindir}/moprc
%attr(755,root,root) %{_bindir}/llogin
%{_mandir}/man?/*
%{_sysconfdir}/latd.conf
#/etc/rc.d/init.d/lat
#/etc/rc.d/rc3.d/S79lat
#/etc/rc.d/rc3.d/K79lat
#%doc README NEWS latd.html
