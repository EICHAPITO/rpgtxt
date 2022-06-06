import time
import pyautogui as py

jogo=1
while jogo==1:
          
          #atributos
          força_jogador=0
          armadura_jogador=0
          velocidade_jogador=0
          magia_jogador=0
          arma_jogador=0
          roupa_jogador=0

          #introduçao
          print("Bem vindo, Jogador!")
          time.sleep(1)
          print("Por favor, eu peço que pegue seu lanche, sente-se, relaxe e aproveite nossa aventura.")
          time.sleep(1)
          name=input("Antes, me diga seu nome:")
          time.sleep(1)
          print("\nOk,",name,"!")
          time.sleep(1)
          print("Não se esqueça de seu nome")
          time.sleep(1)
          print("Me diga o que você é:")
          time.sleep(1)
          classe=input("Guereiro[g]? Mago?[m] Assassino?[a] Tanque?[t]:")
          time.sleep(2)
          if classe=="g":
                    força_jogador=3
                    armadura_jogador=2
                    magia_jogador=0
                    velocidade_jogador=1
                    vida_jogador=15
                    
          if classe=="m":
                    força_jogador=1
                    armadura_jogador=2
                    magia_jogador=3
                    velocidade_jogador=1
                    vida_jogador=10

          if classe=="a":
                    força_jogador=2
                    armadura_jogador=1
                    magia_jogador=0
                    velocidade_jogador=3
                    vida_jogador=10

          if classe=="t":
                    força_jogador=2
                    armadura_jogador=3
                    magia_jogador=0
                    velocidade_jogador=1
                    vida_jogador=20

          print("\nPara começar, preciso que esqueça tudo o que sabe e abra sua mente")
          time.sleep(1)
          print(".")
          time.sleep(1)
          print(".")
          time.sleep(1)
          print(".")
          time.sleep(1)
          print("Abra seu terceiro olho\n")
          time.sleep(2)

          #FASE 1 GUERREIRO --A VILA--
          if classe=="g":
                    idiot=0
                    dinheiro=0
                    força_jogador=3
                    armadura_jogador=2
                    magia_jogador=0
                    velocidade_jogador=1
                    vida_jogador=15
                    arma_jogador=0
                    roupa_jogador='armadura simples'
                    if roupa_jogador=='armadura simples':
                              armadura_jogador=armadura_jogador+2
                    
                    print("Você recobra a consciência no meio de uma batalha")
                    time.sleep(1)
                    print("Olha ao seu redor e vê que sua cidade está sendo destruída pelo clã rival")
                    time.sleep(1)
                    print("De repente você escuta o rugido de um dragão")
                    time.sleep(1)
                    print("O que você faz?\n")
                    time.sleep(1)
                    print("Procura sua espada e vai atrás do dragão[1]")
                    print("Foge do vilarejo com medo[2]")
                    print("Procura sua espada e volta para batalha mantendo distancia do dragão[3]\n")
                    decisao=input("Decisão:")
                    time.sleep(3)

                    if decisao=='1':
                              print("\nVocê corre atrás do dragão, tropeça em uma madeira caida, cai, bate a cabeça e morre")
                              time.sleep(1)
                              print("\nFIM DE JOGO\n")
                              jogo=0
                              print("Créditos\nCriador: João Gomes\nDesenvolvedor: João Gomes\nEditor:João Gomes\nGênio por trás de tudo: João Gomes")
                              break

                    if decisao=='2':
                              print("\nVocê corre pra longe")
                              time.sleep(1)
                              print("Você escapou")
                              time.sleep(1)
                              print("Algumas horas se passam...")
                              time.sleep(1)
                              print("Você volta pro vilarejo")

                    if decisao=='3':
                              print("\nVocê acha uma espada no chão, pega ela e começa a batalhar com todos os guerreiros rivais")
                              arma_jogador='espada simples'
                              time.sleep(1)
                              if arma_jogador=='espada simples':
                                        força_jogador=força_jogador+2
                              print("--",name,"perde 3 pontos de vida em batalha --")
                              vida_jogador=vida_jogador-3
                              time.sleep(1)

                    print("\nA batalha acabou!")
                    print(".")
                    time.sleep(1)
                    print(".")
                    time.sleep(1)
                    print(".")
                    time.sleep(1)
                    print("Você anda pelo vilarejo destruído procurando por sua esposa")
                    time.sleep(1)
                    print("Um grito de socorro!")
                    time.sleep(1)
                    print("Desconhecido: AI, CARALHO! MINHA PERNA\n")#shh! quiet, the templars are here
                    time.sleep(1)
                    print("Ajudar o desconhecido[1]")
                    print("Ignorar o pedido de socorro[2]")
                    print("Esperar o desconhecido morrer de hemorragia e roubar seus pertences[3]\n")
                    decisao=0
                    
                    decisao=input("Decisão:")
                    time.sleep(1)

                    if decisao=='2':
                              idiot=idiot+1
                              print("\nVocê tenta ignorar o pedido de socorro, se distrai, bate de cara em uma parede, cai de cabeça em cima de uma espada e morre")
                              time.sleep(1)
                              print("\nFIM DE JOGO!")
                              time.sleep(2)
                              print("{deseja encerrar a aventura[0] ou refazer sua decisao[1]?}")
                              jogo=input("Sua resposta:")
                              if jogo=='0':
                                        print("Espero que sua longa jornada tenha sido legal\n")
                                        print("Créditos\nCriador: João Gomes\nDesenvolvedor: João Gomes\nEditor:João Gomes\nGênio por trás de tudo: João Gomes")
                                        break
                              if jogo=='1':
                                        time.sleep(1)
                                        print("Voltando ao checkpoint")
                                        time.sleep(2)
                                        print("\nDesconhecido: AI, CARALHO! MINHA PERNA\n")#shh! quiet, the templars are here
                                        time.sleep(1)
                                        print("Ajudar o desconhecido[1]")
                                        print("Ignorar o pedido de socorro[2]")
                                        print("Esperar o desconhecido morrer de hemorragia e roubar seus pertences[3]\n")
                                        decisao=0
                    
                                        decisao=input("Decisão:")
                                        time.sleep(1)

                                        if decisao=='2':
                                                  idiot=idiot+1
                                                  print("\nCriador: Se apertar 2 de novo eu encerro o jogo agora\n")
                                                  time.sleep(2)
                                                  print("Desconhecido: AI, CARALHO! MINHA PERNA\n")#shh! quiet, the templars are here
                                                  time.sleep(1)
                                                  print("Ajudar o desconhecido[1]")
                                                  print("Ignorar o pedido de socorro[2]")
                                                  print("Esperar o desconhecido morrer de hemorragia e roubar seus pertences[3]\n")
                                                  decisao=0
                    
                                                  decisao=input("Decisão:")
                                                  time.sleep(2)

                                                  if decisao=='2':
                                                            print("Criador: Parabéns, otário!\n FIM DE JOGO\n")
                                                            time.sleep(2)
                                                            print("Créditos\nCriador: João Gomes\nDesenvolvedor: João Gomes\nEditor:João Gomes\nGênio por trás de tudo: João Gomes")
                                                            break
                    if decisao=='1':
                              print("\nVocê corre atrás do pedido de soccoro")
                              time.sleep(1)
                              print("Na hora de carregar o desconhecido você deixa ele cair")
                              time.sleep(1)
                              print(".")
                              time.sleep(1)
                              print(".")
                              time.sleep(1)
                              print("Ele cai no chão, bate a cabeça e morre\n")
                              print("Conferir os bolsos e ver se tem algo útil[1]")
                              print("Deixar o corpo ali[2]\n")

                              decisao_bonus=input("Decisão:")
                              time.sleep(1)

                              if decisao_bonus=='1':
                                        print("\n--",name,"recebe 5 dinheiros --")
                                        dinheiro=dinheiro+5
                                        
                              if decisao_bonus=='2':
                                        print("\nAcontece...")
                                        time.sleep(1)
                              
                    if decisao=='3':
                              print("\nVocê espera o indivíduo morrer e depois rouba o falecido(tu n tem vergonha nao?)")
                              time.sleep(1)
                              print("--",name,"recebe 5 dinheiros --\n")
                              time.sleep(1)

                    
                    print("Você percebe que agora é o único ser vivo no vilarejo")
                    time.sleep(1)
                    print("Percebe que o corpo de sua esposa não está no vilarejo")
                    time.sleep(1)
                    print("O que você faz?\n")
                    time.sleep(1)
                    print("Fica sentado sem fazer nada e arrependido[1]")
                    print("Sai do vilarejo em busca de respostas e vingança[2]\n")

                    decisao=input("Decisão:")
                    time.sleep(1)

                    if decisao=='1':
                              idiot=idiot+1
                              print("\nVocê fica sentado no chão, olha pra trás e tem uma minhoca gigante correndo atrás de você")
                              time.sleep(1)
                              print("O que você faz?")
                              time.sleep(1)
                              print("Correr[1]")
                              print("Ficar[2]\n")
                              decisao_bonus=input("Decisão:")
                              time.sleep(1)

                              if decisao_bonus=="1":
                                        print("\nSe correr o bicho pega")
                                        time.sleep(1)
                                        print("Você morreu!")
                                        time.sleep(1)
                                        print("FIM DE JOGO")
                                        time.sleep(3)
                                        print("encerrar jogo[0] ou voltar pro último checkpoint[1]:")         
                                        game_over=input("Sua resposta:")
                                        if game_over=='0':
                                                  jogo=0
                                                  print("Espero que sua longa jornada tenha sido legal\n")
                                                  print("Créditos\nCriador: João Gomes\nDesenvolvedor: João Gomes\nEditor:João Gomes\nGênio por trás de tudo: João Gomes")
                                                  break
                                        if game_over=='1':
                                                  print("Voltando ao checkpoint")
                                                  time.sleep(2)
                                                  print("Você percebe que agora é o único ser vivo no vilarejo")
                                                  time.sleep(1)
                                                  print("Percebe que o corpo de sua esposa não está no vilarejo")
                                                  time.sleep(1)
                                                  print("O que você faz?\n")
                                                  time.sleep(1)
                                                  print("Fica sentado sem fazer nada e arrependido[1]")
                                                  print("Sai do vilarejo em busca de respostas e vingança[2]\n")

                                                  decisao=input("Decisão:")
                                                  time.sleep(1)

                                                  if decisao=='1':
                                                            print("\nPara de ser estúpido,",name)
                                                            time.sleep(1)
                                                            print("\nVocê cansa de sentir pena e sai em busca de respostas")
                                                            time.sleep(1)
                                                            print("E de vingança")
                                                            time.sleep(1)

                              if decisao_bonus=="2":
                                        print("\nSe ficar o bicho come")
                                        time.sleep(1)
                                        print("Você morreu!")
                                        time.sleep(1)
                                        print("FIM DE JOGO")
                                        time.sleep(3)
                                        print("encerrar jogo[0] ou voltar pro último checkpoint[1]:")
                                        game_over=input("Sua resposta:")
                                        if game_over=='0':
                                                  jogo=0
                                                  print("Espero que sua longa jornada tenha sido legal\n")
                                                  print("Créditos\nCriador: João Gomes\nDesenvolvedor: João Gomes\nEditor:João Gomes\nGênio por trás de tudo: João Gomes")
                                                  break
                                        if game_over=='1':
                                                  print("Voltando ao checkpoint")
                                                  time.sleep(2)
                                                  print("Você percebe que agora é o único ser vivo no vilarejo")
                                                  time.sleep(1)
                                                  print("Percebe que o corpo de sua esposa não está no vilarejo")
                                                  time.sleep(1)
                                                  print("O que você faz?\n")
                                                  time.sleep(1)
                                                  print("Fica sentado sem fazer nada e arrependido[1]")
                                                  print("Sai do vilarejo em busca de respostas e vingança[2]\n")

                                                  decisao=input("Decisão:")
                                                  time.sleep(1)

                                                  if decisao=='1':
                                                            print("\nPara de ser estúpido,",name)
                                                            time.sleep(1)
                                                            print("\nVocê cansa de sentir pena e sai em busca de respostas")
                                                            time.sleep(1)
                                                            print("E de vingança")
                                                            time.sleep(1)

                    if decisao=='2':
                              print("\nVocê sai do vilarejo")
                              
                    #FASE 2 GUERREIRO --A FLORESTA--

                    time.sleep(1)
                    print("\nIr atrás do vilarejo rival[1]")
                    print("Esquecer tudo e seguir a vida[2]")
                    print("Caçar um animal para recuperar a vida[3]\n")

                    decisao=input("Decisão:")
                    time.sleep(2)

                    if decisao == '2':
                              print("\nVocê segue seu caminho deixando seu passado para tras")
                              time.sleep(1)
                              print("\nOBRIGADO POR TER JOGADO")
                              time.sleep(1)
                              print("Espero que sua longa jornada tenha sido legal\n")
                              time.sleep(1)
                              print("FIM DE JOGO")
                              time.sleep(1)
                              print("Créditos\nCriador: João Gomes\nDesenvolvedor: João Gomes\nEditor:João Gomes\nGênio por trás de tudo: João Gomes")
                              break
                    if decisao == '3':
                              print("\nVocê encontra um urso")
                              time.sleep(1)
                              print("\nComeçar luta com urso[1]")
                              print("Procurar outro animal[2]")
                              decisao_bonus=input("Decisão:")
                              time.sleep(2)

                              if decisao_bonus =='2':
                                        print("\nVocê sai atrás de outro animal")
                                        time.sleep(1)
                                        print(".")
                                        time.sleep(1)
                                        print('.')
                                        time.sleep(1)
                                        print("Você não encontra nenhum animal nessa enorme floresta e vai atrás do vilarejo rival")
                                        time.sleep(1)

                              if decisao_bonus =='1':
                                        print("\nO urso não notou sua presença")
                                        time.sleep(1)
                                        print("\nEncarar o urso mano a mano[1]")
                                        print("Jogar uma pedra pra distrair o urso[2]")
                                        print("Escalar uma árvore, pular e cravar a espada no pescoço do urso[3]")

                                        decisao_bonus2=input("Decisão:")
                                        time.sleep(2)

                                        if decisao_bonus2 =='1':
                                                  print("\nJogador mata o urso e perde 5 pontos de vida")
                                                  time.sleep(1)
                                                  print("--",name,"recebe pele de urso e carne de urso --")
                                                  vida_jogador=vida_jogador - 5
                                                  time.sleep(1)
                                                  print("\nEquipar pele de urso?[s/n]")
                                                  equip=input("Resposta:")
                                                  if equip =='s':
                                                            roupa_jogador='pele de urso'

                                                  time.sleep(1)
                                                  print("\nComer carne de urso para restaurar vida?[s/n]")
                                                  comer=input("Resposta:")
                                                  time.sleep(1)

                                                  if comer=='s':
                                                            vida_jogador=vida_jogador+3

                                        if decisao_bonus2 =='2':
                                                  idiot=idiot+1
                                                  print("\nO urso te nota")
                                                  time.sleep(1)
                                                  print("Você fica com medo e paralisado")
                                                  time.sleep(1)
                                                  print(".")
                                                  time.sleep(1)
                                                  print('.')
                                                  time.sleep(1)
                                                  print("O Urso te mata")
                                                  time.sleep(1)
                                                  print("Você morreu!")
                                                  time.sleep(2)
                                                  print("FIM DE JOGO")
                                                  time.sleep(3)
                                                  print("encerrar jogo[0] ou voltar pro último checkpoint[1]:")         
                                                  game_over=input("Sua resposta:")
                                                  if game_over=='0':
                                                            jogo=0
                                                            print("Espero que sua longa jornada tenha sido legal\n")
                                                            print("Créditos\nCriador: João Gomes\nDesenvolvedor: João Gomes\nEditor:João Gomes\nGênio por trás de tudo: João Gomes")
                                                            break
                                                  if game_over=='1':
                                                            print("Voltando ao checkpoint")
                                                            time.sleep(2)
                                                            print("\nO urso não notou sua presença")
                                                            print("\nEncarar o urso mano a mano[1]")
                                                            print("Jogar uma pedra pra distrair o urso[2]")
                                                            print("Escalar uma árvore, pular e cravar a espada no pescoço do urso[3]")

                                                            decisao_bonus2=input("Decisão:")
                                                            time.sleep(2)

                                                            if decisao_bonus2 =='2':
                                                                      idiot=idiot+1
                                                                      print(name,"!!!!")
                                                                      time.sleep(1)
                                                                      print("NÃO")
                                                                      time.sleep(1)
                                                                      print("ME")
                                                                      time.sleep(1)
                                                                      print("ESTRESSA")
                                                                      time.sleep(2)
                                                                      print("\nVocê escala a árvore sorretairamente")
                                                                      time.sleep(1)
                                                                      print("Derruba uma colmeia")
                                                                      time.sleep(1)
                                                                      print("O urso vai atrás da colmeia caída pra pegar mel")
                                                                      time.sleep(1)
                                                                      print("Você aproveita ele distraído e pula nas costas dele cravando a espada")
                                                                      time.sleep(2)
                                                                      print("--",name,"mata o urso --")
                                                                      print("--",name,"recebe pele de urso e carne de urso")
                                                                      vida_jogador=vida_jogador - 5
                                                                      time.sleep(1)
                                                                      print("\nEquipar pele de urso?[s/n]")
                                                                      equip=input("Resposta:")
                                                                      if equip =='s':
                                                                                roupa_jogador='pele de urso'

                                                                      time.sleep(1)
                                                                      print("\nComer carne de urso para restaurar vida?[s/n]")
                                                                      comer=input("Resposta:")
                                                                      time.sleep(1)

                                                                      if comer=='s':
                                                                                vida_jogador=vida_jogador+3
                                                            if decisao_bonus2 =='1':
                                                                      print("\nJogador mata o urso e perde 5 pontos de vida")
                                                                      time.sleep(1)
                                                                      print("--",name,"recebe pele de urso e carne de urso --")
                                                                      vida_jogador=vida_jogador - 5
                                                                      time.sleep(1)
                                                                      print("\nEquipar pele de urso?[s/n]")
                                                                      equip=input("Resposta:")
                                                                      if equip =='s':
                                                                                roupa_jogador='pele de urso'

                                                                      time.sleep(1)
                                                                      print("\nComer carne de urso para restaurar vida?[s/n]")
                                                                      comer=input("Resposta:")
                                                                      time.sleep(1)

                                                                      if comer=='s':
                                                                                vida_jogador=vida_jogador+3

                                                            if decisao_bonus2 =='3':
                                                                      print("\nVocê escala a árvore sorretairamente")
                                                                      time.sleep(1)
                                                                      print("Derruba uma colmeia")
                                                                      time.sleep(1)
                                                                      print("O urso vai atrás da colmeia caída pra pegar mel")
                                                                      time.sleep(1)
                                                                      print("Você aproveita ele distraído e pula nas costas dele cravando a espada")
                                                                      time.sleep(2)
                                                                      print("--",name,"mata o urso --")
                                                                      print("--",name,"recebe pele de urso e carne de urso")
                                                                      vida_jogador=vida_jogador - 5
                                                                      time.sleep(1)
                                                                      print("\nEquipar pele de urso?[s/n]")
                                                                      equip=input("Resposta:")
                                                                      if equip =='s':
                                                                                roupa_jogador='pele de urso'

                                                                      time.sleep(1)
                                                                      print("\nComer carne de urso para restaurar vida?[s/n]")
                                                                      comer=input("Resposta:")
                                                                      time.sleep(1)

                                                                      if comer=='s':
                                                                                vida_jogador=vida_jogador+3

                              if decisao_bonus2 =='3':
                                        print("\nVocê escala a árvore sorretairamente")
                                        time.sleep(1)
                                        print("Derruba uma colmeia")
                                        time.sleep(1)
                                        print("O urso vai atrás da colmeia caída pra pegar mel")
                                        time.sleep(1)
                                        print("Você aproveita ele distraído e pula nas costas dele cravando a espada")
                                        time.sleep(2)
                                        print("--",name,"mata o urso --")
                                        print("--",name,"recebe pele de urso e carne de urso")
                                        vida_jogador=vida_jogador - 5
                                        time.sleep(1)
                                        print("\nEquipar pele de urso?[s/n]")
                                        equip=input("Resposta:")
                                        if equip =='s':
                                                  roupa_jogador='pele de urso'

                                        time.sleep(1)
                                        print("\nComer carne de urso para restaurar vida?[s/n]")
                                        comer=input("Resposta:")
                                        time.sleep(1)

                                        if comer=='s':
                                                  vida_jogador=vida_jogador+3
                                        

                    if decisao =='1':
                              print("\nVocê vai atrás do vilarejo rival")
                              time.sleep(1)

                    print("Você se pergunta onde fica o vilarejo")
                    time.sleep(1)
                    print("Você vê um falcão indo em direção as montanhas")
                    time.sleep(1)
                    print("Você lembra que o simbolo do vilarejo rival é um falcão")
                    time.sleep(1)
                    print("\nSeguir Falcão[1]")
                    print("Caminha pela floresta[2]")

                    decisao=input("Decisão:")
                    time.sleep(2)

                    if decisao =='1':
                              print("\nVocê continua caminhando em frente olhando pro céu")
                              time.sleep(1)
                              print("Você não vê uma árvore na sua frente e bate de cara nela")
                              time.sleep(1)
                              print("--",name,"perde 1 de vida --")
                              time.sleep(2)
                              print("\nVocê acorda e olha pra frente")
                              time.sleep(1)

                    if decisao =='2':
                              print("\nVocê caminha pela floresta")
                              time.sleep(1)
                              print(name,": Olha! um caminho de pedra")
                              time.sleep(1)
                              print("Você segue o caminho de pedra")

                    print("Você acha o vilarejo rival")
                    time.sleep(1)

                    print("\nInvadir e sair atacando tudo e todos[1]")
                    print("Se infiltrar[2]")
                    print("Chegar fazendo sinal de paz e falar: Leve-me aos seus superiores[3]")

                    decisao=input("Decisão:")
                    time.sleep(2)

                    if decisao =='1':
                              idiot=idiot+1
                              print("\nCriador: Você ainda não aprendeu nada com o jogo, né?")
                              time.sleep(2)
                              print("Você sai correndo com sede de vingança")
                              time.sleep(1)
                              print("Um camponês coloca o pé na sua frente")
                              time.sleep(1)
                              print("Você tropeça no pé dele e cai em cima da própria espada")
                              time.sleep(1)
                              print("\nVOCÊ MORREU")
                              time.sleep(2)
                              print("FIM DE JOGO")
                              time.sleep(3)
                              print("encerrar jogo[0] ou voltar pro último checkpoint[1]:")         
                              game_over=input("Sua resposta:")
                              if game_over=='0':
                                        jogo=0
                                        print("Espero que sua longa jornada tenha sido legal\n")
                                        print("Créditos\nCriador: João Gomes\nDesenvolvedor: João Gomes\nEditor:João Gomes\nGênio por trás de tudo: João Gomes")
                                        break
                              if game_over=='1':
                                        print("Voltando ao checkpoint")
                                        time.sleep(2)
                                        print("\nBLOQUEADOS POR MOTIVO DE BURRICE[aperte 1 e o jogo acaba]")
                                        print("Se infiltrar[2]")
                                        print("Chegar fazendo sinal de paz e falar: Leve-me aos seus superiores[3]")

                                        decisao=input("Decisão:")
                                        time.sleep(2)

                                        if decisao =='1':
                                                  break

                    if decisao =='3':
                              print("\nVocê entra na vila em paz e pedindo pra ser levado aos superiores")
                              time.sleep(1)
                              print("Um guarda real te leva pra base pra conversar com o Rei Bonvoiage")
                              time.sleep(1)

                    if decisao =='2':
                              print("\nVocê se infiltra")
                              time.sleep(1)
                              print("Todos os camponeses começam a te estranhar")
                              time.sleep(1)
                              print("Camponeses: O que um cara segurando uma espada vestindo uma",roupa_jogador,"andando na ponta dos pés ta fazendo?!?")
                              time.sleep(1)
                              print(".")
                              time.sleep(1)
                              print(".")
                              time.sleep(1)

                    print("\nVocê chega na porta da base e vê uma placa escrito:")
                    time.sleep(1)
                    print("Palácio Real")
                    time.sleep(1)
                    print('.')
                    time.sleep(1)
                    print('.')
                    time.sleep(1)
                    print('Você entra no palácio procurando pelo Rei Bonvoiage')
                    time.sleep(1)


                    #FASE 3 GUERREIRO --O BOBO--

                    print("Você se pergunta como que seu exército perdeu pra um vilarejo que tem um palácio de 10m²")
                    time.sleep(2)
                    print("Um bobo da corte interrompe seus pensamentos e começa a correr debochando da sua cara")
                    time.sleep(2)
                    print("\nBobo: HAHA! Olha só.")
                    time.sleep(1)
                    print("Bobo:Tem um rosto lindo. Parece um acidente de trem")
                    time.sleep(1)
                    print('.')
                    time.sleep(1)
                    print('.')
                    time.sleep(1)
                    print("\nVocê se pergunta como ele sabe da existencia de trens se esse jogo se passa na era medieval")
                    time.sleep(2)

                    print("\nPerguntar pro bobo o que são trens[1]")
                    print("Perguntar como ele sabe da existência de trens[2]")
                    print("Perguntar onde esta o Rei Bonvoiage[3]")

                    decisao=input("Decisão:")
                    time.sleep(2)

                    if decisao =='2':
                              print("\nBobo: Não há tempo para te explicar os conceitos de quarta parede, herege!")
                              time.sleep(1)
                              print("Você se lembra que bobos da corte eram ou idiotas ou gênios que ninguém conseguia compreender")
                              time.sleep(1)

                    if decisao =='1':
                              print("\nBobo: São conjunto de vagões ferroviários ligados entre si e puxados por uma locomotiva;")
                              time.sleep(1)
                              print("Bobo: Mas não há tempo para conversar sobre trens")
                              time.sleep(1)

                    if decisao =='3':
                              print("\nBobo: Ótima pergunta!")
                              time.sleep(1)

                    if idiot>=2:
                              print("Bobo: Humm! Vejo aqui que você é meio burro")
                              time.sleep(1)
                              print("Bobo: Mas eu confio em você pra resolver um enigma")
                              time.sleep(1)

                    print("Bobo: O Rei estava esperando por você")
                    time.sleep(1)
                    print("Bobo: Mas pra saber se você é você mesmo eu preciso saber se você é tu mesmo")
                    time.sleep(2)
                    print("Bobo: Então vamos pra 4 perguntinhas básicas")
                    time.sleep(1)
                    print("Bobo: Por favor, me diga seu nome\n")
                    time.sleep(1)

                    name2=input("Resposta:")

                    if name == name2:
                              print("\nBobo: Confere!")

                    if name != name:
                              print("\nBobo: Não é esse o nome que apareceu pra mim no início, mas ok")

                    time.sleep(1)
                    certo=0
                    print("\nBobo: Próxima pergunta:")
                    time.sleep(1)
                    print("Bobo: O que é o que é: uma pergunta que você nunca pode responder com “sim”?")#charada simples do bobo
                    time.sleep(3)

                    print("\nVocê está dormindo?[1]")
                    print("Tem alguém no banheiro com você?[2]")
                    print("Você acha o bobo da corte engraçado?[3]")

                    decisao=input("Resposta:")
                    time.sleep(2)

                    if decisao =='1':
                              certo=certo+1
                              print("\nBobo: Muito bom!")

                    if decisao =='2':
                              print("\nBobo: Cara... qual o seu problema, seu infiél?")

                    if decisao =='3':
                              certo=certo+1
                              print("\nBobo: Tudo bem (-_-)! Meu humor é só para inteligentes")

                    time.sleep(1)
                    print("\nBobo: Próxima pergunta")
                    time.sleep(1)
                    print("Bobo: Por que as rodas do trem são de ferro e não de borraca?")
                    time.sleep(3)

                    print("\nPorque se fossem de borracha apagariam a linha[1]")
                    print("Por causa do atrito, (Fat = μ.N)[2]")
                    print("Sai mais barato[3]")

                    decisao=input("Resposta:")
                    time.sleep(2)

                    if decisao =='1':
                              certo=certo+1
                              print("\nBobo: Pode falar, essa foi divertida")
                              time.sleep(1)

                    if decisao =='2':
                              print("\nBobo: Cara... eu tenho certeza que você não faz ideia do que você acabou de falar")
                              time.sleep(1)

                    if decisao =='3':
                              print("\nBobo: Eu não faço ideia se sai mais barato. Mas vou considerar essa resposta como certa")
                              certo=certo+1
                              time.sleep(1)

                    print("\nBobo: Muito bom! Vamos para a última pergunta")
                    time.sleep(1)
                    print("Bobo: Qual é")
                    time.sleep(1)
                    print('.')
                    time.sleep(1)
                    print('.')
                    time.sleep(1)
                    print("Bobo: o nome do nosso Rei?")
                    time.sleep(2)

                    print("\nBonvoiagi[1]")
                    print("Bonvoagi[2]")
                    print("Bonboiagi[3]")
                    print("Bomvoiage[4]")
                    print("Bomvoage[5]")

                    decisao=input("Resposta:")
                    time.sleep(2)

                    if decisao =='4':
                              certo=certo+1
                              print("\nBobo: Shoow!")
                              time.sleep(1)
                    else:
                              print("\nBobo: Cara... você leu e teve a chance de rolar a página pra cima pra colar...")
                              time.sleep(1)

                    print("\nBobo: OK! Deixa eu conferir as repostas")
                    time.sleep(1)
                    print('.')
                    time.sleep(1)
                    print('.')
                    time.sleep(1)

                    if certo >=2:
                              print("\nBobo: Parabéns! Você é você mesmo")
                    else:
                              print("\nBobo: Meus sentimentos. Mas você não é você")
                              time.sleep(1)
                              print("Bobo: GUARDAS!!")
                              time.sleep(2)
                              print("\nVocê vê vários guardas vindo na sua direção")
                              time.sleep(2)

                              print("\nFicar[1]")
                              print("Correr[2]")

                              decisao=input("Decisão:")
                              time.sleep(2)
                              
                              if decisao =='1':
                                        print("\nSe ficar os guardas comem?")
                                        time.sleep(1)
                                        print("Você Morreu")
                                        time.sleep(1)
                                        print("\nFIM DE JOGO")
                                        print("Espero que sua longa jornada tenha sido legal\n")
                                        time.sleep(1)
                                        print("Mas ela chegou ao fim. Fique a vontade pra começar tudo de novo")
                                        time.sleep(1)
                                        print("Créditos\nCriador: João Gomes\nDesenvolvedor: João Gomes\nEditor:João Gomes\nGênio por trás de tudo: João Gomes")
                                        break
                              
                              if decisao =='2':
                                        print("\nSe correr os guardas pegam")
                                        time.sleep(1)
                                        print("Você Morreu")
                                        time.sleep(1)
                                        print("\nFIM DE JOGO")
                                        print("Espero que sua longa jornada tenha sido legal\n")
                                        time.sleep(1)
                                        print("Mas ela chegou ao fim. Fique a vontade pra começar tudo de novo")
                                        time.sleep(1)
                                        print("Créditos\nCriador: João Gomes\nDesenvolvedor: João Gomes\nEditor:João Gomes\nGênio por trás de tudo: João Gomes")
                                        break

                    time.sleep(2)
                    print("\nAs portas do trono real começam a se abrir")
                    time.sleep(1)
                    print('.')
                    time.sleep(1)
                    print('.')
                    time.sleep(1)
                    print("\nBonvoiage: Alto lá!")
                    time.sleep(1)
                    print("\nBobo: É melhor trocar de nome, alteza")
                    time.sleep(1)
                    print("\nRei: Chega de suas brincadeiras, bobo! Não é hora")
                    time.sleep(1)
                    print("Rei: Você é",name,", certo?")
                    print("Rei: Filho de Ameno")
                    time.sleep(2)

                    print("\nSim[1]")
                    print("Não[2]")

                    decisao=input("Resposta:")
                    time.sleep(2)

                    print("\nBobo: Isso faz diferença?")
                    time.sleep(1)
                    print("\nTodos se olham")
                    time.sleep(1)
                    print('.')
                    time.sleep(1)
                    print('.')
                    time.sleep(1)
                    print("Rei: Nenhuma. É verdade... ai você falou o que eu não esperava")
                    time.sleep(1)
                    print('.')
                    time.sleep(1)
                    print('.')
                    time.sleep(1)
                    print("Rei: Enfim. Eu sei o porquê da sua vinda até meu reino, peregrino!!")
                    time.sleep(1)
                    print("Rei: Eu não sei como, mas sei que o que buscas é o dragão")
                    time.sleep(1)
                    print("Rei: Receio que por minha culpa, uma pessoa não foi capaz de controlar a magia que habita nosso mundo")
                    time.sleep(1)
                    print("Rei: Receio que essa mesma pessoa se transformou em um dragão")
                    time.sleep(1)
                    print("\nBobo: C-A-R-A-C-A! QUE MANEIRO")
                    time.sleep(1)
                    print("Bobo: De onde eu venho isso é impossível, mas iria ser muito bom")
                    time.sleep(1)
                    print("\nRei: Já disse pra ficar quieto, bobo")
                    time.sleep(1)
                    print("\nBobo: Tecnicamente... o senhor disse que não era hora pra brincadeiras...")
                    print("Bobo: E eu não estou brincando")
                    time.sleep(2)

                    print("\nConcordar com bobo[1]")
                    print("Repreender bobo[2]")

                    decisao=input("Resposta:")
                    time.sleep(2)

                    if decisao =='2':
                              idiot=idiot+1
                              print("\nBobo: Você não sabe do que eu sou capaz, garoto")
                              time.sleep(1)
                              print("Bobo: Tome uma demonstração do meu poder")
                              time.sleep(2)
                              print("Você Morreu")
                              time.sleep(1)
                              print("FIM DE JOGO")
                              time.sleep(3)
                              print("encerrar jogo[0] ou voltar pro último checkpoint[1]:")         
                              game_over=input("Sua resposta:")
                              if game_over=='0':
                                        jogo=0
                                        print("Espero que sua longa jornada tenha sido legal\n")
                                        print("Créditos\nCriador: João Gomes\nDesenvolvedor: João Gomes\nEditor:João Gomes\nGênio por trás de tudo: João Gomes")
                                        break
                              if game_over=='1':
                                        print("Voltando ao checkpoint")
                                        time.sleep(2)
                                        print("\nConcordar com bobo[1]")
                                        print("Repreender bobo[2]")

                                        decisao=input("Resposta:")
                                        time.sleep(2)

                                        if decisao =='2':
                                                  print("\nBobo: Sem tempo para engraçadinhos como você")
                                                  time.sleep(2)
                                                  print("FIM DE JOGO")
                                                  print("Créditos\nCriador: João Gomes\nDesenvolvedor: João Gomes\nEditor:João Gomes\nGênio por trás de tudo: João Gomes")
                                                  break

                    if decisao =='1':
                              print("\nRei: Não acredito que você concorda com esse animal. GUARDAS!!!")
                              time.sleep(1)
                              print("\nOs guardas se aproximam")
                              time.sleep(1)
                              print("Você escuta a marcha ficando cada vez mais próxima e alta")
                              time.sleep(1)
                              print("\nBobo: Tu vai ficar parado que nem um trem estacionado??")
                              time.sleep(2)

                              print("\nO que eu vou fazer bobo?[1]")
                              print("Quem ta tendo um ataque de pelancas é o rei[2]")
                              print("\nDecisão:")
                              time.sleep(1)

                              print("\nBobo: Não temos tempo pra conversa. Me siga. RÁPIDO!")
                              time.sleep(1)
                              print("Bobo: Não fica ai parado. Você já tem a resposta pra sua pergunta")
                              time.sleep(2)

                              print("\nSeguir bobo[1]")
                              print("Morrer nas mãos dos guardas enquanto o rei assite[2]")
                              print("Decisão")
                              time.sleep(1.78)

                              print("\nBobo: *pega na sua mão* Anda logo, biruloiro")
                              time.sleep(1)
                              print("\nO bobo te puxa até a janela mais próxima e grita")
                              time.sleep(1)
                              print("\nBobo: PULA!")
                              time.sleep(1)
                              print("↓")
                              time.sleep(1)
                              print("↓")
                              time.sleep(1)
                              print('↓')
                              time.sleep(1)
                              print("\nBobo: Foi emocionante. Você gritou?")
                              time.sleep(1)
                              print("Bobo: Deixa pra lá")
                              time.sleep(1)
                              print("Bobo: Você precisa correr")
                              time.sleep(1)

                              if idiot >=3:
                                        print("Bobo: Caso você não tenha entendido")
                                        time.sleep(1)
                                        print("Bobo: A pessoa que virou um dagrão é a pessoa que você procura")
                                        time.sleep(1)

                                        print("\nEntendi[1]")
                                        print("Não entendi[2]")

                                        print("\nBobo: Tome o tempo que precisar para entender")

                                        decisao=input("Decisão:")
                                        time.sleep(2)

                                        if decisao =='2':
                                                  print("\nBobo: Por Rá! Você é idiota, só pode")
                                                  time.sleep(1)
                                                  print("Bobo: O Bonvoiage queria lacrar a magia do mundo em uma pessoa e depois matar essa pessoa")
                                                  time.sleep(1)
                                                  print("Bobo: O que ele não contava é que a magia ficou fora de controle e aconteceu o que aconteceu")
                                                  time.sleep(1)

                                        print("\nBobo: Agora que você entende, vá!")
                                        time.sleep(1)
                                        print("Bobo: Fuja, Simba! Fuja para longe. E não volte mais")
                                        time.sleep(1)
                                        print("Bobo: Reconhece essa frase? É de um filme infantil muito querido")
                                        time.sleep(1)
                                        print("Bobo: Brincadeiras a parte. Eu te acompanho se você quiser")
                                        time.sleep(2)

                                        print("\nAdicionar Bobo na aventura[1]")
                                        print("Não deixar Bobo se juntar[2]")

                                        decisao=input("Decisão:")
                                        time.sleep(2)

                                        if decisao =='2':
                                                  print("\nBobo: Tudo bem! Não se incomode comigo")
                                                  time.sleep(1)
                                                  print("Bobo: Não irei te seguir")
                                                  time.sleep(1)
                                                  print("Bobo: Só irei limpar as suas pegadas logo atrás de você para que ninguém te siga")

                                        if decisao =='1':
                                                  print("\nBobo: Shoow!")

                                        time.sleep(2)
                                        print("-- Bobo se juntou a aventura --")
                                        time.sleep(1)
                                        print("\nBobo: Olha! Meu apelido ali em cima")
                                        time.sleep(1)
                                        print("Bobo: A propósito, meu nome é...")
                                        time.sleep(1)
                                        print("Os guardas começam a sair do castelo e correr atrás de vocês")
                                        time.sleep(2)

                                        print("\nCorrer[1]")
                                        print("Esperar bobo terminar a frase[2]")

                                        decisao=input("Decisão:")
                                        time.sleep(2)

                                        if decisao =='2':
                                                  idiot=idiot+1
                                                  print("\nUma flecha te acerta no meio dos olhos")
                                                  time.sleep(1)
                                                  print("Você morreu")
                                                  time.sleep(2)
                                                  print("FIM DE JOGO")
                                                  time.sleep(3)
                                                  print("encerrar jogo[0] ou voltar pro último checkpoint[1]:")         
                                                  game_over=input("Sua resposta:")
                                                  if game_over=='0':
                                                            jogo=0
                                                            print("Espero que sua longa jornada tenha sido legal\n")
                                                            print("Créditos\nCriador: João Gomes\nDesenvolvedor: João Gomes\nEditor:João Gomes\nGênio por trás de tudo: João Gomes")
                                                            break
                                                  if game_over=='1':
                                                            print("Voltando ao checkpoint")
                                                            time.sleep(2)

                                                            print("\nCorrer[1]")
                                                            print("Esperar bobo terminar a frase[2]")

                                                            decisao=input("Decisão:")
                                                            time.sleep(2)

                                                            if decisao =='2':
                                                                      print("\nBobo: MEU DEUS, OS GUARDAS. CORRE, BERG!")
                                                                      time.sleep(1)

                                        if decisao =='1':
                                                  print("\nVocês começam a correr pra fora do vilarejo")
                                                  

                              print("\nAdicionar Bobo na aventura[1]")
                              print("Não deixar Bobo se juntar[2]")

                              decisao=input("Decisão:")
                              time.sleep(2)

                              if decisao =='2':
                                        print("\nBobo: Tudo bem! Não se incomode comigo")
                                        time.sleep(1)
                                        print("Bobo: Não irei te seguir")
                                        time.sleep(1)
                                        print("Bobo: Só irei limpar as suas pegadas logo atrás de você para que ninguém te siga")

                              if decisao =='1':
                                        print("\nBobo: Shoow!")

                              time.sleep(2)
                              print("-- Bobo se juntou a aventura --")
                              time.sleep(1)
                              print("\nBobo: Olha! Meu apelido ali em cima")
                              time.sleep(1)
                              print("Bobo: A propósito, meu nome é...")
                              time.sleep(1)
                              print("Os guardas começam a sair do castelo e correr atrás de vocês")
                              time.sleep(2)

                              print("\nCorrer[1]")
                              print("Esperar bobo terminar a frase[2]")

                              decisao=input("Decisão:")
                              time.sleep(2)

                              if decisao =='2':
                                        idiot=idiot+1
                                        print("Uma flecha te acerta no meio dos olhos")
                                        time.sleep(1)
                                        print("Você morreu")
                                        time.sleep(2)
                                        print("FIM DE JOGO")
                                        time.sleep(3)
                                        print("encerrar jogo[0] ou voltar pro último checkpoint[1]:")         
                                        game_over=input("Sua resposta:")
                                        if game_over=='0':
                                                  jogo=0
                                                  print("Espero que sua longa jornada tenha sido legal\n")
                                                  print("Créditos\nCriador: João Gomes\nDesenvolvedor: João Gomes\nEditor:João Gomes\nGênio por trás de tudo: João Gomes")
                                                  break
                                        if game_over=='1':
                                                  print("Voltando ao checkpoint")
                                                  time.sleep(2)

                                                  print("\nCorrer[1]")
                                                  print("Esperar bobo terminar a frase[2]")

                                                  decisao=input("Decisão:")
                                                  time.sleep(2)

                                                  if decisao =='2':
                                                            print("\nBobo: MEU DEUS, OS GUARDAS. CORRE, BERG!")
                                                            time.sleep(1)

                              if decisao =='1':
                                        print("\nVocês começam a correr pra fora do vilarejo")                   

                    #FASE 4 --A CORRIDA ATÉ A MONTANHA--
                              
                    
                                        
                                        
                    
                               
                    
                    
                    
                    
                              
                    
                                         
                    
                                                  
                                                                      
                                                             
                                                  
                              
                              
                    

                                                  
                    
                              
                              

















