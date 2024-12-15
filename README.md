# SWZad1
_Proszę napisać program serwera (dowolny język programowania), który realizować będzie
następującą funkcjonalność:
a. po uruchomieniu kontenera, serwer pozostawia w logach informację o dacie
uruchomienia, imieniu i nazwisku autora serwera (imię i nazwisko studenta) oraz porcie
TCP, na którym serwer nasłuchuje na zgłoszenia klienta._

```
Logi po uruchomieniu kontenera wyglądają tak:
lenovo@lenovo-VirtualBox:~/test$ docker run -p 8081:8081 -e PORT=8081 ip-server
INFO:root:Serwer uruchomiony
INFO:root:Autor: Krzysztof Ogonek
INFO:root:Data uruchomienia: 2024-12-15 20:42:47.767559
INFO:root:Port TCP: 8081
INFO:root:Serwer nasłuchuje...
```

_b. na podstawie adresu IP klienta łączącego się z serwerem, w przeglądarce powinna
zostać wyświetlona strona informująca o adresie IP klienta i na podstawie tego adresu IP,
o dacie i godzinie w jego strefie czasowej._

W przegladarce wyswietla sie informacja o IP:
Twoj adres IP to: 172.17.0.1

_Opracować plik Dockerfile, który pozwoli na zbudowanie obrazu kontenera realizującego
funkcjonalność opisaną w punkcie 1. Przy ocenie brane będzie sposób opracowania tego pliku
(wieloetapowe budowanie obrazu, ewentualne wykorzystanie warstwy scratch, optymalizacja pod
kątem funkcjonowania cache-a w procesie budowania, optymalizacja pod kątem zawartości i ilości
warstw, healthcheck itd ). Dockerfile powinien również zawierać informację o autorze tego pliku
(ponownie imię oraz nazwisko studenta)._

Wszystkie pliki są dostępne w repo.
```
lenovo@lenovo-VirtualBox:~/test$ docker build -t ip-server .
[+] Building 2.9s (8/8) FINISHED                       	docker:desktop-linux
 => [internal] load build definition from Dockerfile                   	0.0s
 => => transferring dockerfile: 567B                                   	0.0s
 => [internal] load metadata for docker.io/library/python:3.10-slim    	1.6s
 => [internal] load .dockerignore                                      	0.0s
 => => transferring context: 2B                                        	0.0s
 => [1/3] FROM docker.io/library/python:3.10-slim@sha256:61912260e578182d  0.1s
 => => resolve docker.io/library/python:3.10-slim@sha256:61912260e578182d  0.1s
 => [internal] load build context                                      	0.1s
 => => transferring context: 1.46kB                                    	0.0s
 => CACHED [2/3] WORKDIR /app                                          	0.0s
 => [3/3] COPY server.py /app/server.py                                	0.1s
 => exporting to image                                                 	0.6s
 => => exporting layers                                                	0.2s
 => => exporting manifest sha256:3aa067ce40ba46ba2a2a5f5ecb1e54ec0c66476d  0.1s
 => => exporting config sha256:be86d2f785c34eafeff1404d491400e65d2cdf532a  0.0s
 => => exporting attestation manifest sha256:08a1c139437577fa4af626af6f55  0.1s
 => => exporting manifest list sha256:4ef97d250f4d7af3ee76d5cdaf48d9ad015  0.0s
 => => naming to docker.io/library/ip-server:latest                    	0.0s
 => => unpacking to docker.io/library/ip-server:latest                 	0.1s
```

_ Należy podać polecenia niezbędne do:
a. zbudowania opracowanego obrazu kontenera,_

```
docker build -t ip-server 
```

_b. uruchomienia kontenera na podstawie zbudowanego obrazu,_
```
docker run -p 8081:8081 -e PORT=8081 ip-server
```
_c. sposobu uzyskania informacji, które wygenerował serwer w trakcie uruchamiana kontenera
(patrz: punkt 1a),_

Wyświetlają się one po uruchomieniu kontenera w konsoli (patrz wyżej)
Zaś w celu otworzenia strony serwera wpisujemy w przeglądarkę adres localhost z portem jaki ustawiliśmy w plikach (u mnie to 8081)

