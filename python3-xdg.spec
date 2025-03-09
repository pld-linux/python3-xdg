Summary:	Variables defined by the XDG Base Directory Specification
Summary(pl.UTF-8):	Zmienne zdefiniowane w specyfikacji XDG Base Directory
Name:		python3-xdg
Version:	4.0.1
Release:	5
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/xdg/
Source0:	https://files.pythonhosted.org/packages/source/x/xdg/xdg-%{version}.tar.gz
# Source0-md5:	07ff5bf0e315bd4589a51eab18a5b979
Patch0:		%{name}-rename.patch
URL:		https://pypi.org/project/xdg/
BuildRequires:	python3-modules >= 1:3.6
BuildRequires:	python3-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xdg is a tiny Python module which provides the variables defined by
the XDG Base Directory Specification, to save you from duplicating the
same snippet of logic in every Python utility you write that deals
with user cache, configuration, or data files. It has no external
dependencies.

%description -l pl.UTF-8
xdg to mały moduł Pythona, udostępniający zmienne zdefiniowane w
specyfikacji XDG Base Directory, aby oszczędzić duplikowania tej samej
logiki w każdym narzędziu pythonowym, które obsługuje pamięć
podręczną, konfigurację czy pliki danych użytkownika. Moduł nie ma
zewnętrznych zależności.

%prep
%setup -q -n xdg-%{version}

# "xdg" name conflicts with older (but more comprehensive) pyxdg module,
# which uses xdg namespace; rename to allow using both in the same system.
%patch -P 0 -p1
%{__mv} src/{xdg,xdgenv}

%build
%py3_build

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENCE README.md
%{py3_sitescriptdir}/xdgenv
%{py3_sitescriptdir}/xdg-%{version}-py*.egg-info
