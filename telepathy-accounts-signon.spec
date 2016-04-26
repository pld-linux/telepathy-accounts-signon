Summary:	Telepathy providers for libaccounts/libsignon
Summary(pl.UTF-8):	Biblioteki Telepathy dla libaccounts/libsignon
Name:		telepathy-accounts-signon
Version:	1.0
Release:	1
License:	LGPL v2.1+
Group:		Libraries
#Source0Download: https://gitlab.com/accounts-sso/telepathy-accounts-signon/tags
# TODO: in the future use fake GET arg to force sane filename on df
#Source0:	https://gitlab.com/accounts-sso/telepathy-accounts-signon/repository/archive.tar.bz2?ref=%{version}&fake_out=/%{name}-%{version}.tar.bz2
Source0:	archive.tar.gz%3Fref=%{version}
# Source0-md5:	e24f554c764079d938cab71439a2e555
URL:		https://gitlab.com/accounts-sso/telepathy-accounts-signon
BuildRequires:	libaccounts-glib-devel
BuildRequires:	libsignon-glib-devel
BuildRequires:	pkgconfig
BuildRequires:	qt5-qmake
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
%setup -q -n telepathy-accounts-signon-%{version}-a4ae42797a9799fcbecb4c15bd9bd408e34c2eeb

%build
qmake-qt5 \
	QMAKE_CXX="%{__cxx}" \
	QMAKE_CXXFLAGS_RELEASE="%{rpmcxxflags}" \
	QMAKE_LFLAGS_RELEASE="%{rpmldflags}"

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	INSTALL_ROOT=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NOTES README
%attr(755,root,root) %{_libdir}/mission-control-plugins.0/mcp-account-manager-accounts-sso.so
