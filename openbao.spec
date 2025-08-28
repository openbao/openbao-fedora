# Loosely based on vault.spec by John Boero - jboero@hashicorp.com

# This macro can be slightly different than %%{version}.
# For example, it should have a dash instead of tilde for release candidates.
%global package_version 2.4.0

%global oldname vault

Name: openbao
Version: 2.4.0
Release: %autorelease
Summary: A tool for securely accessing secrets
# See LICENSE for primary license
# See LICENSE_DEPENDENCIES.md for bundled dependencies
# CC0-1.0 is normally not permissible for code in Fedora. Because the vendored Go package
# github.com/zeebo/blake3 it applies to has been available in Fedora as golang-github-zeebo-blake3
# since before the cutoff date 2022-08-01, the exception to use it also applies here.
License: MPL-2.0 AND AFL-2.0 AND Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND CC0-1.0 AND ISC AND MIT
Source0: https://github.com/openbao/%{name}/releases/download/v%{package_version}/%{name}-dist-%{package_version}.tar.xz
# This includes extra files to include in the package and is used as a
# single branch to track changes to them and a place where checks can be
# automated using github actions.
Source1: https://github.com/opensciencegrid/%{name}-rpm/releases/download/v%{package_version}/%{name}-rpm-%{package_version}.tar.gz
Patch0: goversion.patch

BuildRequires: golang-bin
BuildRequires: systemd-rpm-macros
%{?sysusers_requires_compat}
%if ! 0%{?el8}
BuildRequires: go-rpm-macros
%endif

URL: https://openbao.org

