#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Text
%define	pnam	DelimMatch
Summary:	DelimMatch - find regexp delimited strings with proper nesting
Summary(pl):	DelimMatch - poszukiwanie ³añcuchów ograniczonych wyra¿eniami regularnymi
Name:		perl-DelimMatch
Version:	1.06a
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pnam}-%{version}.tar.gz
# Source0-md5:	8efb70c2326d0b8f551708e9cdc2b649
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 1:5.8.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DelimMatch is a Perl extension to find regexp delimited strings with
proper nesting.

%description -l pl
DelimMatch jest rozszerzeniem Perla do wyszukiwania ³añcuchów
ograniczonych wyra¿eniami regularnymi z w³a¶ciwym zagnie¿d¿eniem.

%prep
%setup -q -n DelimMatch-1.06

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
%doc README
%{perl_vendorlib}/Text/DelimMatch.pm
# empty autosplit.ix
#%dir %{perl_vendorlib}/auto/Text/DelimMatch
#%%{perl_vendorlib}/auto/Text/DelimMatch/autosplit.ix
%{_mandir}/man3/*
