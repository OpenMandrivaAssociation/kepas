Summary:	KDE Easy Publish and Share
Name:		kepas
Version: 	0.9.3
Release: 	3
Source0: 	http://kent.dl.sourceforge.net/sourceforge/kepas/%name-%version.tar.bz2
Patch0:		kepas-0.9.3-linking.patch
License: 	GPLv2+
Group: 		Networking/Other
Url: 		http://www.kde-apps.org/content/show.php?content=73968
BuildRequires: 	kdelibs4-devel


%description 
Kepas is a zeroconf KDE4 filetransfer tool. 
It discovers your local LAN for buddies (KDNSSD) and lets you transfer
files or klipper entries from a trayicon or via drag 'n drop with the
kepas plasmoid.

Current features: 

* Run Kepas as Plasmoid or Trayicon
* Zeroconf buddy discovery in your LAN (KDNSSD) 
* Filetransfer between buddies (kepas or giver)
* Filetransfer to kopete ICQ contacts 
* Filetransfer to kopete Jabber contacts
* Transfer of klipper entries 
* Activate received klipper entries 
* Drag 'n Drop Files on the kepas Plasmoid 
* Configure the destination folder and nickname
* Start a Public Folder (KPF)
* Monitor your Public Folders
* available Public Folders are shown on Buddy discovery

%files 
%doc AUTHORS 
%{_kde_bindir}/*
%{_kde_libdir}/*.so
%{_kde_appsdir}/plasma/plasma.notifyrc
%{_kde_appsdir}/%name
%{_kde_libdir}/kde4/plasma_applet_kepas.so
%{_kde_applicationsdir}/*.desktop
%{_kde_iconsdir}/*/*/*/*
%{_kde_services}/plasma-applet-kepas.desktop

#--------------------------------------------------------------------
%prep
%setup -q -n %name-%version
%patch0 -p1

%build
%cmake_kde4
%make

%install
%{makeinstall_std} -C build






