#
# Conditional build:
# _with_tests - perform "make test" (needs working, not busy /dev/audio!)
%include	/usr/lib/rpm/macros.perl
%define		pdir	Statistics
%define		pnam	Contingency
Summary:	Statistics::Contingency Perl module
Summary(cs):	Modul Statistics::Contingency pro Perl
Summary(da):	Perlmodul Statistics::Contingency
Summary(de):	Statistics::Contingency Perl Modul
Summary(es):	M�dulo de Perl Statistics::Contingency
Summary(fr):	Module Perl Statistics::Contingency
Summary(it):	Modulo di Perl Statistics::Contingency
Summary(ja):	Statistics::Contingency Perl �⥸�塼��
Summary(ko):	Statistics::Contingency �� ����
Summary(no):	Perlmodul Statistics::Contingency
Summary(pl):	Modu� Perla Statistics::Contingency
Summary(pt):	M�dulo de Perl Statistics::Contingency
Summary(pt_BR):	M�dulo Perl Statistics::Contingency
Summary(ru):	������ ��� Perl Statistics::Contingency
Summary(sv):	Statistics::Contingency Perlmodul
Summary(uk):	������ ��� Perl Statistics::Contingency
Summary(zh_CN):	Statistics::Contingency Perl ģ��
Name:		perl-Statistics-Contingency
Version:	0.02
Release:	2
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Statistics::Contingency module helps you calculate several useful
statistical measures based on 2x2 "contingency tables". The author
uses these measures to help judge the results of automatic text
categorization experiments, but they are useful in other situations as
well.

%description -l pl
Modu� Statistics::Contingency jest pomocny przy obliczaniu kilku
przydatnych miar statystycznych opartych o "tablice wielodzielcze"
rozmiaru 2x2. Autor modu�u u�ywa tych miar jako pomocy przy ocenie
wynik�w eksperyment�w z automatyczn� klasyfikacj� tekstu, lecz s� one
przydatne r�wnie� w innych sytuacjach.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%{?_with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_sitelib}/Statistics/Contingency.pm
%{_mandir}/man3/*
