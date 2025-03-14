# Forked from vault.spec by John Boero - jboero@hashicorp.com

# This can be slightly different than %%{version}.
# For example, it has dash instead of tilde for release candidates.
%global package_version 2.2.0

%global oldname vault

Name: openbao
Version: 2.2.0
Release: 1%{?dist}
Summary: Openbao is a tool for securely accessing secrets
License: MPL
Source0: https://github.com/opensciencegrid/%{name}-rpm/archive/v%{package_version}/%{name}-rpm-%{package_version}.tar.gz
# This is created by ./make-source-tarball
Source1: %{name}-src-%{package_version}.tar.gz

BuildRequires: golang
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd
URL: https://openbao.org

Provides: %{oldname} = %{version}-%{release}
Obsoletes: %{oldname} < 2.0

# This is to avoid
#   *** ERROR: No build ID note found
%global debug_package %{nil}

%description
Openbao secures, stores, and tightly controls access to tokens, passwords,
certificates, API keys, and other secrets in modern computing. Openbao handles
leasing, key revocation, key rolling, and auditing. Through a unified API, users
can access an encrypted Key/Value store and network encryption-as-a-service, or
generate AWS IAM/STS credentials, SQL/NoSQL databases, X.509 certificates, SSH
credentials, and more.

%prep
%setup -q -n %{name}-rpm-%{package_version}
RPMDIR=`pwd`
%setup -q -T -b 1 -n %{name}-src-%{package_version}

%build
# starts out in %{name}-src-%{package_version} directory
cd go/src
./make.bash
cd ../..
export GOPATH="`pwd`/gopath"
export PATH=$PWD/go/bin:$GOPATH/bin:$PATH
export GOPROXY=file://$(go env GOMODCACHE)/cache/download
cd %{name}-%{package_version}
# this prevents it from complaining that ui assets are too old
touch http/web_ui/index.html
# this prevents the build from trying to use git to figure out the version
#  which fails because there's no git info
ln -s /bin/true $GOPATH/bin/git
GO_BUILD_GCFLAGS=
%if "%{?go_debug}" != ""
# add debugging flags
GO_BUILD_GCFLAGS="all=-N -l"
%endif
make dev-ui GO_BUILD_GCFLAGS="$GO_BUILD_GCFLAGS"

%install
# starts out in %{name}-src-%{package_version} directory
mkdir -p %{buildroot}%{_bindir}/
cp -p %{name}-%{package_version}/bin/bao %{buildroot}%{_bindir}/
ln -s bao %{buildroot}%{_bindir}/%{oldname}

cd ../%{name}-rpm-%{package_version}
mkdir -p %{buildroot}%{_sysconfdir}/%{oldname}.d
ln -s %{oldname}.d %{buildroot}%{_sysconfdir}/%{name}.d
cp -p %{oldname}.hcl %{buildroot}%{_sysconfdir}/%{oldname}.d

mkdir -p %{buildroot}%{_sharedstatedir}/%{oldname}
ln -s %{oldname} %{buildroot}%{_sharedstatedir}/%{name}

mkdir -p %{buildroot}/usr/lib/systemd/system/
cp -p %{oldname}.service %{buildroot}/usr/lib/systemd/system/
ln -s %{oldname}.service %{buildroot}/usr/lib/systemd/system/%{name}.service

%clean
export GOPATH="`pwd`/gopath"
export PATH=$PWD/go/bin:$GOPATH/bin:$PATH
go clean -modcache
rm -rf %{buildroot}
rm -rf %{_builddir}/%{name}-*-%{package_version}

%files
%verify(not caps) %{_bindir}/bao
%verify(not caps) %{_bindir}/%{oldname}
%dir %{_sysconfdir}/%{oldname}.d
%{_sysconfdir}/%{name}.d
%config(noreplace) %{_sysconfdir}/%{oldname}.d/%{oldname}.hcl
%attr(0750,%{oldname},%{oldname}) %dir %{_sharedstatedir}/%{oldname}
%{_sharedstatedir}/%{name}
/usr/lib/systemd/system/%{name}.service
/usr/lib/systemd/system/%{oldname}.service

%pre
getent group %{oldname} > /dev/null || groupadd -r %{oldname}
getent passwd %{oldname} > /dev/null || \
    useradd -r -d %{_sharedstatedir}/%{oldname} -g %{oldname} \
    -s /sbin/nologin -c "%{name} secret management tool" %{oldname}
# When the package name changes the old package doesn't see the new one as
# an upgrade and so it disables the service.  Keep track and re-enable
# regardless of whether the scriptlet parameter says it is an install
# or upgrade.
%global wasenabledfile /var/run/.%{oldname}-was-enabled
rm -f %{wasenabledfile}
if systemctl is-enabled %{oldname} &>/dev/null; then
    touch %{wasenabledfile}
