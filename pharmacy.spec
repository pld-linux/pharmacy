Summary:	Pharmacy intends to be a GNOME compliant front-end to CVS.
Name:		pharmacy
Version:	0.2.1
Release:	1
License:	GPL
Group:		Applications/Communications
Group(pl):	Aplikacje/Komunikacja
URL:		http://home.earthlink.net/~nawalker/pharmacy.html
Source0:	http://home.earthlink.net/~nawalker/%{name}-%{version}.tar.gz
Patch0:	%{name}-DESTDIR.patch
Patch1:	%{name}-applnkdir.patch
Requires:	gtk+ >= 1.1.12
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define _prefix /usr/X11R6

%description
Pharmacy intends to be a GNOME compliant front-end to CVS. Currently, it
provides a limited user interface to CVS commands and a "console" for the
lazy power-user.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
automake
%configure
make

%install
make DESTDIR=$RPM_BUILD_ROOT install-strip

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/pharmacy
%{_applnkdir}/Applications/pharmacy.desktop
%{_datadir}/pixmaps/pharmacy.png
%{_datadir}/gnome/help/pharmacy/C/*
