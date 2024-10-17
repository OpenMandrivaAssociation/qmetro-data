Summary:	Maps for qMetro
Name:		qmetro-data
Version:	0
Release:	2
License:	GPLv2+
Group:		Sciences/Geosciences
Url:		https://pmetro.su/Maps.html
# Pack all maps into one tarball
Source0:	%{name}.tar.bz2
BuildArch:	noarch

%description
Maps for the qMetro program.

#----------------------------------------------------------------------------

%package Algeria
Summary:	Metro Maps (Algeria)
Group:		Sciences/Geosciences
Requires:	qmetro

%description Algeria
Maps for the qMetro program (Algeria).

Cities: Algiers.

%files Algeria
%{_datadir}/qmetro/map/Algiers.pmz

#----------------------------------------------------------------------------

%package Argentina
Summary:	Metro Maps (Argentina)
Group:		Sciences/Geosciences
Requires:	qmetro

%description Argentina
Maps for the qMetro program (Argentina).

Cities: Buenos Aires.

%files Argentina
%{_datadir}/qmetro/map/Buenos-Aires.pmz

#----------------------------------------------------------------------------

%package Armenia
Summary:	Metro Maps (Armenia)
Group:		Sciences/Geosciences
Requires:	qmetro

%description Armenia
Maps for the qMetro program (Armenia).

Cities: Yerevan.

%files Armenia
%{_datadir}/qmetro/map/Erevan.pmz

#----------------------------------------------------------------------------

%package Australia
Summary:	Metro Maps (Australia)
Group:		Sciences/Geosciences
Requires:	qmetro

%description Australia
Maps for the qMetro program (Australia).

Cities: Sydney.

%files Australia
%{_datadir}/qmetro/map/Sydney.pmz

#----------------------------------------------------------------------------

%package Austria
Summary:	Metro Maps (Austria)
Group:		Sciences/Geosciences
Requires:	qmetro

%description Austria
Maps for the qMetro program (Austria).

Cities: Vienna, Linz, Serfaus.

%files Austria
%{_datadir}/qmetro/map/Wienn.pmz
%{_datadir}/qmetro/map/Linz.pmz
%{_datadir}/qmetro/map/Serfaus.pmz

#----------------------------------------------------------------------------

%package Azerbaijan
Summary:	Metro Maps (Azerbaijan)
Group:		Sciences/Geosciences
Requires:	qmetro

%description Azerbaijan
Maps for the qMetro program (Azerbaijan).

Cities: Baku.

%files Azerbaijan
%{_datadir}/qmetro/map/Baku.pmz

#----------------------------------------------------------------------------

%package Belarus
Summary:	Metro Maps (Belarus)
Group:		Sciences/Geosciences
Requires:	qmetro

%description Belarus
Maps for the qMetro program (Belarus).

Cities: Minsk.

%files Belarus
%{_datadir}/qmetro/map/Minsk.pmz

#----------------------------------------------------------------------------

%package Belgium
Summary:	Metro Maps (Belgium)
Group:		Sciences/Geosciences
Requires:	qmetro

%description Belgium
Maps for the qMetro program (Belgium).

Cities: Brussels, Antwerp, Charleroi.

%files Belgium
%{_datadir}/qmetro/map/Brussels.pmz
%{_datadir}/qmetro/map/Antwerpen.pmz
%{_datadir}/qmetro/map/Charleroi.pmz

#----------------------------------------------------------------------------

%package Brazil
Summary:	Metro Maps (Brazil)
Group:		Sciences/Geosciences
Requires:	qmetro

%description Brazil
Maps for the qMetro program (Brazil).

Cities: São Paulo, Belo Horizonte, Rio de Janeiro, Brasília, Recife,
Porto Alegre, Teresina, Salvador, Fortaleza.

