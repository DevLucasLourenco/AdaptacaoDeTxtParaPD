import pandas as pd
import numpy as np

with open(r"Alunos.txt","r") as alunos:
    lista = alunos.readlines()
    
    del lista[:4]
    
    youtube_org = []
    instafacebook_org = []
    site_org = [] 
    qtde_anuncio = 0


    for linha in lista:
        adapatacao = linha.split(',')
        email, origem = adapatacao
        email = email.strip('"')

        if '_org' in origem:
            if 'hashtag_yt_org' in origem:
                youtube_org.append(email)
                
            
            if "hashtag_site_org" in origem:
                site_org.append(email)
                

            if 'hashtag_igfb_org' in origem or 'hashtag_ig_org' in origem:
                instafacebook_org.append(email)
                                
        else:
            qtde_anuncio += 1


qtde_org = len(youtube_org) + len(instafacebook_org) + len(site_org)

qtde_dados = [qtde_anuncio, qtde_org, len(site_org), len(youtube_org), len(instafacebook_org)]
qtde_alunos_df = pd.DataFrame(qtde_dados, columns=['Quantidade'], index=['Anuncios', 'Orgânico', 'Site', 'Youtube', 'Instagram/Facebook'])

display(qtde_alunos_df)


dados_youtube = list(zip(youtube_org))
youtube_org_df = pd.DataFrame(dados_youtube, columns=['Orgânico de Youtube'])

dados_site = list(zip(site_org))
site_org_df = pd.DataFrame(dados_site, columns=['Orgânico de Site'])

dados_instafb = list(zip(instafacebook_org))
instafb_org_df = pd.DataFrame(dados_instafb, columns=['Orgânico do Insta/FB'])

df_geral = pd.concat([instafb_org_df, site_org_df, youtube_org_df])
df_geral = df_geral.replace(np.nan, '')
#df_geral.fillna('', inplace=True)


display(df_geral)


txt = [f'Quantidade Youtube: {len(youtube_org)}\n',  f'Quantidade Site: {len(site_org)}\n', f'Quantidade Instagram/Facebook: {len(instafacebook_org)}\n', f'Quantidade Orgânico: {len(instafacebook_org) + len(site_org) + len(youtube_org)}\n', f'Quantidade Anuncio: {qtde_anuncio}\n']
amostrar = [sequencia for sequencia in txt]

#Gera um arquivo de leitura
with open("Qtde de Alunos por Separação", "w") as qtde_indicadores:
    qtde_indicadores.write('\n'.join(amostrar))
