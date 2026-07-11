%global tl_name oldstandard
%global tl_revision 79187

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.7b
Release:	%{tl_revision}.1
Summary:	OldStandard fonts with LaTeX support
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/oldstandard
License:	ofl gfl lppl fdl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/oldstandard.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/oldstandard.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

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