%files Brazil
%{_datadir}/qmetro/map/San-Paulo.pmz
%{_datadir}/qmetro/map/Belo-Horizonte.pmz
%{_datadir}/qmetro/map/Rio-De-Janeiro.pmz
%{_datadir}/qmetro/map/Brasilia.pmz
%{_datadir}/qmetro/map/Recife.pmz
%{_datadir}/qmetro/map/Porto-Alegre.pmz
%{_datadir}/qmetro/map/Teresina.pmz
%{_datadir}/qmetro/map/Salvador.pmz
%{_datadir}/qmetro/map/Fortaleza.pmz

#----------------------------------------------------------------------------

%package Bulgaria
Summary:	Metro Maps (Bulgaria)
Group:		Sciences/Geosciences
Requires:	qmetro

%description Bulgaria
Maps for the qMetro program (Bulgaria).

Cities: Sofia.

%files Bulgaria
%{_datadir}/qmetro/map/Sofia.pmz

#----------------------------------------------------------------------------

%package Canada
Summary:	Metro Maps (Canada)
Group:		Sciences/Geosciences
Requires:	qmetro

%description Canada
Maps for the qMetro program (Canada).

Cities: Toronto, Montreal, Vancouver, Edmonton, Calgary, Ottawa.

%files Canada
%{_datadir}/qmetro/map/Toronto.pmz
%{_datadir}/qmetro/map/Montreal.pmz
%{_datadir}/qmetro/map/Vancouver.pmz
%{_datadir}/qmetro/map/Edmonton.pmz
%{_datadir}/qmetro/map/Calgary.pmz
%{_datadir}/qmetro/map/Ottawa.pmz

#----------------------------------------------------------------------------

%package Chile
Summary:	Metro Maps (Chile)
Group:		Sciences/Geosciences
Requires:	qmetro

%description Chile
Maps for the qMetro program (Chile).

Cities: Santiago, Valparaíso.

%files Chile
%{_datadir}/qmetro/map/Santiago.pmz
%{_datadir}/qmetro/map/Valparaiso.pmz

#----------------------------------------------------------------------------

%package China
Summary:	Metro Maps (China)
Group:		Sciences/Geosciences
Requires:	qmetro

%description China
Maps for the qMetro program (China).

Cities: Beijing, Hong Kong, Chongqing, Nanjing, Shenzhen, Wuhan,
Tianjin, Guangzhou, Shanghai, Dalian, Shenyang, Kunming, Chengdu,
Hangzhou, Suzhou, Xi'an.

%files China
%{_datadir}/qmetro/map/Beijing.pmz
%{_datadir}/qmetro/map/Hong-Kong.pmz
%{_datadir}/qmetro/map/Chongqing.pmz
%{_datadir}/qmetro/map/Nanjing.pmz
%{_datadir}/qmetro/map/Shenzhen.pmz
%{_datadir}/qmetro/map/Wuhan.pmz
%{_datadir}/qmetro/map/Tianjin.pmz
%{_datadir}/qmetro/map/Guangzhou.pmz
%{_datadir}/qmetro/map/Shanghai.pmz
%{_datadir}/qmetro/map/Dalian.pmz
%{_datadir}/qmetro/map/Shenyang.pmz
%{_datadir}/qmetro/map/Kunming.pmz
%{_datadir}/qmetro/map/Chengdu.pmz
%{_datadir}/qmetro/map/Hangzhou.pmz
%{_datadir}/qmetro/map/Suzhou.pmz
%{_datadir}/qmetro/map/Xi'an.pmz

#----------------------------------------------------------------------------

%package Colombia
Summary:	Metro Maps (Colombia)
Group:		Sciences/Geosciences
Requires:	qmetro

%description Colombia
Maps for the qMetro program (Colombia).

Cities: Medellín.

%files Colombia
%{_datadir}/qmetro/map/Medellin.pmz

#----------------------------------------------------------------------------

%package CzechRepublic
Summary:	Metro Maps (Czech Republic)
Group:		Sciences/Geosciences
Requires:	qmetro

