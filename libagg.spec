%define name libagg
%define version	2.5
%define major 2
%define release %mkrel 4
%define lib_name %mklibname agg %{major}
%define devel_name %mklibname agg -d

Name: 		%{name}
Summary: 	Open Source, free of charge graphic library
Version: 	%{version}
Release: 	%{release}
Group: 		System/Libraries
License: 	AGG License
URL: 		http://www.antigrain.com/
Source:		agg-2.5.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: autoconf2.5 
BuildRequires: libx11-devel
BuildRequires:	freetype2-devel
BuildRequires:	SDL-devel

%description
Anti-Grain Geometry (AGG) is an Open Source, free of charge graphic library, 
written in industrially standard C++. The terms and conditions of use AGG 
are described on The License page. AGG doesn't depend on any graphic API or 
technology. Basically, you can think of AGG as of a rendering engine that 
produces pixel images in memory from some vectorial data.

%package -n %{lib_name}
Summary: Main library for %{name}
Group: System/Libraries
Provides: %{name} = %{version}-%{release}

%description -n %{lib_name}
This package contains the library needed to run programs dynamically
linked with %{name}.

%package -n %{devel_name}
Summary: Headers for developing programs that will use %{name}
Group: Development/C
Requires: %{lib_name} = %{version}-%{release}
Provides: agg-devel = %{version}-%{release}
Obsoletes: libagg2-devel

%description -n %{devel_name}
This package contains the headers that programmers will need to develop
applications which will use %{name}.

%prep
%setup -q -n agg-2.5

%build
sh ./autogen.sh
%configure2_5x --datadir=%{_datadir}
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%clean 
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post -n %{lib_name} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{lib_name} -p /sbin/ldconfig
%endif

%files -n %{lib_name}
%defattr(-,root,root)
%_libdir/*.la
%_libdir/*.a
%_libdir/*.so.%{major}*


%files -n %{devel_name}
%defattr(-,root,root)
%dir %_includedir/agg2/
%_includedir/agg2/*.h
%dir %_includedir/agg2/ctrl/
%_includedir/agg2/ctrl/*.h
%dir %_includedir/agg2/platform/
%_includedir/agg2/platform/*.h
%dir %_includedir/agg2/util/
%_includedir/agg2/util/*.h
%_datadir/aclocal/*.m4
%_libdir/*.so

%dir %_libdir/pkgconfig/
%_libdir/pkgconfig/libagg.pc


