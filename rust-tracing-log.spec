# Generated by rust2rpm 21
%bcond_without check
%global debug_package %{nil}

%global crate tracing-log

Name:           rust-%{crate}
Version:        0.1.2
Release:        %autorelease
Summary:        Provides compatibility between `tracing` and the `log` crate

# Upstream license specification: MIT
License:        MIT
URL:            https://crates.io/crates/tracing-log
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}

BuildRequires:  rust-packaging >= 21

%global _description %{expand:
Provides compatibility between `tracing` and the `log` crate.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/LICENSE
%doc %{crate_instdir}/CHANGELOG.md
%doc %{crate_instdir}/README.md
%{crate_instdir}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+env_logger-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+env_logger-devel %{_description}

This package contains library source intended for building other packages which
use the "env_logger" feature of the "%{crate}" crate.

%files       -n %{name}+env_logger-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+log-tracer-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+log-tracer-devel %{_description}

This package contains library source intended for building other packages which
use the "log-tracer" feature of the "%{crate}" crate.

%files       -n %{name}+log-tracer-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+std-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+std-devel %{_description}

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%files       -n %{name}+std-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+trace-logger-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+trace-logger-devel %{_description}

This package contains library source intended for building other packages which
use the "trace-logger" feature of the "%{crate}" crate.

%files       -n %{name}+trace-logger-devel
%ghost %{crate_instdir}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%changelog
%autochangelog