%description CzechRepublic
Maps for the qMetro program (Czech Republic).

Cities: Prague.

%files CzechRepublic
%{_datadir}/qmetro/map/Praha.pmz

#----------------------------------------------------------------------------

%package Denmark
Summary:	Metro Maps (Denmark)
Group:		Sciences/Geosciences
Requires:	qmetro

%description Denmark
Maps for the qMetro program (Denmark).

Cities: Copenhagen.

%files Denmark
%{_datadir}/qmetro/map/Copenhagen.pmz

#----------------------------------------------------------------------------

%package DominicanRepublic
Summary:	Metro Maps (Dominican Republic)
Group:		Sciences/Geosciences
Requires:	qmetro

%description DominicanRepublic
Maps for the qMetro program (Dominican Republic).

Cities: Santo Domingo.

%files DominicanRepublic
%{_datadir}/qmetro/map/Santo-Domingo.pmz

#----------------------------------------------------------------------------

%package Egypt
Summary:	Metro Maps (Egypt)
Group:		Sciences/Geosciences
Requires:	qmetro

%description Egypt
Maps for the qMetro program (Egypt).

Cities: Cairo, Alexandria.

%files Egypt
%{_datadir}/qmetro/map/Cairo.pmz
%{_datadir}/qmetro/map/Alexandria.pmz

#----------------------------------------------------------------------------

%package Finland
Summary:	Metro Maps (Finland)
Group:		Sciences/Geosciences
Requires:	qmetro

%description Finland
Maps for the qMetro program (Finland).

Cities: Helsinki.

%files Finland
%{_datadir}/qmetro/map/Helsinki.pmz

#----------------------------------------------------------------------------

%package France
Summary:	Metro Maps (France)
Group:		Sciences/Geosciences
Requires:	qmetro

%description France
Maps for the qMetro program (France).

Cities: Paris, Marseille, Toulouse, Rouen, Rennes, Lyon, Lille,
Strasbourg.

%files France
%{_datadir}/qmetro/map/Paris.pmz
%{_datadir}/qmetro/map/Marseille.pmz
%{_datadir}/qmetro/map/Toulouse.pmz
%{_datadir}/qmetro/map/Rouen.pmz
%{_datadir}/qmetro/map/Rennes.pmz
%{_datadir}/qmetro/map/Lyon.pmz
%{_datadir}/qmetro/map/Lille.pmz
%{_datadir}/qmetro/map/Strasbourg.pmz

#----------------------------------------------------------------------------

%package Georgia
Summary:	Metro Maps (Georgia)
Group:		Sciences/Geosciences
Requires:	qmetro

%description Georgia
Maps for the qMetro program (Georgia).

Cities: Tbilisi.

%files Georgia
%{_datadir}/qmetro/map/Tbilisi.pmz

#----------------------------------------------------------------------------

%package Germany
Summary:	Metro Maps (Germany)
Group:		Sciences/Geosciences
Requires:	qmetro

%description Germany
Maps for the qMetro program (Germany).

Cities: Berlin, Nuremberg, Wuppertal, Hamburg, Munich, Bielefeld,
Bochum, Frankfurt am Main, Stuttgart, Essen, Düsseldorf, Dortmund,
Hanover, Bonn-Cologne.

%files Germany
%{_datadir}/qmetro/map/Berlin.pmz
%{_datadir}/qmetro/map/Nurnberg.pmz
%{_datadir}/qmetro/map/Wuppertal.pmz
%{_datadir}/qmetro/map/Hamburg.pmz
%{_datadir}/qmetro/map/Munich.pmz
%{_datadir}/qmetro/map/Bielefeld.pmz
%{_datadir}/qmetro/map/Bochum.pmz
%{_datadir}/qmetro/map/Frankfurt.pmz
%{_datadir}/qmetro/map/Stuttgart.pmz
%{_datadir}/qmetro/map/Essen.pmz
%{_datadir}/qmetro/map/Dusseldorf.pmz
%{_datadir}/qmetro/map/Dortmund.pmz
%{_datadir}/qmetro/map/Hannover.pmz
%{_datadir}/qmetro/map/Bonn-Koln.pmz

