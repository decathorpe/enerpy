Summary: python package for gaussian error propagation
Name: enerpy
Version: 0.0.1
Release: 1%{?dist}
License: GPLv2
URL: http://github.com/defathorpe/enerpy

Source0: enerpy-0.0.1.tar.gz

BuildArchitectures: noarch

BuildRequires: python3-devel

Requires: python3


%description
enerpy is a python package for gaussian error propagation


%prep
%setup -q -n enerpy-0.0.1


%build


%install
rm -rf $RPM_BUILD_ROOT
%{__python3} ./setup.py install --root=$RPM_BUILD_ROOT --install-lib=%{python3_sitelib}


%clean
rm -rf $RPM_BUILD_ROOT


%check


%post
%postun


%files



%changelog

