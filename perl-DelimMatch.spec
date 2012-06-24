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
Summary(es):	M�dulo de Perl DelimMatch
Summary(fr):	Module Perl DelimMatch
Summary(it):	Modulo di Perl DelimMatch
Summary(ja):	DelimMatch Perl �⥸�塼��
Summary(ko):	DelimMatch �� ����
Summary(no):	Perlmodul DelimMatch
Summary(pl):	Modu� Perla DelimMatch
Summary(pt):	M�dulo de Perl DelimMatch
Summary(pt_BR):	M�dulo Perl DelimMatch
Summary(ru):	������ ��� Perl DelimMatch
Summary(sv):	DelimMatch Perlmodul
Summary(uk):	������ ��� Perl DelimMatch
Summary(zh_CN):	DelimMatch Perl ģ��
Name:		perl-DelimMatch
Version:	1.06a
Release:	1
License:	GPL or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pnam}-%{version}.tar.gz
# Source0-md5:	8efb70c2326d0b8f551708e9cdc2b649
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 5.6.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DelimMatch - Perl extension to find regexp delimited strings with
proper nesting.

%description -l pl
DelimMatch - rozszerzenie Perla do wyszukiwania �a�cuch�w
ograniczonych wyra�eniami regularnymi z w�a�ciwym zagnie�d�eniem.

%prep
%setup -q -n DelimMatch-1.06

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