#----------------------------------------------------------------------------

%package Greece
Summary:	Metro Maps (Greece)
Group:		Sciences/Geosciences
Requires:	qmetro

%description Greece
Maps for the qMetro program (Greece).

Cities: Athens.

%files Greece
%{_datadir}/qmetro/map/Athenas.pmz

#----------------------------------------------------------------------------

%package Hungary
Summary:	Metro Maps (Hungary)
Group:		Sciences/Geosciences
Requires:	qmetro

%description Hungary
Maps for the qMetro program (Hungary).

Cities: Budapest.

%files Hungary
%{_datadir}/qmetro/map/Budapest.pmz

#----------------------------------------------------------------------------

%package India
Summary:	Metro Maps (India)
Group:		Sciences/Geosciences
Requires:	qmetro

%description India
Maps for the qMetro program (India).

Cities: Delhi, Kolkata, Chennai, Mumbai, Bangalore.

%files India
%{_datadir}/qmetro/map/Delhi.pmz
%{_datadir}/qmetro/map/Calcutta.pmz
%{_datadir}/qmetro/map/Chennai.pmz
%{_datadir}/qmetro/map/Mumbai.pmz
%{_datadir}/qmetro/map/Bangalore.pmz

#----------------------------------------------------------------------------

%package Iran
Summary:	Metro Maps (Iran)
Group:		Sciences/Geosciences
Requires:	qmetro

%description Iran
Maps for the qMetro program (Iran).

Cities: Tehran, Mashhad.

%files Iran
%{_datadir}/qmetro/map/Tehran.pmz
%{_datadir}/qmetro/map/Mashhad.pmz

#----------------------------------------------------------------------------

%package Israel
Summary:	Metro Maps (Israel)
Group:		Sciences/Geosciences
Requires:	qmetro

%description Israel
Maps for the qMetro program (Israel).

Cities: Haifa.

%files Israel
%{_datadir}/qmetro/map/Haifa.pmz

#----------------------------------------------------------------------------

%package Italy
Summary:	Metro Maps (Italy)
Group:		Sciences/Geosciences
Requires:	qmetro

%description Italy
Maps for the qMetro program (Italy).

Cities: Rome, Naples, Genoa, Milan, Catania, Turin, Perugia, Brescia.

%files Italy
%{_datadir}/qmetro/map/Roma.pmz
%{_datadir}/qmetro/map/Napoli.pmz
%{_datadir}/qmetro/map/Genova.pmz
%{_datadir}/qmetro/map/Milano.pmz
%{_datadir}/qmetro/map/Catania.pmz
%{_datadir}/qmetro/map/Torino.pmz
%{_datadir}/qmetro/map/Perugia.pmz
%{_datadir}/qmetro/map/Brescia.pmz

#----------------------------------------------------------------------------

%package Japan
Summary:	Metro Maps (Japan)
Group:		Sciences/Geosciences
Requires:	qmetro

%description Japan
Maps for the qMetro program (Japan).

Cities: Tokyo, Yokohama, Kobe, Sapporo, Naha, Hiroshima, Kitakyūshū,
Sendai, Fukuoka, Kyoto, Nagoya, Osaka.

%files Japan
%{_datadir}/qmetro/map/Tokyo.pmz
%{_datadir}/qmetro/map/Yokohama.pmz
%{_datadir}/qmetro/map/Kobe.pmz
%{_datadir}/qmetro/map/Sapporo.pmz
%{_datadir}/qmetro/map/Naha.pmz
%{_datadir}/qmetro/map/Hiroshima.pmz
%{_datadir}/qmetro/map/Kitakyushu.pmz
%{_datadir}/qmetro/map/Sendai.pmz
%{_datadir}/qmetro/map/Fukuoka.pmz
%{_datadir}/qmetro/map/Kyoto.pmz
%{_datadir}/qmetro/map/Nagoya.pmz
%{_datadir}/qmetro/map/Osaka.pmz

