Summary:	Pharmacy intends to be a GNOME compliant front-end to CVS
Summary(pl):	Pharmacy stara si� by� zgodnym z GNOME front-end'em do CVS
Name:		pharmacy
Version:	0.3
Release:	1
License:	GPL
Group:		Applications/Communications
Group(de):	Applikationen/Kommunikation
Group(pl):	Aplikacje/Komunikacja
Source0:	http://prdownloads.sourceforge.net/pharmacy/%{name}-%{version}.tar.gz
Patch0:		%{name}-DESTDIR.patch
Patch1:		%{name}-am_fix.patch
URL:		http://pharmacy.sourceforge.net
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gnome-libs-devel
BuildRequires:	gtk+-devel >= 1.1.12
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
Pharmacy intends to be a GNOME compliant front-end to CVS. Currently,
it provides a limited user interface to CVS commands and a "console"
for the lazy power-user.

%description -l pl
Pharmacy stara si� by� zgodnym z GNOME front-end'em do CVS.
Aktualnie dostarcza ograniczony interfejs do komend CVS'u oraz
"konsol�" dla leniwych power-user.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
rm -f missing acinclude.m4
libtoolize --copy --force
gettextize --copy --force
aclocal -I macros
autoconf
automake -a -c
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
%{_pixmapsdir}/*
