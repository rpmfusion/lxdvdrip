Name:           lxdvdrip
Version:        1.77
Release:        20%{?dist}
Summary:        A command line tool to rip&burn a video DVD

Group:          Applications/Multimedia
License:        GPLv2+
URL:            https://sourceforge.net/projects/lxdvdrip/
Source0:        https://sourceforge.net/projects/lxdvdrip/files/lxdvdrip-%{version}.tgz

# Set make file to compile properly
Patch0:         lxdvdrip-makefile.patch
#Define code for PPC
Patch1:         lxdvdrip-%{version}-requant.patch
# Add missing include files (-Werror=implicit-function-declaration)
Patch2:         lxdvdrip-1.77-header-include.patch
# Fix sigaction struct usage (-Werror=incompatible-pointer-types)
# sa_flags does not contain SA_SIGINFO, so sa_handler must be used
Patch3:         lxdvdrip-1.77-sigaction-hander-type.patch

BuildRequires:  gcc
BuildRequires:  libdvdread-devel >= 4.1.3
BuildRequires:  libdvdnav-devel
Requires:       dvdauthor

#According to requant/requant_lxdvdrip.c
#Only the following arches are supported in 1.74
ExclusiveArch:  i686 x86_64 ppc ppc64

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
%patch -P0 -p0 -b .makefile
%patch -P1 -p0 -b .requant
%patch -P2 -p1 -b .include
%patch -P3 -p1 -b .sigaction

chmod 644 doc-pak/lxdvdrip.conf.*

# Remove spurious permissions
for i in `find . -type f \( -name "*.h" -o -name "*.c" \)`; do
chmod a-x $i
done

%build
make %{?_smp_mflags} \
 CFLAGS="${RPM_OPT_FLAGS}" \
 LDFLAGS="${RPM_LD_FLAGS}"


%install
rm -rf $RPM_BUILD_ROOT

make CFLAGS="${RPM_OPT_FLAGS}" \
 LDFLAGS="${RPM_LD_FLAGS}" \
 install INSTALLDIR=$RPM_BUILD_ROOT BINDIR=%{_bindir} MANDIR=%{_mandir} \
 DATADIR=%{_datadir}/%{name}-%{version} SYSCONFDIR=%{_sysconfdir} \
 PREFIX=$RPM_BUILD_ROOT%{_prefix} INSTBIN=$RPM_BUILD_ROOT%{_bindir}

# Set permissions
chmod 755 $RPM_BUILD_ROOT%{_bindir}/*

%files
%doc doc-pak/Changelog* doc-pak/lxdvdrip.conf*
%doc doc-pak/README.*
%license doc-pak/COPYING
%{_bindir}/*
%{_mandir}/man1/*
%{_datadir}/lxdvdrip*
%config(noreplace) %{_sysconfdir}/lxdvdrip.conf

%changelog
* Fri Oct 11 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.77-20
- Patch to fix -Werror=implicit-function-declaration
- Patch to fix -Werror=imcompatible-pointer-types
- Patch to stop suppressing compiler warnings

* Fri Aug 02 2024 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1.77-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Feb 03 2024 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1.77-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Aug 02 2023 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1.77-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Aug 07 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1.77-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild and ffmpeg
  5.1

* Wed Feb 09 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1.77-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Aug 03 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.77-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Feb 03 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.77-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Oct 21 2020 Leigh Scott <leigh123linux@gmail.com> - 1.77-12
- Rebuild for new libdvdread

* Tue Aug 18 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.77-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Feb 05 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.77-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Nov 15 2019 Dominik 'Rathann' Mierzejewski <rpm@greysector.net> - 1.77-9
- rebuild for libdvdread ABI bump

* Fri Aug 09 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.77-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Mar 04 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.77-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 27 2018 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.77-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 01 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 1.77-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 31 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 1.77-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Mar 19 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 1.77-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Aug 15 2016 Leigh Scott <leigh123linux@googlemail.com> - 1.77-2
- Remove surplus hardening flags

* Wed Feb 24 2016 Antonio Trande <sagitter@fedoraproject.org> - 1.77-1
- Update to 1.77
- Update Source and URL
- Patches updated
- License tagged with %%license
- Set flags for hardened builds
- Remove spurious permissions
- Remove Source1: dvdbackup.tar.bz2, upstream have the same source.

* Sun Aug 31 2014 Sérgio Basto <sergio@serjux.com> - 1.74-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Dec 30 2012 Nicolas Chauvet <kwizart@gmail.com> - 1.74-6
- Set ExclusiveArch rfbz#2464

* Wed Feb 08 2012 Nicolas Chauvet <kwizart@gmail.com> - 1.74-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Mar 29 2009 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 1.74-4
- rebuild for new F11 features

* Sun Feb 22 2009 David Juran <david@juran.se> - 1.74-3
- ppc, second try

* Sun Feb 22 2009 David Juran <david@juran.se> - 1.74-2
- fix build on ppc

* Sat Feb 21 2009 David Juran <david@juran.se> - 1.74-1
- update to 1.74
- keep dvdbackup from lxdvdrip-1.70 due to requirement on new libdvdread
- clean up rpmlint errors

* Tue Nov 18 2008 David Juran <david@juran.se> - 1.70-4
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
