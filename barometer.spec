Name:           barometer
Version:				1.0
Release:        1%{?dist}
Summary:        Scripts for Barometer deployment on using Apex

License:        GPLv2+
URL:            https://wiki.opnfv.org/display/fastpath/%{name}+Home
Source0:        https://github.com/kishoreakhila/test/%{name}-%{version}.tar.gz

BuildRequires:    python-setuptools python34-devel
Requires:         openvswitch qemu-kvm bridge-utils libguestfs-tools python34-libvirt

%description
The ability to monitor the Network Function Virtualization Infrastructure (NFVI) where
VNFs are in operation will be a key part of Service Assurance within an NFV environment,
in order to enforce SLAs or to detect violations, faults or degradation in the
performance of NFVI resources so that events and relevant metrics are reported to
higher level fault management systems.


%prep
rm -rf $RPM_BUILD_DIR/barometer
tar -xvzf $RPM_SOURCE_DIR/barometer-1.0.tar.gz

%setup


%build
make


%install
mkdir -p %{buildroot}/%{_bindir}
install -m 0755 %{name} %{buildroot}/%{_bindir}/%{name}
rm -rf $RPM_BUILD_ROOT
%make install


%files
%{_bindir}/%{name}
%doc



%changelog
