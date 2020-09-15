# FRESH BLOOD

# Ana Paula Castro 31927017
# Beatriz Cesário Bertan 31955312
# Marcela de Oliveira Sousa 31958443
# Turma 1H - 2019

import time
import random

nome = str(input("Insira seu nome para começarmos:"))
print ("Tudo pronto! \n")
time.sleep(1)
print ("Iniciando o jogo... \n")
time.sleep(1)
print ("----------------------------------------- \n")
time.sleep(1)
print ("Você,", nome, ", é um(a) agente da Divison of Security Operations (DSO) e recebeu uma missão de resgatar a filha do presidente, Mildred, que está presa em uma mansão. \n")
time.sleep(2.5)
print ("Acontece que, ao chegar lá, você descobre que a casa estava cercada por zombies e descofia que a garota já havia sido transformada em um desses monstros. \n")
time.sleep(2.5)
print ("Sua missão agora é salvar sua própria vida e conseguir achar Mildred. \n")
time.sleep(2.5)
print ("Será que você é capaz? \n")
time.sleep(3)
print ("Mas antes, leia as instruções do jogo. \n")
time.sleep(1.5)
print ("Instruções: Esse jogo será dividido em três partes.")
time.sleep(1.5)
print ("O sistema de pontuação será baseado na sua quantidade de balas.")
time.sleep(1.5)
print ("Cada zombie morre com 1 bala na cabeça, procure não errar para não ficar sem munição.")
time.sleep(1.5)
print ("Você sempre começará o jogo com 8 balas. \n")
time.sleep(1.5)
print ("Boa sorte. \n")
time.sleep(1)
print ("----------------------------------------- \n")
time.sleep(1)


# Munição
bala = 8

    
# Entrando na mansão
start = str(input("Aperte enter para começar:"))
time.sleep(1.5)
print ("Um carro da DSO o(a) deixou próximo a mansão onde está seu objetivo. \n")
time.sleep(1.5)
print ("Você salta do carro, e vai em direção aos fundos da mansão. \n")
time.sleep(1.5)
print ("Sua chegada não passou despercebida. \n")
time.sleep(1.5)
print ("Atravessando o jardim em alta velocidade, pois está infestado de zombies, você logo chega até a casa e avista uma porta de vidro quebrada que é a entrada da cozinha. \n")
time.sleep(1.5)
print ("Ao passar pela porta quebrada, você vê um armário e o utiliza para tampar aquela abertura. \n")
time.sleep(1.5)
print ("Dentro da cozinha, você avista um walkie-talkie em cima do balcão, você se aproxima para pegá-lo, mas algo te impede. \n")
time.sleep(1.5)
print ("CUIDADO! \n")
time.sleep(1.5)
print ("Dois cachorros-zombie enormes estão logo atrás de você, o rosnado deles te arrepia, porém ainda há tempo de tomar decisões sobre o que fazer. \n")

choise1 = input("Você escolhe atirar/correr/gritar: \n")
              
