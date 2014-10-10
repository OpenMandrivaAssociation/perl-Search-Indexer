%define upstream_name  	    Search-Indexer
%define upstream_version 0.77

Name:		perl-%{upstream_name}
Version:	%perl_convert_version 0.77
Release:	2
License:	GPL or Artistic
Group:		Development/Perl
Summary:	Full-text indexer
Url:		http://search.cpan.org/dist/%{upstream_name}
Source:		http://www.cpan.org/modules/by-module/Search/Search-Indexer-0.77.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(BerkeleyDB)
BuildRequires:	perl(List::MoreUtils)
BuildRequires:	perl(Search::QueryParser)
BuildArch:	noarch

%description
This module provides support for indexing a collection of documents, for
searching the collection, and displaying the sorted results, together with
contextual excerpts of the original document.

%prep
%setup -q -n %{upstream_name}-%{upstream_version} 

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Mon Apr 25 2011 Funda Wang <fwang@mandriva.org> 0.760.0-3mdv2011.0
+ Revision: 658879
- rebuild for updated spec-helper

* Tue Jul 13 2010 Jérôme Quelin <jquelin@mandriva.org> 0.760.0-2mdv2011.0
+ Revision: 552003
- rebuild

* Sat Jun 27 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.760.0-1mdv2010.0
+ Revision: 389826
- new version

* Fri May 15 2009 Jérôme Quelin <jquelin@mandriva.org> 0.75-2mdv2010.0
+ Revision: 375904
- rebuild

* Tue Mar 31 2009 Jérôme Quelin <jquelin@mandriva.org> 0.75-1mdv2009.1
+ Revision: 362907
- import perl-Search-Indexer


* Tue Mar 31 2009 cpan2dist 0.75-1mdv
- initial mdv release, generated with cpan2dist


