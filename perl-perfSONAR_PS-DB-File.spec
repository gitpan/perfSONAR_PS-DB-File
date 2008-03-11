Name:           perl-perfSONAR_PS-DB-File
Version:        0.07
Release:        1%{?dist}
Summary:        perfSONAR_PS::DB::File Perl module
License:        distributable, see LICENSE
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/perfSONAR_PS-DB-File/
Source0:        http://www.cpan.org/modules/by-module/perfSONAR_PS/perfSONAR_PS-DB-File-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
Requires:       perl(Data::Compare)
Requires:       perl(Log::Log4perl) >= 1
Requires:       perl(Params::Validate) >= 0.64
Requires:       perl(XML::LibXML) >= 1.6
Requires:       perl(perfSONAR_PS::Common)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
perfSONAR_PS::DB::File is a module that provides a perfSONAR_PS::DB interface
to an XML file.

%prep
%setup -q -n perfSONAR_PS-DB-File-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -type d -depth -exec rmdir {} 2>/dev/null \;

chmod -R u+rwX,go+rX,go-w $RPM_BUILD_ROOT/*

%check
make test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc Changes LICENSE README modules perl-perfSONAR_PS-DB-File.spec
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Thu Feb 28 2008 aaron@internet2.edu 0.07-1
- Specfile autogenerated.