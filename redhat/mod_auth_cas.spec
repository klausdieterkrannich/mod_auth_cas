Name:           mod_auth_cas
Version:        1.0.9.1
Release:        2%{?dist}
Summary:        Apache 2.0/2.2/2.4 compliant module that supports the CASv1 and CASv2 protocols

Group:          System Environment/Daemons
License:        GPLv3+ with exceptions
URL:            http://www.ja-sig.org/wiki/display/CASC/mod_auth_cas
# The source for this package was pulled from a git repo that was forked
# from Jasig's own repo. Releases are tagged on Github and are natively
# downladable as .tar.gz archives.

Source0:        mod_auth_cas-1.0.9.1.tar.gz
Source1:        auth_cas.conf

# From https://confluence.ucdavis.edu/confluence/display/IETP/CAS+SSL+Certificate+Fixes
# https://confluence.ucdavis.edu/confluence/download/attachments/33685830/mod_auth_cas.c.diff?version=1&modificationDate=1328301602000
Patch0:		    SSL-CA-chains.patch

BuildRoot:      %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildRequires:  openssl-devel
BuildRequires:  httpd-devel
BuildRequires:  libcurl-devel

Requires:       httpd

%description
mod_auth_cas is an Apache 2.0/2.2/2.4 compliant module that supports the CASv1
and CASv2 protocols

%prep
%setup -q
%patch0 

%build
%configure --with-apxs=%{_sbindir}/apxs
make %{?_smp_mflags}


%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
mkdir -p %{buildroot}/%{_sysconfdir}/httpd/conf.d
install -p -m 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/httpd/conf.d/auth_cas.conf


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc README
%{_libdir}/httpd/modules/mod_auth_cas.so
%config(noreplace) %{_sysconfdir}/httpd/conf.d/*.conf

%changelog
* Fri Feb 13 2015 Jonathan Gazeley <jonathan.gazeley@bristol.ac.uk> - 1.0.9.1-2
- Rebuilt for EL7 using spec file from EPEL6 and fork of original code to support Apache 2.4

* Thu Sep 19 2013 Scott Williams <vwbusguy@fedoraproject.org> - 1.0.9.1-1
- Upgraded to 1.0.9.1 with patch for SSL CA Chains

* Tue Oct 18 2011 Adam Miller <maxamillion@fedoraproject.org> - 1.0.8.1-3
- Fixed auth_cas.conf as per BZ# 708550 (Thanks to Jimmy Ngo) for the patch

* Tue Jun 29 2010 Adam Miller <maxamillion@fedoraproject.org> - 1.0.8.1-2
- Fixed svn export link, upstream changed canonical URL names.

* Wed Apr 28 2010 Adam Miller <maxamillion@fedoraproject.org> - 1.0.8.1-1
- added requires of httpd 
- fixed mixed use of macros
- updated to latest version

* Fri Aug 07 2009 Adam Miller <maxamillion@fedoraproject.org> - 1.0.8-1
- First attempt to package mod_auth_cas for Fedora

