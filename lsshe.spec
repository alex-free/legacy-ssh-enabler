Name:           legacy-ssh-enabler
Version:        1.0
Summary:        Allow your newer OpenSSH client and server to talk with older SSH clients and servers, system-wide.
Release:        1%{?dist}
License:        3-BSD
URL:            https://github.com/alex-free/ezre
Packager:       Alex Free

%description
Allow your newer OpenSSH client and server to talk with older SSH clients and servers, system-wide.

%install
mkdir -p %{buildroot}/usr/bin
cp %{_sourcedir}/lsshe %{buildroot}/usr/bin/

%files
/usr/bin/lsshe
