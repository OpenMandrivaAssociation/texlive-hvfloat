# revision 25570
# category Package
# catalog-ctan /macros/latex/contrib/hvfloat
# catalog-date 2012-03-05 13:21:26 +0100
# catalog-license lppl
# catalog-version 1.1
Name:		texlive-hvfloat
Version:	1.1
Release:	7
Summary:	Rotating caption and object of floats independently
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/hvfloat
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hvfloat.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hvfloat.doc.tar.xz
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
%{_texmfdistdir}/tex/latex/hvfloat/hvfloat.sty
%doc %{_texmfdistdir}/doc/latex/hvfloat/README
%doc %{_texmfdistdir}/doc/latex/hvfloat/bateaux.jpg
%doc %{_texmfdistdir}/doc/latex/hvfloat/hvfloat.pdf
%doc %{_texmfdistdir}/doc/latex/hvfloat/hvfloat.tex
%doc %{_texmfdistdir}/doc/latex/hvfloat/rose.png

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Fri Mar 09 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.1-4
+ Revision: 783462
- rebuild without scriptlet dependencies

* Wed Mar 07 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.1-3
+ Revision: 783007
- Update to latest release.

* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.1-2
+ Revision: 752587
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.1-1
+ Revision: 718625
- texlive-hvfloat
- texlive-hvfloat
- texlive-hvfloat
- texlive-hvfloat

