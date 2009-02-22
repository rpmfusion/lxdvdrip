Name:           lxdvdrip
Version:        1.74
Release:        3%{?dist}
Summary:        A command line tool to rip&burn a video DVD

Group:          Applications/Multimedia
License:        GPLv2
URL:            http://lxdvdrip.berlios.de/
Source0:        http://download.berlios.de/lxdvdrip/lxdvdrip-1.74.tar.gz
Source1:        dvdbackup.tar.bz2
Patch0:         lxdvdrip-makefile.patch
Patch1:         lxdvdrip-1.74-requant.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  libdvdread-devel >= 4.1.3 libdvdnav-devel
Requires:       dvdauthor

%description
This program is able to rip a DVD title or chapters, reauthor the files to a
DVD-Structure,preview the Files and burn to a DVD+/-R.

The "traditional" way to Rip in 4 Steps (Rip Video&Requant, Rip Audio, Mplex,
dvdauthor) is included, too. Activation through Command Line Parameter
"-st=mplayer" for mplayer or "-st=transcode" for transcode.

A very fast Method is "Transcode parallel", all Commands are piped, so that
only a single Pass Read is needed.

%prep
%setup -q -n lxdvdrip
%patch0 -p1 -b .makefile
%patch1 -p1 -b .requant

rm -fR dvdbackup
tar -xjf %{SOURCE1}
chmod 644 doc-pak/lxdvdrip.conf.*

%build
make CFLAGS="${RPM_OPT_FLAGS}" %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT

make install INSTALLDIR=$RPM_BUILD_ROOT BINDIR=%{_bindir} MANDIR=%{_mandir} \
DATADIR=%{_datadir}/%{name}-%{version} SYSCONFDIR=%{_sysconfdir} \
PREFIX=$RPM_BUILD_ROOT%{_usr} INSTBIN=$RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc doc-pak/Changelog* doc-pak/COPYING doc-pak/lxdvdrip.conf*
%doc doc-pak/README.* doc-pak/TODO
%{_bindir}/*
%{_mandir}/man1/*
%{_datadir}/lxdvdrip*
%config(noreplace) %{_sysconfdir}/lxdvdrip.conf

%changelog
* Sun Feb 22 2009 David Juran <david@juran.se> - 1.74-3
- ppc, second try

* Sun Feb 22 2009 David Juran <david@juran.se> - 1.74-2
- fix build on ppc

* Sat Feb 21 2009 David Juran <david@juran.se> - 1.74-1
- update to 1.74
- keep dvdbackup from lxdvdrip-1.70 due to requirement on new libdvdread
- clean up rpmlint errors

* Thu Nov 18 2008 David Juran <david@juran.se> - 1.70-4
- dvdread changed the header structure back. Dropping patch

* Wed Aug 20 2008 David Juran <david@juran.se> - 1.70-3
- Patch for new libdvdread

* Tue Aug 19 2008 David Juran <david@juran.se> - 1.70-2
- Bump release for rpmfusion

* Sun Dec 09 2007 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- 1.70-1
- version upgrade

* Sat Mar 18 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
1.51-2
- remove -dl workaround

* Thu Mar 16 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
1.51-1
- version upgrade
- fix devel build

* Thu Mar 09 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- switch to new release field

* Tue Feb 28 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- add dist

* Tue Jun 14 2005 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
1.46-0.lvn.1
- Initial Release
