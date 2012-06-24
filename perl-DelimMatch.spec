%include	/usr/lib/rpm/macros.perl
Summary:	DelimMatch perl module
Summary(pl):	Modu� perla DelimMatch
Name:		perl-DelimMatch
Version:	1.03
Release:	6
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Text/DelimMatch-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DelimMatch - Perl extension to find regexp delimited strings with
proper nesting.

%description -l pl
Modu� perla DelimMatch.

%prep
%setup -q -n DelimMatch-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/Text/DelimMatch.pm
%{_mandir}/man3/*
