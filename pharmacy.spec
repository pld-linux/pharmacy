Summary:	Pharmacy intends to be a GNOME compliant front-end to CVS
Summary(pl):	Pharmacy stara siê byæ zgodnym z GNOME front-end'em do CVS
Name:		pharmacy
Version:	0.3
Release:	1
License:	GPL
Group:		Applications/Communications
Source0:	http://prdownloads.sourceforge.net/pharmacy/%{name}-%{version}.tar.gz
Patch0:		%{name}-DESTDIR.patch
Patch1:		%{name}-am_fix.patch
URL:		http://pharmacy.sourceforge.net
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gnome-libs-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
Pharmacy intends to be a GNOME compliant front-end to CVS. Currently,
it provides a limited user interface to CVS commands and a "console"
for the lazy power-user.

%description -l pl
Pharmacy stara siê byæ zgodnym z GNOME front-end'em do CVS. Aktualnie
dostarcza ograniczony interfejs do komend CVS'u oraz "konsolê" dla
leniwych power-user.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
rm -f missing acinclude.m4
%{__libtoolize}
%{__gettextize}
%{__aclocal} -I macros
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	sysdir=%{_applnkdir}/Utilities


%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/pharmacy
%{_applnkdir}/Utilities/pharmacy.desktop
%{_pixmapsdir}/*
