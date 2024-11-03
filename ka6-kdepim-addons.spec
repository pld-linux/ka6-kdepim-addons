#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeappsver	24.08.2
%define		kframever	5.94.0
%define		qtver		5.15.2
%define		kaname		kdepim-addons
Summary:	kdepim addons
Name:		ka6-%{kaname}
Version:	24.08.2
Release:	4
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	5a6206b27512300569a7d4e2a50988cf
URL:		http://www.kde.org/
BuildRequires:	Qt6Core-devel >= %{qtver}
BuildRequires:	Qt6Gui-devel
BuildRequires:	Qt6Network-devel >= 5.11.1
BuildRequires:	Qt6Positioning-devel >= 5.11.1
BuildRequires:	Qt6PrintSupport-devel >= 5.11.1
BuildRequires:	Qt6Qml-devel >= 5.11.1
BuildRequires:	Qt6Quick-devel >= 5.11.1
BuildRequires:	Qt6Test-devel
BuildRequires:	Qt6WebChannel-devel >= 5.11.1
BuildRequires:	Qt6WebEngine-devel
BuildRequires:	Qt6Widgets-devel
BuildRequires:	cmake >= 3.20
BuildRequires:	gettext-devel
BuildRequires:	gpgme-devel
BuildRequires:	gpgme-qt6-devel >= 1.8.0
BuildRequires:	ka6-akonadi-calendar-devel >= %{kdeappsver}
BuildRequires:	ka6-akonadi-contacts-devel >= %{kdeappsver}
BuildRequires:	ka6-akonadi-devel >= %{kdeappsver}
BuildRequires:	ka6-akonadi-import-wizard-devel >= %{kdeappsver}
BuildRequires:	ka6-akonadi-mime-devel >= %{kdeappsver}
BuildRequires:	ka6-akonadi-notes-devel >= %{kdeappsver}
BuildRequires:	ka6-calendarsupport-devel >= %{kdeappsver}
BuildRequires:	ka6-eventviews-devel >= %{kdeappsver}
BuildRequires:	ka6-grantleetheme-devel >= %{kdeappsver}
BuildRequires:	ka6-incidenceeditor-devel >= %{kdeappsver}
BuildRequires:	ka6-kaddressbook-devel >= %{kdeappsver}
BuildRequires:	ka6-kcalutils-devel >= %{kdeappsver}
BuildRequires:	ka6-kidentitymanagement-devel >= %{kdeappsver}
BuildRequires:	ka6-kimap-devel >= %{kdeappsver}
BuildRequires:	ka6-kitinerary-devel >= %{kdeappsver}
BuildRequires:	ka6-kmailtransport-devel >= %{kdeappsver}
BuildRequires:	ka6-kmime-devel >= %{kdeappsver}
BuildRequires:	ka6-kpimtextedit-devel >= %{kdeappsver}
BuildRequires:	ka6-kpkpass-devel >= %{kdeappsver}
BuildRequires:	ka6-ktnef-devel >= %{kdeappsver}
BuildRequires:	ka6-libgravatar-devel >= %{kdeappsver}
BuildRequires:	ka6-libkdepim-devel >= %{kdeappsver}
BuildRequires:	ka6-libkleo-devel >= %{kdeappsver}
BuildRequires:	ka6-libksieve-devel >= %{kdeappsver}
BuildRequires:	ka6-mailcommon-devel >= %{kdeappsver}
BuildRequires:	ka6-mailimporter-devel >= %{kdeappsver}
BuildRequires:	ka6-messagelib-devel >= %{kdeappsver}
BuildRequires:	ka6-pimcommon-devel >= %{kdeappsver}
BuildRequires:	kf6-extra-cmake-modules >= %{kframever}
BuildRequires:	kf6-kcalendarcore-devel >= %{kframever}
BuildRequires:	kf6-kconfig-devel >= %{kframever}
BuildRequires:	kf6-kcontacts-devel >= %{kframever}
BuildRequires:	kf6-kdbusaddons-devel >= %{kframever}
BuildRequires:	kf6-kdeclarative-devel >= %{kframever}
BuildRequires:	kf6-kholidays-devel >= %{kframever}
BuildRequires:	kf6-ki18n-devel >= %{kframever}
BuildRequires:	kf6-kiconthemes-devel >= %{kframever}
BuildRequires:	kf6-kio-devel >= %{kframever}
BuildRequires:	kf6-kparts-devel >= %{kframever}
BuildRequires:	kf6-ktexttemplate-devel >= %{kframever}
BuildRequires:	kf6-kxmlgui-devel >= %{kframever}
BuildRequires:	kf6-prison-devel >= %{kframever}
BuildRequires:	kf6-syntax-highlighting-devel >= %{kframever}
BuildRequires:	ktextaddons-devel >= 1.5.4
BuildRequires:	libmarkdown-devel
BuildRequires:	ninja
BuildRequires:	qt6-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Obsoletes:	ka5-%{kaname} < %{version}
ExcludeArch:	x32 i686
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Addons for KDE PIM applications, such as extensions for KMail,
additional themes, and plugins providing extra or advanced
functionality.

