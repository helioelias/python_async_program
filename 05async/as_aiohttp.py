import asyncio
import aiofiles
import aiohttp
import bs4

async def pegar_links():
    links = []
    async with aiofiles.open('links.txt') as arquivo:
        async for link in arquivo:
            links.append(link.strip())
    return links

async def pegar_html(link):
    print(f'Pegando o HTML do curso {link}')
    headers = {
        'User-Agent': 'python-requests/2.26.0',
        'Accept-Encoding': 'gzip, deflate',
        'Accept': '*/*',
        'Connection': 'keep-alive',
    }
    
    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.get(link) as resp:
            try:
                resp.raise_for_status()
                return await resp.text()
            except aiohttp.client_exceptions.ClientResponseError as err:
                print("******************************")
                print(err)
                print("******************************")

def pegar_titulo(html):
    soup = bs4.BeautifulSoup(html, 'html.parser')
    
    title = soup.select_one('title')
    
    title = title.text.split('|')[0].strip()
    
    return title

async def imprimir_titulos():
    links = await pegar_links()
    
    tarefas = []
    for link in links:
        tarefas.append(asyncio.create_task(pegar_html(link)))
      
    for tarefa in tarefas:
        html = await tarefa
        
        title = pegar_titulo(html)
        
        print(f'Curso: {title}')
        
def main():
    el = asyncio.get_event_loop()
    el.run_until_complete(imprimir_titulos())
    el.close()
    
if __name__ == '__main__':
    main()