# The bundled provides are generated from an awk/sed pipeline in the
# make-spec script (which is included in Source1) that reads from go.mod.
Provides: bundled(golang(cel.dev/expr)) = v0.24.0
Provides: bundled(golang(cloud.google.com/go)) = v0.121.2
Provides: bundled(golang(cloud.google.com/go/auth)) = v0.16.3
Provides: bundled(golang(cloud.google.com/go/auth/oauth2adapt)) = v0.2.8
Provides: bundled(golang(cloud.google.com/go/compute/metadata)) = v0.7.0
Provides: bundled(golang(cloud.google.com/go/iam)) = v1.5.2
Provides: bundled(golang(cloud.google.com/go/kms)) = v1.22.0
Provides: bundled(golang(cloud.google.com/go/longrunning)) = v0.6.7
Provides: bundled(golang(cloud.google.com/go/monitoring)) = v1.24.2
Provides: bundled(golang(dario.cat/mergo)) = v1.0.1
Provides: bundled(golang(filippo.io/edwards25519)) = v1.1.0
Provides: bundled(golang(github.com/Azure/azure_sdk_for_go)) = v67.2.0+incompatible
Provides: bundled(golang(github.com/Azure/azure_sdk_for_go/sdk/azcore)) = v1.11.1
Provides: bundled(golang(github.com/Azure/azure_sdk_for_go/sdk/azidentity)) = v1.6.0
Provides: bundled(golang(github.com/Azure/azure_sdk_for_go/sdk/internal)) = v1.8.0
Provides: bundled(golang(github.com/Azure/azure_sdk_for_go/sdk/keyvault/azkeys)) = v0.10.0
Provides: bundled(golang(github.com/Azure/azure_sdk_for_go/sdk/keyvault/internal)) = v0.7.1
Provides: bundled(golang(github.com/Azure/go_ansiterm)) = v0.0.0_20230124172434_306776ec8161
Provides: bundled(golang(github.com/Azure/go_autorest)) = v14.2.0+incompatible
Provides: bundled(golang(github.com/Azure/go_autorest/autorest)) = v0.11.29
Provides: bundled(golang(github.com/Azure/go_autorest/autorest/adal)) = v0.9.22
Provides: bundled(golang(github.com/Azure/go_autorest/autorest/azure/auth)) = v0.5.12
Provides: bundled(golang(github.com/Azure/go_autorest/autorest/azure/cli)) = v0.4.5
Provides: bundled(golang(github.com/Azure/go_autorest/autorest/date)) = v0.3.0
Provides: bundled(golang(github.com/Azure/go_autorest/autorest/to)) = v0.4.0
Provides: bundled(golang(github.com/Azure/go_autorest/autorest/validation)) = v0.3.1
Provides: bundled(golang(github.com/Azure/go_autorest/logger)) = v0.2.1
Provides: bundled(golang(github.com/Azure/go_autorest/tracing)) = v0.6.0
Provides: bundled(golang(github.com/Azure/go_ntlmssp)) = v0.0.0_20221128193559_754e69321358
Provides: bundled(golang(github.com/AzureAD/microsoft_authentication_library_for_go)) = v1.2.2
Provides: bundled(golang(github.com/BurntSushi/toml)) = v1.5.0
Provides: bundled(golang(github.com/DataDog/datadog_go)) = v3.2.0+incompatible
Provides: bundled(golang(github.com/Jeffail/gabs/v2)) = v2.1.0
Provides: bundled(golang(github.com/Masterminds/goutils)) = v1.1.1
Provides: bundled(golang(github.com/Masterminds/semver/v3)) = v3.3.1
Provides: bundled(golang(github.com/Masterminds/sprig/v3)) = v3.2.3
Provides: bundled(golang(github.com/Microsoft/go_winio)) = v0.6.2
Provides: bundled(golang(github.com/Nvveen/Gotty)) = v0.0.0_20120604004816_cd527374f1e5
Provides: bundled(golang(github.com/ProtonMail/go_crypto)) = v1.3.0
Provides: bundled(golang(github.com/agext/levenshtein)) = v1.2.1
Provides: bundled(golang(github.com/aliyun/alibaba_cloud_sdk_go)) = v1.62.301
Provides: bundled(golang(github.com/antlr4_go/antlr/v4)) = v4.13.0
Provides: bundled(golang(github.com/apparentlymart/go_textseg/v13)) = v13.0.0
Provides: bundled(golang(github.com/apparentlymart/go_textseg/v15)) = v15.0.0
Provides: bundled(golang(github.com/armon/go_metrics)) = v0.4.1
Provides: bundled(golang(github.com/armon/go_radix)) = v1.0.0
Provides: bundled(golang(github.com/asaskevich/govalidator)) = v0.0.0_20230301143203_a9d515a09cc2
Provides: bundled(golang(github.com/aws/aws_sdk_go)) = v1.55.6
Provides: bundled(golang(github.com/beorn7/perks)) = v1.0.1
Provides: bundled(golang(github.com/bgentry/speakeasy)) = v0.1.0
Provides: bundled(golang(github.com/boombuler/barcode)) = v1.0.1
Provides: bundled(golang(github.com/caddyserver/certmagic)) = v0.24.0
Provides: bundled(golang(github.com/caddyserver/zerossl)) = v0.1.3
Provides: bundled(golang(github.com/cenkalti/backoff/v4)) = v4.3.0
Provides: bundled(golang(github.com/cespare/xxhash/v2)) = v2.3.0
Provides: bundled(golang(github.com/circonus_labs/circonus_gometrics)) = v2.3.1+incompatible
Provides: bundled(golang(github.com/circonus_labs/circonusllhist)) = v0.1.3
Provides: bundled(golang(github.com/cloudflare/circl)) = v1.6.1
Provides: bundled(golang(github.com/containerd/continuity)) = v0.4.5
Provides: bundled(golang(github.com/containerd/errdefs)) = v1.0.0
Provides: bundled(golang(github.com/containerd/errdefs/pkg)) = v0.3.0
Provides: bundled(golang(github.com/containerd/log)) = v0.1.0
Provides: bundled(golang(github.com/coreos/go_oidc/v3)) = v3.11.0
Provides: bundled(golang(github.com/coreos/go_systemd/v22)) = v22.5.0
Provides: bundled(golang(github.com/davecgh/go_spew)) = v1.1.2_0.20180830191138_d8f796af33cc
Provides: bundled(golang(github.com/denverdino/aliyungo)) = v0.0.0_20190125010748_a747050bb1ba
Provides: bundled(golang(github.com/digitalocean/godo)) = v1.7.5
Provides: bundled(golang(github.com/dimchansky/utfbom)) = v1.1.1
Provides: bundled(golang(github.com/distribution/reference)) = v0.6.0
Provides: bundled(golang(github.com/docker/cli)) = v28.3.3+incompatible
Provides: bundled(golang(github.com/docker/docker)) = v28.3.3+incompatible
Provides: bundled(golang(github.com/docker/go_connections)) = v0.5.0
Provides: bundled(golang(github.com/docker/go_units)) = v0.5.0
Provides: bundled(golang(github.com/duosecurity/duo_api_golang)) = v0.0.0_20190308151101_6c680f768e74
Provides: bundled(golang(github.com/dustin/go_humanize)) = v1.0.1
Provides: bundled(golang(github.com/ebitengine/purego)) = v0.8.4
Provides: bundled(golang(github.com/emicklei/go_restful/v3)) = v3.11.0
Provides: bundled(golang(github.com/evanphx/json_patch/v5)) = v5.6.0
Provides: bundled(golang(github.com/fatih/color)) = v1.18.0
Provides: bundled(golang(github.com/fatih/structs)) = v1.1.0
Provides: bundled(golang(github.com/felixge/httpsnoop)) = v1.0.4
Provides: bundled(golang(github.com/fxamacker/cbor/v2)) = v2.7.0
Provides: bundled(golang(github.com/gammazero/deque)) = v0.2.1
Provides: bundled(golang(github.com/gammazero/workerpool)) = v1.1.3
Provides: bundled(golang(github.com/go_asn1_ber/asn1_ber)) = v1.5.7
Provides: bundled(golang(github.com/go_errors/errors)) = v1.5.1
Provides: bundled(golang(github.com/go_jose/go_jose/v3)) = v3.0.4
Provides: bundled(golang(github.com/go_jose/go_jose/v4)) = v4.1.2
Provides: bundled(golang(github.com/go_ldap/ldap/v3)) = v3.4.9
Provides: bundled(golang(github.com/go_ldap/ldif)) = v0.0.0_20200320164324_fd88d9b715b3
Provides: bundled(golang(github.com/go_logr/logr)) = v1.4.3
Provides: bundled(golang(github.com/go_logr/stdr)) = v1.2.2
Provides: bundled(golang(github.com/go_ole/go_ole)) = v1.2.6
Provides: bundled(golang(github.com/go_openapi/jsonpointer)) = v0.21.0
Provides: bundled(golang(github.com/go_openapi/jsonreference)) = v0.20.2
Provides: bundled(golang(github.com/go_openapi/swag)) = v0.23.0
Provides: bundled(golang(github.com/go_sql_driver/mysql)) = v1.9.3
Provides: bundled(golang(github.com/go_test/deep)) = v1.1.0
Provides: bundled(golang(github.com/go_viper/mapstructure/v2)) = v2.4.0
Provides: bundled(golang(github.com/gocql/gocql)) = v1.7.0
Provides: bundled(golang(github.com/gogo/protobuf)) = v1.3.2
Provides: bundled(golang(github.com/golang/protobuf)) = v1.5.4
Provides: bundled(golang(github.com/golang/snappy)) = v0.0.4
Provides: bundled(golang(github.com/golang_jwt/jwt/v4)) = v4.5.2
Provides: bundled(golang(github.com/golang_jwt/jwt/v5)) = v5.3.0
Provides: bundled(golang(github.com/google/cel_go)) = v0.26.1
Provides: bundled(golang(github.com/google/gnostic_models)) = v0.6.9
Provides: bundled(golang(github.com/google/go_cmp)) = v0.7.0
Provides: bundled(golang(github.com/google/go_metrics_stackdriver)) = v0.2.0
Provides: bundled(golang(github.com/google/go_querystring)) = v1.1.0
Provides: bundled(golang(github.com/google/pprof)) = v0.0.0_20250607225305_033d6d78b36a
Provides: bundled(golang(github.com/google/s2a_go)) = v0.1.9
Provides: bundled(golang(github.com/google/shlex)) = v0.0.0_20191202100458_e7afc7fbc510
Provides: bundled(golang(github.com/google/uuid)) = v1.6.0
Provides: bundled(golang(github.com/googleapis/enterprise_certificate_proxy)) = v0.3.6
Provides: bundled(golang(github.com/googleapis/gax_go/v2)) = v2.15.0
Provides: bundled(golang(github.com/gophercloud/gophercloud)) = v0.1.0
Provides: bundled(golang(github.com/gorilla/websocket)) = v1.5.4_0.20250319132907_e064f32e3674
Provides: bundled(golang(github.com/grpc_ecosystem/grpc_gateway/v2)) = v2.24.0
Provides: bundled(golang(github.com/hailocab/go_hostpool)) = v0.0.0_20160125115350_e80d13ce29ed
Provides: bundled(golang(github.com/hashicorp/cap)) = v0.10.0
Provides: bundled(golang(github.com/hashicorp/cli)) = v1.1.7
Provides: bundled(golang(github.com/hashicorp/consul/sdk)) = v0.14.0
Provides: bundled(golang(github.com/hashicorp/errwrap)) = v1.1.0
Provides: bundled(golang(github.com/hashicorp/go_cleanhttp)) = v0.5.2
Provides: bundled(golang(github.com/hashicorp/go_discover)) = v0.0.0_20210818145131_c573d69da192
Provides: bundled(golang(github.com/hashicorp/go_hclog)) = v1.6.3
Provides: bundled(golang(github.com/hashicorp/go_immutable_radix)) = v1.3.1
Provides: bundled(golang(github.com/hashicorp/go_memdb)) = v1.3.5
Provides: bundled(golang(github.com/hashicorp/go_metrics)) = v0.5.4
Provides: bundled(golang(github.com/hashicorp/go_msgpack)) = v1.1.5
Provides: bundled(golang(github.com/hashicorp/go_msgpack/v2)) = v2.1.2
Provides: bundled(golang(github.com/hashicorp/go_multierror)) = v1.1.1
Provides: bundled(golang(github.com/hashicorp/go_plugin)) = v1.7.0
Provides: bundled(golang(github.com/hashicorp/go_raftchunking)) = v0.7.1
Provides: bundled(golang(github.com/hashicorp/go_retryablehttp)) = v0.7.8
Provides: bundled(golang(github.com/hashicorp/go_rootcerts)) = v1.0.2
Provides: bundled(golang(github.com/hashicorp/go_secure_stdlib/awsutil)) = v0.3.0
Provides: bundled(golang(github.com/hashicorp/go_secure_stdlib/base62)) = v0.1.2
Provides: bundled(golang(github.com/hashicorp/go_secure_stdlib/fileutil)) = v0.1.0
Provides: bundled(golang(github.com/hashicorp/go_secure_stdlib/gatedwriter)) = v0.1.1
Provides: bundled(golang(github.com/hashicorp/go_secure_stdlib/kv_builder)) = v0.1.2
Provides: bundled(golang(github.com/hashicorp/go_secure_stdlib/mlock)) = v0.1.3
Provides: bundled(golang(github.com/hashicorp/go_secure_stdlib/nonceutil)) = v0.1.0
Provides: bundled(golang(github.com/hashicorp/go_secure_stdlib/parseutil)) = v0.2.0
Provides: bundled(golang(github.com/hashicorp/go_secure_stdlib/password)) = v0.1.4
Provides: bundled(golang(github.com/hashicorp/go_secure_stdlib/reloadutil)) = v0.1.1
Provides: bundled(golang(github.com/hashicorp/go_secure_stdlib/strutil)) = v0.1.2
Provides: bundled(golang(github.com/hashicorp/go_secure_stdlib/tlsutil)) = v0.1.3
Provides: bundled(golang(github.com/hashicorp/go_sockaddr)) = v1.0.7
Provides: bundled(golang(github.com/hashicorp/go_syslog)) = v1.0.0
Provides: bundled(golang(github.com/hashicorp/go_uuid)) = v1.0.3
Provides: bundled(golang(github.com/hashicorp/go_version)) = v1.7.0
Provides: bundled(golang(github.com/hashicorp/golang_lru)) = v0.5.4
Provides: bundled(golang(github.com/hashicorp/golang_lru/v2)) = v2.0.7
Provides: bundled(golang(github.com/hashicorp/hcl)) = v1.0.1_vault_5
Provides: bundled(golang(github.com/hashicorp/hcl/v2)) = v2.23.0
Provides: bundled(golang(github.com/hashicorp/logutils)) = v1.0.0
Provides: bundled(golang(github.com/hashicorp/mdns)) = v1.0.4
Provides: bundled(golang(github.com/hashicorp/raft)) = v1.7.3
Provides: bundled(golang(github.com/hashicorp/raft_autopilot)) = v0.3.0
Provides: bundled(golang(github.com/hashicorp/raft_boltdb/v2)) = v2.0.0_20210421194847_a7e34179d62c
Provides: bundled(golang(github.com/hashicorp/raft_snapshot)) = v1.0.4
Provides: bundled(golang(github.com/hashicorp/vault_plugin_mock)) = v0.19.13
Provides: bundled(golang(github.com/hashicorp/vic)) = v1.5.1_0.20190403131502_bbfe86ec9443
Provides: bundled(golang(github.com/hashicorp/yamux)) = v0.1.2
Provides: bundled(golang(github.com/huandu/xstrings)) = v1.4.0
Provides: bundled(golang(github.com/imdario/mergo)) = v0.3.15
Provides: bundled(golang(github.com/influxdata/influxdb1_client)) = v0.0.0_20200827194710_b269163b24ab
Provides: bundled(golang(github.com/jackc/pgpassfile)) = v1.0.0
Provides: bundled(golang(github.com/jackc/pgservicefile)) = v0.0.0_20240606120523_5a60cdf6a761
Provides: bundled(golang(github.com/jackc/pgx/v5)) = v5.7.5
Provides: bundled(golang(github.com/jackc/puddle/v2)) = v2.2.2
Provides: bundled(golang(github.com/jcmturner/aescts/v2)) = v2.0.0
Provides: bundled(golang(github.com/jcmturner/dnsutils/v2)) = v2.0.0
Provides: bundled(golang(github.com/jcmturner/gofork)) = v1.7.6
Provides: bundled(golang(github.com/jcmturner/goidentity/v6)) = v6.0.1
Provides: bundled(golang(github.com/jcmturner/gokrb5/v8)) = v8.4.4
Provides: bundled(golang(github.com/jcmturner/rpc/v2)) = v2.0.3
Provides: bundled(golang(github.com/jefferai/isbadcipher)) = v0.0.0_20190226160619_51d2077c035f
Provides: bundled(golang(github.com/jefferai/jsonx)) = v1.0.1
Provides: bundled(golang(github.com/jmespath/go_jmespath)) = v0.4.0
Provides: bundled(golang(github.com/josharian/intern)) = v1.0.0
Provides: bundled(golang(github.com/joyent/triton_go)) = v1.7.1_0.20200416154420_6801d15b779f
Provides: bundled(golang(github.com/json_iterator/go)) = v1.1.12
Provides: bundled(golang(github.com/kelseyhightower/envconfig)) = v1.4.0
Provides: bundled(golang(github.com/klauspost/compress)) = v1.18.0
Provides: bundled(golang(github.com/klauspost/cpuid/v2)) = v2.2.10
Provides: bundled(golang(github.com/kr/pretty)) = v0.3.1
Provides: bundled(golang(github.com/kr/text)) = v0.2.0
Provides: bundled(golang(github.com/kylelemons/godebug)) = v1.1.0
Provides: bundled(golang(github.com/libdns/libdns)) = v1.0.0
Provides: bundled(golang(github.com/linode/linodego)) = v0.7.1
Provides: bundled(golang(github.com/lufia/plan9stats)) = v0.0.0_20211012122336_39d0f177ccd0
Provides: bundled(golang(github.com/mailru/easyjson)) = v0.7.7
Provides: bundled(golang(github.com/mattn/go_colorable)) = v0.1.14
Provides: bundled(golang(github.com/mattn/go_isatty)) = v0.0.20
Provides: bundled(golang(github.com/mediocregopher/radix/v4)) = v4.1.4
Provides: bundled(golang(github.com/mholt/acmez/v3)) = v3.1.2
Provides: bundled(golang(github.com/michaelklishin/rabbit_hole/v3)) = v3.1.0
Provides: bundled(golang(github.com/miekg/dns)) = v1.1.63
Provides: bundled(golang(github.com/miekg/pkcs11)) = v1.1.2_0.20231115102856_9078ad6b9d4b
Provides: bundled(golang(github.com/mitchellh/copystructure)) = v1.2.0
Provides: bundled(golang(github.com/mitchellh/go_homedir)) = v1.1.0
Provides: bundled(golang(github.com/mitchellh/go_testing_interface)) = v1.14.1
Provides: bundled(golang(github.com/mitchellh/go_wordwrap)) = v1.0.1
Provides: bundled(golang(github.com/mitchellh/mapstructure)) = v1.5.0
Provides: bundled(golang(github.com/mitchellh/pointerstructure)) = v1.2.1
Provides: bundled(golang(github.com/mitchellh/reflectwalk)) = v1.0.2
Provides: bundled(golang(github.com/moby/docker_image_spec)) = v1.3.1
Provides: bundled(golang(github.com/moby/go_archive)) = v0.1.0
Provides: bundled(golang(github.com/moby/patternmatcher)) = v0.6.0
Provides: bundled(golang(github.com/moby/spdystream)) = v0.5.0
Provides: bundled(golang(github.com/moby/sys/sequential)) = v0.6.0
Provides: bundled(golang(github.com/moby/sys/user)) = v0.4.0
Provides: bundled(golang(github.com/moby/sys/userns)) = v0.1.0
Provides: bundled(golang(github.com/moby/term)) = v0.5.0
Provides: bundled(golang(github.com/modern_go/concurrent)) = v0.0.0_20180306012644_bacd9c7ef1dd
Provides: bundled(golang(github.com/modern_go/reflect2)) = v1.0.2
Provides: bundled(golang(github.com/munnerz/goautoneg)) = v0.0.0_20191010083416_a7dc8b61c822
Provides: bundled(golang(github.com/mxk/go_flowrate)) = v0.0.0_20140419014527_cca7078d478f
Provides: bundled(golang(github.com/natefinch/atomic)) = v1.0.1
Provides: bundled(golang(github.com/nicolai86/scaleway_sdk)) = v1.10.2_0.20180628010248_798f60e20bb2
Provides: bundled(golang(github.com/oklog/run)) = v1.1.0
Provides: bundled(golang(github.com/okta/okta_sdk_golang/v2)) = v2.20.0
Provides: bundled(golang(github.com/onsi/ginkgo/v2)) = v2.23.4
Provides: bundled(golang(github.com/onsi/gomega)) = v1.37.0
Provides: bundled(golang(github.com/openbao/go_kms_wrapping/entropy/v2)) = v2.1.0
Provides: bundled(golang(github.com/openbao/go_kms_wrapping/v2)) = v2.5.0
Provides: bundled(golang(github.com/openbao/go_kms_wrapping/wrappers/aead/v2)) = v2.2.0
Provides: bundled(golang(github.com/openbao/go_kms_wrapping/wrappers/alicloudkms/v2)) = v2.2.0
Provides: bundled(golang(github.com/openbao/go_kms_wrapping/wrappers/awskms/v2)) = v2.3.0
Provides: bundled(golang(github.com/openbao/go_kms_wrapping/wrappers/azurekeyvault/v2)) = v2.2.0
Provides: bundled(golang(github.com/openbao/go_kms_wrapping/wrappers/gcpckms/v2)) = v2.2.0
Provides: bundled(golang(github.com/openbao/go_kms_wrapping/wrappers/kmip/v2)) = v2.1.0
Provides: bundled(golang(github.com/openbao/go_kms_wrapping/wrappers/ocikms/v2)) = v2.2.0
Provides: bundled(golang(github.com/openbao/go_kms_wrapping/wrappers/pkcs11/v2)) = v2.4.0
Provides: bundled(golang(github.com/openbao/go_kms_wrapping/wrappers/static/v2)) = v2.0.0
Provides: bundled(golang(github.com/openbao/go_kms_wrapping/wrappers/transit/v2)) = v2.6.0
Provides: bundled(golang(github.com/openbao/openbao/api/auth/approle/v2)) = v2.0.0
Provides: bundled(golang(github.com/openbao/openbao/api/auth/kubernetes/v2)) = v2.0.1
Provides: bundled(golang(github.com/openbao/openbao/api/auth/userpass/v2)) = v2.0.0
Provides: bundled(golang(github.com/openbao/openbao/api/v2)) = v2.4.0
Provides: bundled(golang(github.com/openbao/openbao/sdk/v2)) = v2.4.0
Provides: bundled(golang(github.com/openbao/openbao_template)) = v1.0.1
Provides: bundled(golang(github.com/opencontainers/go_digest)) = v1.0.0
Provides: bundled(golang(github.com/opencontainers/image_spec)) = v1.1.0
Provides: bundled(golang(github.com/opencontainers/runc)) = v1.2.3
Provides: bundled(golang(github.com/opentracing/opentracing_go)) = v1.2.1_0.20220228012449_10b1cf09e00b
Provides: bundled(golang(github.com/oracle/oci_go_sdk/v60)) = v60.0.0
Provides: bundled(golang(github.com/ory/dockertest/v3)) = v3.12.0
Provides: bundled(golang(github.com/ovh/kmip_go)) = v0.3.3
Provides: bundled(golang(github.com/packethost/packngo)) = v0.1.1_0.20180711074735_b9cb5096f54c
Provides: bundled(golang(github.com/patrickmn/go_cache)) = v2.1.0+incompatible
Provides: bundled(golang(github.com/petermattis/goid)) = v0.0.0_20250813065127_a731cc31b4fe
Provides: bundled(golang(github.com/pierrec/lz4)) = v2.6.1+incompatible
Provides: bundled(golang(github.com/pires/go_proxyproto)) = v0.8.1
Provides: bundled(golang(github.com/pkg/browser)) = v0.0.0_20240102092130_5ac0b6a4141c
Provides: bundled(golang(github.com/pkg/errors)) = v0.9.1
Provides: bundled(golang(github.com/pmezard/go_difflib)) = v1.0.1_0.20181226105442_5d4384ee4fb2
Provides: bundled(golang(github.com/posener/complete)) = v1.2.3
Provides: bundled(golang(github.com/power_devops/perfstat)) = v0.0.0_20210106213030_5aafc221ea8c
Provides: bundled(golang(github.com/pquerna/otp)) = v1.5.0
Provides: bundled(golang(github.com/prometheus/client_golang)) = v1.22.0
Provides: bundled(golang(github.com/prometheus/client_model)) = v0.6.1
Provides: bundled(golang(github.com/prometheus/common)) = v0.62.0
Provides: bundled(golang(github.com/prometheus/procfs)) = v0.15.1
Provides: bundled(golang(github.com/rboyer/safeio)) = v0.2.3
Provides: bundled(golang(github.com/renier/xmlrpc)) = v0.0.0_20170708154548_ce4a1a486c03
Provides: bundled(golang(github.com/rogpeppe/go_internal)) = v1.14.1
Provides: bundled(golang(github.com/ryanuber/columnize)) = v2.1.2+incompatible
Provides: bundled(golang(github.com/ryanuber/go_glob)) = v1.0.0
Provides: bundled(golang(github.com/sasha_s/go_deadlock)) = v0.3.5
Provides: bundled(golang(github.com/sethvargo/go_limiter)) = v1.0.0
Provides: bundled(golang(github.com/shirou/gopsutil/v4)) = v4.25.6
Provides: bundled(golang(github.com/shopspring/decimal)) = v1.3.1
Provides: bundled(golang(github.com/sirupsen/logrus)) = v1.9.3
Provides: bundled(golang(github.com/softlayer/softlayer_go)) = v0.0.0_20180806151055_260589d94c7d
Provides: bundled(golang(github.com/sony/gobreaker)) = v0.5.0
Provides: bundled(golang(github.com/spf13/cast)) = v1.5.1
Provides: bundled(golang(github.com/spf13/pflag)) = v1.0.6
Provides: bundled(golang(github.com/stoewer/go_strcase)) = v1.3.0
Provides: bundled(golang(github.com/stretchr/objx)) = v0.5.2
Provides: bundled(golang(github.com/stretchr/testify)) = v1.10.0
Provides: bundled(golang(github.com/tencentcloud/tencentcloud_sdk_go)) = v1.0.162
Provides: bundled(golang(github.com/tilinna/clock)) = v1.0.2
Provides: bundled(golang(github.com/tink_crypto/tink_go/v2)) = v2.4.0
Provides: bundled(golang(github.com/tklauser/go_sysconf)) = v0.3.12
Provides: bundled(golang(github.com/tklauser/numcpus)) = v0.6.1
Provides: bundled(golang(github.com/tv42/httpunix)) = v0.0.0_20191220191345_2ba4b9c3382c
Provides: bundled(golang(github.com/vmware/govmomi)) = v0.18.0
Provides: bundled(golang(github.com/x448/float16)) = v0.8.4
Provides: bundled(golang(github.com/xeipuuv/gojsonpointer)) = v0.0.0_20190905194746_02993c407bfb
Provides: bundled(golang(github.com/xeipuuv/gojsonreference)) = v0.0.0_20180127040603_bd5ef7bd5415
Provides: bundled(golang(github.com/xeipuuv/gojsonschema)) = v1.2.0
Provides: bundled(golang(github.com/yeqown/go_qrcode/v2)) = v2.2.5
Provides: bundled(golang(github.com/yeqown/reedsolomon)) = v1.0.0
Provides: bundled(golang(github.com/yusufpapurcu/wmi)) = v1.2.4
Provides: bundled(golang(github.com/zclconf/go_cty)) = v1.13.0
Provides: bundled(golang(github.com/zeebo/blake3)) = v0.2.4
Provides: bundled(golang(go.etcd.io/bbolt)) = v1.4.3
Provides: bundled(golang(go.opentelemetry.io/auto/sdk)) = v1.1.0
Provides: bundled(golang(go.opentelemetry.io/contrib/instrumentation/google.golang.org/grpc/otelgrpc)) = v0.61.0
Provides: bundled(golang(go.opentelemetry.io/contrib/instrumentation/net/http/otelhttp)) = v0.61.0
Provides: bundled(golang(go.opentelemetry.io/otel)) = v1.37.0
Provides: bundled(golang(go.opentelemetry.io/otel/metric)) = v1.37.0
Provides: bundled(golang(go.opentelemetry.io/otel/sdk)) = v1.37.0
Provides: bundled(golang(go.opentelemetry.io/otel/trace)) = v1.37.0
Provides: bundled(golang(go.uber.org/atomic)) = v1.11.0
Provides: bundled(golang(go.uber.org/goleak)) = v1.3.0
Provides: bundled(golang(go.uber.org/multierr)) = v1.11.0
Provides: bundled(golang(go.uber.org/zap)) = v1.27.0
Provides: bundled(golang(go.uber.org/zap/exp)) = v0.3.0
Provides: bundled(golang(golang.org/x/crypto)) = v0.41.0
Provides: bundled(golang(golang.org/x/exp)) = v0.0.0_20250819193227_8b4c13bb791b
Provides: bundled(golang(golang.org/x/mod)) = v0.27.0
Provides: bundled(golang(golang.org/x/net)) = v0.43.0
Provides: bundled(golang(golang.org/x/oauth2)) = v0.30.0
Provides: bundled(golang(golang.org/x/sync)) = v0.16.0
Provides: bundled(golang(golang.org/x/sys)) = v0.35.0
Provides: bundled(golang(golang.org/x/term)) = v0.34.0
Provides: bundled(golang(golang.org/x/text)) = v0.28.0
Provides: bundled(golang(golang.org/x/time)) = v0.12.0
Provides: bundled(golang(golang.org/x/tools)) = v0.36.0
Provides: bundled(golang(google.golang.org/api)) = v0.246.0
Provides: bundled(golang(google.golang.org/genproto)) = v0.0.0_20250603155806_513f23925822
Provides: bundled(golang(google.golang.org/genproto/googleapis/api)) = v0.0.0_20250707201910_8d1bb00bc6a7
Provides: bundled(golang(google.golang.org/genproto/googleapis/rpc)) = v0.0.0_20250728155136_f173205681a0
Provides: bundled(golang(google.golang.org/grpc)) = v1.75.0
Provides: bundled(golang(google.golang.org/protobuf)) = v1.36.6
Provides: bundled(golang(gopkg.in/evanphx/json_patch.v4)) = v4.12.0
Provides: bundled(golang(gopkg.in/inf.v0)) = v0.9.1
Provides: bundled(golang(gopkg.in/ini.v1)) = v1.67.0
Provides: bundled(golang(gopkg.in/jcmturner/goidentity.v3)) = v3.0.0
Provides: bundled(golang(gopkg.in/resty.v1)) = v1.12.0
Provides: bundled(golang(gopkg.in/yaml.v2)) = v2.4.0
Provides: bundled(golang(gopkg.in/yaml.v3)) = v3.0.1
Provides: bundled(golang(k8s.io/api)) = v0.33.0
Provides: bundled(golang(k8s.io/apimachinery)) = v0.33.0
Provides: bundled(golang(k8s.io/client_go)) = v0.33.0
Provides: bundled(golang(k8s.io/klog/v2)) = v2.130.1
Provides: bundled(golang(k8s.io/kube_openapi)) = v0.0.0_20250318190949_c8a335a9a2ff
Provides: bundled(golang(k8s.io/utils)) = v0.0.0_20241104100929_3ea5e8cea738
Provides: bundled(golang(layeh.com/radius)) = v0.0.0_20230922032716_6579be8edf5d
Provides: bundled(golang(sigs.k8s.io/json)) = v0.0.0_20241010143419_9aa6b5e7a4b3
Provides: bundled(golang(sigs.k8s.io/randfill)) = v1.0.0
Provides: bundled(golang(sigs.k8s.io/structured_merge_diff/v4)) = v4.6.0
Provides: bundled(golang(sigs.k8s.io/yaml)) = v1.4.0

