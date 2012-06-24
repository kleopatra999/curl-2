#
# Conditional build:
%bcond_with	ares	# with c-ares (asynchronous DNS operations) library (disables IPv6)
%bcond_without	ssl	# without SSL support
%bcond_without	heimdal	# without HEIMDAL support
#
Summary:	A utility for getting files from remote servers (FTP, HTTP, and others)
Summary(es):	Un cliente para bajar archivos de servidores (FTP, HTTP, y otros)
Summary(pl):	Narz�dzie do �ci�gania plik�w z serwer�w (FTP, HTTP i innych)
Summary(pt_BR):	Busca URL (suporta FTP, TELNET, LDAP, GOPHER, DICT, HTTP e HTTPS)
Summary(ru):	������� ��� ��������� ������ � �������� FTP, HTTP � ������
Summary(uk):	���̦�� ��� ��������� ���̦� � �����Ҧ� FTP, HTTP �� �����
Name:		curl
Version:	7.15.4
Release:	1
License:	MIT-like
Group:		Applications/Networking
Source0:	http://curl.haxx.se/download/%{name}-%{version}.tar.bz2
# Source0-md5:	d9345a55c8bc67eafcd37fa1b728e00e
Patch0:		%{name}-no_strip.patch
Patch1:		%{name}-ac.patch
Patch2:		%{name}-heimdal.patch
URL:		http://curl.haxx.se/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
%{?with_ares:BuildRequires:	c-ares-devel}
%{?with_heimdal:BuildRequires:	heimdal-devel >= 0.7}
BuildRequires:	libidn-devel >= 0.4.1
BuildRequires:	libtool
%{?with_ssl:BuildRequires:	openssl-devel >= 0.9.7d}
Requires:	%{name}-libs = %{version}-%{release}
Requires:	libidn >= 0.4.1
Requires:	openssl-tools >= 0.9.7d
Obsoletes:	libcurl2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
cURL is a tool for getting files with URL syntax, supporting FTP,
HTTP, HTTPS, GOPHER, TELNET, DICT, FILE and LDAP. cURL supports HTTP
POST, HTTP PUT, FTP uploading, HTTP form based upload, proxies,
cookies, user+password authentication and a busload of other useful
tricks. The main use for curl is when you want to get or send files
automatically to or from a site using one of the supported protocols.

cURL is a tool for getting files from FTP, HTTP, Gopher, Telnet, and
Dict servers, using any of the supported protocols. cURL is designed
to work without user interaction or any kind of interactivity. cURL
offers many useful capabilities, like proxy support, user
authentication, FTP upload, HTTP post, and file transfer resume.

%description -l pl
cURL jest narz�dziem do �ci�gania plik�w o sk�adni URL. Obs�uguje FTP,
HTTP, HTTPS, GOPHER, TELNET, DICT, FILE i LDAP. cURL obs�uguje r�wnie�
HTTP POST, HTTP PUT, za�adowywanie (uploading) FTP, za�adowywanie HTTP
oparte na formularzu, serwery proksy, ciasteczka, autoryzacja
u�ytkownik/has�o oraz wiele innych u�ytecznych sztuczek. Curla u�ywa
si� g��wnie wtedy, kiedy chce si� automatycznie �ci�gn�� lub wys�a�
pliki z/na serwer u�ywaj�c jednego z dost�pnych protoko��w.
%{?with_ssl:Ten pakiet obs�uguje tak�e SSL.}

%description -l pt_BR
Curl � um cliente para baixar/enviar arquivos de/para servidores
usando um dos protocolos suportados. � projetado para funcionar sem a
intera��o do usu�rio.

Curl trabalha com proxy, autentica��o, FTP put, HTTP post, e pode
continuar transfer�ncias interrompidas, e mais...

%description -l ru
curl - ��� ������ � ���������� �������������� ���������� ��� ���������
������ � ��������, ���������������� ��� ������ ��� � ���������������
������, ��� � � ������������ ������� � �������������.

