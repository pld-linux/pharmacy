Summary:	Pharmacy intends to be a GNOME compliant front-end to CVS
Name:		pharmacy
Version:	0.2.1
Release:	2
License:	GPL
Group:		Applications/Communications
Group(de):	Applikationen/Kommunikation
Group(pl):	Aplikacje/Komunikacja
Source0:	http://home.earthlink.net/~nawalker/pharmacy/%{name}-%{version}.tar.gz
Patch0:		%{name}-DESTDIR.patch
URL:		http://www.cvs.com/
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gnome-libs-devel
BuildRequires:	gtk+-devel >= 1.1.12
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
Pharmacy intends to be a GNOME compliant front-end to CVS. Currently,
it provides a limited user interface to CVS commands and a "console"
for the lazy power-user.

%prep
%setup -q
%patch0 -p1

%build
gettextize --copy --force
automake
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	sysdir=%{_applnkdir}/Utilities

gzip -9nf AUTHORS ChangeLog NEWS README TODO

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/pharmacy
%{_applnkdir}/Utilities/pharmacy.desktop
%{_datadir}/pixmaps/*
