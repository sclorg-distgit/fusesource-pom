%global pkg_name fusesource-pom
%{?scl:%scl_package %{pkg_name}}
%{?maven_find_provides_and_requires}

Name:             %{?scl_prefix}%{pkg_name}
Version:          1.9
Release:          7.11%{?dist}
Summary:          Parent POM for FuseSource Maven projects
License:          ASL 2.0
URL:              http://fusesource.com/
Source0:          http://repo1.maven.org/maven2/org/fusesource/fusesource-pom/%{version}/fusesource-pom-%{version}.pom
Source1:          http://www.apache.org/licenses/LICENSE-2.0.txt
BuildArch:        noarch

BuildRequires:    %{?scl_prefix_java_common}maven-local

%description
This is a shared POM parent for FuseSource Maven projects

%prep
%setup -c -T
%{?scl:scl enable maven30 %{scl} - <<"EOF"}
set -e -x
cp %{SOURCE0} pom.xml
cp -p %{SOURCE1} LICENSE

%pom_remove_plugin :clirr-maven-plugin

# WebDAV wagon is not available in Fedora.
%pom_xpath_remove "pom:extension[pom:artifactId[text()='wagon-webdav-jackrabbit']]"
%{?scl:EOF}

%build
%{?scl:scl enable maven30 %{scl} - <<"EOF"}
set -e -x
%mvn_build
%{?scl:EOF}

%install
%{?scl:scl enable maven30 %{scl} - <<"EOF"}
set -e -x
%mvn_install
%{?scl:EOF}

%files -f .mfiles
%dir %{_mavenpomdir}/%{pkg_name}
%doc LICENSE

%changelog
* Sat Jan 09 2016 Michal Srb <msrb@redhat.com> - 1.9-7.11
- maven33 rebuild

* Thu Jan 15 2015 Michal Srb <msrb@redhat.com> - 1.9-7.10
- Fix directory ownership

* Tue Jan 13 2015 Michael Simacek <msimacek@redhat.com> - 1.9-7.9
- Mass rebuild 2015-01-13

* Tue Jan 06 2015 Michael Simacek <msimacek@redhat.com> - 1.9-7.8
- Mass rebuild 2015-01-06

* Mon May 26 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.9-7.7
- Mass rebuild 2014-05-26

* Wed Feb 19 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.9-7.6
- Mass rebuild 2014-02-19

* Wed Feb 19 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.9-7.5
- Rebuild to get rid of auto-requires on java-devel

* Tue Feb 18 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.9-7.4
- Mass rebuild 2014-02-18

* Tue Feb 18 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.9-7.3
- Rebuild to fix incorrect auto-requires

* Thu Feb 13 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.9-7.2
- Rebuild to regenerate auto-requires

* Tue Feb 11 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.9-7.1
- First maven30 software collection build

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 1.9-7
- Mass rebuild 2013-12-27

* Thu Aug 15 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.9-6
- Update to current packaging guidelines

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.9-4
- Remove wagon-webdav-jackrabbit from POM
- Resolves: rhbz#911552

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1.9-2
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Thu Sep 20 2012 Marek Goldmann <mgoldman@redhat.com> - 1.9-1
- Upstream release 1.9
- Removed Requires

* Tue Sep  4 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.5-5
- Install LICENSE file
- Convert patch to POM macro

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 20 2011 Tomas Radej <tradej@redhat.com> - 1.5-2
- Changed R on plexus-maven-plugin to component-metadata
- Guidelines fixes

* Fri May 27 2011 Marek Goldmann <mgoldman@redhat.com> 1.5-1
- Initial packaging

