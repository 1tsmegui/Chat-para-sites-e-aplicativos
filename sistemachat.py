#Titulo  passo a passo 
#Botao: iniciar chat 
#titulo: Bem vindo ao Neworld 
#campo de texto: Escreva seu nome no chat 
#botão: Entrar no chat 
#sumir com o titulo e o botão inicial 
#fechar o popp
#Criar o chat (com a mensagem de "nome do usuario entrou no chat")
#Embaixo do chat:
#campo de texto: Digite sua mensagem 
#botão: enviar 
#vai aparecer a mensagem no chat com o nome do usuário 

import flet as ft

def main(pagina):
    titulo = ft.Text("Neworld",size=50)

    def enviar_mensagem_tunel(mensagem):
        chat.controls.append(ft.Text(mensagem))
        pagina.update()

    pagina.pubsub.subscribe(enviar_mensagem_tunel) #cria o tunel de comunicação
    
    titulo_janela = ft.Text("Bem vindo ao Neworld")
    campo_nome_usuario = ft.TextField(label="Escreva seu nome no chat")
    
    
    def enviar_mensagem(evento):
        texto= f"{campo_nome_usuario.value}:{texto_mensagem.value}"
        # enviar a mensagem no chat:
            # usuario:mensagem
        
        # enviar a mensagem no tunel 
        pagina.pubsub.send_all(texto)

        # limpar campo da mensagem
        texto_mensagem.value =""
        pagina.update()

    texto_mensagem = ft.TextField(label="Digite sua mensagem",on_submit=enviar_mensagem)
    botao_enviar = ft.ElevatedButton("Enviar",on_click=enviar_mensagem)
    chat=ft.Column()
    
    #colunas e linhas 
    linha_mensagem=ft.Row([texto_mensagem, botao_enviar])
  
    def entrar_chat(evento):
        #tirar o titulo 
        pagina.remove(titulo) 
        #tirar o botao_iniciar
        pagina.remove(botao_iniciar)
        #tirar o popup
        janela.open = False
        #criar o chat 
        pagina.add(chat)
        #adicionar a linha de mensagem 
        pagina.add(linha_mensagem)
        #escrever a mensagem: usuario entrou no chat 
        texto_entrou_no_chat=f"{campo_nome_usuario.value} entrou no chat"
        pagina.pubsub.send_all(texto_entrou_no_chat)

        
        pagina.update()

    botao_entrar=ft.ElevatedButton("Entrar no chat",on_click=entrar_chat)
  
    
    janela = ft.AlertDialog(
        title=titulo_janela,
        content=campo_nome_usuario,
        actions=[botao_entrar]
    )

    def abrir_popup(evento):
        pagina.dialog= janela
        janela.open = True
        pagina.update()

    botao_iniciar = ft.ElevatedButton("Iniciar chat", on_click=abrir_popup)
    
    pagina.add(titulo)
    pagina.add(botao_iniciar)

    
ft.app(main, view=ft.WEB_BROWSER)
