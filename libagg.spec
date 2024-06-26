%global _disable_rebuild_configure 1

## MD rename src pkg dir to agg
%define major 2
%define libname %mklibname %{name} %{major}
%define libfft %mklibname aggfontfreetype %{major}
%define libX11 %mklibname aggplatformX11_ %{major}
%define libsdl %mklibname aggplatformsdl %{major}
%define devname %mklibname %{name} -d

Summary:	Open Source, free of charge graphic library
Name:		agg
Version:	2.8.25
Release:	1
License:	MIT
Group:		System/Libraries
Url:		https://github.com/cppfw/agg
# Pre-fork Url:		http://www.antigrain.com/
Source0:	https://github.com/cppfw/agg/archive/refs/tags/%{version}.tar.gz
Patch0:		https://abf.io/import/agg/raw/rosa2019.1/agg-2.8.1-linkage_fix.diff
Patch2:		agg-2.5-no-rpath.patch
BuildRequires:	pkgconfig(freetype2)
BuildRequires:	pkgconfig(sdl)
BuildRequires:	pkgconfig(x11)

%description
Anti-Grain Geometry (AGG) is an Open Source, free of charge graphic library,
written in industrially standard C++. The terms and conditions of use AGG
are described on The License page. AGG doesn't depend on any graphic API or
technology. Basically, you can think of AGG as of a rendering engine that
produces pixel images in memory from some vectorial data.

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	Shared library for %{name}
Group:		System/Libraries

%description -n %{libname}
This package contains a library needed to run programs dynamically
linked with %{name}.

%files -n %{libname}
%{_libdir}/libagg.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{libfft}
Summary:	Shared library for %{name}
Group:		System/Libraries
Conflicts:	%{_lib}agg2 < 2.5-10

%description -n %{libfft}
This package contains a library needed to run programs dynamically
linked with %{name}.

%files -n %{libfft}
%{_libdir}/libaggfontfreetype.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{libsdl}
Summary:	Shared library for %{name}
Group:		System/Libraries
Conflicts:	%{_lib}agg2 < 2.5-10

%description -n %{libsdl}
This package contains a library needed to run programs dynamically
linked with %{name}.

%files -n %{libsdl}
%{_libdir}/libaggplatformsdl.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{libX11}
Summary:	Shared library for %{name}
Group:		System/Libraries
Conflicts:	%{_lib}agg2 < 2.5-10

%description -n %{libX11}
This package contains a library needed to run programs dynamically
linked with %{name}.

%files -n %{libX11}
%{_libdir}/libaggplatformX11.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	Headers for developing programs that will use %{name}
Group:		Development/C
Requires:	%{libname} = %{EVRD}
Requires:	%{libfft} = %{EVRD}
Requires:	%{libX11} = %{EVRD}
Requires:	%{libsdl} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}

%description -n %{devname}
This package contains the headers that programmers will need to develop
applications which will use %{name}.

%files -n %{devname}
%{_includedir}/agg2/
%{_datadir}/aclocal/*.m4
%{_libdir}/*.so
%{_libdir}/pkgconfig/libagg.pc

#----------------------------------------------------------------------------

%prep
%setup -q
%autopatch -p1
cd src/agg
sh ./autogen.sh

%configure \
	--disable-examples

# nuke -Wl,--no-undefined in just two places
sed -i -e "s|-Wl,--no-undefined||g" src/platform/X11/Makefile
sed -i -e "s|-Wl,--no-undefined||g" src/platform/sdl/Makefile

%build
%make_build -C src/agg

%install
%make_install -C src/agg

