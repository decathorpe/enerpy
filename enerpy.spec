Summary: python package for gaussian error propagation
Name: enerpy
Version: 0.0.5
Release: 1%{?dist}
License: GPLv2
URL: http://github.com/defathorpe/enerpy

Source0: enerpy-%{version}.tar.gz

BuildArchitectures: noarch

BuildRequires: python3-devel

Requires: python3


%description
enerpy is a python package for gaussian error propagation


%prep
%setup -q -n enerpy-%{version}


%build


%install
rm -rf $RPM_BUILD_ROOT
%{__python3} ./setup.py install --root=$RPM_BUILD_ROOT # --install-lib=%{python3_sitelib}


%clean
rm -rf $RPM_BUILD_ROOT


%check


%post
%postun


%files
%{python3_sitelib}/enerpy
%{python3_sitelib}/enerpy-%{version}-py3.4.egg-info

%changelog
* Tue Jun 23 2015 Fabio Valentini <decathorpe@gmail.com> - 0.0.5-1
- Bump to version 0.0.5.

* Wed Jun 17 2015 Fabio Valentini <decathorpe@gmail.com> - 0.0.4-1
- Bump version to 0.0.4.

* Mon Jun 15 2015 Fabio Valentini <decathorpe@gmail.com> - 0.0.3-3
- REALLY fix spec file.

* Mon Jun 15 2015 Fabio Valentini <decathorpe@gmail.com> - 0.0.3-2
- Fix spec file.

* Mon Jun 15 2015 Fabio Valentini <decathorpe@gmail.com> - 0.0.3-1
- Bump to version 0.0.3.

* Fri Jun 12 2015 Fabio Valentini <decathorpe@gmail.com> - 0.0.2-1
- Bump version to 0.0.2.

* Fri Jun 12 2015 Fabio Valentini <decathorpe@gmail.com> - 0.0.1-2
- Basic bugfixes.

* Thu Jun 11 2015 Fabio Valentini <decathorpe@gmail.com> - 0.0.1-1
- Initial package.


