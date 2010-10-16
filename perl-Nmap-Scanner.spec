%define upstream_name    Nmap-Scanner
%define upstream_version 1.0

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:    Perform and manipulate nmap scans using perl
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Nmap/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Class::Generate)
BuildRequires: perl(File::Temp)
BuildRequires: perl(IPC::Open3)
BuildRequires: perl(LWP::UserAgent)
BuildRequires: perl(XML::SAX)
Requires: nmap
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
This set of modules provides perl class wrappers for the network mapper
(nmap) scanning tool (see http://www.insecure.org/nmap/). Using these
modules, a developer, network administrator, or other techie can create
perl routines or classes which can be used to automate and integrate nmap
scans elegantly into new and existing perl scripts.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/*


