Name:           qt5-qtwebsockets
Version:        5.9.5
Release:        1
Summary:        Qt 5 WebSockets Library
License:        LGPLv3
Group:          Qt/Qt
Url:            https://www.qt.io
Source:         %{name}-%{version}.tar.gz
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Quick)

%description
The QtWebSockets module implements the WebSocket protocol as specified in RFC
6455. It solely depends on Qt (no external dependencies).

%package -n qt5-qtdeclarative-import-websockets
Summary:        Qt 5 WebSockets Library - QML imports
Group:          Qt/Qt
Requires:       %{name} = %{version}-%{release}

%description -n qt5-qtdeclarative-import-websockets
Qt 5 WebSockets Library - QML imports

%package devel
Summary:        Development files for %{name}
Group:          Qt/Qt
Requires:       %{name} = %{version}-%{release}

%description devel
Development files for %{name}

%prep
%setup -q -n %{name}-%{version}

%build
touch .git
%qmake5
make %{?_smp_mflags}

%install
%qmake5_install
# Fix wrong path in pkgconfig files
find %{buildroot}%{_libdir}/pkgconfig -type f -name '*.pc' \
-exec perl -pi -e "s, -L%{_builddir}/?\S+,,g" {} \;
# Fix wrong path in prl files
find %{buildroot}%{_libdir} -type f -name '*.prl' \
-exec sed -i -e "/^QMAKE_PRL_BUILD_DIR/d;s/\(QMAKE_PRL_LIBS =\).*/\1/" {} \;
# Remove unneeded .la files
rm -f %{buildroot}/%{_libdir}/*.la

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,755)
%doc *GPL*
%{_libdir}/libQt5WebSockets.so.*

%files -n qt5-qtdeclarative-import-websockets
%defattr(-,root,root,755)
%doc *GPL*
%{_libdir}/qt5/qml/Qt/WebSockets/
%{_libdir}/qt5/qml/QtWebSockets/

%files devel
%defattr(-,root,root,755)
%doc *GPL*
%{_includedir}/qt5/QtWebSockets
%{_libdir}/cmake/Qt5*
%{_libdir}/libQt5WebSockets.prl
%{_libdir}/libQt5WebSockets.so
%{_libdir}/pkgconfig/Qt5WebSockets.pc
%{_datadir}/qt5/mkspecs/modules/*.pri