%prep
%setup -q -n %{kaname}-%{version}

%build
%cmake \
	-B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DKDE_INSTALL_DOCBUNDLEDIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	-DQT_MAJOR_VERSION=6
%ninja_build -C build

%if %{with tests}
ctest --test-dir build
%endif


%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{kaname}.lang
%defattr(644,root,root,755)
/etc/xdg/kmail.antispamrc
/etc/xdg/kmail.antivirusrc
%attr(755,root,root) %{_bindir}/kmail_antivir.sh
%attr(755,root,root) %{_bindir}/kmail_clamav.sh
%attr(755,root,root) %{_bindir}/kmail_fprot.sh
%attr(755,root,root) %{_bindir}/kmail_sav.sh
%attr(755,root,root) %{_libdir}/libakonadidatasetools.so.*.*
%ghost %{_libdir}/libakonadidatasetools.so.6
%attr(755,root,root) %{_libdir}/libdkimverifyconfigure.so.*.*
%ghost %{_libdir}/libdkimverifyconfigure.so.6
%attr(755,root,root) %{_libdir}/libexpireaccounttrashfolderconfig.so.*.*
%ghost %{_libdir}/libexpireaccounttrashfolderconfig.so.6
%attr(755,root,root) %{_libdir}/libfolderconfiguresettings.so.*.*
%ghost %{_libdir}/libfolderconfiguresettings.so.6
%attr(755,root,root) %{_libdir}/libkaddressbookmergelibprivate.so.*.*
%ghost %{_libdir}/libkaddressbookmergelibprivate.so.6
%attr(755,root,root) %{_libdir}/libkmailconfirmbeforedeleting.so.*.*
%ghost %{_libdir}/libkmailconfirmbeforedeleting.so.6
%attr(755,root,root) %{_libdir}/libkmailmarkdown.so.*.*
%ghost %{_libdir}/libkmailmarkdown.so.6
%attr(755,root,root) %{_libdir}/libkmailquicktextpluginprivate.so.*.*
%ghost %{_libdir}/libkmailquicktextpluginprivate.so.6
%attr(755,root,root) %{_libdir}/libopenurlwithconfigure.so.*.*
%ghost %{_libdir}/libopenurlwithconfigure.so.6
%attr(755,root,root) %{_libdir}/libshorturlpluginprivate.so.*.*
%ghost %{_libdir}/libshorturlpluginprivate.so.6
%attr(755,root,root) %{_libdir}/qt6/plugins/pim6/akonadi/emailaddressselectionldapdialogplugin.so
%dir %{_libdir}/qt6/plugins/pim6/contacteditor
%dir %{_libdir}/qt6/plugins/pim6/contacteditor/editorpageplugins
%attr(755,root,root) %{_libdir}/qt6/plugins/pim6/contacteditor/editorpageplugins/cryptopageplugin.so
%attr(755,root,root) %{_libdir}/qt6/plugins/pim6/importwizard/evolutionv1importerplugin.so
%attr(755,root,root) %{_libdir}/qt6/plugins/pim6/importwizard/evolutionv2importerplugin.so
%attr(755,root,root) %{_libdir}/qt6/plugins/pim6/importwizard/gearyimporterplugin.so
%attr(755,root,root) %{_libdir}/qt6/plugins/pim6/importwizard/operaimporterplugin.so
%dir %{_libdir}/qt6/plugins/pim6/kaddressbook
%dir %{_libdir}/qt6/plugins/pim6/kaddressbook/importexportplugin
%attr(755,root,root) %{_libdir}/qt6/plugins/pim6/kaddressbook/importexportplugin/kaddressbook_importexportgmxplugin.so
%attr(755,root,root) %{_libdir}/qt6/plugins/pim6/kaddressbook/importexportplugin/kaddressbook_importexportldapplugin.so
%attr(755,root,root) %{_libdir}/qt6/plugins/pim6/kaddressbook/importexportplugin/kaddressbook_importexportldifplugin.so
%attr(755,root,root) %{_libdir}/qt6/plugins/pim6/kaddressbook/importexportplugin/kaddressbook_importexportvcardplugin.so
%attr(755,root,root) %{_libdir}/qt6/plugins/pim6/kaddressbook/importexportplugin/kaddressbook_importexportwindowscontactplugin.so
%dir %{_libdir}/qt6/plugins/pim6/kaddressbook/mainview
%attr(755,root,root) %{_libdir}/qt6/plugins/pim6/kaddressbook/mainview/kaddressbook_checkgravatarplugin.so
%attr(755,root,root) %{_libdir}/qt6/plugins/pim6/kaddressbook/mainview/kaddressbook_mergecontactsplugin.so
%attr(755,root,root) %{_libdir}/qt6/plugins/pim6/kaddressbook/mainview/kaddressbook_searchduplicatesplugin.so
%attr(755,root,root) %{_libdir}/qt6/plugins/pim6/kaddressbook/mainview/kaddressbook_sendmailplugin.so
%attr(755,root,root) %{_libdir}/qt6/plugins/pim6/kaddressbook/mainview/kaddressbook_sendvcardsplugin.so
%dir %{_libdir}/qt6/plugins/pim6/kmail
%dir %{_libdir}/qt6/plugins/pim6/kmail/mainview
%attr(755,root,root) %{_libdir}/qt6/plugins/pim6/kmail/mainview/kmail_akonadidatabasetoolplugin.so
%attr(755,root,root) %{_libdir}/qt6/plugins/pim6/kmail/mainview/kmail_antispamplugin.so
%attr(755,root,root) %{_libdir}/qt6/plugins/pim6/kmail/mainview/kmail_antivirusplugin.so
%attr(755,root,root) %{_libdir}/qt6/plugins/pim6/kmail/mainview/kmail_expertplugin.so
%dir %{_libdir}/qt6/plugins/pim6/kmail/plugincheckbeforesend
%attr(755,root,root) %{_libdir}/qt6/plugins/pim6/kmail/plugincheckbeforesend/kmail_automaticaddcontactseditorplugin.so
%attr(755,root,root) %{_libdir}/qt6/plugins/pim6/kmail/plugincheckbeforesend/kmail_checkbeforesendeditorplugin.so
%attr(755,root,root) %{_libdir}/qt6/plugins/pim6/kmail/plugincheckbeforesend/kmail_confirmaddresseditorplugin.so
%dir %{_libdir}/qt6/plugins/pim6/kmail/plugineditor
%attr(755,root,root) %{_libdir}/qt6/plugins/pim6/kmail/plugineditor/kmail_autocorrectioneditorplugin.so
%attr(755,root,root) %{_libdir}/qt6/plugins/pim6/kmail/plugineditor/kmail_changecaseeditorplugin.so
%attr(755,root,root) %{_libdir}/qt6/plugins/pim6/kmail/plugineditor/kmail_insertemaileditorplugin.so
%attr(755,root,root) %{_libdir}/qt6/plugins/pim6/kmail/plugineditor/kmail_insertshorturleditorplugin.so
%attr(755,root,root) %{_libdir}/qt6/plugins/pim6/kmail/plugineditor/kmail_insertspecialcharactereditorplugin.so
%attr(755,root,root) %{_libdir}/qt6/plugins/pim6/kmail/plugineditor/kmail_nonbreakingspaceeditorplugin.so
%attr(755,root,root) %{_libdir}/qt6/plugins/pim6/kmail/plugineditor/kmail_quicktextplugin.so
%attr(755,root,root) %{_libdir}/qt6/plugins/pim6/kmail/plugineditor/kmail_sharetexteditorplugin.so
%attr(755,root,root) %{_libdir}/qt6/plugins/pim6/kmail/plugineditor/kmail_zoomtexteditorplugin.so
%dir %{_libdir}/qt6/plugins/pim6/kmail/plugineditorconverttext
%attr(755,root,root) %{_libdir}/qt6/plugins/pim6/kmail/plugineditorconverttext/kmail_markdownplugin.so
%dir %{_libdir}/qt6/plugins/pim6/kmail/plugineditorgrammar
%attr(755,root,root) %{_libdir}/qt6/plugins/pim6/kmail/plugineditorgrammar/kmail_grammalecteplugin.so
%attr(755,root,root) %{_libdir}/qt6/plugins/pim6/kmail/plugineditorgrammar/kmail_languagetoolplugin.so
%dir %{_libdir}/qt6/plugins/pim6/kmail/plugineditorinit
%attr(755,root,root) %{_libdir}/qt6/plugins/pim6/kmail/plugineditorinit/kmail_externalcomposereditorplugin.so
%dir %{_libdir}/qt6/plugins/pim6/libksieve
%attr(755,root,root) %{_libdir}/qt6/plugins/pim6/libksieve/emaillineeditplugin.so
%attr(755,root,root) %{_libdir}/qt6/plugins/pim6/libksieve/imapfoldercompletionplugin.so
%attr(755,root,root) %{_libdir}/qt6/plugins/pim6/mailtransport/mailtransport_sendplugin.so
%dir %{_libdir}/qt6/plugins/pim6/messageviewer/bodypartformatter
%attr(755,root,root) %{_libdir}/qt6/plugins/pim6/messageviewer/bodypartformatter/messageviewer_bodypartformatter_application_gnupgwks.so
%attr(755,root,root) %{_libdir}/qt6/plugins/pim6/messageviewer/bodypartformatter/messageviewer_bodypartformatter_application_mstnef.so
%attr(755,root,root) %{_libdir}/qt6/plugins/pim6/messageviewer/bodypartformatter/messageviewer_bodypartformatter_pkpass.so
%attr(755,root,root) %{_libdir}/qt6/plugins/pim6/messageviewer/bodypartformatter/messageviewer_bodypartformatter_semantic.so
%attr(755,root,root) %{_libdir}/qt6/plugins/pim6/messageviewer/bodypartformatter/messageviewer_bodypartformatter_text_calendar.so
%attr(755,root,root) %{_libdir}/qt6/plugins/pim6/messageviewer/bodypartformatter/messageviewer_bodypartformatter_text_highlighter.so
%attr(755,root,root) %{_libdir}/qt6/plugins/pim6/messageviewer/bodypartformatter/messageviewer_bodypartformatter_text_markdown.so
%attr(755,root,root) %{_libdir}/qt6/plugins/pim6/messageviewer/bodypartformatter/messageviewer_bodypartformatter_text_vcard.so
%dir %{_libdir}/qt6/plugins/pim6/messageviewer/checkbeforedeleting
%attr(755,root,root) %{_libdir}/qt6/plugins/pim6/messageviewer/checkbeforedeleting/kmail_confirmbeforedeletingplugin.so
%dir %{_libdir}/qt6/plugins/pim6/messageviewer/configuresettings
%attr(755,root,root) %{_libdir}/qt6/plugins/pim6/messageviewer/configuresettings/messageviewer_dkimconfigplugin.so
%attr(755,root,root) %{_libdir}/qt6/plugins/pim6/messageviewer/configuresettings/messageviewer_expireaccounttrashfolderconfigplugin.so
%attr(755,root,root) %{_libdir}/qt6/plugins/pim6/messageviewer/configuresettings/messageviewer_folderconfiguresettingsplugin.so
%attr(755,root,root) %{_libdir}/qt6/plugins/pim6/messageviewer/configuresettings/messageviewer_gravatarconfigplugin.so
%attr(755,root,root) %{_libdir}/qt6/plugins/pim6/messageviewer/configuresettings/messageviewer_openurlwithconfigplugin.so
%dir %{_libdir}/qt6/plugins/pim6/messageviewer/headerstyle
%attr(755,root,root) %{_libdir}/qt6/plugins/pim6/messageviewer/headerstyle/messageviewer_briefheaderstyleplugin.so
%attr(755,root,root) %{_libdir}/qt6/plugins/pim6/messageviewer/headerstyle/messageviewer_fancyheaderstyleplugin.so
%attr(755,root,root) %{_libdir}/qt6/plugins/pim6/messageviewer/headerstyle/messageviewer_grantleeheaderstyleplugin.so
%attr(755,root,root) %{_libdir}/qt6/plugins/pim6/messageviewer/headerstyle/messageviewer_longheaderstyleplugin.so
%attr(755,root,root) %{_libdir}/qt6/plugins/pim6/messageviewer/headerstyle/messageviewer_standardsheaderstyleplugin.so
%dir %{_libdir}/qt6/plugins/pim6/messageviewer/kf6
%dir %{_libdir}/qt6/plugins/pim6/messageviewer/kf6/ktexttemplate
%attr(755,root,root) %{_libdir}/qt6/plugins/pim6/messageviewer/kf6/ktexttemplate/kitinerary_ktexttemplate_extension.so
%dir %{_libdir}/qt6/plugins/pim6/messageviewer/viewercommonplugin
%attr(755,root,root) %{_libdir}/qt6/plugins/pim6/messageviewer/viewercommonplugin/messageviewer_expandurlplugin.so
%attr(755,root,root) %{_libdir}/qt6/plugins/pim6/messageviewer/viewercommonplugin/messageviewer_translatorplugin.so
%dir %{_libdir}/qt6/plugins/pim6/messageviewer/viewerplugin
%attr(755,root,root) %{_libdir}/qt6/plugins/pim6/messageviewer/viewerplugin/messageviewer_createeventplugin.so
%attr(755,root,root) %{_libdir}/qt6/plugins/pim6/messageviewer/viewerplugin/messageviewer_createtodoplugin.so
%attr(755,root,root) %{_libdir}/qt6/plugins/pim6/messageviewer/viewerplugin/messageviewer_externalscriptplugin.so
%dir %{_libdir}/qt6/plugins/pim6/pimcommon
%dir %{_libdir}/qt6/plugins/pim6/pimcommon/customtools
%attr(755,root,root) %{_libdir}/qt6/plugins/pim6/pimcommon/customtools/pimcommon_translatorplugin.so
%dir %{_libdir}/qt6/plugins/pim6/pimcommon/shorturlengine
%attr(755,root,root) %{_libdir}/qt6/plugins/pim6/pimcommon/shorturlengine/pimcommon_isgdshorturlengineplugin.so
%attr(755,root,root) %{_libdir}/qt6/plugins/pim6/pimcommon/shorturlengine/pimcommon_tinyurlengineplugin.so
%attr(755,root,root) %{_libdir}/qt6/plugins/pim6/pimcommon/shorturlengine/pimcommon_triopabshorturlengineplugin.so
%dir %{_libdir}/qt6/plugins/pim6/templateparser
%attr(755,root,root) %{_libdir}/qt6/plugins/pim6/templateparser/templateparseraddressrequesterplugin.so
%dir %{_libdir}/qt6/plugins/pim6/webengineviewer
%dir %{_libdir}/qt6/plugins/pim6/webengineviewer/urlinterceptor
%attr(755,root,root) %{_libdir}/qt6/plugins/pim6/webengineviewer/urlinterceptor/webengineviewer_donottrackplugin.so
%attr(755,root,root) %{_libdir}/qt6/plugins/plasmacalendarplugins/pimevents.so
%dir %{_libdir}/qt6/plugins/plasmacalendarplugins/pimevents
%{_libdir}/qt6/plugins/plasmacalendarplugins/pimevents/PimEventsConfig.qml
%dir %{_libdir}/qt6/qml/org/kde/plasma/PimCalendars
%attr(755,root,root) %{_libdir}/qt6/qml/org/kde/plasma/PimCalendars/libpimcalendarsplugin.so
%{_libdir}/qt6/qml/org/kde/plasma/PimCalendars/qmldir
%{_datadir}/qlogging-categories6/kdepim-addons.categories
%{_datadir}/qlogging-categories6/kdepim-addons.renamecategories
#%dir %{_datadir}/qtcreator
#%dir %{_datadir}/qtcreator/templates
#%dir %{_datadir}/qtcreator/templates/kmaileditorconvertertextplugins
#%{_datadir}/qtcreator/templates/kmaileditorconvertertextplugins/CMakeLists.txt
#%{_datadir}/qtcreator/templates/kmaileditorconvertertextplugins/plugin.json.impl
#%{_datadir}/qtcreator/templates/kmaileditorconvertertextplugins/plugineditor.cpp
#%{_datadir}/qtcreator/templates/kmaileditorconvertertextplugins/plugineditor.h
#%{_datadir}/qtcreator/templates/kmaileditorconvertertextplugins/plugineditorinterface.cpp
#%{_datadir}/qtcreator/templates/kmaileditorconvertertextplugins/plugineditorinterface.h
#%{_datadir}/qtcreator/templates/kmaileditorconvertertextplugins/wizard.json