%description
Openbao secures, stores, and tightly controls access to tokens, passwords,
certificates, API keys, and other secrets in modern computing. Openbao handles
leasing, key revocation, key rolling, and auditing. Through a unified API, users
can access an encrypted Key/Value store and network encryption-as-a-service, or
generate AWS IAM/STS credentials, SQL/NoSQL databases, X.509 certificates, SSH
credentials, and more.

%package %{oldname}-compat
Summary: Vault-compatible command and service
Requires: %{name} = %{version}-%{release}
Provides: %{oldname} = %{version}-%{release}
Obsoletes: %{oldname} < 2.0

%description %{oldname}-compat
Provides a compatibility layer on top of OpenBao to emulate a Hashicorp
Vault package.

%prep
%setup -q -T -b 1 -n %{name}-rpm-%{package_version}
%setup -q -n %{name}-dist-%{package_version}
%autopatch

%build
# starts out in %%{name}-dist-%%{package_version} directory

# this prevents it from complaining that ui assets are too old
touch http/web_ui/index.html

GO_BUILDTAGS="ui"
GO_LDFLAGS="-X github.com/%{name}/%{name}/version.fullVersion=%{version}-%{release}"
GO_LDFLAGS+=" -X github.com/%{name}/%{name}/version.GitCommit="
BUILD_DATE="$(date -d "@${SOURCE_DATE_EPOCH:-$(date +%s)}" +%Y-%m-%d)"
GO_LDFLAGS+=" -X github.com/%{name}/%{name}/version.BuildDate=${BUILD_DATE}"

