%define _prefix /opt/pushpin
%define service_user pushpin
%define service_home /var/opt/pushpin
%define mongrel2_version 1.11.0
%define zurl_version 1.5.1

Summary: PushPin service
Name: pushpin
Version: 1.8.0
Release: 2%{dist}
Source0: https://dl.bintray.com/fanout/source/pushpin-%{version}.tar.bz2
Source1: https://github.com/mongrel2/mongrel2/releases/download/v%{mongrel2_version}/mongrel2-v%{mongrel2_version}.tar.bz2
Source2: https://dl.bintray.com/fanout/source/zurl-%{zurl_version}.tar.bz2
Source3: pushpin.service
License: AGPL
Group: Server
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Vendor: subuk
Prefix: %{_prefix}
BuildRequires: qt5-qtwebchannel-devel cppzmq-devel sqlite-devel libcurl-devel
BuildRequires: systemd
%{?systemd_requires}
Requires(pre): /usr/sbin/useradd /usr/sbin/groupadd /usr/bin/getent

%description
PushPin web service

%prep
%setup -q -T -b 1 -n mongrel2-v%{mongrel2_version}
%setup -q -T -b 2 -n zurl-%{zurl_version}
%setup -q

%build
pushd ../zurl-%{zurl_version}
./configure --prefix=%{_prefix}
make
popd

pushd ../mongrel2-v%{mongrel2_version}
make PREFIX=%{_prefix} DESTDIR=%{buildroot}
popd

./configure --prefix=%{_prefix} --configdir=/etc
make %{_smp_mflags}

%install
pushd ../zurl-%{zurl_version}
make install INSTALL_ROOT=%{buildroot}
popd

pushd ../mongrel2-v%{mongrel2_version}
make install PREFIX=%{_prefix} DESTDIR=%{buildroot}
popd

make install INSTALL_ROOT=%{buildroot}
install -m 755 -d %{buildroot}%{_unitdir}
install -m 644 %{_sourcedir}/pushpin.service %{buildroot}%{_unitdir}/pushpin.service

%post
if ! getent passwd  | grep -q "^%{service_user}:"; then
    echo -n "Adding system user %{service_user} ..."
    useradd --system --no-create-home --shell=/bin/false --home-dir=%{service_home} %{service_user}
    echo " done"
fi

install -d -m 0750 -o %{service_user} -g %{service_user} %{service_home}
%systemd_post pushpin.service

%preun
%systemd_preun pushpin.service

%postun
%systemd_postun pushpin.service

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_prefix}/bin/zurl
%{_prefix}/bin/m2adapter
%{_prefix}/bin/pushpin-handler
%{_prefix}/bin/pushpin-proxy
%{_prefix}/bin/pushpin-publish
%{_prefix}/bin/pushpin
%{_prefix}/bin/m2sh
%{_prefix}/bin/mongrel2
%{_prefix}/bin/procer
%{_prefix}/lib
%{_unitdir}/pushpin.service
%config(noreplace) /etc/pushpin/routes
%config(noreplace) /etc/pushpin/pushpin.conf

%changelog
* Sat Mar 12 2016 21:12:34 +0300 Matvey Kruglov <kubuzzzz@gmail.com> 1.8.0-1
- First public release