curl ������������ ����� �������� ������������, ����� ������� ���������
������, ����������� ������������, ����������� �� FTP, ��������� HTTP
POST, �������������� ���������� ��������� � ������ ������.

curl - �� �̦��� � �������� Ц������������ ����������� ��� ���������
���̦� � �����Ҧ�, ������������� ��� ������ �� � �Ŧ�������������
����ͦ, ��� � � �����צ��� Ħ����� � ������������.

curl Ц�����դ ������ �������� �����������, ����� ���� Ц�������
����Ӧ, ��������æ� �����������, צ����������� �� FTP, HTTP POST,
צ��������� ��������ϧ ��������� �� ������ ������.

%package libs
Summary:	curl library
Summary(pl):	Biblioteka curl
Group:		Libraries

%description libs
curl library.

%description libs -l pl
Biblioteka curl.

%package devel
Summary:	Header files and development documentation for curl library
Summary(pl):	Pliki nag��wkowe i dokumentacja do biblioteki curl
Summary(pt_BR):	Arquivos de cabe�alho e bibliotecas de desenvolvimento
Summary(ru):	����� ��� ���������� � �������������� ���������� curl
Summary(uk):	����� ��� �������� � ������������� ¦�̦����� curl
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
%{?with_heimdal:Requires:	heimdal-devel}
Requires:	libidn-devel >= 0.4.1
%{?with_ssl:Requires:	openssl-devel >= 0.9.7c}
Obsoletes:	libcurl2-devel

%description devel
Header files and development documentation for curl library.

%description devel -l pl
Pliki nag��wkowe i dokumentacja do biblioteki curl.

%description devel -l pt_BR
Arquivos de cabe�alho e bibliotecas de desenvolvimento.

%description devel -l ru
���� ����� �������� �����, ����������� ��� ���������� �������� �
�������������� ���������� curl.

%description devel -l uk
��� ����� ͦ����� �����, ����Ȧ�Φ ��� �������� ������� �
������������� ¦�̦����� curl.

%package static
Summary:	Static version of curl library
Summary(pl):	Statyczna wersja biblioteki curl
Summary(pt_BR):	Bibliotecas est�ticas para desenvolvimento com o curl
Summary(ru):	����������� ���������� ��� ���������� � �������������� ���������� curl
Summary(uk):	������Φ ¦�̦����� ��� �������� � ������������� ¦�̦����� curl
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static version of curl library.

%description static -l pl
Statyczna wersja biblioteki curl.

%description static -l pt_BR
Bibliotecas est�ticas para desenvolvimento com o curl.

%description static -l ru
���� ����� �������� ����������� ���������� ��� ���������� �������� �
�������������� ���������� curl.

%description static -l uk
��� ����� ͦ����� �������� ¦�̦����� ��� �������� ������� �
������������� ¦�̦����� curl.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%{?with_heimdal:%patch2 -p0}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{?with_ssl:--with-ssl=%{_prefix}} \
	%{?with_ssl:--with-ca-bundle=/usr/share/ssl/ca-bundle.crt} \
	%{?with_heimdal:--with-gssapi=%{_prefix}} \
	%{?with_ares:--enable-ares=%{_prefix}} \
	--%{?with_ares:dis}%{!?with_ares:en}able-ipv6

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc CHANGES COPYING README docs/{BUGS,FAQ,FEATURES,HISTORY,KNOWN_BUGS,MANUAL,SSLCERTS,THANKS,TODO,TheArtOfHttpScripting}
%attr(755,root,root) %{_bindir}/curl
%{_mandir}/man1/curl.1*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcurl.so.*.*.*

%files devel
%defattr(644,root,root,755)
%doc docs/{CONTRIBUTE,INTERNALS,LICENSE-MIXING,RESOURCES}
%attr(755,root,root) %{_bindir}/curl-config
%attr(755,root,root) %{_libdir}/libcurl.so
%{_libdir}/libcurl.la
%{_includedir}/curl
%{_pkgconfigdir}/libcurl.pc
%{_mandir}/man1/curl-config.1*
%{_mandir}/man3/*curl*.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/libcurl.a
