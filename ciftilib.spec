%global optflags %(echo %{optflags} -std=c++11)

Name:           ciftilib
Version:        1.3
Release:        1%{?dist}
Summary:        C++ Library for reading and writing CIFTI-2 and CIFTI-1 files

License:        BSD
URL:            https://github.com/Washington-University/CiftiLib
Source0:        https://github.com/Washington-University/CiftiLib/archive/v%{version}/%{name}-%{version}.tar.gz
# https://github.com/Washington-University/CiftiLib/pull/2
Patch0:         0001-use-boost-shared_ptr-to-avoid-problems-with-c-11.patch
BuildRequires:  git-core
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  libxml++-devel glibmm24-devel
BuildRequires:  boost-devel
BuildRequires:  zlib-devel

%description
%{summary}.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for %{name}.

%prep
%autosetup -n CiftiLib-%{version} -S git
rm -rf build/
mkdir -p build/
sed -i -e '/CMAKE_CXX_FLAGS/s|-W -Wall|%{optflags}|' CMakeLists.txt

%build
pushd build/
  %cmake ../ -DIGNORE_QT=TRUE
  %make_build
popd

%install
pushd build/
  %make_install
popd

%files
%license LICENSE

%files devel
%doc examples/*.cxx

%changelog
* Wed Nov 04 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 1.3-1
- Initial package