%if 0%{?el8}
# Define the %%gobuild macro on el8 because it is outdated and doesn't work.

GO_LDFLAGS+=" -B gobuildid"
GO_BUILDTAGS+=" rpm_crashtraceback libtrust_openssl"
GO_LDFLAGS+=" -linkmode=external -compressdwarf=false"
GO_LDFLAGS+=" -extldflags '%__global_ldflags'"

%define gobuild go build -compiler gc -buildmode pie -ldflags "${GO_LDFLAGS}" -tags "${GO_BUILDTAGS}"

%else
# Use more modern gobuild macro.

# Except for el9, this defaults to not use go modules.  Enable go modules
# because it is allowed and is a simpler option than making the additional go
# macros required to manage the non-module form on el8 where they're missing.
%global gomodulesmode GO111MODULE=on

%if 0%{?el9}
# the el9 gobuild macro only accepts LDFLAGS, not GO_LDFLAGS
LDFLAGS=${GO_LDFLAGS}
%endif
%endif

%if "%{?go_debug}" != ""
# add debugging & testing flags
GO_BUILD_GCFLAGS="all=-N -l"
GO_LDFLAGS+=" -X github.com/%{name}/%{name}/version.VersionMetadata=testonly"
# openbao documentation says testonly should not be used for production builds
GO_BUILDTAGS+=" testonly"
%gobuild -o bin/bao -gcflags "${GO_BUILD_GCFLAGS}"
%else
%gobuild -o bin/bao
%endif


