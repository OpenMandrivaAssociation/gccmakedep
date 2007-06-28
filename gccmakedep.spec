Name: gccmakedep
Version: 1.0.2
Release: %mkrel 2
Summary: Create dependencies in makefiles using 'gcc -M'
Group: System/X11
URL: http://xorg.freedesktop.org
Source: http://xorg.freedesktop.org/releases/individual/util/%{name}-%{version}.tar.bz2
License: MIT
Packager: Gustavo Pichorim Boiko <boiko@mandriva.com> 
BuildRoot: %{_tmppath}/%{name}-root

BuildRequires: x11-util-macros >= 1.0.1

%description
Create dependencies in makefiles using 'gcc -M'

%prep
%setup -q -n %{name}-%{version}

%build
%configure2_5x 	--x-includes=%{_includedir} \
		--x-libraries=%{_libdir}
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/gccmakedep
%{_mandir}/man1/gccmakedep.1x.bz2