_d. sprawdzenia, ile warstw posiada zbudowany obraz_
```
lenovo@lenovo-VirtualBox:~/test$ docker images
REPOSITORY   TAG   	IMAGE ID   	CREATED     	SIZE
ip-server	latest	4ef97d250f4d   3 minutes ago   191MB
lenovo@lenovo-VirtualBox:~/test$ docker history ip-server:latest
IMAGE      	CREATED      	CREATED BY                                  	SIZE  	COMMENT
4ef97d250f4d   4 minutes ago	CMD ["python" "server.py"]                  	0B    	buildkit.dockerfile.v0
<missing>  	4 minutes ago	EXPOSE map[8081/tcp:{}]                     	0B    	buildkit.dockerfile.v0
<missing>  	4 minutes ago	COPY server.py /app/server.py # buildkit    	12.3kB	buildkit.dockerfile.v0
<missing>  	36 minutes ago   WORKDIR /app                                	8.19kB	buildkit.dockerfile.v0
<missing>  	36 minutes ago   ENV PORT=8081                               	0B    	buildkit.dockerfile.v0
<missing>  	11 days ago  	CMD ["python3"]                             	0B    	buildkit.dockerfile.v0
<missing>  	11 days ago  	RUN /bin/sh -c set -eux;  for src in idle3 p…   16.4kB	buildkit.dockerfile.v0
<missing>  	11 days ago  	RUN /bin/sh -c set -eux;   savedAptMark="$(a…   48.8MB	buildkit.dockerfile.v0
<missing>  	11 days ago  	ENV PYTHON_SHA256=bfb249609990220491a1b92850…   0B    	buildkit.dockerfile.v0
<missing>  	11 days ago  	ENV PYTHON_VERSION=3.10.16                  	0B    	buildkit.dockerfile.v0
<missing>  	11 days ago  	ENV GPG_KEY=A035C8C19219BA821ECEA86B64E628F8…   0B    	buildkit.dockerfile.v0
<missing>  	11 days ago  	RUN /bin/sh -c set -eux;  apt-get update;  a…   9.59MB	buildkit.dockerfile.v0
<missing>  	11 days ago  	ENV LANG=C.UTF-8                            	0B    	buildkit.dockerfile.v0
<missing>  	11 days ago  	ENV PATH=/usr/local/bin:/usr/local/sbin:/usr…   0B    	buildkit.dockerfile.v0
<missing>  	13 days ago  	# debian.sh --arch 'amd64' out/ 'bookworm' '…   85.2MB	debuerreotype 0.15
```

# SWZad2

_Podstawą do wykonania zadania jest przykład analizowany w trakcie laboratorium nr 9. Przykład ten
zawiera łańcuch CI dla usługi Github Actions pozwalający na zbudowanie obrazu Docker dla dwóch
architektur sprzętowych wraz z metodą tagowania tego obrazu oraz z wykorzystaniem cache
w procesie jego budowania.
Proszę KONIECZNIE zapoznać się z dokumentacją i przykładami dostarczonymi przez Docker:
https://docs.docker.com/build/ci/github-actions/
Odpowiednio zmodyfikowany opis workflow należy uzupełnić o testowanie obrazu pod kątem
podatności na zagrożenia w oparciu o usługę Docker Scout. Sposób uzupełnienia łańcucha opiera się
o informację zawarte w materiałach laboratoryjnych jak i dokumentacji środowiska Docker:
https://github.com/docker/scout-action
https://docs.docker.com/scout/integrations/ci/gha/_

Niestety udało mi się to zadanie wykonać tylko w połowie, ponieważ napotkałem problem z pushowaniem obrazu do docker hub:
Error: buildx failed with: ERROR: failed to solve: failed to push my-docker-image:latest: push access denied, repository does not exist or may require authorization: server message: insufficient_scope: authorization failed
Jest to najprawdopodobniej problem z samym repozytorium, ponieważ logowanie przebiegło pomyślnie zgodnie z logami github action.
