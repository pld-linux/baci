Summary:	BenAri Concurrent Interpreter
Summary(pl):	Wspó³bie¿ny interpreter BACI
Name:		baci
Version:	1.0
Release:	2
License:	freeware
Group:		Development/Languages
Source0:	http://www.mines.edu/fs_home/tcamp/baci/%{name}src.tar.gz
BuildRequires:	flex
BuildRequires:	tk-devel
URL:		http://www.mines.edu/fs_home/tcamp/baci/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
BenAri Concurrent Pascal PCODE Interpreter & Compiler.

%description -l pl
Kompilator i interpreter jêzyka BACI.

%prep
%setup -q -n %{name}src

%build
for i in lib pascomp disasm ccomp; do
	make -C $i CFLAGS="%{rpmcflags}"
done
%{__make} -C interp gui std

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install ccomp/bacc disasm/badis pascomp/bapas interp/{bainterp,bagui} $RPM_BUILD_ROOT/%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
