#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xDBD2CE893E2D1C87 (cfeck@kde.org)
#
Name     : cantor
Version  : 18.12.2
Release  : 12
URL      : https://download.kde.org/stable/applications/18.12.2/src/cantor-18.12.2.tar.xz
Source0  : https://download.kde.org/stable/applications/18.12.2/src/cantor-18.12.2.tar.xz
Source99 : https://download.kde.org/stable/applications/18.12.2/src/cantor-18.12.2.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause GFDL-1.2 GPL-2.0
Requires: cantor-bin = %{version}-%{release}
Requires: cantor-data = %{version}-%{release}
Requires: cantor-lib = %{version}-%{release}
Requires: cantor-license = %{version}-%{release}
Requires: cantor-locales = %{version}-%{release}
BuildRequires : R
BuildRequires : R-dev
BuildRequires : analitza-dev
BuildRequires : attica-dev
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : docbook-xml
BuildRequires : extra-cmake-modules
BuildRequires : gmp-dev
BuildRequires : karchive-dev
BuildRequires : kauth-dev
BuildRequires : kbookmarks-dev
BuildRequires : kcodecs-dev
BuildRequires : kcompletion-dev
BuildRequires : kconfig
BuildRequires : kconfig-dev
BuildRequires : kconfigwidgets-dev
BuildRequires : kcoreaddons-dev
BuildRequires : kcrash-dev
BuildRequires : kdoctools-dev
BuildRequires : ki18n-dev
BuildRequires : kiconthemes-dev
BuildRequires : kio-dev
BuildRequires : kitemviews-dev
BuildRequires : kjobwidgets-dev
BuildRequires : knewstuff-dev
BuildRequires : kparts-dev
BuildRequires : kpty-dev
BuildRequires : kservice-dev
BuildRequires : ktexteditor-dev
BuildRequires : ktextwidgets-dev
BuildRequires : kwidgetsaddons-dev
BuildRequires : kxmlgui-dev
BuildRequires : libxml2
BuildRequires : mesa-dev
BuildRequires : mpfr-dev
BuildRequires : pkg-config
BuildRequires : pkgconfig(Qt5Svg)
BuildRequires : pkgconfig(Qt5XmlPatterns)
BuildRequires : pkgconfig(cln)
BuildRequires : pkgconfig(libqalculate)
BuildRequires : pkgconfig(libspectre)
BuildRequires : pkgconfig(luajit)
BuildRequires : pkgconfig(python3)
BuildRequires : python3-dev
BuildRequires : qtbase-dev
BuildRequires : solid-dev
BuildRequires : sonnet-dev
BuildRequires : syntax-highlighting-dev

%description
## Cantor
Cantor is a KDE Application aimed to provide a nice Interface
for doing Mathematics and Scientific Computing. It doesn't implement
its own Computation Logic, but instead is built around different
Backends.

%package bin
Summary: bin components for the cantor package.
Group: Binaries
Requires: cantor-data = %{version}-%{release}
Requires: cantor-license = %{version}-%{release}

%description bin
bin components for the cantor package.


%package data
Summary: data components for the cantor package.
Group: Data

%description data
data components for the cantor package.


%package dev
Summary: dev components for the cantor package.
Group: Development
Requires: cantor-lib = %{version}-%{release}
Requires: cantor-bin = %{version}-%{release}
Requires: cantor-data = %{version}-%{release}
Provides: cantor-devel = %{version}-%{release}

%description dev
dev components for the cantor package.


%package doc
Summary: doc components for the cantor package.
Group: Documentation

%description doc
doc components for the cantor package.


%package lib
Summary: lib components for the cantor package.
Group: Libraries
Requires: cantor-data = %{version}-%{release}
Requires: cantor-license = %{version}-%{release}

%description lib
lib components for the cantor package.


%package license
Summary: license components for the cantor package.
Group: Default

%description license
license components for the cantor package.


%package locales
Summary: locales components for the cantor package.
Group: Default

%description locales
locales components for the cantor package.


