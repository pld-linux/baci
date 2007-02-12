%define		_date	20051027
Summary:	BenAri Concurrent Interpreter
Summary(pl.UTF-8):	Współbieżny interpreter BACI
Name:		baci
Version:	1.0.%{_date}
Release:	1
License:	Freeware
Group:		Development/Languages
Source0:	http://www.mines.edu/fs_home/tcamp/baci/%{name}src.tar.gz
# Source0-md5:	14e0500bf7079a17664469ecead8bb4f
Patch0:		%{name}-20051026.patch
Patch1:		%{name}-%{_date}.patch
Patch2:		%{name}-amd64.patch
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	tk-devel
URL:		http://www.mines.edu/fs_home/tcamp/baci/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
BenAri Concurrent Pascal PCODE Interpreter & Compiler.

%description -l pl.UTF-8
Kompilator i interpreter języka BACI.

%prep
%setup -q -n %{name}src
%patch0 -p1
%patch1 -p1
%if "%{_lib}" == "lib64"
%patch2 -p1
%endif

%build
for i in lib disasm ccomp pascomp ar ld; do
	%{__make} -C $i \
		CFLAGS="%{rpmcflags}"
done
%{__make} -C interp gui std

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install ccomp/bacc disasm/badis pascomp/bapas interp/{bainterp,bagui} \
	ar/baar ld/bald	$RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
