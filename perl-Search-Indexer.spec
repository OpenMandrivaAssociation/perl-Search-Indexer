
%define realname   Search-Indexer
%define version    0.75
%define release    %mkrel 1

Name:       perl-%{realname}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Full-text indexer
Source:     http://www.cpan.org/modules/by-module/Search/%{realname}-%{version}.tar.gz
Url:        http://search.cpan.org/dist/%{realname}
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: perl-devel
BuildRequires: perl(BerkeleyDB)
BuildRequires: perl(List::MoreUtils)
BuildRequires: perl(Search::QueryParser)

BuildArch: noarch

%description
This module provides support for indexing a collection of documents, for
searching the collection, and displaying the sorted results, together with
contextual excerpts of the original document.

Documents
    As far as this module is concerned, a _document_ is just a buffer of
    plain text, together with a unique identifying number. The caller is
    responsible for supplying unique numbers, and for converting the
    original source (HTML, PDF, whatever) into plain text. Documents could
    also contain more information (other fields like date, author, Dublin
    Core, etc.), but this must be handled externally, in a database or any
    other store. A candidate for storing metadata about documents could be
    File::Tabular, which uses the same query parser.

Search syntax
    Searching requests may include plain terms, "exact phrases", '+' or '-'
    prefixes, boolean operators and parentheses. See the
    Search::QueryParser manpage for details.

%prep
%setup -q -n %{realname}-%{version} 

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


