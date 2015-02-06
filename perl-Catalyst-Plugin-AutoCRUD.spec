%define upstream_name    Catalyst-Plugin-AutoCRUD
%define upstream_version 1.110731

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Instant AJAX web front-end for DBIx::Class
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Catalyst/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Catalyst::Action::RenderView)
BuildRequires:	perl(Catalyst::Model::DBIC::Schema)
BuildRequires:	perl(Catalyst::Runtime)
BuildRequires:	perl(Catalyst::View::JSON)
BuildRequires:	perl(Catalyst::View::TT)
BuildRequires:	perl(Data::Page)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(JSON::Any)
BuildRequires:	perl(Module::Find)
BuildRequires:	perl(MRO::Compat)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test::WWW::Mechanize)
BuildRequires:	perl(Test::WWW::Mechanize::Catalyst)
BuildArch:	noarch

%description
This module contains an application which will automatically construct a
web interface for a database on the fly. The web interface supports Create,
Retrieve, Update, Delete and Search operations.

The interface is not written to static files on your system, and uses AJAX
to act upon the database without reloading your web page (much like other
Web 2.0 appliactions, for example Google Mail).

Almost all the information required by the plugin is retrieved from the the
DBIx::Class manpage ORM frontend to your database, which it is expected
that you have already set up (although see the /USAGE manpage, below). This
means that any change in database schema ought to be reflected immediately
in the web interface after a page refresh.

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
%doc README Changes META.yml
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 1.110.731-2mdv2011.0
+ Revision: 657394
- rebuild for updated spec-helper

* Fri Mar 18 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.110.731-1
+ Revision: 646319
- update to new version 1.110731

* Fri Feb 18 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.110.471-1
+ Revision: 638459
- update to new version 1.110471

* Wed Sep 22 2010 Shlomi Fish <shlomif@mandriva.org> 0.680.0-1mdv2011.0
+ Revision: 580539
- import perl-Catalyst-Plugin-AutoCRUD