#----------------------------------------------------------------------------

%package Kazakhstan
Summary:	Metro Maps (Kazakhstan)
Group:		Sciences/Geosciences
Requires:	qmetro

%description Kazakhstan
Maps for the qMetro program (Kazakhstan).

Cities: Almaty.

%files Kazakhstan
%{_datadir}/qmetro/map/Almati.pmz

#----------------------------------------------------------------------------

%package Malaysia
Summary:	Metro Maps (Malaysia)
Group:		Sciences/Geosciences
Requires:	qmetro

%description Malaysia
Maps for the qMetro program (Malaysia).

Cities: Kuala Lumpur.

%files Malaysia
%{_datadir}/qmetro/map/Kuala-Lumpur.pmz

#----------------------------------------------------------------------------

%package Mexico
Summary:	Metro Maps (Mexico)
Group:		Sciences/Geosciences
Requires:	qmetro

%description Mexico
Maps for the qMetro program (Mexico).

Cities: Mexico City, Monterrey, Guadalajara.

%files Mexico
%{_datadir}/qmetro/map/Mexico.pmz
%{_datadir}/qmetro/map/Monterrey.pmz
%{_datadir}/qmetro/map/Guadalajara.pmz

#----------------------------------------------------------------------------

%package Netherlands
Summary:	Metro Maps (Netherlands)
Group:		Sciences/Geosciences
Requires:	qmetro

%description Netherlands
Maps for the qMetro program (Netherlands).

Cities: Amsterdam, Rotterdam, Utrecht, The Hague.

%files Netherlands
%{_datadir}/qmetro/map/Amsterdam.pmz
%{_datadir}/qmetro/map/Rotterdam.pmz
%{_datadir}/qmetro/map/Utrecht.pmz
%{_datadir}/qmetro/map/Den-Haag.pmz

#----------------------------------------------------------------------------

%package NorthKorea
Summary:	Metro Maps (North Korea)
Group:		Sciences/Geosciences
Requires:	qmetro

%description NorthKorea
Maps for the qMetro program (North Korea).

Cities: Pyongyang.

%files NorthKorea
%{_datadir}/qmetro/map/Pyongyang.pmz

#----------------------------------------------------------------------------

%package Norway
Summary:	Metro Maps (Norway)
Group:		Sciences/Geosciences
Requires:	qmetro

%description Norway
Maps for the qMetro program (Norway).

Cities: Oslo.

%files Norway
%{_datadir}/qmetro/map/Oslo.pmz

#----------------------------------------------------------------------------

%package Peru
Summary:	Metro Maps (Peru)
Group:		Sciences/Geosciences
Requires:	qmetro

%description Peru
Maps for the qMetro program (Peru).

Cities: Lima.

%files Peru
%{_datadir}/qmetro/map/Lima.pmz

#----------------------------------------------------------------------------

%package Philippines
Summary:	Metro Maps (Philippines)
Group:		Sciences/Geosciences
Requires:	qmetro

%description Philippines
Maps for the qMetro program (Philippines).

Cities: Manila.

%files Philippines
%{_datadir}/qmetro/map/Manila.pmz

#----------------------------------------------------------------------------

%package Poland
Summary:	Metro Maps (Poland)
Group:		Sciences/Geosciences
Requires:	qmetro

%description Poland
Maps for the qMetro program (Poland).

Cities: Warsaw, Gdańsk, Poznań.

%files Poland
%{_datadir}/qmetro/map/Warsaw.pmz
%{_datadir}/qmetro/map/Gdansk.pmz
%{_datadir}/qmetro/map/Poznan.pmz

#----------------------------------------------------------------------------

%package Portugal
Summary:	Metro Maps (Portugal)
Group:		Sciences/Geosciences
Requires:	qmetro

