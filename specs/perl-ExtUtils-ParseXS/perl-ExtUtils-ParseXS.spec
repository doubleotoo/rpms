# $Id$
# Authority: dries
# Upstream: Ken Williams <ken$mathforum,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name ExtUtils-ParseXS

Summary: Converts Perl XS code into C code
Name: perl-ExtUtils-ParseXS
Version: 2.18
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/ExtUtils-ParseXS/

Source: http://www.cpan.org/modules/by-module/ExtUtils/ExtUtils-ParseXS-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
With this module, you can Convert Perl XS code into C code.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install
%{__rm} -f %{buildroot}%{perl_archlib}/perllocal.pod
%{__rm} -f %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes
%doc %{_mandir}/man3/*
%{perl_vendorlib}/ExtUtils/ParseXS.pm
%{perl_vendorlib}/ExtUtils/xsubpp

%changelog
* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 2.18-1
- Updated to release 2.18.

* Wed Jan 03 2007 Dries Verachtert <dries@ulyssis.org> - 2.17-1
- Updated to release 2.17.

* Mon Sep 18 2006 Dries Verachtert <dries@ulyssis.org> - 2.16-1
- Updated to release 2.16.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 2.15-1.2
- Rebuild for Fedora Core 5.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 2.15-1
- Updated to release 2.15.

* Wed Jun  8 2005 Dries Verachtert <dries@ulyssis.org> - 2.10-1
- Updated to release 2.10.

* Thu Jul 22 2004 Dries Verachtert <dries@ulyssis.org> - 2.08-1
- Initial package.
