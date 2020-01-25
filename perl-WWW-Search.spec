#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	WWW
%define		pnam	Search
Summary:	WWW::Search - Virtual base class for WWW searches
Name:		perl-WWW-Search
Version:	2.518
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/WWW/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	ad4c7f2094db18a62d71d459b84ad777
URL:		https://metacpan.org/release/WWW-Search/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Bit-Vector
BuildRequires:	perl-Date-Manip
BuildRequires:	perl-File-Slurp
BuildRequires:	perl-HTML-Parser >= 2.23
BuildRequires:	perl-HTML-Tree
BuildRequires:	perl-IO-Capture
BuildRequires:	perl-Test-File
BuildRequires:	perl-URI
BuildRequires:	perl-User
BuildRequires:	perl-libwww
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This class is the parent for all access methods supported by the
WWW::Search library. This library implements a Perl API to web-based
search engines.

See README for a list of search engines currently supported, and for a
lot of interesting high-level information about this distribution.

Search results can be limited, and there is a pause between each
request to avoid overloading either the client or the server.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%attr(755,root,root) %{_bindir}/AutoSearch
%attr(755,root,root) %{_bindir}/WebSearch
%{_mandir}/man1/AutoSearch.1p*
%{_mandir}/man1/WebSearch.1p*
%{perl_vendorlib}/WWW/*.pm
%{perl_vendorlib}/WWW/Search
%{_mandir}/man3/*