%install
# starts out in %%{name}-dist-%%{package_version} directory
mkdir -p %{buildroot}%{_bindir}/
cp -p bin/bao %{buildroot}%{_bindir}/
ln -s bao %{buildroot}%{_bindir}/%{oldname}

cd ../%{name}-rpm-%{package_version}
mkdir -p %{buildroot}%{_sysconfdir}/%{name}.d/tls
cp -p %{name}.hcl %{buildroot}%{_sysconfdir}/%{name}.d
ln -s %{name}.d %{buildroot}%{_sysconfdir}/%{oldname}.d

mkdir -p %{buildroot}%{_datadir}/man/man1
gzip -c bao.1 >%{buildroot}%{_datadir}/man/man1/bao.1.gz
ln -s bao.1 %{buildroot}%{_datadir}/man/man1/%{oldname}.1.gz

mkdir -p %{buildroot}%{_sharedstatedir}/%{name}
ln -s %{name} %{buildroot}%{_sharedstatedir}/%{oldname}

mkdir -p %{buildroot}%{_unitdir}
cp -p %{name}.service %{buildroot}%{_unitdir}
ln -s %{name}.service %{buildroot}%{_unitdir}/%{oldname}.service

mkdir -p %{buildroot}%{_sysusersdir}
cp %{name}.conf %{buildroot}%{_sysusersdir}/%{name}.conf

#
# NOTE: we can't run the standard go tests because some of them
# require network access.
#

%pre
%sysusers_create_compat %{name}.conf

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%files
%verify(not caps) %{_bindir}/bao
%dir %{_sysconfdir}/%{name}.d
%attr(0700,%{name},%{name}) %dir %{_sysconfdir}/%{name}.d/tls
%config(noreplace) %{_sysconfdir}/%{name}.d/%{name}.hcl
%attr(0700,%{name},%{name}) %dir %{_sharedstatedir}/%{name}
%{_unitdir}/%{name}.service
%{_sysusersdir}/%{name}.conf
%{_datadir}/man/man1/bao.1.gz
%license LICENSE
%license LICENSE_DEPENDENCIES.md
%doc README.md
%doc CHANGELOG.md

%files %{oldname}-compat
%{_bindir}/%{oldname}
%{_sysconfdir}/%{oldname}.d
%{_sharedstatedir}/%{oldname}
%{_datadir}/man/man1/%{oldname}.1.gz
%{_unitdir}/%{oldname}.service

%changelog
%autochangelog