if choise1 == "atirar":
    print ("Você saca sua arma com silenciador e atira no primeiro cachorro que avança em você, conseguindo o matar.\n")
    print ("Porém o segundo cachorro é mais veloz, ele pula em você tão rapidamente, que você nem consegue atirar.\n")
    time.sleep(1.5)
    print ("Lutando com a fera infectada, sua arma é jogada para longe de você, fazendo com que sua única arma seja um pedaço de madeira jogado no meio da cozinha.\n")
    time.sleep(1.5)
    print ("Em um movimento rápido, você pega o pedaço de madeira, e enfia na cabeça do cachorro-zombie, e consegue se livrar do monstro feroz. \n")
    time.sleep (1.5)
    ran1 = random.randrange(1, 5)
    print ("Você gastou", ran1, "balas.\n")
    bala1 = bala - ran1
    time.sleep(1.5)
    print ("Agora você possui", bala1, "balas. \n")
    time.sleep(1)
    print ("Após o momento de tensão, você se levanta empurrando o cachorro de cima de você e pega o walkie-talkie, você tenta fazer contato com alguém através do aparelho, porém não há resposta. \n")
    time.sleep(1.5)
    print ("Você teme que algum zombie da mansão tenha escutado toda a ação, então você rapidamente vasculha a cozinha. \n")
    
    choise2 = input("Vasculhar os armarios/gavetas:\n")
    
    if choise2 == "gavetas":
        print("Você vascula as gavetas, a procura de algo útil.\n")
        time.sleep(1.5)
        print("Ótima escolha! Você encontrou munição!\n")
        time.sleep(1.5)
        ran2 = random.randrange(1, 6)
        bala2 = bala1 + ran2
        print("Você ganhou", ran2, "balas.\n")
        time.sleep(1.5)
        print("Agora você possui", bala2, "balas.\n")

        
    else:
        print("Você vasculha os armários, a procura de algo útil.\n")
        time.sleep(1.5)
        print("Porém tudo o que encontra é pó e comida enlatada.\n")
        time.sleep(1.5)
        bala2 = bala1
        print("Você continua com", bala2,"balas.\n")
        
    time.sleep(1.5)
    print("Você sai da cozinha rapidamente, e passa pelo salão principal da mansão, você avista alguns zombies, porém mesmo com todo o barulho da cena anterior, eles não estão agitados, e nem ao menos perceberam você ali.\n")
    time.sleep(1.5)
    print("Entretanto, o walkie-talkie começa a receber uma mensagem com um som consideravelmente alto. Era uma voz feminina, perguntanto se tinha alguém do outro lado, essas poucas palavras foram o suficiente para chamar a atenção dos zombies que estavam logo a frente.\n")
    time.sleep(1.5)
    ran3 = random.randrange(2,5)
    print("Isso faz com que todos os zombies apareçam na sua frente, indo em sua direção. Você acredita que consegue enfrentá-los, mesmo eles estando em", ran3,".\n")

    choise3 = input("Você escolhe atirar na cabeça/perna/braço dos zombies?\n")
    
    if choise3 == "cabeça":
        print("Você acertou o ponto fraco dos zombies.\n")
        time.sleep(1)
        print("Você acerta todos os tiros, executando belos headshots, passando pelo obstáculo com maestria.\n")
        time.sleep(1.5)
        bala3 = bala2 - ran3
        print("Você gastou ", ran3, "balas.\n")
        time.sleep(1)
        print("Agora você possui", bala3,"balas.\n")
        time.sleep(2)

        print("Logo após o extermínio dos zombies, você pega novamente o walkie-talkie, que está preso no seu cinto, e tenta se comunicar novamente, e finalmente você obteve uma resposta.\n")
        time.sleep(1.5)
        print("Era Mildred! Ela estava escondida no andar de cima da casa, dentro de um armário, mas não conseguia sair pois tinha ouvido barulhos estranhos, então ficou aguardando por ajuda. \n")
        time.sleep(1.5)
        print("Quem é você?, pergunta Mildred, e você responde: Meu nome é", nome,", sou o(a) agente contratado(a) para resgatar você! \n")
        time.sleep(1.5)
        print("Você escuta um breve choro pelo walkie-talkie, Mildred agradece por você ter vindo ajudá-la a sair dali. \n")
        time.sleep(1.5)
        print("Você pede para ela manter a calma e que logo estará a salvo, e reforça que já está indo para o próximo piso. \n")
        time.sleep(4)
        print ("-----------------------------------------\n")
        time.sleep(4)
        # Entrando no quarto de Sofia
        print ("Você sabia que sua missão era salvar a filha do presidente, mas não achava que zombies estavam incluídos no pacote. Então, ao subir as escadas e dar de cara com um corredor, torcia para que Mildred estivesse bem, já que a garota não respondia mais ao walkie-talkie. \n")
        time.sleep(3.5)
        print ("Andando pelo corredor, você encontra duas portas um pouco abertas. Uma localizada à direita e a outra à esquerda.\n")
        porta = input("Você entra na direita/esquerda: \n")
        if porta == "direita":
            print("Você abre a porta da direita e lá está Mildred, com uma garotinha, brincando de boneca. \n")
            time.sleep(2.5)
            print ("Entretanto, Mildred parece assustada. \n")
            time.sleep(2.5)
            print ("A criança se vira ao perceber sua presença, diz que se chama Sofia e a sua boneca - ela aponta para Mildred - se chama Charlotte. \n")
            time.sleep(2.5)
            print("- Você também quer brincar? \n")
            resp = (input("Você responde que sim/não: \n"))
            if resp == "sim":
                print("Você decide brincar com Sofia e Mildred, e caminha para se sentar na terceira cadeirinha que estava vazia.")
                time.sleep(2.5)
                print("Esquecendo de sua missão, você, Mildred e Sofia têm uma tarde agradável, brincando e tomando chá \n")
                time.sleep(2.5)
                print ("Entretanto, ao anoitecer, Sofia diz que está com fome. Ela revela sua verdadeira forma e ataca Mildred e você. \n")
                time.sleep(2.5)
                print("~you are dead ~ \n")
                time.sleep(1.5)
                print("Você não apenas foi comido(a), como também fracassou em sua missão. Mas veja pelo lado bom, o jantar estava delicioso :D")
            else:
                print ("Você responde que não, pois infelizmente está com pressa e precisa ir... mas é preciso levar Charlotte. \n")
                time.sleep(3.5)
                print ("Sofia não parece gostar da notícia e, agora, é possível notar o walkie-talkie em sua mão, e você entende o motivo de Mildred parar de responder. A criança balança a cabeça, evitando se enfurecer, e pega um dado entre seus brinquedos. Então, ela te propõe um desafio:\n")
                time.sleep(2)
                print ("Escolha um número de 1 a 6, caso o valor do dado resulte no de sua escolha, você vence e pode ir embora com Mildred. Caso contrário, Mildred fica e você…\n \n")
                time.sleep(3)
                print("morre. \n")
                time.sleep(1.0)
   # Condição / Desafio
                a = int (input ("Escolha seu número:") )
                time.sleep(1.0)
                b = random.randrange(1,7,2)
                if  b == a:
                    print("\n Por alguns segundo o dado rodou e rodou, até finalmente parar em um número... o seu número:", a)
                    time.sleep(2.5)
                    print("- Você... ganhou - Sofia murmura, seu olhar fixo no dado. \n")
                    time.sleep(2.5)
                    print("Pode ser impressão sua, mas havia um tique nos lábios da menina. \n")
                    time.sleep(3.5)
                    print("Mas não era impressão, pois no segundo seguinte, ela arfa e de sua boca escapa um grito suficientemente alto para toda a casa ouvir. \n")
                    time.sleep(3.5)
                    print("- Não, não, não, não, não, não, não, NÃO! Charlotte não vai embora, Charlotte não vai embora. Charlotte vai ficar aqui, junto comigo. Você não vai levar Charlotte embora, ela é a minha boneca e eu vou ficar com ela... - Sofia chora em agonia, mas para. - Nem que eu precise matar você. \n")
                    time.sleep(3.5)
                    print("Ao longe, os zombies que habitavam a mansão pareciam responder ao grito de Sofia, e estavam famintos e ferozes. Não obstante, a menina tremia, com seu corpo deformando aos poucos. \n")
                    time.sleep(2.5)
                    print("Você sente um arrepio por seu corpo, te alertando: ficar ali era sinônimo de morte.\n")
                    time.sleep(3.5)
                    print("Sem perder tempo, você agarra o braço de Mildred, que durante todo o tempo parecia estar em estado de choque, e corre porta a fora, se encontrando mais uma vez no corredor. \n")
                    time.sleep(3)

                    print ("-----------------------------------------\n")
                    
                    time.sleep(3)
                    # Entrando no Terraço
                    print ("Você está desesperado(a) para sair dali, pois conforme seus instintos, Sofia não seria um oponente fácil de combater , você e Mildred sobem todos os lances de escada que a mansão possuía, \n")
                    time.sleep(1.5)
                    print("porém se deparam com 2 zombies à frente, você pode parar e cobrar esses zombies, ou seguir em frente.\n")       

                    st = (input("Você decide parar/seguir:\n"))
                    if st == "seguir":
                        print("Você decide não parar para matar aqueles zombies, que, afinal de contas, nem estavam no seu caminho\n")
                        time.sleep(1.5)
                        print("Você gastou 0 balas.\n")
                        time.sleep(1.5)
                        bala4 = bala3
                        print("Portanto, sua quantidade de balas é: ", bala4,"\n")
                    else: 
                        print("Você decide parar para atacar os zombies, mas será que tinha necessidade mesmo?\n")
                        time.sleep(1.5)
                        print("Você mata os dois zombies, mas perde 2 balas, valeu a pena?\n")
                        time.sleep(1.5)
                        print("Portanto, você fica com ", bala4 - 2, "balas.\n")
                        time.sleep(1.5)
                        
                    print ("Chegando ao último lance de escada, no andar mais alto da casa. Não há mais volta e nem por onde ir, mas avistaram uma porta, a única existente, adentraram e perceberam que estão no terraço.\n")
                    time.sleep(1.5)
                    print ("Mildred se afasta um pouco para observar o local e procurar alguma coisa para se defender, e acaba encontrando uma pequena caixa de munição que se localizava em cima de uma lata de lixo, ela pega a caixa e te entrega.\n")
                    time.sleep(1.5)
                    ran4 = random.randrange(1,9)
                    bala5 = bala4 + ran4
                    print("Você ganha", ran4, "balas.")
                    time.sleep(1.5)
                    print("Agora você possui", bala5, "balas.")
                    time.sleep(1.5)
                    print ("Você agradece a garota e ambos escutam barulhos, vindos da porta do terraço, os dois se afastam dali e Sofia aparece para  enfrentá-los. Sua aparência é horrenda e a cada segundo fica mais bizarra e difícil de decifrar o que exatamente é Sofia.\n")
                    time.sleep(1.5)
                    print ("Vocês precisam escolher entre qual parte do terraço ficar.\n")
                    ter = (input("Escolha entre esquerda/direita:"))
                                 
                    if ter == "esquerda" or ter == "direita":
                        print("Você fica em um dos cantos do terraço, o que facilita na hora de encontrar uma saída.\n")
                        qzombie = random.randrange(3,9)
                        print("E é nesse momento em que vários zombies aparecem no local em que vocês se encontram, e para não conseguirem atacar nem você ou Mildred você acaba atirando em todos os ",qzombie, "zombies.\n")
                        time.sleep(1.5)
                        bala6 = bala5 - qzombie
                        print("Você gasta", qzombie + 1, "balas.\n")
                        time.sleep(1.5)        
                        print("Agora você possui", bala6, "balas.\n")
                        time.sleep(1.5)
                        print("Sofia está furiosa por não ter conseguido matar você e nem ter ficado com Mildred, então ela finalmente os ataca. Sofia corre para cima de você.\n")
                        time.sleep(1.5)
                        print("Voce consegue desviar do ataque de Sofia e revida contra a mesma, atirando algumas vezes. Conforme vai acertando todos os tiros em Sofia, que já está se sentindo mais fraca e lenta, porém, a mesma não desiste e continua suas investidas, pois, só desistiria quando você estivesse morto(a).\n")
                        time.sleep(1.5)
                        print ("Após um tempo desviando dos ataques, você está exausto(a), você atira mais uma vez, e se sente extremamente ofegante e sem uma boa qualidade de mira. Mildred está com algumas lesões no corpo, mas mesmo assim estava bem e você está com alguns ferimentos.\n")
                        time.sleep(1.5)
                        print ("No que seria o último ataque de Sofia, ela para e vocês escutam um barulho, e ficam todos cegos por uma forte luz e surdos por conta do barulho elevado. Está luz branca estava diretamente direcionada no terraço.\n")
                        time.sleep(1.5)
                        print ("São outros agentes da DSO! Chegaram com um enorme helicóptero, para ajudar a concluir a missão, ou seja, salvar Mildred. Eles realizaram um ataque forte e bem planejado contra Sofia e a mesma gritava em agonia por ser atingida pelos tiros e por querer escapar dessa situação, entretanto caiu perto da sacada, bateu a cabeça e morreu por ali.\n")
                        time.sleep(1.5)
                        print ("Você e Mildred foram diretamente para o helicóptero, onde paramédicos os esperavam para tratar seus ferimentos.\n")
                        time.sleep(3)
                        print ("Você concluiu sua missão e saiu vivo.\n")
                        time.sleep(3)
                        print ("Seu total de balas é:", bala6)
                        time.sleep(1)
                        
                        if bala6 <= 1:
                            print("Sua pontuação foi baixa. Boa sorte na próxima jogada.\n")
                        elif bala6 >= 1 and bala6 <= 4:
                            print ("Sua pontuação foi média, mas você ainda pode melhorar. Boa sorte na próxima jogada.\n")
                        else:
                            print ("Sua pontuação foi alta! Parabénss!!! Você é um verdadeiro agente, a empresa está orgulhosa! \n")
                        time.sleep(1)
                        print ("Parabéns, você finalizou o jogo.")
                        time.sleep(3)

