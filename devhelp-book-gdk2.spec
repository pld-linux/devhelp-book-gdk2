Summary:	DevHelp book: gdk
Summary(pl):	Ksi±¿ka do DevHelp'a o gdk
Name:		devhelp-book-gdk
Version:	2.0
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://www.devhelp.net/books/books/gdk-2.0.tar.gz
URL:		http://www.devhelp.net/
Requires:	devhelp
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6/share/devhelp/

%description
DevHelp book about gdk 1.2

%description -l pl
Ksi±¿ka do DevHelp o gdk 1.2

%prep
%setup -q -c gdk-%{version} -n gdk-%{version}

%build
mv -f book gdk-%{version}
mv -f book.devhelp gdk-%{version}.devhelp

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_prefix}/books/gdk-%{version}
install -d $RPM_BUILD_ROOT%{_prefix}/specs
install gdk-%{version}.devhelp $RPM_BUILD_ROOT%{_prefix}/specs
install gdk-%{version}/* $RPM_BUILD_ROOT%{_prefix}/books/gdk-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(644,root,root,755)
#%doc *.gz
%{_prefix}/books
%{_prefix}/specs
