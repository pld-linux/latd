Summary:	LAT daemon
Summary(pl):	Serwer LAT
Name:		latd
Version:	1.16
Release:	1
Vendor:		Patrick Caulfield
License:	GPL
Group:		Networking/Utilities
Source0:	http://download.sourceforge.net/linux-decnet/%{name}-%{version}.tar.gz
# Source0-md5:	5ca68d0257b7fadb4c62112f0277fa2d
BuildRoot:      %{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LAT implementation for Linux.

%description -l pl
Implementacja LAT dla linuksa.

%prep
%setup -q -n %{name}

%build
%{__make} OPTDEBUG="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_mandir}/man{1,5,8}
for i in 1 5 8; do
	install *.$i $RPM_BUILD_ROOT%{_mandir}/man$i/
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/latcp
%attr(755,root,root) %{_sbindir}/latd
%attr(755,root,root) %{_sbindir}/moprc
%attr(755,root,root) %{_bindir}/llogin
%{_mandir}/man?/*
#%{_sysconfdir}/latd.conf
#/etc/rc.d/init.d/lat
#/etc/rc.d/rc3.d/S79lat
#/etc/rc.d/rc3.d/K79lat
#%doc README NEWS latd.html
