Summary:	Create dependencies in makefiles using 'gcc -M'
Name:		gccmakedep
Version:	1.0.3
Release:	7
Group:		System/X11
License:	MIT
Url:		https://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/util/%{name}-%{version}.tar.bz2
BuildArch:	noarch
BuildRequires:	pkgconfig(xorg-macros)

%description
Create dependencies in makefiles using 'gcc -M'.

%prep
%setup -q

%build
%configure2_5x \
	--x-includes=%{_includedir} \
	--x-libraries=%{_libdir}
%make

%install
%makeinstall_std

%files
%{_bindir}/gccmakedep
%{_mandir}/man1/gccmakedep.*

