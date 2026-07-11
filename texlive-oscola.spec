%global tl_name oscola
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.7
Release:	%{tl_revision}.1
Summary:	BibLaTeX style for the Oxford Standard for the Citation of Legal Authorities
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/biblatex-contrib/oscola
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/oscola.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/oscola.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides a set of style files for use with BibLaTeX (v 2+)
and Biber (v 1+) to produce citations and bibliographies in accordance
with the widely-used Oxford Standard for the Citation of Legal
Authorities. It also includes facilities for constructing tables of
cases and legislation from citations (in conjunction with appropriate
indexing packages).

