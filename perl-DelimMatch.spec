#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Text
%define		pnam	DelimMatch
Summary:	DelimMatch Perl module
Summary(cs):	Modul DelimMatch pro Perl
Summary(da):	Perlmodul DelimMatch
Summary(de):	DelimMatch Perl Modul
Summary(es):	Módulo de Perl DelimMatch
Summary(fr):	Module Perl DelimMatch
Summary(it):	Modulo di Perl DelimMatch
Summary(ja):	DelimMatch Perl ¥â¥¸¥å¡¼¥ë
Summary(ko):	DelimMatch ÆÞ ¸ðÁÙ
Summary(no):	Perlmodul DelimMatch
Summary(pl):	Modu³ Perla DelimMatch
Summary(pt):	Módulo de Perl DelimMatch
Summary(pt_BR):	Módulo Perl DelimMatch
Summary(ru):	íÏÄÕÌØ ÄÌÑ Perl DelimMatch
Summary(sv):	DelimMatch Perlmodul
Summary(uk):	íÏÄÕÌØ ÄÌÑ Perl DelimMatch
Summary(zh_CN):	DelimMatch Perl Ä£¿é
Name:		perl-DelimMatch
Version:	1.05
Release:	2
License:	GPL or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl >= 5.6.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DelimMatch - Perl extension to find regexp delimited strings with
proper nesting.

%description -l pl
DelimMatch - rozszerzenie Perla do wyszukiwania ³añcuchów
ograniczonych wyra¿eniami regularnymi z w³a¶ciwym zagnie¿d¿eniem.

%prep
%setup -q -n DelimMatch-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}
%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorlib}/Text/DelimMatch.pm
# empty autosplit.ix
#%dir %{perl_vendorlib}/auto/Text/DelimMatch
#%%{perl_vendorlib}/auto/Text/DelimMatch/autosplit.ix
%{_mandir}/man3/*