%prep
%setup -q -n cantor-18.12.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1549878405
mkdir -p clr-build
pushd clr-build
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1549878405
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/cantor
cp COPYING %{buildroot}/usr/share/package-licenses/cantor/COPYING
cp COPYING.DOC %{buildroot}/usr/share/package-licenses/cantor/COPYING.DOC
cp cmake/COPYING-CMAKE-SCRIPTS %{buildroot}/usr/share/package-licenses/cantor/cmake_COPYING-CMAKE-SCRIPTS
pushd clr-build
%make_install
popd
%find_lang cantor

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/cantor
/usr/bin/cantor_python3server
/usr/bin/cantor_rserver
/usr/bin/cantor_scripteditor

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.kde.cantor.desktop
/usr/share/cantor/maximabackend/cantor-initmaxima.lisp
/usr/share/cantor/octavebackend/cantor_eigenvectors.m
/usr/share/cantor/octavebackend/cantor_plot2d.m
/usr/share/cantor/octavebackend/cantor_plot3d.m
/usr/share/cantor/octavebackend/cantor_print.m
/usr/share/cantor/sagebackend/cantor-execsage
/usr/share/cantor/xslt/latex.xsl
/usr/share/config.kcfg/cantor.kcfg
/usr/share/config.kcfg/cantor_libs.kcfg
/usr/share/config.kcfg/kalgebrabackend.kcfg
/usr/share/config.kcfg/luabackend.kcfg
/usr/share/config.kcfg/maximabackend.kcfg
/usr/share/config.kcfg/octavebackend.kcfg
/usr/share/config.kcfg/python3backend.kcfg
/usr/share/config.kcfg/qalculatebackend.kcfg
/usr/share/config.kcfg/rserver.kcfg
/usr/share/config.kcfg/sagebackend.kcfg
/usr/share/config.kcfg/scilabbackend.kcfg
/usr/share/icons/hicolor/128x128/apps/cantor.png
/usr/share/icons/hicolor/16x16/apps/cantor.png
/usr/share/icons/hicolor/22x22/apps/cantor.png
/usr/share/icons/hicolor/32x32/apps/cantor.png
/usr/share/icons/hicolor/48x48/apps/cantor.png
/usr/share/icons/hicolor/48x48/apps/juliabackend.png
/usr/share/icons/hicolor/48x48/apps/kalgebrabackend.png
/usr/share/icons/hicolor/48x48/apps/luabackend.png
/usr/share/icons/hicolor/48x48/apps/maximabackend.png
/usr/share/icons/hicolor/48x48/apps/octavebackend.png
/usr/share/icons/hicolor/48x48/apps/pythonbackend.png
/usr/share/icons/hicolor/48x48/apps/qalculatebackend.png
/usr/share/icons/hicolor/48x48/apps/rbackend.png
/usr/share/icons/hicolor/48x48/apps/sagebackend.png
/usr/share/icons/hicolor/48x48/apps/scilabbackend.png
/usr/share/icons/hicolor/64x64/apps/cantor.png
/usr/share/kxmlgui5/cantor/cantor_advancedplot_assistant.rc
/usr/share/kxmlgui5/cantor/cantor_create_matrix_assistant.rc
/usr/share/kxmlgui5/cantor/cantor_differentiate_assistant.rc
/usr/share/kxmlgui5/cantor/cantor_eigenvalues_assistant.rc
/usr/share/kxmlgui5/cantor/cantor_eigenvectors_assistant.rc
/usr/share/kxmlgui5/cantor/cantor_import_package_assistant.rc
/usr/share/kxmlgui5/cantor/cantor_integrate_assistant.rc
/usr/share/kxmlgui5/cantor/cantor_invert_matrix_assistant.rc
/usr/share/kxmlgui5/cantor/cantor_part.rc
/usr/share/kxmlgui5/cantor/cantor_plot2d_assistant.rc
/usr/share/kxmlgui5/cantor/cantor_plot3d_assistant.rc
/usr/share/kxmlgui5/cantor/cantor_qalculateplotassistant.rc
/usr/share/kxmlgui5/cantor/cantor_runscript_assistant.rc
/usr/share/kxmlgui5/cantor/cantor_scripteditor.rc
/usr/share/kxmlgui5/cantor/cantor_shell.rc
/usr/share/kxmlgui5/cantor/cantor_solve_assistant.rc
/usr/share/metainfo/org.kde.cantor.appdata.xml
/usr/share/xdg/cantor.knsrc
/usr/share/xdg/cantor_kalgebra.knsrc
/usr/share/xdg/cantor_lua.knsrc
/usr/share/xdg/cantor_maxima.knsrc
/usr/share/xdg/cantor_octave.knsrc
/usr/share/xdg/cantor_python3.knsrc
/usr/share/xdg/cantor_qalculate.knsrc
/usr/share/xdg/cantor_r.knsrc
/usr/share/xdg/cantor_sage.knsrc
/usr/share/xdg/cantor_scilab.knsrc