fi

# If the service is running, stop it now and restart it after install
%global wasrunningfile /var/run/.%{oldname}-was-running
rm -f %{wasrunningfile}
if systemctl is-active %{oldname} &>/dev/null; then
    touch %{wasrunningfile}
fi

%post
setcap cap_ipc_lock=+ep %{_bindir}/bao
systemctl daemon-reload
%systemd_post %{oldname}.service

%preun
%systemd_preun %{oldname}.service

%postun
%systemd_postun_with_restart %{oldname}.service

%posttrans
if [ -f "%{wasenabledfile}" ]; then
    rm -f %{wasenabledfile}
    if ! systemctl is-enabled %{oldname}; then
        systemctl enable %{oldname}
    fi
fi
if [ -f "%{wasrunningfile}" ]; then
    rm -f %{wasrunningfile}
    systemctl start %{oldname}
fi

%changelog
* Thu Mar  6 2025 Dave Dykstra <dwd@fnal.gov> 2.2.0-1
- Convert to use openbao instead of vault.
- Include required go version in source tarball again.

* Tue Aug 20 2024 Dave Dykstra <dwd@fnal.gov> 1.17.2-2
- Stop including go in the source tarball, instead assume the build pulls
  in a new enough version of golang.

* Mon Jul 22 2024 Dave Dykstra <dwd@fnal.gov> 1.17.2-1
- Update to upstream 1.17.2
- Add a temporary wrapper script on the vault command to avoid an irrelevant
  warning issued by the gosnowflake dependency when DBUS_SESSION_BUS_ADDRESS
  is not set

* Thu Jan  4 2024 Dave Dykstra <dwd@fnal.gov> 1.15.4-1
- Update to upstream 1.15.4

* Tue May  2 2023 Dave Dykstra <dwd@fnal.gov> 1.13.2-1
- Update to upstream 1.13.2

* Tue Apr 11 2023 Dave Dykstra <dwd@fnal.gov> 1.13.1-1
- Update to upstream 1.13.1

* Thu Nov 10 2022 Dave Dykstra <dwd@fnal.gov> 1.12.1-1
- Update to upstream 1.12.1

* Thu Jul 28 2022 Dave Dykstra <dwd@fnal.gov> 1.11.1-1
- Update to upstream 1.11.1, which includes a fix to avoid denial of
  service on HA installation.
- Remove $GOPATH/mod/*.* from the source tarball, leaving just
  $GOPATH/mod/cache/download.  That saves about 300M while still
  allowing offline builds.

* Wed Mar 23 2022 Dave Dykstra <dwd@fnal.gov> 1.10.0-1
- Update to upstream 1.10.0

* Tue Feb 15 2022 Dave Dykstra <dwd@fnal.gov> 1.9.3-1
- Update to upstream 1.9.3

* Wed Dec  1 2021 Dave Dykstra <dwd@fnal.gov> 1.9.0-1
- Update to upstream 1.9.0

* Thu Nov  4 2021 Dave Dykstra <dwd@fnal.gov> 1.8.4-1
- Update to upstream 1.8.4

* Fri Aug 27 2021 Dave Dykstra <dwd@fnal.gov> 1.8.2-1
- Update to upstream 1.8.2

* Thu Aug  5 2021 Dave Dykstra <dwd@fnal.gov> 1.8.1-1
- Update to upstream 1.8.1

* Wed Aug  4 2021 Dave Dykstra <dwd@fnal.gov> 1.8.0-1
- Update to upstream 1.8.0

* Thu Jun 17 2021 Dave Dykstra <dwd@fnal.gov> 1.7.3-1
- Update to upstream 1.7.3

* Thu May 20 2021 Dave Dykstra <dwd@fnal.gov> 1.7.2-1
- Update to upstream 1.7.2, a security release.

* Wed Apr 21 2021 Dave Dykstra <dwd@fnal.gov> 1.7.1-1
- Update to upstream 1.7.1.  Add patch for el7 to allow go 1.15.5.
- Stop disabling vault service on upgrade.

* Wed Mar 31 2021 Dave Dykstra <dwd@fnal.gov> 1.7.0-2
- Add %verify(not caps) to the vault binary to make rpm -V happy

* Thu Mar 25 2021 Dave Dykstra <dwd@fnal.gov> 1.7.0-1
- Update to upstream 1.7.0

* Wed Feb 17 2021 Dave Dykstra <dwd@fnal.gov> 1.6.2-1
- Initial build
