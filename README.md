# SiteIKEA — Automação de testes (busca de produtos ikea.pt)

Testes automatizados em Python/Selenium para o fluxo de **busca de produtos** do
site [ikea.pt](https://www.ikea.pt).

## Estrutura

| Arquivo | Papel |
|---|---|
| `data.py` | URL do site e termos de busca usados nos testes |
| `helpers.py` | Utilitários: checar site no ar, digitação/pausas "humanizadas" |
| `IKEA.py` | Page Objects: `IkeaHomePage`, `IkeaSearchResultsPage`, `IkeaProductPage` |
| `TestersiteIkea.py` | Testes pytest |

## Sobre a digitação "humanizada"

Em vez de preencher o campo de busca instantaneamente, `helpers.human_type` digita
caractere por caractere com pequenas pausas aleatórias, e `helpers.human_pause`
insere pausas curtas entre ações — deixando a automação com um ritmo mais parecido
com o de uma pessoa real interagindo com o site.

## Casos de teste

- Busca por um termo válido ("cadeira") retorna resultados.
- Busca por um termo inexistente mostra a mensagem "Sem resultados para...".
- Abrir o primeiro produto da lista exibe título e preço.
- Adicionar o primeiro produto ao carrinho.

## Instalação

```bash
pip install -r requirements.txt
```

Requer o [ChromeDriver](https://chromedriver.chromium.org/) compatível com sua
versão do Chrome no PATH.

## Rodando os testes

```bash
pytest TestersiteIkea.py -v
```

## Publicando no GitHub

```bash
git add .
git commit -m "Automação de testes de busca de produtos - ikea.pt"
git remote add origin <URL_DO_SEU_REPOSITORIO_GITHUB>
git push -u origin master
```
