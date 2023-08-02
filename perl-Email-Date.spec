#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Email-Date
Version  : 1.104
Release  : 26
URL      : https://cpan.metacpan.org/authors/id/R/RJ/RJBS/Email-Date-1.104.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/R/RJ/RJBS/Email-Date-1.104.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libe/libemail-date-perl/libemail-date-perl_1.104-2.debian.tar.xz
Summary  : 'Find and Format Date Headers'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Email-Date-license = %{version}-%{release}
Requires: perl-Email-Date-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Capture::Tiny)
BuildRequires : perl(Date::Parse)
BuildRequires : perl(Email::Abstract)
BuildRequires : perl(Email::Date::Format)
BuildRequires : perl(Email::Simple)
BuildRequires : perl(MRO::Compat)
BuildRequires : perl(Module::Pluggable)

%description
This archive contains the distribution Email-Date,
version 1.104:
Find and Format Date Headers

%package dev
Summary: dev components for the perl-Email-Date package.
Group: Development
Provides: perl-Email-Date-devel = %{version}-%{release}
Requires: perl-Email-Date = %{version}-%{release}

%description dev
dev components for the perl-Email-Date package.


%package license
Summary: license components for the perl-Email-Date package.
Group: Default

%description license
license components for the perl-Email-Date package.


%package perl
Summary: perl components for the perl-Email-Date package.
Group: Default
Requires: perl-Email-Date = %{version}-%{release}

%description perl
perl components for the perl-Email-Date package.


%prep
%setup -q -n Email-Date-1.104
cd %{_builddir}
tar xf %{_sourcedir}/libemail-date-perl_1.104-2.debian.tar.xz
cd %{_builddir}/Email-Date-1.104
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/Email-Date-1.104/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Email-Date
cp %{_builddir}/Email-Date-1.104/LICENSE %{buildroot}/usr/share/package-licenses/perl-Email-Date/bfea969d3d8595459ec8fb27172f317821ebcbb0
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-Email-Date/89bf4961ee022f8f6214242003fdf408d048f43a
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Email::Date.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Email-Date/89bf4961ee022f8f6214242003fdf408d048f43a
/usr/share/package-licenses/perl-Email-Date/bfea969d3d8595459ec8fb27172f317821ebcbb0

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
