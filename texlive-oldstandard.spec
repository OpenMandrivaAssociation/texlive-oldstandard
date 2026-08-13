%global tl_name oldstandard
%global tl_revision 79187
%global tl_version 2.7b

Name:		texlive-%{tl_name}
Epoch:		1
Version:	%{tl_version}
Release:	%{tl_revision}.1
Summary:	OldStandard fonts with LaTeX support
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/oldstandard
License:	ofl gfl lppl fdl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/oldstandard.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/oldstandard.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{version}

%description
Old Standard is designed to reproduce the actual printing style of the
early 20th century, reviving a specific type of Modern (classicist)
style of serif typefaces, very commonly used in various editions of the
late 19th and early 20th century, but almost completely abandoned later.
The font supports typesetting of Old and Middle English, Old Icelandic,
Cyrillic (with historical characters, extensions for Old Slavonic and
localised forms), Gothic transliterations, critical editions of
Classical Greek and Latin, and many more. This package works with TeX
engines that directly support OpenType features, such as XeTeX and
LuaTeX, as well as traditional engines such as TeX and pdfTeX.


%install -a
mkdir -p %{buildroot}%{_texmf_updmap_d}
cat > %{buildroot}%{_texmf_updmap_d}/%{tl_name} <<'TL_DROPIN_EOF'
# from oldstandard:
Map OldStandard.map
TL_DROPIN_EOF
