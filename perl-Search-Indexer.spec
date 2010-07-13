%define upstream_name  	    Search-Indexer
%define upstream_version    0.76

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Full-text indexer
Url:        http://search.cpan.org/dist/%{upstream_name}
Source:     http://www.cpan.org/modules/by-module/Search/%{upstream_name}-%{upstream_version}.tar.gz
BuildRequires: perl(BerkeleyDB)
BuildRequires: perl(List::MoreUtils)
BuildRequires: perl(Search::QueryParser)
BuildArch: noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}

%description
This module provides support for indexing a collection of documents, for
searching the collection, and displaying the sorted results, together with
contextual excerpts of the original document.

%prep
%setup -q -n %{upstream_name}-%{upstream_version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

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