%files dev
%defattr(-,root,root,-)
/usr/include/cantor/animationresult.h
/usr/include/cantor/backend.h
/usr/include/cantor/cantor_export.h
/usr/include/cantor/cantor_macros.h
/usr/include/cantor/completionobject.h
/usr/include/cantor/defaulthighlighter.h
/usr/include/cantor/defaultvariablemodel.h
/usr/include/cantor/epsresult.h
/usr/include/cantor/expression.h
/usr/include/cantor/extension.h
/usr/include/cantor/helpresult.h
/usr/include/cantor/imageresult.h
/usr/include/cantor/latexresult.h
/usr/include/cantor/result.h
/usr/include/cantor/session.h
/usr/include/cantor/syntaxhelpobject.h
/usr/include/cantor/textresult.h
/usr/include/cantor/worksheetaccess.h
/usr/lib64/libcantor_config.so
/usr/lib64/libcantor_pythonbackend.so
/usr/lib64/libcantorlibs.so

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/HTML/ca/cantor/create-dlg.png
/usr/share/doc/HTML/ca/cantor/differentiate-dlg.png
/usr/share/doc/HTML/ca/cantor/import-dlg.png
/usr/share/doc/HTML/ca/cantor/index.cache.bz2
/usr/share/doc/HTML/ca/cantor/index.docbook
/usr/share/doc/HTML/ca/cantor/integrate-dlg.png
/usr/share/doc/HTML/ca/cantor/latex_formula.png
/usr/share/doc/HTML/ca/cantor/matrix-dlg.png
/usr/share/doc/HTML/ca/cantor/plot2d-dlg.png
/usr/share/doc/HTML/ca/cantor/plot3d-dlg.png
/usr/share/doc/HTML/ca/cantor/screenshot.png
/usr/share/doc/HTML/ca/cantor/solve-equations-dlg.png
/usr/share/doc/HTML/de/cantor/index.cache.bz2
/usr/share/doc/HTML/de/cantor/index.docbook
/usr/share/doc/HTML/en/cantor/create-dlg.png
/usr/share/doc/HTML/en/cantor/differentiate-dlg.png
/usr/share/doc/HTML/en/cantor/import-dlg.png
/usr/share/doc/HTML/en/cantor/index.cache.bz2
/usr/share/doc/HTML/en/cantor/index.docbook
/usr/share/doc/HTML/en/cantor/integrate-dlg.png
/usr/share/doc/HTML/en/cantor/latex_formula.png
/usr/share/doc/HTML/en/cantor/matrix-dlg.png
/usr/share/doc/HTML/en/cantor/plot-dlg1.png
/usr/share/doc/HTML/en/cantor/plot-dlg2.png
/usr/share/doc/HTML/en/cantor/plot2d-dlg.png
/usr/share/doc/HTML/en/cantor/plot3d-dlg.png
/usr/share/doc/HTML/en/cantor/screenshot.png
/usr/share/doc/HTML/en/cantor/solve-equations-dlg.png
/usr/share/doc/HTML/es/cantor/index.cache.bz2
/usr/share/doc/HTML/es/cantor/index.docbook
/usr/share/doc/HTML/es/cantor/screenshot.png
/usr/share/doc/HTML/et/cantor/index.cache.bz2
/usr/share/doc/HTML/et/cantor/index.docbook
/usr/share/doc/HTML/fr/cantor/index.cache.bz2
/usr/share/doc/HTML/fr/cantor/index.docbook
/usr/share/doc/HTML/fr/cantor/screenshot.png
/usr/share/doc/HTML/gl/cantor/index.cache.bz2
/usr/share/doc/HTML/gl/cantor/index.docbook
/usr/share/doc/HTML/it/cantor/index.cache.bz2
/usr/share/doc/HTML/it/cantor/index.docbook
/usr/share/doc/HTML/nl/cantor/index.cache.bz2
/usr/share/doc/HTML/nl/cantor/index.docbook
/usr/share/doc/HTML/pt/cantor/index.cache.bz2
/usr/share/doc/HTML/pt/cantor/index.docbook
/usr/share/doc/HTML/pt_BR/cantor/index.cache.bz2
/usr/share/doc/HTML/pt_BR/cantor/index.docbook
/usr/share/doc/HTML/pt_BR/cantor/screenshot.png
/usr/share/doc/HTML/ru/cantor/index.cache.bz2
/usr/share/doc/HTML/ru/cantor/index.docbook
/usr/share/doc/HTML/sv/cantor/index.cache.bz2
/usr/share/doc/HTML/sv/cantor/index.docbook
/usr/share/doc/HTML/uk/cantor/create-dlg.png
/usr/share/doc/HTML/uk/cantor/differentiate-dlg.png
/usr/share/doc/HTML/uk/cantor/import-dlg.png
/usr/share/doc/HTML/uk/cantor/index.cache.bz2
/usr/share/doc/HTML/uk/cantor/index.docbook
/usr/share/doc/HTML/uk/cantor/integrate-dlg.png
/usr/share/doc/HTML/uk/cantor/matrix-dlg.png
/usr/share/doc/HTML/uk/cantor/plot-dlg1.png
/usr/share/doc/HTML/uk/cantor/plot-dlg2.png
/usr/share/doc/HTML/uk/cantor/plot2d-dlg.png
/usr/share/doc/HTML/uk/cantor/plot3d-dlg.png
/usr/share/doc/HTML/uk/cantor/screenshot.png
/usr/share/doc/HTML/uk/cantor/solve-equations-dlg.png

