Name:		texlive-hvfloat
Version:	1.1
Release:	1
Summary:	Rotating caption and object of floats independently
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/hvfloat
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hvfloat.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hvfloat.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
This package defines a macro to place objects (tables and
figures) and their captions in different positions with
different rotating angles within a float. All objects and
captions can be framed. The main command is \hvFloat{float
type}{floating object}{caption}{label}; a simple example is
\hvFloat{figure}{\includegraphics{rose}}{Caption}{fig:0}.
Options are included to place captions to the right or left,
and rotated. Setting nonFloat=true results in placing the float
here.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/hvfloat/hvfloat.sty
%doc %{_texmfdistdir}/doc/latex/hvfloat/VERSION-1.1
%doc %{_texmfdistdir}/doc/latex/hvfloat/bateaux.jpg
%doc %{_texmfdistdir}/doc/latex/hvfloat/hvfloat.pdf
%doc %{_texmfdistdir}/doc/latex/hvfloat/hvfloat.tex
%doc %{_texmfdistdir}/doc/latex/hvfloat/rose.eps
%doc %{_texmfdistdir}/doc/latex/hvfloat/rose.png

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
