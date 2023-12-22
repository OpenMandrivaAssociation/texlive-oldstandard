Name:		texlive-oldstandard
Version:	69153
Release:	1
Summary:	Old Standard: A Unicode Font for Classical and Medieval Studies
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/oldstandard
License:	OFL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/oldstandard.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/oldstandard.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Old Standard is designed to reproduce the actual printing style
of the early 20th century, reviving a specific type of Modern
(classicist) style of serif typefaces, very commonly used in
various editions of the late 19th and early 20th century, but
almost completely abandoned later. The font supports
typesetting of Old and Middle English, Old Icelandic, Cyrillic
(with historical characters, extensions for Old Slavonic and
localised forms), Gothic transliterations, critical editions of
Classical Greek and Latin, and many more. Old Standard works
with TeX engines that directly support OpenType features, such
as XeTeX and LuaTeX.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/map/dvips
%{_texmfdistdir}/fonts/enc/dvips
%{_texmfdistdir}/fonts/opentype/public/oldstandard
%{_texmfdistdir}/fonts/tfm/public/oldstandard
%{_texmfdistdir}/fonts/type1/public/oldstandard
%{_texmfdistdir}/fonts/vf/public/oldstandard
%doc %{_texmfdistdir}/doc/fonts/oldstandard

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts doc %{buildroot}%{_texmfdistdir}