%description Portugal
Maps for the qMetro program (Portugal).

Cities: Lisbon, Porto.

%files Portugal
%{_datadir}/qmetro/map/Lisboa.pmz
%{_datadir}/qmetro/map/Porto.pmz

#----------------------------------------------------------------------------

%package PuertoRico
Summary:	Metro Maps (Puerto Rico)
Group:		Sciences/Geosciences
Requires:	qmetro

%description PuertoRico
Maps for the qMetro program (Puerto Rico).

Cities: San Juan.

%files PuertoRico
%{_datadir}/qmetro/map/San-Juan.pmz

#----------------------------------------------------------------------------

%package Romania
Summary:	Metro Maps (Romania)
Group:		Sciences/Geosciences
Requires:	qmetro

%description Romania
Maps for the qMetro program (Romania).

Cities: Bucharest.

%files Romania
%{_datadir}/qmetro/map/Bucarest.pmz

#----------------------------------------------------------------------------

%package Russia
Summary:	Metro Maps (Russia)
Group:		Sciences/Geosciences
Requires:	qmetro

%description Russia
Maps for the qMetro program (Russia).

Cities: Moscow, Saint Petersburg, Novosibirsk, Nizhny Novgorod, Ekaterinburg,
Samara, Kazan, Volgograd.

%files Russia
%{_datadir}/qmetro/map/Moscow.pmz
%{_datadir}/qmetro/map/Peterburg.pmz
%{_datadir}/qmetro/map/Novosibirsk.pmz
%{_datadir}/qmetro/map/NNovgorod.pmz
%{_datadir}/qmetro/map/Ekaterinburg.pmz
%{_datadir}/qmetro/map/Samara.pmz
%{_datadir}/qmetro/map/Kazan.pmz
%{_datadir}/qmetro/map/Volgograd.pmz

#----------------------------------------------------------------------------

%package SaudiArabia
Summary:	Metro Maps (Saudi Arabia)
Group:		Sciences/Geosciences
Requires:	qmetro

%description SaudiArabia
Maps for the qMetro program (Saudi Arabia).

Cities: Mecca.

%files SaudiArabia
%{_datadir}/qmetro/map/Mecca.pmz

#----------------------------------------------------------------------------

%package Singapore
Summary:	Metro Maps (Singapore)
Group:		Sciences/Geosciences
Requires:	qmetro

%description Singapore
Maps for the qMetro program (Singapore).

%files Singapore
%{_datadir}/qmetro/map/Singapore.pmz

#----------------------------------------------------------------------------

%package SouthKorea
Summary:	Metro Maps (South Korea)
Group:		Sciences/Geosciences
Requires:	qmetro

%description SouthKorea
Maps for the qMetro program (South Korea).

Cities: Seoul, Daegu, Busan, Gwangju, Incheon, Daejeon, Uijeongbu.

%files SouthKorea
%{_datadir}/qmetro/map/Seoul.pmz
%{_datadir}/qmetro/map/Daegu.pmz
%{_datadir}/qmetro/map/Busan.pmz
%{_datadir}/qmetro/map/Gwangju.pmz
%{_datadir}/qmetro/map/Incheon.pmz
%{_datadir}/qmetro/map/Daejeon.pmz
%{_datadir}/qmetro/map/Uijeongbu.pmz

#----------------------------------------------------------------------------

%package Spain
Summary:	Metro Maps (Spain)
Group:		Sciences/Geosciences
Requires:	qmetro

%description Spain
Maps for the qMetro program (Spain).

Cities: Madrid, Barcelona, Bilbao, Valencia, Palma, Alicante, Seville.

%files Spain
%{_datadir}/qmetro/map/Madrid.pmz
%{_datadir}/qmetro/map/Barcelona.pmz
%{_datadir}/qmetro/map/Bilbao.pmz
%{_datadir}/qmetro/map/Valencia.pmz
%{_datadir}/qmetro/map/Palma.pmz
%{_datadir}/qmetro/map/Alicante.pmz
%{_datadir}/qmetro/map/Sevilla.pmz

