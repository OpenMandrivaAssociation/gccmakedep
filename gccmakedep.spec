Name:		gccmakedep
Version:	1.0.2
Release:	11
Summary:	Create dependencies in makefiles using 'gcc -M'
Group:		System/X11
License:	MIT
URL:		http://xorg.freedesktop.org
Source:		http://xorg.freedesktop.org/releases/individual/util/%{name}-%{version}.tar.bz2
BuildRequires:	x11-util-macros >= 1.0.1
BuildArch:	noarch

%description
Create dependencies in makefiles using 'gcc -M'.

%prep
%setup -q

%build
%configure2_5x 	--x-includes=%{_includedir} \
		--x-libraries=%{_libdir}
%make

%install
%makeinstall_std

%files
%{_bindir}/gccmakedep
%{_mandir}/man1/gccmakedep.*

%changelog
* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.2-9mdv2011.0
+ Revision: 664811
- mass rebuild

* Thu Dec 02 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.2-8mdv2011.0
+ Revision: 605441
- rebuild

* Mon Feb 08 2010 Sandro Cazzaniga <kharec@mandriva.org> 1.0.2-7mdv2010.1
+ Revision: 502382
- Clean spec file
- fix rpmlint's warning

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.0.2-6mdv2010.0
+ Revision: 424552
- rebuild

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 1.0.2-5mdv2009.1
+ Revision: 351191
- rebuild

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 1.0.2-4mdv2009.0
+ Revision: 221031
- rebuild

* Sat Jan 12 2008 Thierry Vignaud <tv@mandriva.org> 1.0.2-3mdv2008.1
+ Revision: 150093
- rebuild
- kill re-definition of %%buildroot on Pixel's request
- fix man pages extension

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Thu Jun 28 2007 Adam Williamson <awilliamson@mandriva.org> 1.0.2-2mdv2008.0
+ Revision: 45373
- rebuild for 2008


* Wed Aug 02 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-08-02 16:14:46 (43009)
- new upstream release (1.0.2):
   * RM needed some more quoting.
   * RM should be rm -f for monolithic compatibility.

* Wed May 31 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-31 18:32:34 (31796)
- rebuild to fix cooker uploading

* Mon May 29 2006 Andreas Hasenack <andreas@mandriva.com>
+ 2006-05-29 14:36:37 (31646)
- renamed mdv to packages because mdv is too generic and it's hosting only packages anyway

* Mon May 22 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-22 16:05:41 (27854)
- adding package gccmakedep

