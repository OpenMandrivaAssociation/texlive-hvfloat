Name:		texlive-hvfloat
Version:	73130
Release:	1
Summary:	Rotating caption and object of floats independently
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/hvfloat
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hvfloat.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hvfloat.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package defines a macro to place objects (tables and
figures) and their captions in different positions with
different rotating angles within a float. All objects and
captions can be framed. The main command is \hvFloat{float
type}{floating object}{caption}{label}; a simple example is
\hvFloat{figure}{\includegraphics{rose}}{Caption}{fig:0}.
Options are provided to place captions to the right or left,
and rotated. Setting nonFloat=true results in placing the float
here.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/hvfloat
%doc %{_texmfdistdir}/doc/latex/hvfloat

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
