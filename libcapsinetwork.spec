#
# Conditional build:
%bcond_without	static_libs	# don't build static library
#
Summary:	A network library for C++ server daemons
Summary(pl.UTF-8):	Sieciowa biblioteka C++ dla demonów
Name:		libcapsinetwork
Version:	0.3.0
Release:	3
License:	LGPL/GPL
Group:		Libraries
Source0:	http://robertjohnkaper.com/downloads/atlantik/%{name}-%{version}.tar.bz2
# Source0-md5:	47829a36d663dfe6ae8e59e16a9d0bb7
# redirects to http://www.robertjohnkaper.com/software/atlantik/download.html
URL:		http://unixcode.org/libcapsinetwork/
BuildRequires:	automake
BuildRequires:	autoconf
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libCapsiNetwork is a network library for C++ server daemons aimed at
easy development of server daemons.

%description -l pl.UTF-8
libCapsiNetwork jest sieciową biblioteką C++ pozwalającą w łatwy
sposób tworzyć demony.

%package devel
Summary:	libcapsinetwork header files
Summary(pl.UTF-8):	Pliki nagłówkowe libcapsinetwork
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel

%description devel
libcapsinetwork header files.

%description devel -l pl.UTF-8
Pliki nagłówkowe libcapsinetwork.

%package static
Summary:	libcapsinetwork static library
Summary(pl.UTF-8):	Statyczna biblioteka libcapsinetwork
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
libcapsinetwork static library.

%description static -l pl.UTF-8
Statyczna biblioteka libcapsinetwork.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	%{!?with_static_libs:--disable-static}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_libdir}/libcapsinetwork.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libcapsinetwork.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcapsinetwork.so
%{_libdir}/libcapsinetwork.la
%{_includedir}/libcapsinetwork

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libcapsinetwork.a
%endif