#----------------------------------------------------------------------------

%package Sweden
Summary:	Metro Maps (Sweden)
Group:		Sciences/Geosciences
Requires:	qmetro

%description Sweden
Maps for the qMetro program (Sweden).

Cities: Stockholm.

%files Sweden
%{_datadir}/qmetro/map/Stockholm.pmz

#----------------------------------------------------------------------------

%package Switzerland
Summary:	Metro Maps (Switzerland)
Group:		Sciences/Geosciences
Requires:	qmetro

%description Switzerland
Maps for the qMetro program (Switzerland).

Cities: Lausanne.

%files Switzerland
%{_datadir}/qmetro/map/Lausanne.pmz

#----------------------------------------------------------------------------

%package Taiwan
Summary:	Metro Maps (Taiwan)
Group:		Sciences/Geosciences
Requires:	qmetro

%description Taiwan
Maps for the qMetro program (Taiwan).

Cities: Taipei, Kaohsiung.

%files Taiwan
%{_datadir}/qmetro/map/Taipei.pmz
%{_datadir}/qmetro/map/Kaohsiung.pmz

#----------------------------------------------------------------------------

%package Thailand
Summary:	Metro Maps (Thailand)
Group:		Sciences/Geosciences
Requires:	qmetro

%description Thailand
Maps for the qMetro program (Thailand).

Cities: Bangkok.

%files Thailand
%{_datadir}/qmetro/map/Bangkok.pmz

#----------------------------------------------------------------------------

%package Tunisia
Summary:	Metro Maps (Tunisia)
Group:		Sciences/Geosciences
Requires:	qmetro

%description Tunisia
Maps for the qMetro program (Tunisia).

Cities: Tunis.

%files Tunisia
%{_datadir}/qmetro/map/Tunis.pmz

#----------------------------------------------------------------------------

%package Turkey
Summary:	Metro Maps (Turkey)
Group:		Sciences/Geosciences
Requires:	qmetro

%description Turkey
Maps for the qMetro program (Turkey).

Cities: Istanbul, Ankara, Izmir, Bursa, Adana.

%files Turkey
%{_datadir}/qmetro/map/Istanbul.pmz
%{_datadir}/qmetro/map/Ankara.pmz
%{_datadir}/qmetro/map/Izmir.pmz
%{_datadir}/qmetro/map/Bursa.pmz
%{_datadir}/qmetro/map/Adana.pmz

#----------------------------------------------------------------------------

%package UAE
Summary:	Metro Maps (United Arab Emirates)
Group:		Sciences/Geosciences
Requires:	qmetro

%description UAE
Maps for the qMetro program (United Arab Emirates).

Cities: Dubai.

%files UAE
%{_datadir}/qmetro/map/Dubai.pmz

#----------------------------------------------------------------------------

%package Ukraine
Summary:	Metro Maps (Ukraine)
Group:		Sciences/Geosciences
Requires:	qmetro

%description Ukraine
Maps for the qMetro program (Ukraine).

Cities: Kiev, Kharkiv, Dnipropetrovsk, Kryvyi Rih.

%files Ukraine
%{_datadir}/qmetro/map/Kiev.pmz
%{_datadir}/qmetro/map/Kharkov.pmz
%{_datadir}/qmetro/map/Dnepropetrovsk.pmz
%{_datadir}/qmetro/map/KrivoyRog.pmz

#----------------------------------------------------------------------------

%package UnitedKingdom
Summary:	Metro Maps (United Kingdom)
Group:		Sciences/Geosciences
Requires:	qmetro

%description UnitedKingdom
Maps for the qMetro program (United Kingdom).

Cities: London, Glasgow, Newcastle, Birmingham, Liverpool, Manchester.

