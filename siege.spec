Summary:	An HTTP regression testing/benchmarking utility
Summary(pl):	Narzêdzie do testowania serwerów HTTP
Name:		siege
Version:	2.53
Release:	1
License:	GPL v2
Group:		Networking/Utilities
Source0:	ftp://ftp.armstrong.com/pub/siege/%{name}-%{version}.tar.gz
Patch0:		%{name}-DESTDIR.patch
Patch1:		%{name}-am_fixes.patch
URL:		http://www.joedog.org/siege/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	openssl-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Siege is a regression test and benchmark utility. It can stress test a
single URL with a user defined number of simulated users, or it can
read many URLs into memory and stress them simultaneously. The program
reports the total number of hits recorded, bytes transferred, response
time, concurrency, and return status. Siege supports HTTP/1.0 and 1.1
protocols, GET and POST directives, cookies, transaction logging, and
basic authentication. Its features are configurable on a per user
basis.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
rm -f missing
aclocal
autoconf
automake -a -c -f
%configure --with-ssl
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README README.https AUTHORS KNOWNBUGS NEWS ChangeLog

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/*
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
