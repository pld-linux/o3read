Summary:	OpenOffice.org document to HTML converter
Summary(pl):	Konwerter dokumentów OpenOffice.org do HTML-a
Name:		o3read
Version:	0.0.3
Release:	1
License:	GPL v2
Group:		Applications/Text
Source0:	http://siag.nu/pub/o3read/%{name}-%{version}.tar.gz
# Source0-md5:	ff6d5462de6e4a302c15db0500bba778
URL:		http://siag.nu/o3read/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a standalone converter for the OpenOffice.org swriter (.sxw)
and scalc (.sxc) formats. It doesn't depend on Open Office or any
other external tools or libraries.

%description -l pl
Wolnostojący konwerter dokumentów swritera (.sxw) oraz scalca (.sxc)
OpenOffice.org. Nie zależy od Open Office ani żadnych innych
zewnętrznych narzędzi czy bibliotek.

%prep
%setup -q

%build
%{__make} CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install o3read o3tohtml o3totxt utf8tolatin1 $RPM_BUILD_ROOT%{_bindir}
install *.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
