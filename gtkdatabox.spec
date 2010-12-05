%define api 0.9.1
%define major 1
%define libname %mklibname %{name} %{api} %{major}
%define develname %mklibname %{name} -d

Summary:	A Gtk+-Widget for Fast Data Display
Name:		gtkdatabox
Version:	0.9.1.1
Release:	%mkrel 2
License:	LGPLv2+
Group:		System/Libraries
URL:		http://www.eudoxos.net/gtk/gtkdatabox/
Source0:	http://www.eudoxos.net/gtk/gtkdatabox/download/%name-%version.tar.gz
Patch0:		gtkdatabox-0.9.0.1-linkage.patch
BuildRequires:	gtk+2-devel
BuildRequires:	gtk-doc
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
GtkDatabox is a widget for the Gtk+-library designed to display large
amounts of numerical data fast and easy. One or more data sets of
thousands of data points (X and Y coordinate) may be displayed and
updated in split seconds. The widget is therfore used in many scientific
and private projects that need to show quickly changing data "live".

GtkDatabox offers the ability to zoom into and out of the data and to
navigate through your data by scrolling. In addition to rulers and
a simple coordinate cross, GtkDatabox now also allows you to add one
(or even more) configurable grids like on an oscilloscope.

%package -n %{libname}
Summary:	A Gtk+-Widget for Fast Data Display
Group:		System/Libraries

%description -n	%{libname}
GtkDatabox is a widget for the Gtk+-library designed to display large
amounts of numerical data fast and easy. 

%package -n %{develname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n	%{develname}
This package contains all necessary files to compile or develop
programs/libraries that use %{name}.

%prep
%setup -q
%patch0 -p0

%build
autoreconf -fi
%configure2_5x --disable-static
%make

%install
rm -rf %{buildroot}
%makeinstall_std

rm -f %buildroot%{_libdir}/*.la

%clean
rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/lib%{name}-%{api}.so.%{major}
%{_libdir}/lib%{name}-%{api}.so.%{major}.*

%files -n %{develname}
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_datadir}/gtk-doc/html/%name
