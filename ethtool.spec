#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : ethtool
Version  : 5.16
Release  : 42
URL      : https://www.kernel.org/pub/software/network/ethtool/ethtool-5.16.tar.xz
Source0  : https://www.kernel.org/pub/software/network/ethtool/ethtool-5.16.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: ethtool-bin = %{version}-%{release}
Requires: ethtool-data = %{version}-%{release}
Requires: ethtool-license = %{version}-%{release}
Requires: ethtool-man = %{version}-%{release}
BuildRequires : pkgconfig(libmnl)

%description
This utility allows querying and changing settings such as speed,
port, auto-negotiation, PCI locations and checksum offload on many
network devices, especially Ethernet devices.

%package bin
Summary: bin components for the ethtool package.
Group: Binaries
Requires: ethtool-data = %{version}-%{release}
Requires: ethtool-license = %{version}-%{release}

%description bin
bin components for the ethtool package.


%package data
Summary: data components for the ethtool package.
Group: Data

%description data
data components for the ethtool package.


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
%setup -q -n ethtool-5.16
cd %{_builddir}/ethtool-5.16

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1642604917
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1642604917
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/ethtool
cp %{_builddir}/ethtool-5.16/COPYING %{buildroot}/usr/share/package-licenses/ethtool/4cc77b90af91e615a64ae04893fdffa7939db84c
cp %{_builddir}/ethtool-5.16/LICENSE %{buildroot}/usr/share/package-licenses/ethtool/d25eb6311e5d0398a98818545298bc0fa10efab1
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/ethtool

%files data
%defattr(-,root,root,-)
/usr/share/bash-completion/completions/ethtool

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/ethtool/4cc77b90af91e615a64ae04893fdffa7939db84c
/usr/share/package-licenses/ethtool/d25eb6311e5d0398a98818545298bc0fa10efab1

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man8/ethtool.8
