%if %{fedora} > 22
%define debug_package %{nil}
%endif

Name: enerpy
Version: 0.3.2
Release: 1%{?dist}

Summary: gaussian error propagation python3 module
License: GPLv2
URL: http://github.com/defathorpe/enerpy

Source0: enerpy-%{version}.tar.gz

BuildRequires: python3-devel

Requires: python3-enerpy

%description
enerpy is a python module for gaussian error propagation


%package -n python3-enerpy
Summary: python package for gaussian error propagation
%description -n python3-enerpy
enerpy is a python script and for gaussian error propagation.
this package contains the python3 module.


%prep
%setup -q -n enerpy-%{version}


%build
%py3_build


%install
%py3_install


%clean
rm -rf $RPM_BUILD_ROOT


%post
%postun

%post -n python3-enerpy
%postun -n python3-enerpy


%files

%files -n python3-enerpy
%{python3_sitelib}/enerpy/
%{python3_sitelib}/enerpy-%{version}-py%{python3_version}.egg-info


%changelog
* Sat Feb 20 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.2-1
- Bump version to 0.3.2.

* Thu Feb 18 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1-1
- Bump to version 0.3.1.

* Thu Feb 18 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.0-1
- Bump for version 0.3.0. Clean up spec.

* Sat Sep 26 2015 Fabio Valentini <decathorpe@gmail.com>
- Modernize spec.

* Fri Aug 14 2015 Fabio Valentini - 0.2.1-1
- Update to release 0.2.1.

* Thu Aug 13 2015 Fabio Valentini - 0.2.0-1
- Bump to version 0.2.0.

* Sat Aug 08 2015 Fabio Valentini - 0.1.1-1
- Added small documentation for new infix operators.

* Sat Aug 08 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.0-1
- Update to version 0.1.0.

* Sat Jul 11 2015 Fabio Valentini <decathorpe@gmail.com> - 0.0.7-1
- Bump to version 0.0.7.

* Thu Jul 02 2015 Fabio Valentini <decathorpe@gmail.com> - 0.0.6-1
- Bump version to 0.0.6.

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

