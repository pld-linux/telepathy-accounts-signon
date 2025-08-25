Summary:	Telepathy providers for libaccounts/libsignon
Summary(pl.UTF-8):	Biblioteki Telepathy dla libaccounts/libsignon
Name:		telepathy-accounts-signon
Version:	2.0
Release:	1
License:	LGPL v2.1+
Group:		Libraries
#Source0Download: https://gitlab.com/accounts-sso/telepathy-accounts-signon/tags
Source0:	https://gitlab.com/accounts-sso/telepathy-accounts-signon/-/archive/%{version}/%{name}-%{version}.tar.bz2
# Source0-md5:	972acfd54cd2ff09a18ada3a7bb7c76b
URL:		https://gitlab.com/accounts-sso/telepathy-accounts-signon
BuildRequires:	libaccounts-glib-devel
BuildRequires:	libsignon-glib-devel >= 2.0
BuildRequires:	meson
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 2.042
BuildRequires:	telepathy-mission-control-devel
Requires:	telepathy-mission-control
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A mission control plugin for Telepathy, integrating with libaccounts
and libsignon to provide IM accounts and authentication. This code is
based on Nemo Mobile's fork of the plugin from Empathy's
ubuntu-online-account support.

%description -l pl.UTF-8
Wtyczka mission control dla Telepathy, integrująca z libaccounts i
libsignon w celu dostarczenia kont i uwierzytelnienia do
komunikatorów. Kod jest oparty na gałęzi Nemo Mobile wtyczki z obsługą
ubunto-online-account dla Empathy.

%prep
%setup -q

%build
%meson

%meson_build

%install
rm -rf $RPM_BUILD_ROOT

%meson_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{_libdir}/mission-control-plugins.0/mcp-account-manager-accounts-sso.so
