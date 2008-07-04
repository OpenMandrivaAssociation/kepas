Summary:	KDE Easy Publish and Share
Name:		kepas
Version: 	0.9
Release: 	%mkrel 2
Source0: 	http://kent.dl.sourceforge.net/sourceforge/kepas/%name-%version.tar.bz2
# fwang: plasmoid was disabled because it is using old API
Patch0:		kepas-0.9-disable-plasmoid.patch
License: 	GPLv2+
Group: 		Networking/Other
Url: 		http://www.kde-apps.org/content/show.php?content=73968
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: 	kdebase4-workspace-devel

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

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%files -f %name.lang
%defattr(-,root,root)
%_kde_bindir/*
%_kde_libdir/*.so
%_kde_appsdir/plasma/plasma.notifyrc
%_kde_appsdir/%name

#--------------------------------------------------------------------
%prep
%setup -q -n %name-%version
%patch0 -p0

%build
%cmake_kde4
%make

%install
rm -rf %{buildroot}
cd build
%{makeinstall_std}
cd -

%find_lang %name --with-html

%clean
rm -rf %{buildroot}

