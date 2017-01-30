Name     : jdk-felix-bundlerepository
Version  : 1.6.6
Release  : 2
URL      : http://repo2.maven.org/maven2/org/apache/felix/org.apache.felix.bundlerepository/1.6.6/org.apache.felix.bundlerepository-1.6.6.jar
Source0  : http://repo2.maven.org/maven2/org/apache/felix/org.apache.felix.bundlerepository/1.6.6/org.apache.felix.bundlerepository-1.6.6.jar
Source1  : http://repo2.maven.org/maven2/org/apache/felix/org.apache.felix.bundlerepository/1.6.6/org.apache.felix.bundlerepository-1.6.6.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: jdk-felix-bundlerepository-data
BuildRequires : javapackages-tools
BuildRequires : lxml
BuildRequires : openjdk-dev
BuildRequires : python3
BuildRequires : six

%description
No detailed description available

%package data
Summary: data components for the jdk-felix-bundlerepository package.
Group: Data

%description data
data components for the jdk-felix-bundlerepository package.


%prep

%build

%install
mkdir -p %{buildroot}/usr/share/maven-poms
mkdir -p %{buildroot}/usr/share/maven-metadata
mkdir -p %{buildroot}/usr/share/java

mv %{SOURCE0} %{buildroot}/usr/share/java/felix-bundlerepository.jar
mv %{SOURCE1} %{buildroot}/usr/share/maven-poms/felix-bundlerepository.pom

# Creates metadata
python3 /usr/share/java-utils/maven_depmap.py \
-n "" \
--pom-base %{buildroot}/usr/share/maven-poms \
--jar-base %{buildroot}/usr/share/java \
%{buildroot}/usr/share/maven-metadata/felix-bundlerepository.xml \
%{buildroot}/usr/share/maven-poms/felix-bundlerepository.pom \
%{buildroot}/usr/share/java/felix-bundlerepository.jar \

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/felix-bundlerepository.jar
/usr/share/maven-metadata/felix-bundlerepository.xml
/usr/share/maven-poms/felix-bundlerepository.pom
