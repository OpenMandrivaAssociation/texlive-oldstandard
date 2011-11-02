Name:		texlive-oldstandard
Version:	2.0.2
Release:	1
Summary:	Old Standard: A Unicode Font for Classical and Medieval Studies
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/oldstandard
License:	OFL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/oldstandard.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/oldstandard.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/oldstandard.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
Old Standard is supposed to reproduce the actual printing style
of the early 20th century, reviving a specific type of Modern
(classicist) style of serif typefaces, very commonly used in
various editions of the late 19th and early 20th century, but
almost completely abandoned later. It supports typesetting of
Old and Middle English, Old Icelandic, Cyrillic (with
historical characters, extensions for Old Slavonic and
localised forms), Gothic transliterations, critical editions of
Classical Greek and Latin, and many more. Old Standard works
with TeX engines that directly support OpenType features, such
as XeTeX and LuaTeX.

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
%{_texmfdistdir}/fonts/opentype/public/oldstandard/OldStandard-Bold.otf
%{_texmfdistdir}/fonts/opentype/public/oldstandard/OldStandard-Italic.otf
%{_texmfdistdir}/fonts/opentype/public/oldstandard/OldStandard-Regular.otf
%doc %{_texmfdistdir}/doc/fonts/oldstandard/FONTLOG.txt
%doc %{_texmfdistdir}/doc/fonts/oldstandard/OFL-FAQ.txt
%doc %{_texmfdistdir}/doc/fonts/oldstandard/OFL.txt
%doc %{_texmfdistdir}/doc/fonts/oldstandard/README
%doc %{_texmfdistdir}/doc/fonts/oldstandard/didot-de.png
%doc %{_texmfdistdir}/doc/fonts/oldstandard/didot-fr.png
%doc %{_texmfdistdir}/doc/fonts/oldstandard/gendocs.sh
%doc %{_texmfdistdir}/doc/fonts/oldstandard/genfonts.sh
%doc %{_texmfdistdir}/doc/fonts/oldstandard/greek-contextual.png
%doc %{_texmfdistdir}/doc/fonts/oldstandard/oldstand-manual.pdf
%doc %{_texmfdistdir}/doc/fonts/oldstandard/oldstand-manual.tex
%doc %{_texmfdistdir}/doc/fonts/oldstandard/opentype.png
%doc %{_texmfdistdir}/doc/fonts/oldstandard/ost-generate.py
%doc %{_texmfdistdir}/doc/fonts/oldstandard/serbian.png
%doc %{_texmfdistdir}/doc/fonts/oldstandard/spadmin-add.png
%doc %{_texmfdistdir}/doc/fonts/oldstandard/spadmin.png
%doc %{_texmfdistdir}/doc/fonts/oldstandard/stand-su.png
%doc %{_texmfdistdir}/doc/fonts/oldstandard/teubner.png
%doc %{_texmfdistdir}/doc/fonts/oldstandard/truetype.png
#- source
%doc %{_texmfdistdir}/source/fonts/oldstandard/OldStandard-Bold.sfd
%doc %{_texmfdistdir}/source/fonts/oldstandard/OldStandard-Italic.sfd
%doc %{_texmfdistdir}/source/fonts/oldstandard/OldStandard-Regular.sfd

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts doc source %{buildroot}%{_texmfdistdir}