%files UnitedKingdom
%{_datadir}/qmetro/map/London.pmz
%{_datadir}/qmetro/map/Glasgow.pmz
%{_datadir}/qmetro/map/Newcastle.pmz
%{_datadir}/qmetro/map/Birmingham.pmz
%{_datadir}/qmetro/map/Liverpool.pmz
%{_datadir}/qmetro/map/Manchester.pmz

#----------------------------------------------------------------------------

%package USA
Summary:	Metro Maps (USA)
Group:		Sciences/Geosciences
Requires:	qmetro

%description USA
Maps for the qMetro program (USA).

Cities: Washington, New York, Chicago, Atlanta, Miami, Baltimore,
Detroit, San Francisco, Cleveland, Buffalo, Jacksonville, Las Vegas,
Salt Lake City, St. Louis, Minneapolis, Philadelphia, Los Angeles,
Houston, Newark, Boston, Dallas, Denver, San Diego, Sacramento,
San Jose, Portland, Pittsburgh, Jersey City.

%files USA
%{_datadir}/qmetro/map/Washington.pmz
%{_datadir}/qmetro/map/New-York.pmz
%{_datadir}/qmetro/map/Chicago.pmz
%{_datadir}/qmetro/map/Atlanta.pmz
%{_datadir}/qmetro/map/Miami.pmz
%{_datadir}/qmetro/map/Baltimore.pmz
%{_datadir}/qmetro/map/Detroit.pmz
%{_datadir}/qmetro/map/San-Francisco.pmz
%{_datadir}/qmetro/map/Cleveland.pmz
%{_datadir}/qmetro/map/Buffalo.pmz
%{_datadir}/qmetro/map/Jacksonville.pmz
%{_datadir}/qmetro/map/Las-Vegas.pmz
%{_datadir}/qmetro/map/Salt-Lake-City.pmz
%{_datadir}/qmetro/map/Saint-Louis.pmz
%{_datadir}/qmetro/map/Minneapolis.pmz
%{_datadir}/qmetro/map/Philadelphia.pmz
%{_datadir}/qmetro/map/Los-Angeles.pmz
%{_datadir}/qmetro/map/Houston.pmz
%{_datadir}/qmetro/map/Newark.pmz
%{_datadir}/qmetro/map/Boston.pmz
%{_datadir}/qmetro/map/Dallas.pmz
%{_datadir}/qmetro/map/Denver.pmz
%{_datadir}/qmetro/map/San-Diego.pmz
%{_datadir}/qmetro/map/Sacramento.pmz
%{_datadir}/qmetro/map/San-Jose.pmz
%{_datadir}/qmetro/map/Portland.pmz
%{_datadir}/qmetro/map/Pittsburgh.pmz
%{_datadir}/qmetro/map/Charlotte.pmz
%{_datadir}/qmetro/map/Jersey-City.pmz

#----------------------------------------------------------------------------

%package Uzbekistan
Summary:	Metro Maps (Uzbekistan)
Group:		Sciences/Geosciences
Requires:	qmetro

%description Uzbekistan
Maps for the qMetro program (Uzbekistan).

Cities: Tashkent.

%files Uzbekistan
%{_datadir}/qmetro/map/Tashkent.pmz

#----------------------------------------------------------------------------

%package Venezuela
Summary:	Metro Maps (Venezuela)
Group:		Sciences/Geosciences
Requires:	qmetro

%description Venezuela
Maps for the qMetro program (Venezuela).

Cities: Caracas, Valencia.

%files Venezuela
%{_datadir}/qmetro/map/Caracas.pmz
%{_datadir}/qmetro/map/ValenciaV.pmz

#----------------------------------------------------------------------------

%prep
%setup -n %{name}
for N in *.zip
do
unzip $N "*.pmz"
done

%build

%install
install -dm 0755 %{buildroot}%{_datadir}/qmetro/map
install -pm 0644 *.pmz %{buildroot}%{_datadir}/qmetro/map

