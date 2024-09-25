# Generated by rust2rpm 26
%bcond_without check
%global debug_package %{nil}

%global crate ariadne

Name:           rust-ariadne
Version:        0.4.1
Release:        %autorelease
Summary:        Fancy diagnostics & reporting crate

License:        MIT
URL:            https://crates.io/crates/ariadne
Source:         %{crates_source}

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
A fancy diagnostics & reporting crate.}

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

%package     -n %{name}+auto-color-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+auto-color-devel %{_description}

This package contains library source intended for building other packages which
use the "auto-color" feature of the "%{crate}" crate.

%files       -n %{name}+auto-color-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+concolor-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+concolor-devel %{_description}

This package contains library source intended for building other packages which
use the "concolor" feature of the "%{crate}" crate.

%files       -n %{name}+concolor-devel
%ghost %{crate_instdir}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version} -p1
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
