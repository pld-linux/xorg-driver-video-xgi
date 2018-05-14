Summary:	X.org video drivers for XGI adapters
Summary(pl.UTF-8):	Sterowniki obrazu X.org do kart graficznych XGI
Name:		xorg-driver-video-xgi
Version:	1.6.1
Release:	5
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-video-xgi-%{version}.tar.bz2
# Source0-md5:	103a17936676318b4b09af94dbc420a9
Patch0:		%{name}-build.patch
Patch1:		xserver-1.19.patch
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	libdrm-devel >= 2.0
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	rpmbuild(macros) >= 1.389
BuildRequires:	xorg-lib-libpciaccess-devel >= 0.8.0
BuildRequires:	xorg-proto-fontsproto-devel
BuildRequires:	xorg-proto-glproto-devel
BuildRequires:	xorg-proto-randrproto-devel
BuildRequires:	xorg-proto-renderproto-devel
BuildRequires:	xorg-proto-videoproto-devel
BuildRequires:	xorg-proto-xextproto-devel >= 7.0.99.1
BuildRequires:	xorg-proto-xf86dgaproto-devel
BuildRequires:	xorg-proto-xf86driproto-devel
BuildRequires:	xorg-proto-xineramaproto-devel
BuildRequires:	xorg-util-util-macros >= 1.8
BuildRequires:	xorg-xserver-server-devel >= 1.1.0
%{?requires_xorg_xserver_videodrv}
Requires:	xorg-xserver-libdri >= 1.1.0
Requires:	xorg-xserver-libglx >= 1.1.0
Requires:	xorg-xserver-server >= 1.1.0
Provides:	xorg-driver-video
Obsoletes:	XFree86-driver-xgi < 1:7.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X.org video drivers for XGI adapters:
- Volari V3XT/V3XE/V5/V8
- Volari Z7/Z9/Z9s/Z11

%description -l pl.UTF-8
Sterowniki obrazu X.org do kart graficznych XGI:
- Volari V3XT/V3XE/V5/V8
- Volari Z7/Z9/Z9s/Z11

%prep
%setup -q -n xf86-video-xgi-%{version}
%patch0 -p1
%patch1 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/xorg/modules/*/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README
%attr(755,root,root) %{_libdir}/xorg/modules/drivers/xgi_drv.so
%{_mandir}/man4/xgi.4*
