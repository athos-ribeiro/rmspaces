Name:           rmspaces
Version:        0.6
Release:        2%{?dist}
Summary:        Remove spaces from file names
License:        GPLv3
URL:            http://search.cpan.org/dist/App-rmspaces/
Source0:        http://www.cpan.org/modules/by-module/App/App-rmspaces-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  make
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(Pod::Usage)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Tests
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Script)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
This is a simple script to remove those anoying spaces from file names. Just
run rmspaces FILENAME.

Note that it could also be used to change multiple file names by using the
--target and the --separator arguments.

%prep
%setup -q -n App-rmspaces-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README.md
%license LICENSE
%{_bindir}/rmspaces
%{perl_vendorlib}/*
%{_mandir}/man1/*
%{_mandir}/man3/*

%changelog
* Wed Nov 25 2020 Athos Ribeiro <athoscr@fedoraproject.org> 0.6-2
- Update version

* Fri Sep 15 2017 Athos Ribeiro <athoscr@fedoraproject.org> 0.6-1
- Update version

* Wed Jul 26 2017 Athos Ribeiro <athoscr@fedoraproject.org> 0.5-1
- Update version

* Wed Jul 19 2017 Athos Ribeiro <athoscr@fedoraproject.org> 0.4-1
- Initial package
