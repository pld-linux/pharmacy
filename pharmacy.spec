Summary:	Pharmacy intends to be a GNOME compliant front-end to CVS
Summary(pl):	Pharmacy stara siê byæ zgodnym z GNOME frontendem do CVS
Name:		pharmacy
Version:	0.3
Release:	5
License:	GPL
Group:		Applications/Communications
Source0:	http://dl.sourceforge.net/pharmacy/%{name}-%{version}.tar.gz
# Source0-md5:	4fed3c8df18556aaaa43aa8028119b56
Patch0:		%{name}-DESTDIR.patch
Patch1:		%{name}-am_fix.patch
Patch2:		%{name}-desktop.patch
Patch3:		%{name}-po.patch
URL:		http://pharmacy.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gnome-libs-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Pharmacy intends to be a GNOME compliant front-end to CVS. Currently,
it provides a limited user interface to CVS commands and a "console"
for the lazy power-user.

%description -l pl
Pharmacy stara siê byæ zgodnym z GNOME frontendem do CVS. Aktualnie
dostarcza ograniczony interfejs do komend CVS-u oraz "konsolê" dla
leniwych power-userów.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

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
	sysdir=%{_desktopdir}

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/pharmacy
%{_desktopdir}/pharmacy.desktop
%{_pixmapsdir}/*
