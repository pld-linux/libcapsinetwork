Summary:	A network library for C++ server daemons
Summary(pl):	Sieciowa biblioteka C++ dla demonów
Name:		libcapsinetwork
Version:	0.2.3
Release:	1
License:	LGPL/GPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/sourceforge/%{name}/%{name}-%{version}.tar.bz2
# Source0-md5:	492a032e4999e41f9ad6cfc0dd026ef3
URL:		http://unixcode.org/libcapsinetwork/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libCapsiNetwork is a network library for C++ server daemons aimed at
easy development of server daemons.

%description -l pl
libCapsiNetwork jest sieciow± bibliotek± C++ pozwalaj±c± w ³atwy
sposób tworzyæ demony.

%package devel
Summary:	libcapsinetwork header files
Summary(pl):	Pliki nag³ówkowe libcapsinetwork
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
libcapsinetwork header files.

%description devel -l pl
Pliki nag³ówkowe libcapsinetwork.

%package static
Summary:	libcapsinetwork static library
Summary(pl):	Statyczna biblioteka libcapsinetwork
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
libcapsinetwork static library.

%description static -l pl
Statyczna biblioteka libcapsinetwork.

%prep
%setup -q

%build
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/libcapsinetwork

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
