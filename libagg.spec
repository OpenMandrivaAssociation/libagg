%define major 2
%define lib_name %mklibname agg %{major}
%define devel_name %mklibname agg -d

Summary: 	Open Source, free of charge graphic library
Name: 		libagg
Version: 	2.5
Release: 	8
Group: 		System/Libraries
License: 	AGG License
URL: 		http://www.antigrain.com/
Source0:	agg-2.5.tar.bz2
Patch0:		agg-2.5-linkage_fix.diff
Patch1:		agg-2.5-deansification.diff
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(freetype2)
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
%patch0 -p1
%patch1 -p1 -b .deansi

%build
#autoreconf -ivf
sh ./autogen.sh
%configure2_5x --datadir=%{_datadir}

# nuke -Wl,--no-undefined in just two places
perl -pi -e "s|-Wl,--no-undefined||g" src/platform/X11/Makefile
perl -pi -e "s|-Wl,--no-undefined||g" src/platform/sdl/Makefile

%make

%install
rm -rf %{buildroot}
%makeinstall

%if %mdkversion < 200900
%post -n %{lib_name} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{lib_name} -p /sbin/ldconfig
%endif

%files -n %{lib_name}
%_libdir/*.a
%_libdir/*.so.%{major}*


%files -n %{devel_name}
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

%changelog
* Thu Feb 14 2013 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 2.5-8
- Spec cleanup and rebuild

* Sun Aug 15 2010 Emmanuel Andry <eandry@mandriva.org> 2.5-7mdv2011.0
+ Revision: 570188
- Rebuild

* Fri Sep 11 2009 Thierry Vignaud <tv@mandriva.org> 2.5-6mdv2010.0
+ Revision: 438513
- rebuild

* Sat Nov 08 2008 Oden Eriksson <oeriksson@mandriva.com> 2.5-5mdv2009.1
+ Revision: 301072
- fix linkage
- rebuilt against new libxcb

  + Emmanuel Andry <eandry@mandriva.org>
    - apply devel policy
    - remove old conditional
    - check major

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Mon Feb 18 2008 Thierry Vignaud <tv@mandriva.org> 2.5-2mdv2008.1
+ Revision: 170940
- rebuild
- fix "foobar is blabla" summary (=> "blabla") so that it looks nice in rpmdrake

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 2.5-1mdv2008.1
+ Revision: 136546
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - fix summary-ended-with-dot


* Sun Mar 04 2007 Emmanuel Andry <eandry@mandriva.org> 2.5-1mdv2007.0
+ Revision: 132707
- fix datadir path
- New version 2.5
- Import libagg

* Sat Jul 22 2006 Laurent MONTEL <lmontel@mandriva.com> 2.3-6
- Rebuild

* Mon Jun 19 2006 Laurent MONTEL <lmontel@mandriva.com> 2.3-5
- Fix missing build requires

* Thu May 18 2006 Laurent MONTEL <lmontel@mandriva.com> 2.3-4mdk
- Rebuild

* Mon Jan 23 2006 Laurent MONTEL <lmontel@mandriva.com> 2.3-3mdk
- Add missing build requires

* Fri Dec 02 2005 Laurent MONTEL <lmontel@mandriva.com> 2.3-2mdk
- Fix provides

* Tue Nov 22 2005 Laurent MONTEL <lmontel@mandriva.com> 2.3-1mdk
- initial spec file created

