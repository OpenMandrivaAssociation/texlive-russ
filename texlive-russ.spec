Name:		texlive-russ
Version:	25209
Release:	1
Summary:	LaTeX in Russian, without babel
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/russ
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/russ.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/russ.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package aims to facilitate Russian typesetting (based on
input using MicroSoft Code Page 1251). Russian hyphenation is
selected, and various mathematical commands are set up in
Russian style. Furthermore all Cyrillic letters' catcodes are
set to "letter", so that commands with Cyrillic letters in
their names may be defined.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/russ/russ.sty
%doc %{_texmfdistdir}/doc/latex/russ/README
%doc %{_texmfdistdir}/doc/latex/russ/readme.RU.txt
%doc %{_texmfdistdir}/doc/latex/russ/russ_doc.pdf
%doc %{_texmfdistdir}/doc/latex/russ/russ_doc.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
