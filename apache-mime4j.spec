%{?_javapackages_macros:%_javapackages_macros}
Name:           apache-mime4j
Version:        0.7.2
Release:        10.1
Summary:        Apache JAMES Mime4j
Group:          Development/Java
License:        ASL 2.0
URL:            http://james.apache.org/mime4j
Source0:        http://apache.online.bg//james/mime4j/apache-mime4j-project-%{version}-source-release.zip
BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  apache-commons-logging
BuildRequires:  log4j
BuildRequires:  junit
BuildRequires:  apache-commons-io
BuildRequires:  apache-james-project
BuildRequires:  javacc-maven-plugin
BuildRequires:  maven-remote-resources-plugin
BuildRequires:  apache-rat-plugin
BuildRequires:  apache-resource-bundles
BuildRequires:  maven-surefire-provider-junit

%description
Java stream based MIME message parser.

%package javadoc
Group:          Documentation
Summary:        Javadoc for %{name}

%description javadoc
API documentation for %{name}.

%prep
%setup -q -n %{name}-project-%{version}
rm -fr stage
# prevents rat plugin from failing the build
rm -fr DEPENDENCIES

# Compat symlinks for jboss-as
for p in core dom storage; do
  %mvn_file :*$p %{name}/%{name}-$p %{name}/$p
done

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE NOTICE RELEASE_NOTES.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Mar 04 2014 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0.7.2-9
- Use Requires: java-headless rebuild (#1067528)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 0.7.2-6
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Thu Jan 10 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.7.2-5
- Build with xmvn

* Thu Jan 10 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.7.2-4
- Install NOTICE file with javadoc package

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Apr 23 2012 Marek Goldmann <mgoldman@redhat.com> 0.7.2-2
- Add apache-mime4j-project POM to depmap, RHBZ#815448

* Thu Feb 23 2012 Alexander Kurtakov <akurtako@redhat.com> 0.7.2-1
- Update to latest upstream.

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Nov 30 2011 Alexander Kurtakov <akurtako@redhat.com> 0.7.1-1
- Update to latest upstream.

* Wed Nov 30 2011 Alexander Kurtakov <akurtako@redhat.com> 0.6.1-2
- Adapt to current guidelines.

* Wed Feb 23 2011 Alexander Kurtakov <akurtako@redhat.com> 0.6.1-1
- Initial package.