#Condições de EndGame


                else:
                    print("\n Por alguns segundo o dado rodou e rodou, até finalmente parar em um número... mas não era o seu:", b)
                    time.sleep(2.5)
                    print("\n Sofia sorri, batendo palmas animadamente.\n")
                    print("- Ownn, parece que alguém perdeu…")
                    time.sleep(1.5)
                    print ("\n ~ you are dead ~")

                        
        else:
            print("Você abre a porta da esquerda, dando de cara com um zombie. \n")
            time.sleep(1.5)
            print ("Você tenta pegar sua arma, mas, infelizmente para você, o monstro é mais rápido.  \n")
            time.sleep(1.5)
            print("~ you are dead ~ ")


    elif choise3 == "perna":
        print("Você acertou as pernas dos zombies.\n")
        time.sleep(1)
        print("É uma estratégia válida para atrasá-los, mas não matá-los.\n")
        time.sleep(1.5)
        print("Não importa mais quantas balas foram gastas, você é alcançado pelos zombies, e é encurralado(a).")
        time.sleep(1.5)
        print("~you are dead~")
        
    else:
        print("Você acertou os braços dos zombies.\n")
        time.sleep(1)
        print("É uma estratégia nem um pouco efetiva, preste mais atenção nas instruções.\n")
        time.sleep(1.5)
        print("Não importa mais quantas balas foram gastas, você é alcançado pelos zombies, e é encurralado(a).")
        time.sleep(1.5)
        print("~you are dead~")
          


    
elif choise1 == "correr":
    print ("Você decide correr, esquecendo de todo o seu treinamento, porém os cachorros não desistem, pulam em você e te matam com seus dentes infecciosos.")
    time.sleep(2)
    print ("~you are dead~")


    
else:
    print ("Você se desespera e acaba soltando um grito agudo, o que deixa os cachorros-zombie muito animados pela carne fresca e medrosa à frente deles.")
    time.sleep(1)
    print ("Você ainda se chama de profissional?")
    time.sleep(1)
    print ("Enquanto você tenta responder essa pergunta, os cachorros avançam em você e te matam com seus dentes infecciosos.")
    time.sleep(2)
    print ("~you are dead~")
              




