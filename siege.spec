Summary:	An HTTP regression testing/benchmarking utility
Summary(pl):	Narzêdzie do testowania serwerów HTTP
Name:		siege
Version:	2.53
Release:	1
License:	GPL v2
Group:		Networking/Utilities
Source0:	ftp://ftp.armstrong.com/pub/siege/%{name}-%{version}.tar.gz
# Source0-md5:	91610bcaaf0a90cced472dc7ed8caae4
Patch0:		%{name}-DESTDIR.patch
Patch1:		%{name}-am_fixes.patch
URL:		http://www.joedog.org/siege/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	openssl-devel >= 0.9.7
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

%description -l pl
Siege to narzêdzie do testowania dzia³ania i wydajno¶ci serwerów HTTP.
Mo¿e testowaæ odporno¶æ dla pojedynczego URL-a ze zdefiniowan± liczb±
symulowanych u¿ytkowników, lub ¶ci±gaæ wiele URL-i do pamiêci,
obci±¿aj±c je równocze¶nie. Program raportuje ca³kowit± liczbê
¶ci±gniêtych dokumentów, liczbê przes³anych bajtów, czas reakcji,
liczbê jednoczesnych po³±czeñ i status operacji. Siege obs³uguje
protoko³y HTTP/1.0 i 1.1, metody GET i POST, cookie, logowanie
transakcji oraz zwyk³± autentykacjê. Opcje s± konfigurowalne dla
u¿ytkownika.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
rm -f missing
%{__aclocal}
%{__autoconf}
%{__automake}
%configure --with-ssl
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}

%{__make} install DESTDIR=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README README.https AUTHORS KNOWNBUGS NEWS ChangeLog
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/*
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
