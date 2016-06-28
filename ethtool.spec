#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : ethtool
Version  : 4.6
Release  : 13
URL      : http://ftp.kernel.org/pub/software/network/ethtool/ethtool-4.6.tar.xz
Source0  : http://ftp.kernel.org/pub/software/network/ethtool/ethtool-4.6.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: ethtool-bin
Requires: ethtool-doc

%description
This utility allows querying and changing settings such as speed,
port, auto-negotiation, PCI locations and checksum offload on many
network devices, especially Ethernet devices.

%package bin
Summary: bin components for the ethtool package.
Group: Binaries

%description bin
bin components for the ethtool package.


%package doc
Summary: doc components for the ethtool package.
Group: Documentation

%description doc
doc components for the ethtool package.


%prep
%setup -q -n ethtool-4.6

%build
export LANG=C
%configure --disable-static
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/ethtool

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man8/*
