%global debug_package   %{nil}
%global import_path     github.com/gorilla/context
%global gopath          %{_datadir}/gocode
%global commit          b06ed15e1c7a08fa1ba783fe94fff89127587f9e
%global shortcommit     %(c=%{commit}; echo ${c:0:7})

Name:           golang-github-gorilla-context
Version:        0
Release:        0.24.git%{shortcommit}%{?dist}
Summary:        A golang registry for global request variables
License:        BSD
URL:            http://www.gorillatoolkit.org/pkg/context
Source0:        https://%{import_path}/archive/%{commit}/context-%{shortcommit}.tar.gz
ExclusiveArch:  %{?go_arches:%{go_arches}}%{!?go_arches:x86_64 aarch64 ppc64le s390x}

%description
Package gorilla/context stores values shared during a request lifetime.

For example, a router can set variables extracted from the URL and later
application handlers can access those values, or it can be used to store
sessions values to be saved at the end of a request. There are several
other common uses.

%package devel
BuildRequires:  golang
Requires:       golang
Summary:        A golang registry for global request variables
Provides:       golang(%{import_path}) = %{version}-%{release}

%description devel
Package gorilla/context stores values shared during a request lifetime.

For example, a router can set variables extracted from the URL and later
application handlers can access those values, or it can be used to store
sessions values to be saved at the end of a request. There are several
other common uses.

This package contains library source intended for building other packages
which use gorilla/context.

%prep
%setup -n context-%{commit}

%build

%install
install -d %{buildroot}/%{gopath}/src/%{import_path}
cp -av *.go %{buildroot}/%{gopath}/src/%{import_path}

%check
# disabled check for now:
# https://bugzilla.redhat.com/show_bug.cgi?id=1110497
#GOPATH=%{buildroot}/%{gopath} go test %{import_path}

%files devel
%defattr(-,root,root,-)
%doc LICENSE README.md
%dir %attr(755,root,root) %{gopath}
%dir %attr(755,root,root) %{gopath}/src
%dir %attr(755,root,root) %{gopath}/src/github.com
%dir %attr(755,root,root) %{gopath}/src/github.com/gorilla
%dir %attr(755,root,root) %{gopath}/src/github.com/gorilla/context
%{gopath}/src/%{import_path}/*.go

%changelog
* Fri Apr 21 2017 Josh Boyer <jwboyer@redhat.com> 0-0.24.git
- Resolves: rhbz#1344590 - built for all architectures

* Tue Jun 17 2014 Lokesh Mandvekar <lsm5@redhat.com> 0-0.23.git
- Resolves: rhbz#1108722 - update for docker-1.0.0
- Resolves: rhbz#1110491 - make exclusivearch for x86_64 since golang only available for x86_64
- go test disabled

* Wed Jan 15 2014 Lokesh Mandvekar <lsm5@redhat.com> 0-0.22.git708054d
- golang exclusivearch for el6+
- add check

* Wed Jan 15 2014 Lokesh Mandvekar <lsm5@redhat.com> 0-0.21.git708054d
- revert golang 1.2 requirement

* Wed Jan 15 2014 Lokesh Mandvekar <lsm5@redhat.com> 0-0.20.git708054d
- require golang 1.2 and up

* Wed Oct 16 2013 Lokesh Mandvekar <lsm5@redhat.com> 0-0.19.git708054d
- double quotes removed from provides

* Tue Oct 08 2013 Lokesh Mandvekar <lsm5@redhat.com> 0-0.18.git708054d
- noarch for f19+ and rhel7+, exclusivearch otherwise

* Mon Oct 07 2013 Lokesh Mandvekar <lsm5@redhat.com> 0-0.17.git708054d
- exclusivearch as per golang package
- debug_package nil

* Sun Oct 06 2013 Lokesh Mandvekar <lsm5@redhat.com> 0-0.16.git708054d
- excluded for ppc64

* Sun Sep 22 2013 Matthew Miller <mattdm@fedoraproject.org> 0-0.15.git708054d
- install just the source code for devel package

* Tue Sep 17 2013 Lokesh Mandvekar <lsm5@redhat.com> 0-0.14.git708054d
- docdir unversioned

* Tue Sep 17 2013 Lokesh Mandvekar <lsm5@redhat.com> 0-0.13.git708054d
- Version format changed

* Mon Sep 16 2013 Lokesh Mandvekar <lsm5@redhat.com> git708054d-12
- debuginfo not generated, was empty to begin with
- devel package buildrequires golang
- package owns all directories in import_path

* Mon Sep 16 2013 Lokesh Mandvekar <lsm5@redhat.com> git708054d-11
- Only devel package generated
- docdir corrected
- Provides moved to devel package

* Thu Sep 12 2013 Lokesh Mandvekar <lsm5@redhat.com> git708054d-10
- package owns directories it creates
- devel package requires golang

* Wed Sep 11 2013 Lokesh Mandvekar <lsm5@redhat.com> git708054d-9
- rm from install removed

* Tue Sep 10 2013 Lokesh Mandvekar <lsm5@redhat.com> git708054d-8
- cleanup in prep and build as per guidelines

* Tue Sep 10 2013 Lokesh Mandvekar <lsm5@redhat.com> git708054d-7
- rpm builds under all circumstances
- 
* Mon Sep 09 2013 Lokesh Mandvekar <lsm5@redhat.com> git708054d-6
- Devel package summary corrected

* Mon Sep 09 2013 Lokesh Mandvekar <lsm5@redhat.com> git708054d-5
- Installed files listed explicitly
- Pkg archive directory issues solved (thanks to Vincent Batts)
- Pkg archive files installed in devel package

* Thu Aug 29 2013 Lokesh Mandvekar <lsm5@redhat.com> git708054d-4
- variables introduced: pkgarch, GOPATH and so on- arch specific .a archives installed
- credit to Vincent Batts (vbatts@redhat.com) for golang-* help

* Thu Aug 29 2013 Lokesh Mandvekar <lsm5@redhat.com> 0.0.1-3
- global debug lines removed
- package name changed
- source file installation location updated

* Wed Aug 28 2013 Lokesh Mandvekar <lsm5@redhat.com> 0.0.1-2
- Fixed permissions

* Mon Aug 26 2013 Lokesh Mandvekar <lsm5@redhat.com> 0.0.1-1
- Initial fedora package
