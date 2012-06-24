#
# Conditional build:
# _without_ssl	- without SSL support
#
Summary:	A utility for getting files from remote servers (FTP, HTTP, and others)
Summary(es):	Busca URL (soporta FTP, TELNET, LDAP, GOPHER, DICT, HTTP y HTTPS)
Summary(pl):	Narz�dzie do �ci�gania plik�w z serwer�w (FTP, HTTP i innych)
Summary(pt_BR):	Busca URL (suporta FTP, TELNET, LDAP, GOPHER, DICT, HTTP e HTTPS)
Summary(ru):	������� ��� ��������� ������ � �������� FTP, HTTP � ������
Summary(uk):	���̦�� ��� ��������� ���̦� � �����Ҧ� FTP, HTTP �� �����
Name:		curl
Version:	7.10.7
Release:	1
License:	MPL
Vendor:		Daniel Stenberg <Daniel.Stenberg@sth.frontec.se>
Group:		Applications/Networking
Source0:	http://curl.haxx.se/download/%{name}-%{version}.tar.bz2
# Source0-md5:	19f2f77279cd5d3026c71997463db791
Patch0:		%{name}-no_strip.patch
URL:		http://curl.haxx.se/
%{!?_without_ssl:BuildRequires:	openssl-devel >= 0.9.7c}
Requires:	openssl-tools >= 0.9.7c
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	libcurl2

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

%description -l es
Curl es un cliente para bajar documentos/archivos de servidores usando
uno de los protocolos soportados. Est� proyectado para funcionar sin
interacci�n del usuario.

Curl trabaja con proxy, autenticaci�n, ftp put, HTTP post, y puede
continuar transferencias interrumpidas, y adem�s...

%description -l pl
cURL jest narz�dziem do �ci�gania plik�w o sk�adni URL. Obs�uguje FTP,
HTTP, HTTPS, GOPHER, TELNET, DICT, FILE i LDAP. cURL obs�uguje r�wnie�
HTTP POST, HTTP PUT, za�adowywanie (uploading) FTP, za�adowywanie HTTP
oparte na formularzu, serwery proksy, ciasteczka, autoryzacja
u�ytkownik/has�o oraz wiele innych u�ytecznych sztuczek. Curla u�ywa
si� g��wnie wtedy, kiedy chce si� automatycznie �ci�gn�� lub wys�a�
pliki z/na serwer u�ywaj�c jednego z dost�pnych protoko��w.
%{!?_without_ssl:Ten pakiet obs�uguje tak�e SSL.}

%description -l pt_BR
Curl � um cliente para baixar/enviar arquivos de/para servidores
usando um dos protocolos suportados. � projetado para funcionar sem a
intera��o do usu�rio.

Curl trabalha com proxy, autentica��o, ftp put, HTTP post, e pode
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

%package devel
Summary:	Header files and development documentation for curl library
Summary(pl):	Pliki nag��wkowe i dokumentacja do biblioteki curl
Summary(pt_BR):	Arquivos de cabe�alho e bibliotecas de desenvolvimento
Summary(ru):	����� ��� ���������� � �������������� ���������� curl
Summary(uk):	����� ��� �������� � ������������� ¦�̦����� curl
Group:		Development/Libraries
Requires:	%{name} = %{version}
%{!?_without_ssl:Requires:	openssl-devel >= 0.9.7c}
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
Requires:	%{name}-devel = %{version}

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

%build
%configure \
	%{!?_without_ssl:--with-ssl=%{_prefix}} \
	%{!?_without_ssl:--with-ca-bundle=/usr/share/ssl/ca-bundle.crt} \
	--with-ipv6

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%{_mandir}/man1/*

%files devel
%defattr(644,root,root,755)
%doc CHANGES README docs/TheArtOfHttpScripting
%doc docs/{BUGS,CONTRIBUTE,FAQ,FEATURES,INTERNALS,MANUAL,README*,RESOURCES,THANKS,TODO}
%attr(755,root,root) %{_bindir}/%{name}-config
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*
%{_mandir}/man3/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
