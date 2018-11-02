#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : ethtool
Version  : 4.19
Release  : 27
URL      : https://www.kernel.org/pub/software/network/ethtool/ethtool-4.19.tar.xz
Source0  : https://www.kernel.org/pub/software/network/ethtool/ethtool-4.19.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: ethtool-bin = %{version}-%{release}
Requires: ethtool-license = %{version}-%{release}
Requires: ethtool-man = %{version}-%{release}

%description
This utility allows querying and changing settings such as speed,
port, auto-negotiation, PCI locations and checksum offload on many
network devices, especially Ethernet devices.

%package bin
Summary: bin components for the ethtool package.
Group: Binaries
Requires: ethtool-license = %{version}-%{release}
Requires: ethtool-man = %{version}-%{release}

%description bin
bin components for the ethtool package.


%package license
Summary: license components for the ethtool package.
Group: Default

%description license
license components for the ethtool package.


%package man
Summary: man components for the ethtool package.
Group: Default

%description man
man components for the ethtool package.


%prep
%setup -q -n ethtool-4.19

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1541190493
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1541190493
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/ethtool
cp COPYING %{buildroot}/usr/share/package-licenses/ethtool/COPYING
cp LICENSE %{buildroot}/usr/share/package-licenses/ethtool/LICENSE
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/ethtool

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/ethtool/COPYING
/usr/share/package-licenses/ethtool/LICENSE

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man8/ethtool.8
