Name:           qt5-qtwebsockets
Version:        5.5.1
Release:        1
Summary:        Qt 5 WebSockets Library
License:        LGPLv2 with exception or LGPLv3 or Qt Commercial
Url:            http://qt.digia.com
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
Requires:       %{name} = %{version}-%{release}

%description -n qt5-qtdeclarative-import-websockets
Qt 5 WebSockets Library - QML imports

%package devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description devel
Development files for %{name}

%prep
%setup -q -n %{name}-%{version}/upstream

%build
touch .git
%qmake5
make %{?_smp_mflags}

%install
%qmake5_install
# kill .la files
rm -f %{buildroot}%{_libdir}/lib*.la

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,755)
%license LICENSE.LGPLv21 LGPL_EXCEPTION.txt LICENSE.LGPLv3 LICENSE.GPLv3
%{_libdir}/libQt5WebSockets.so.*

%files -n qt5-qtdeclarative-import-websockets
%defattr(-,root,root,755)
%{_qt5_archdatadir}/qml/Qt/WebSockets/
%{_qt5_archdatadir}/qml/QtWebSockets/

%files devel
%defattr(-,root,root,755)
%{_qt5_includedir}/QtWebSockets
%{_qt5_libdir}/cmake/Qt5*
%{_qt5_libdir}/libQt5WebSockets.prl
%{_qt5_libdir}/libQt5WebSockets.so
%{_qt5_libdir}/pkgconfig/Qt5WebSockets.pc
%{_qt5_archdatadir}/mkspecs/modules/*.pri
