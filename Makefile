PKG_NAME := jdk-felix-bundlerepository
URL := http://repo2.maven.org/maven2/org/apache/felix/org.apache.felix.bundlerepository/1.6.6/org.apache.felix.bundlerepository-1.6.6.jar
ARCHIVES := http://repo2.maven.org/maven2/org/apache/felix/org.apache.felix.bundlerepository/1.6.6/org.apache.felix.bundlerepository-1.6.6.pom %{buildroot}

include ../common/Makefile.common
