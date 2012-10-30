# revision 27490
# category Package
# catalog-ctan /macros/latex/contrib/biblatex-contrib/oscola
# catalog-date 2012-08-20 08:49:07 +0200
# catalog-license lppl1.3
# catalog-version 1
Name:		texlive-oscola
Version:	1
Release:	1
Summary:	BibLaTeX style for the Oxford Standard for the Citation of Legal Authorities
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/biblatex-contrib/oscola
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/oscola.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/oscola.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides a set of style files for use with Biblatex
(v 2+) and Biber (v 1+) to produce citations and bibliographies
in accordance with the widely-used Oxford Standard for the
Citation of Legal Authorities. It also includes facilities for
constructing tables of cases and legislation from citations (in
conjunction with appropriate indexing packages).

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/makeindex/oscola/oscola.ist
%{_texmfdistdir}/tex/latex/oscola/english-oscola.lbx
%{_texmfdistdir}/tex/latex/oscola/oscola.bbx
%{_texmfdistdir}/tex/latex/oscola/oscola.cbx
%doc %{_texmfdistdir}/doc/latex/oscola/README
%doc %{_texmfdistdir}/doc/latex/oscola/README.TEXLIVE
%doc %{_texmfdistdir}/doc/latex/oscola/oscola-examples.bib

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar makeindex tex doc %{buildroot}%{_texmfdistdir}