%files lib
%defattr(-,root,root,-)
/usr/lib64/libcantorlibs.so.18.12.2
/usr/lib64/libcantorlibs.so.20
/usr/lib64/qt5/plugins/cantor/assistants/cantor_advancedplotassistant.so
/usr/lib64/qt5/plugins/cantor/assistants/cantor_creatematrixassistant.so
/usr/lib64/qt5/plugins/cantor/assistants/cantor_differentiateassistant.so
/usr/lib64/qt5/plugins/cantor/assistants/cantor_eigenvaluesassistant.so
/usr/lib64/qt5/plugins/cantor/assistants/cantor_eigenvectorsassistant.so
/usr/lib64/qt5/plugins/cantor/assistants/cantor_importpackageassistant.so
/usr/lib64/qt5/plugins/cantor/assistants/cantor_integrateassistant.so
/usr/lib64/qt5/plugins/cantor/assistants/cantor_invertmatrixassistant.so
/usr/lib64/qt5/plugins/cantor/assistants/cantor_plot2dassistant.so
/usr/lib64/qt5/plugins/cantor/assistants/cantor_plot3dassistant.so
/usr/lib64/qt5/plugins/cantor/assistants/cantor_qalculateplotassistant.so
/usr/lib64/qt5/plugins/cantor/assistants/cantor_runscriptassistant.so
/usr/lib64/qt5/plugins/cantor/assistants/cantor_solveassistant.so
/usr/lib64/qt5/plugins/cantor/backends/cantor_kalgebrabackend.so
/usr/lib64/qt5/plugins/cantor/backends/cantor_luabackend.so
/usr/lib64/qt5/plugins/cantor/backends/cantor_maximabackend.so
/usr/lib64/qt5/plugins/cantor/backends/cantor_nullbackend.so
/usr/lib64/qt5/plugins/cantor/backends/cantor_octavebackend.so
/usr/lib64/qt5/plugins/cantor/backends/cantor_python3backend.so
/usr/lib64/qt5/plugins/cantor/backends/cantor_qalculatebackend.so
/usr/lib64/qt5/plugins/cantor/backends/cantor_rbackend.so
/usr/lib64/qt5/plugins/cantor/backends/cantor_sagebackend.so
/usr/lib64/qt5/plugins/cantor/backends/cantor_scilabbackend.so
/usr/lib64/qt5/plugins/cantor/panels/cantor_helppanelplugin.so
/usr/lib64/qt5/plugins/cantor/panels/cantor_variablemanagerplugin.so
/usr/lib64/qt5/plugins/libcantorpart.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/cantor/COPYING
/usr/share/package-licenses/cantor/COPYING.DOC
/usr/share/package-licenses/cantor/cmake_COPYING-CMAKE-SCRIPTS

%files locales -f cantor.lang
%defattr(-,root,root,-)

