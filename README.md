## 👉 Materiál pro lektory Engeta 👈

Ahoj! Toto je repozitář s materiály k **objektově orientovanému programování
v Pythonu od Engeta.**

Pokud jsi novým nebo stávajícím lektorem/lektorkou tohoto
[typu akademie](https://engeto.cz/python-akademie/), neváhej materiály omrknout
a vyzkoušet.

<br>

## 💻 Jak na materiály 💻

Máš prakticky **dvě možnosti**:
1. Naklonovat repozitář a otevřít sešity (*Jupyter*, *Colaboratory*),
2. spustit *docker* a pracovat uvnitř s Jupyter Hubem.

Vyber to, co ti více sedí, nebo znáš.

Pokud budeš mít jakýkoliv dotaz, napiš na Slacku Engeta (sekce `#python`).
Nebo jako zprávu přímo autorovi (**Matouš Holinka**).

Pokud chceš s materiálem pracovat trvale a přidávat si poznámky, doporučuji
vytvořit si *vlastního klona* a *vlastní pracovní větev*:
```
git clone <url>
git checkout -v <jmeno_me_vetve>
```

<br>

## 🐳 Práce pomocí Dockeru 🐳

Pro možnost práce s materiály potřebuješ nainstalovat:
1. [Docker](https://docs.docker.com/desktop/install/linux-install/),
2. [docker-compose](https://docs.docker.com/compose/install/compose-desktop/).

Po naklonování repozitáře nezapomeň vytvořit **lokální větev**, se kterou budeš
pracovat:
```
git clone https://github.com/ENGETO-Python-Akademie/python-academy-2023
git checkout -b <jmeno_me_vetve>
```

Dále potřebuješ vytvořit konfigurace pro jednotlivé služby (stačí JupyterHub):
```
./build
INFO: Creating folder config ..
INFO: Creating config file jupyter.env
INFO: do not forget to change the credentials in config/ ..
```

Potom si doplň přihlašovací údaje (nahraď stávající u `config/jupyter.env`.

<br>

## ▶️ Spuštění ▶️

Pro spuštění všech služeb (nutná je pouze Jupyter):
```
docker-compose up -d
```

V rámci prohlížeče přejít na URL:
```
localhost:8888
```

.. a zadat tebou předdefinované heslo.

<br>

## 🤖 Úprava a aktualizace materiálů 🤖

Pokud budeš mít nějaký fajn nápad, jak akademii vylepšit, určitě se opět ozvi
na Slacku. Budeme moc rádi za každý potenciální zlepšovák!

Co se chyb týče, můžeš přímo chystat:
* oznámění do channelu, pokud se ti něco nezdá,
* nachystat **pull request** v Gitu.
