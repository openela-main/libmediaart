Name:           libmediaart
Version:        1.9.4
Release:        4%{?dist}
Summary:        Library for managing media art caches

License:        LGPLv2+
URL:            https://gitlab.gnome.org/GNOME/libmediaart
Source0:        https://download.gnome.org/sources/%{name}/1.9/%{name}-%{version}.tar.xz

BuildRequires:  pkgconfig(glib-2.0) pkgconfig(gio-2.0) pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
%if 0%{?fedora} || 0%{?rhel} > 7
# Test requires the jpeg gdk-pixbuf loader
BuildRequires:  gdk-pixbuf2-modules
%endif
BuildRequires:  vala vala-devel
BuildRequires:  dbus

%description
Library tasked with managing, extracting and handling media art caches.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package  tests
Summary:  Tests for the %{name} package
Group:    Development/Libraries
Requires: %{name}%{?_isa} = %{version}-%{release}

%description tests
The %{name}-tests package contains tests that can be used to verify
the functionality of the installed %{name} package.

%prep
%setup -q


%build
%configure --disable-static \
  --enable-gdkpixbuf \
  --disable-qt \
  --enable-installed-tests
make %{?_smp_mflags}


%install
%make_install
find $RPM_BUILD_ROOT -name '*.la' -delete -print

%check
dbus-run-session -- make check

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%license COPYING.LESSER
%doc AUTHORS NEWS
%{_libdir}/libmediaart-2.0.so.*
%{_libdir}/girepository-1.0/MediaArt-2.0.typelib

%files devel
%{_includedir}/libmediaart-2.0
%{_libdir}/libmediaart-2.0.so
%{_libdir}/pkgconfig/libmediaart-2.0.pc
%{_datadir}/gir-1.0/MediaArt-2.0.gir
%{_datadir}/gtk-doc/html/libmediaart
%{_datadir}/vala/vapi/libmediaart-2.0.vapi

%files tests
%{_libexecdir}/installed-tests/libmediaart
%{_datadir}/installed-tests


%changelog
* Tue Jul 31 2018 Debarshi Ray <rishi@fedoraproject.org> - 1.9.4-4
- Update URL

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Dec 07 2017 Merlin Mathesius <mmathesi@redhat.com> - 1.9.4-2
- Cleanup spec file conditionals

* Fri Aug 11 2017 Yanko Kaneti <yaneti@declera.com> - 1.9.4-1
- Update to 1.9.4

* Thu Aug 10 2017 Yanko Kaneti <yaneti@declera.com> - 1.9.3-1
- Update to 1.9.3

* Wed Aug  9 2017 Yanko Kaneti <yaneti@declera.com> - 1.9.2-1
- Update to 1.9.2

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jul 19 2017 Yanko Kaneti <yaneti@declera.com> - 1.9.1-2
- Drop Xvfb requirements for tests, use plain dbus-run-session

* Sun Mar  5 2017 Yanko Kaneti <yaneti@declera.com> - 1.9.1-1
- Update to 1.9.1
- Drop upstreamed patches

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Sep 22 2016 Kalev Lember <klember@redhat.com> - 1.9.0-5
- BR vala instead of obsolete vala-tools subpackage

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Yanko Kaneti <yaneti@declera.com> - 1.9.0-3
- BR: gdk-pixbuf2-modules, required by tests

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Jan 20 2015 Yanko Kaneti <yaneti@declera.com> - 1.9.0
- Update to libmediart-2.0
- Run tests

* Fri Dec 19 2014 Vadim Rutkovsky <vrutkovs@redhat.com>
- Build and package installed tests (Vadim Rutkovsky) (bug 1163431)

* Mon Sep 22 2014 Yanko Kaneti <yaneti@declera.com> - 0.7.0-1
- Update to 0.7.0

* Tue Aug 19 2014 Kalev Lember <kalevlember@gmail.com> - 0.6.0-1
- Update to 0.6.0

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jul 22 2014 Kalev Lember <kalevlember@gmail.com> - 0.4.0-3
- Rebuilt for gobject-introspection 1.41.4

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Apr  1 2014 Yanko Kaneti <yaneti@declera.com> - 0.4.0-1
- Update to 0.4.0

* Fri Mar  7 2014 Yanko Kaneti <yaneti@declera.com> - 0.3.0-1
- Update to 0.3.0. Drop upstreamed patches.

* Sat Feb  8 2014 Yanko Kaneti <yaneti@declera.com> - 0.2.0-4
- Add patches to avoid unnecessary linkage

* Sat Feb  8 2014 Yanko Kaneti <yaneti@declera.com> - 0.2.0-3
- Incorporate most changes suggested in the review (#1062686)

* Fri Feb  7 2014 Yanko Kaneti <yaneti@declera.com> - 0.2.0-2
- Qt can be ignored, its only there for systems without gdk-pixbuf

* Fri Feb  7 2014 Yanko Kaneti <yaneti@declera.com> - 0.2.0-1
- Initial attempt
