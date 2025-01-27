%define upstream_name    Nmap-Scanner
%define upstream_version 1.0

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	7

Summary:	Perform and manipulate nmap scans using perl
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Nmap/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Class::Generate)
BuildRequires:	perl(File::Temp)
BuildRequires:	perl(IPC::Open3)
BuildRequires:	perl(HTML::Entities)
BuildRequires:	perl(LWP::UserAgent)
BuildRequires:	perl(XML::SAX)
Provides:	perl(Nmap::Scanner::Address)  
Provides:	perl(Nmap::Scanner::Distance)  
Provides:	perl(Nmap::Scanner::ExtraPorts)  
Provides:	perl(Nmap::Scanner::Host)  
Provides:	perl(Nmap::Scanner::Hostname)  
Provides:	perl(Nmap::Scanner::Hosts)  
Provides:	perl(Nmap::Scanner::NmapRun)  
Provides:	perl(Nmap::Scanner::OS)  
Provides:	perl(Nmap::Scanner::OS::Class)  
Provides:	perl(Nmap::Scanner::OS::Fingerprint)  
Provides:	perl(Nmap::Scanner::OS::IPIdSequence)  
Provides:	perl(Nmap::Scanner::OS::Match)  
Provides:	perl(Nmap::Scanner::OS::PortUsed)  
Provides:	perl(Nmap::Scanner::OS::TCPSequence)  
Provides:	perl(Nmap::Scanner::OS::TCPTSSequence)  
Provides:	perl(Nmap::Scanner::OS::Uptime)  
Provides:	perl(Nmap::Scanner::Port)  
Provides:	perl(Nmap::Scanner::RunStats)  
Provides:	perl(Nmap::Scanner::RunStats::Finished)  
Provides:	perl(Nmap::Scanner::ScanInfo)  
Provides:	perl(Nmap::Scanner::Service)  
Provides:	perl(Nmap::Scanner::Task)  
Provides:	perl(Nmap::Scanner::TaskProgress)  
Requires:	nmap
BuildArch:	noarch

%description
This set of modules provides perl class wrappers for the network mapper
(nmap) scanning tool (see http://www.insecure.org/nmap/). Using these
modules, a developer, network administrator, or other techie can create
perl routines or classes which can be used to automate and integrate nmap
scans elegantly into new and existing perl scripts.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sun Apr 24 2011 Funda Wang <fwang@mandriva.org> 1.0.0-4mdv2011.0
+ Revision: 658164
- add br
- rebuild for updated spec-helper

* Sun Oct 17 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.0.0-3mdv2011.0
+ Revision: 586168
- fix dependencies

* Sun Oct 17 2010 Thierry Vignaud <tv@mandriva.org> 1.0.0-2mdv2011.0
+ Revision: 586145
- actuall requires nmap
- fix description

* Sat Oct 16 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.0.0-1mdv2011.0
+ Revision: 586116
- import perl-Nmap-Scanner

