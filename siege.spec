Summary:	An HTTP regression testing/benchmarking utility
Summary(pl.UTF-8):	Narzędzie do testowania serwerów HTTP
Name:		siege
Version:	2.69
Release:	2
License:	GPL v2
Group:		Networking/Utilities
Source0:	ftp://sid.joedog.org/pub/siege/%{name}-%{version}.tar.gz
# Source0-md5:	77190ad255dfa14232137d03fd0d994b
Patch0:		%{name}-DESTDIR.patch
Patch1:		%{name}-am_fixes.patch
Patch2:		%{name}-config.patch
URL:		http://www.joedog.org/index/siege-home
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	openssl-devel >= 0.9.7d
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

%description -l pl.UTF-8
Siege to narzędzie do testowania działania i wydajności serwerów HTTP.
Może testować odporność dla pojedynczego URL-a ze zdefiniowaną liczbą
symulowanych użytkowników, lub ściągać wiele URL-i do pamięci,
obciążając je równocześnie. Program raportuje całkowitą liczbę
ściągniętych dokumentów, liczbę przesłanych bajtów, czas reakcji,
liczbę jednoczesnych połączeń i status operacji. Siege obsługuje
protokoły HTTP/1.0 i 1.1, metody GET i POST, cookie, logowanie
transakcji oraz zwykłą autentykację. Opcje są konfigurowalne dla
użytkownika.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
rm -f missing
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--localstatedir=%{_localstatedir}/log \
	--with-ssl
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README README.https AUTHORS KNOWNBUGS NEWS ChangeLog
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%{_mandir}/man5/*
%{_mandir}/man7/*
