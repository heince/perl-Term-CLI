Name:           perl-Term-CLI
Version:        0.03002
Release:        1%{?dist}
Summary:        CLI interpreter based on Term::ReadLine
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Term-CLI/
Source0:        http://www.cpan.org/modules/by-module/Term/Term-CLI-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl >= 0:5.014_001
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(File::Which)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Modern::Perl)
BuildRequires:  perl(Moo)
BuildRequires:  perl(Moo::Role)
BuildRequires:  perl(namespace::clean)
BuildRequires:  perl(parent)
BuildRequires:  perl(Pod::Coverage::TrustPod)
BuildRequires:  perl(Pod::Text::Termcap)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(strict)
BuildRequires:  perl(Term::ReadLine)
BuildRequires:  perl(Term::ReadLine::Gnu)
BuildRequires:  perl(Test::Class)
BuildRequires:  perl(Test::Compile)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Output)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(Text::ParseWords)
BuildRequires:  perl(Types::Standard)
BuildRequires:  perl(warnings)
Requires:       perl(File::Which)
Requires:       perl(FindBin)
Requires:       perl(Getopt::Long)
Requires:       perl(List::Util)
Requires:       perl(Modern::Perl)
Requires:       perl(Moo)
Requires:       perl(Moo::Role)
Requires:       perl(namespace::clean)
Requires:       perl(parent)
Requires:       perl(Pod::Text::Termcap)
Requires:       perl(POSIX)
Requires:       perl(Term::ReadLine)
Requires:       perl(Term::ReadLine::Gnu)
Requires:       perl(Text::ParseWords)
Requires:       perl(Types::Standard)
Requires:       perl(warnings)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
Implement an easy-to-use command line interpreter based on
Term::ReadLine(3p) and Term::ReadLine::Gnu(3p).

%prep
%setup -q -n Term-CLI-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc Changes cpanfile examples LICENSE META.json README tutorial
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Mon Feb 26 2018 Steven Bakker <sb@monkey-mind.net> 0.03002-1
- New upstream release.
* Mon Feb 26 2018 Steven Bakker <sb@monkey-mind.net> 0.03001-1
- New upstream release.
* Mon Feb 26 2018 Steven Bakker <sb@monkey-mind.net> 0.03-1
- New upstream release.
* Sun Feb 25 2018 Steven Bakker <sb@monkey-mind.net> 0.02-1
- Specfile autogenerated by cpanspec 1.78.
