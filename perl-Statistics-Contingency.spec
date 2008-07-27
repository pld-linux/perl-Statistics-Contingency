#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Statistics
%define		pnam	Contingency
Summary:	Statistics::Contingency Perl module
Summary(cs.UTF-8):	Modul Statistics::Contingency pro Perl
Summary(da.UTF-8):	Perlmodul Statistics::Contingency
Summary(de.UTF-8):	Statistics::Contingency Perl Modul
Summary(es.UTF-8):	Módulo de Perl Statistics::Contingency
Summary(fr.UTF-8):	Module Perl Statistics::Contingency
Summary(it.UTF-8):	Modulo di Perl Statistics::Contingency
Summary(ja.UTF-8):	Statistics::Contingency Perl モジュール
Summary(ko.UTF-8):	Statistics::Contingency 펄 모줄
Summary(nb.UTF-8):	Perlmodul Statistics::Contingency
Summary(pl.UTF-8):	Moduł Perla Statistics::Contingency
Summary(pt.UTF-8):	Módulo de Perl Statistics::Contingency
Summary(pt_BR.UTF-8):	Módulo Perl Statistics::Contingency
Summary(ru.UTF-8):	Модуль для Perl Statistics::Contingency
Summary(sv.UTF-8):	Statistics::Contingency Perlmodul
Summary(uk.UTF-8):	Модуль для Perl Statistics::Contingency
Summary(zh_CN.UTF-8):	Statistics::Contingency Perl 模块
Name:		perl-Statistics-Contingency
Version:	0.06
Release:	3
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	270d65583f053b078af90359011fb5c9
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Statistics::Contingency module helps you calculate several useful
statistical measures based on 2x2 "contingency tables". The author
uses these measures to help judge the results of automatic text
categorization experiments, but they are useful in other situations as
well.

%description -l pl.UTF-8
Moduł Statistics::Contingency jest pomocny przy obliczaniu kilku
przydatnych miar statystycznych opartych o "tablice wielodzielcze"
rozmiaru 2x2. Autor modułu używa tych miar jako pomocy przy ocenie
wyników eksperymentów z automatyczną klasyfikacją tekstu, lecz są one
przydatne również w innych sytuacjach.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/Statistics/Contingency.pm
%{_mandir}/man3/*
