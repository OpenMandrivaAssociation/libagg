%define major	2
%define libname %mklibname agg %{major}
%define devname %mklibname agg -d

Summary:	Open Source, free of charge graphic library
Name:		libagg
Version:	2.5
Release:	10
Group:		System/Libraries
License:	AGG License
Url:		http://www.antigrain.com/
Source0:	agg-2.5.tar.bz2
Patch0:		agg-2.5-linkage_fix.diff
Patch1:		agg-2.5-deansification.diff
BuildRequires:	pkgconfig(freetype2)
BuildRequires:	pkgconfig(sdl)
BuildRequires:	pkgconfig(x11)

%description
Anti-Grain Geometry (AGG) is an Open Source, free of charge graphic library, 
written in industrially standard C++. The terms and conditions of use AGG 
are described on The License page. AGG doesn't depend on any graphic API or 
technology. Basically, you can think of AGG as of a rendering engine that 
produces pixel images in memory from some vectorial data.

%package -n %{libname}
Summary:	Main library for %{name}
Group:		System/Libraries
Provides:	%{name} = %{version}-%{release}

%description -n %{libname}
This package contains the library needed to run programs dynamically
linked with %{name}.

%package -n %{devname}
Summary:	Headers for developing programs that will use %{name}
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	agg-devel = %{version}-%{release}

%description -n %{devname}
This package contains the headers that programmers will need to develop
applications which will use %{name}.

%prep
%setup -qn agg-2.5
%apply_patches

sh ./autogen.sh

%build
%configure2_5x \
	--disable-static \
	--datadir=%{_datadir}

# nuke -Wl,--no-undefined in just two places
sed -i -e "s|-Wl,--no-undefined||g" src/platform/X11/Makefile
sed -i -e "s|-Wl,--no-undefined||g" src/platform/sdl/Makefile

%make

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/libagg.so.%{major}*

%files -n %{devname}
%dir %{_includedir}/agg2/
%{_includedir}/agg2/*.h
%dir %{_includedir}/agg2/ctrl/
%{_includedir}/agg2/ctrl/*.h
%dir %{_includedir}/agg2/platform/
%{_includedir}/agg2/platform/*.h
%dir %{_includedir}/agg2/util/
%{_includedir}/agg2/util/*.h
%{_datadir}/aclocal/*.m4
%{_libdir}/*.so
%dir %{_libdir}/pkgconfig/
%{_libdir}/pkgconfig/libagg.pc

