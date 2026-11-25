# Política de Privacidade — Hyakki Survivor: Até o amanhecer

> **Nota para o desenvolvedor (não faz parte da política):** a fonte desta política (este `.md`) e a
> página publicada (`/privacy-policy.html`, na raiz deste repositório `netstart/netstart.github.io`)
> vivem AQUI, no repositório do site; o repositório do jogo (hyakki) não tem mais cópia. A URL
> oficial, usada na Play Console e no jogo, é <https://netstart.github.io/privacy-policy.html>; as
> URLs antigas <https://netstart.github.io/games/hyakki/privacy-policy.html> e
> <https://netstart.github.io/hyakki/privacy-policy.html> só redirecionam para ela. Mantenha este
> `.md` e o `.html` com o mesmo conteúdo e a mesma data (o hook `.githooks/check_site.py` confere a
> data). Revise a seção "Anúncios" se mudar a rede de anúncios, o SDK ou se passar a haver servidor
> próprio. O guia de publicação continua em `docs/store/play-console-guia.md` do hyakki.

Última atualização: 25 de novembro de 2026

## Português (Brasil)

**Quem somos.** *Hyakki Survivor: Até o amanhecer* (pacote Android `io.github.netstart.hyakki`) é um jogo
independente para Android e para PC (Windows, vendido na Steam) feito por um desenvolvedor individual
(GitHub: netstart), que é o controlador dos dados descritos aqui. Contato de privacidade:
**netstart@gmail.com**.

**Resumo.** O jogo não tem conta, login, chat nem conteúdo enviado por jogadores, e não pede sua
localização, contatos, fotos, microfone ou câmera. Não temos servidor: não recebemos nenhum dado seu.
No Android, o jogo mostra apenas anúncios premiados opcionais, que você escolhe assistir; não há
anúncio ao abrir o jogo. Nenhum anúncio interrompe uma partida. O jogo pede seu consentimento onde a
lei exige. Na versão de PC (Steam), o jogo é pago e já vem completo: não há anúncios, ID de
publicidade nem compras no jogo (veja "Versão de PC (Steam)").

**O que fica no seu aparelho.** O progresso (ryō, desbloqueios, conquistas, a sequência do Desafio Diário, quantas Bênçãos do Santuário você usou no dia, quais ofertas do jogo você já viu e as configurações, incluindo as opções de acessibilidade, como o modo daltônico, o tremor de tela e as legendas), uma partida suspensa e um registro local das partidas, usado só para equilibrar o jogo dentro do próprio
aparelho, ficam salvos na memória interna do aparelho. Esses dados não são enviados a nós nem a
terceiros. Se o backup do Android estiver ligado no aparelho, o progresso, a partida suspensa e as
configurações (não o registro das partidas) podem entrar no backup da sua própria conta Google
(Google Drive, criptografado no Android 9 ou superior) e voltar ao reinstalar o jogo ou trocar de
celular; você controla isso nas configurações do aparelho. Apagar o app ou usar Opções › Apagar
progresso remove tudo do aparelho, de forma definitiva.

**Permissões (Android).** O jogo funciona sem internet. As permissões de internet e de estado da rede existem
para os anúncios, para a compra pelo Google Play e para o cooperativo na rede local; a vibração é usada nos efeitos do
jogo e pode ser desligada em Opções. As bibliotecas do Google incluídas no app também declaram as
permissões de ID de publicidade (`AD_ID`) e de faturamento do Google Play (`BILLING`).

**Anúncios (Android).** No Android, o jogo usa o Google AdMob apenas para anúncios premiados que você escolhe
assistir; não há anúncio ao abrir o jogo e nenhum anúncio interrompe uma partida. Cada anúncio só aparece quando você toca para assistir, em troca de uma recompensa no jogo (por exemplo, na Loja, para reviver, para dobrar o ryō ou na Bênção do Santuário, que nos Resultados dá mais uma sorte do baú, até 3 vezes por dia); não há anúncio intersticial, banner nem anúncio obrigatório. Quem fez a compra "Apoiar o jogo" recebe as recompensas sem assistir anúncio. O SDK do Google Mobile Ads, operado pelo Google,
pode coletar e compartilhar com o Google, de forma criptografada (TLS): o endereço IP (para estimar a
localização aproximada), o ID de publicidade do Android e o ID do conjunto de apps, interações com os
anúncios (aberturas, toques, vídeos vistos) e dados de diagnóstico (desempenho do app e do SDK), para
publicidade, análise e prevenção de fraudes. Onde a lei exige (por exemplo, no Espaço Econômico
Europeu, no Reino Unido e na Suíça), o jogo mostra antes o formulário de consentimento do Google
(UMP); se você recusar, verá anúncios não personalizados. Você pode rever a escolha em
Opções › Privacidade e anúncios e redefinir ou excluir o ID de publicidade nas configurações do
Android. O jogo só solicita anúncios quando há conexão com a internet. Como o Google usa esses dados:
<https://policies.google.com/privacy> e
<https://policies.google.com/technologies/partner-sites>. A versão de PC não tem anúncios nem o SDK
do Google Mobile Ads.

**Cooperativo local (Duas Lanternas).** O modo para 2 jogadores funciona só entre dois aparelhos na mesma rede local (Wi-Fi ou, no PC, também por cabo); não há partida online, servidor, busca de partidas, lista de salas nem anúncio contínuo da sala na rede. Os aparelhos se conectam diretamente (ENet sobre UDP, portas 47320 a 47329), e o aparelho que abre a sala só aceita endereços de rede privada (10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16 e link-local) e recusa os demais. O código de 4 números da sala vem do endereço IP local do aparelho que abre a sala. Para achar a sala quando esse endereço não basta (por exemplo, no roteador do celular com o Wi-Fi também ligado), o aparelho que entra manda, só enquanto conecta e por até 10 segundos, um pequeno pacote UDP com o código da sala para a rede local (em broadcast e para os endereços da própria rede local); o aparelho que abriu a sala escuta nas portas 47330 a 47339 e responde só ao código dele e só a endereços de rede privada, com a porta da sala. Esses pacotes levam só o código e a porta; nada disso sai da rede local nem chega a nós. Durante a partida, os dois aparelhos trocam só o necessário para jogar: o estado da partida (posições, vida e afins), os comandos de controle, o nome da versão do jogo, a guardiã escolhida e os bônus de progresso dela para a partida (Santuário, Laço, Hōju e Omamori). Esses dados passam pela rede local sem criptografia própria do jogo, então jogue numa rede em que você confia. Não há chat, nome de usuário nem conta, e o outro aparelho não guarda seus dados: cada aparelho grava só o resultado e as missões no próprio progresso. No Android, o modo não pede nenhuma permissão nova além da internet e do estado da rede; no PC, o Windows pode pedir que você permita o acesso do jogo à rede na primeira vez que abrir uma sala.

**Compras (Android).** No Android, as compras únicas (não consumíveis) "Apoiar o jogo", "Ampulheta de Fūjin" (velocidade 2x/3x, que também sai com ryō do jogo), a liberação de guardiões (Kuroe, Kurogoromo e os guardiões das fases, que também chegam de graça ao vencer a fase) e os pacotes "Noite da Queda" (Kuroe e Kurogoromo) e "Ordem Completa" (as 7 guardiãs das fases, Kuroe, Kurogoromo e a Ampulheta de Fūjin) são processadas pelo Google
Play, segundo os termos e a política de privacidade do Google. Não recebemos seu nome, e-mail nem
dados de pagamento; o jogo só confere as compras no próprio aparelho, sem servidor próprio, e guarda
no aparelho apenas se cada uma foi feita. Para recuperar as compras (por exemplo, após reinstalar o jogo), use Opções › Restaurar compras. Se uma compra for reembolsada pelo Google Play, o jogo retira só o que veio dela; o que você ganhou jogando (como uma guardiã liberada ao vencer a fase ou a Ampulheta paga com ryō) ou comprou à parte continua seu.

**Versão de PC (Steam).** A versão para PC (Windows) é vendida na Steam, é paga e já inclui tudo o
que no Android é vendido à parte ("Apoiar o jogo", a "Ampulheta de Fūjin" e os guardiões Kuroe e
Kurogoromo; os guardiões das fases chegam ao vencer a fase, como no Android). Nela não há anúncios:
o SDK do Google Mobile Ads e o formulário de consentimento do Google (UMP) não fazem parte do jogo,
nenhum ID de publicidade é lido ou enviado, e as recompensas opcionais chegam de presente. Não há
compras no jogo nem Google Play Billing, e o jogo não inclui o SDK da Steam (Steamworks): não envia
dados à Steam, ao Google nem a nós. A compra, o download e as atualizações são feitos pela Steam,
operada pela Valve Corporation, e regidos pelo Acordo de Assinatura do Steam
(<https://store.steampowered.com/subscriber_agreement/>) e pela Política de Privacidade da Valve
(<https://store.steampowered.com/privacy_agreement/>); a Valve trata os dados da sua conta Steam e do
pagamento, e nós não recebemos seu nome, e-mail nem dados de pagamento. O progresso, a partida
suspensa, as configurações e o registro local das partidas ficam só no computador, na pasta de dados
do usuário (no Windows, `%APPDATA%\Godot\app_userdata\Hyakki`); o jogo não envia esse progresso para
a nuvem. Desinstalar o jogo pela Steam pode não apagar essa pasta: para remover tudo, use
Opções › Apagar progresso ou apague a pasta. Sem internet, o jogo funciona normalmente; a rede só é
usada pelo cooperativo local, descrito acima. As permissões, o backup do Android, os anúncios e as
compras pelo Google Play descritos acima valem só para o Android.

**Crianças.** O jogo é direcionado a pessoas a partir de 13 anos e não coleta, de forma intencional,
dados de crianças menores de 13 anos. Se você é responsável e acredita que uma criança nos enviou
dados, escreva para o contato acima.

**Segurança, retenção e exclusão.** Não guardamos dados em servidores próprios, então não há nada a
reter ou excluir do nosso lado. Os dados locais ficam até você apagar o progresso ou desinstalar o
app; uma cópia no backup do Android fica na sua conta Google e segue as regras e as ferramentas de
backup do Google. No PC, os dados locais ficam até você apagar o progresso ou a pasta de dados do
jogo. Dados tratados pelo Google seguem os prazos e as ferramentas do Google (por
exemplo, a redefinição do ID de publicidade e <https://myaccount.google.com>); dados da sua conta
Steam seguem as regras e as ferramentas da Valve.

**Seus direitos (LGPD e GDPR).** Você pode pedir confirmação de tratamento, acesso, correção,
exclusão, portabilidade e informações sobre compartilhamento, e retirar o consentimento a qualquer
momento. Como não recebemos dados, a resposta, na maioria dos casos, será que não temos dados seus;
para os dados tratados pelo Google ou pela Valve, indicaremos as ferramentas deles. Respondemos em até 15 dias
pelo e-mail acima. Você também pode reclamar à ANPD (Brasil) ou à autoridade de proteção de dados do
seu país. No Android, a base legal para anúncios personalizados é o consentimento; para anúncios não
personalizados e prevenção de fraudes, o legítimo interesse.

**Mudanças.** Se esta política mudar, a nova versão será publicada neste endereço com a data
atualizada. Mudanças relevantes, como trocar a rede de anúncios, também serão avisadas nas notas da versão.

## English

**Who we are.** *Hyakki Survivor: Until Dawn* (Android package `io.github.netstart.hyakki`) is an independent
game for Android and PC (Windows, sold on Steam) made by an individual developer (GitHub: netstart),
who is the controller of the data described here. Privacy contact: **netstart@gmail.com**.

**Summary.** The game has no account, login, chat or user-generated content, and does not ask for
your location, contacts, photos, microphone or camera. We run no server and receive no data from
you. On Android, the game shows only optional rewarded ads that you choose to watch; there is no ad
when the game opens. No ad interrupts a run. The game asks for your consent where the law requires
it. The PC edition (Steam) is a paid game that comes complete: it has no ads, no advertising ID and
no in-game purchases (see "PC edition (Steam)").

**What stays on your device.** Progress (ryō, unlocks, achievements, your Daily Challenge streak, how many Shrine Blessings you used that day, which in-game offers you have already seen and settings, including accessibility options such as color-blind mode, screen shake and captions), a suspended run and
a local log of runs, used only to balance the game on the device itself, are stored in the device's
internal storage. This data is not sent to us or to third parties. If Android backup is turned on
for the device, your progress, suspended run and settings (not the run log) may be included in your
own Google Account backup (Google Drive, encrypted on Android 9 or later) and come back when you
reinstall the game or switch phones; you control this in the device settings. Uninstalling the app
or using Options › Erase progress removes everything from the device permanently.

**Permissions (Android).** The game works offline. The internet and network-state permissions exist for ads,
for purchases through Google Play and for local network co-op; vibration is used for game effects and can be
turned off in Options. The Google libraries bundled with the app also declare the advertising ID
(`AD_ID`) and Google Play billing (`BILLING`) permissions.

**Ads (Android).** On Android, the game uses Google AdMob only for
rewarded ads that you choose to watch; there is no ad when the game opens and no ad ever interrupts a
run. Each ad only appears when you tap to watch it, in exchange for an in-game reward (for example in the Shop, to revive, to double ryō or for the Shrine Blessing, which gives one more chest draw on the Results screen, up to 3 times a day); there are no interstitial, banner or mandatory ads. If you made the "Support the game" purchase, you get the rewards without watching an ad. The Google Mobile Ads SDK, operated by Google, may collect and share with
Google, encrypted in transit (TLS): the IP address (to estimate approximate location), the Android
advertising ID and app set ID, ad interactions (launches, taps, video views) and diagnostics (app and
SDK performance), for advertising, analytics and fraud prevention. Where the law requires it (for
example in the European Economic Area, the United Kingdom and Switzerland), the game first shows
Google's consent form (UMP); if you decline, you will see non-personalized ads. You can review your
choice in Options › Privacy and ads, and reset or delete the advertising ID in Android settings.
The game only requests ads when an internet connection is available. How Google uses this data: <https://policies.google.com/privacy> and
<https://policies.google.com/technologies/partner-sites>. The PC edition has no ads and does not
include the Google Mobile Ads SDK.

**Local co-op (Twin Lanterns).** The 2-player mode works only between two devices on the same local network (Wi-Fi or, on PC, also a wired connection); there is no online play, server, matchmaking, room list or continuous room broadcast on the network. The devices connect directly (ENet over UDP, ports 47320 to 47329), and the device that opens the room only accepts private network addresses (10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16 and link-local) and refuses all others. The 4-digit room code comes from the local IP address of the device that opens the room. To find the room when that address is not enough (for example, on a phone hotspot with Wi-Fi also on), the joining device sends, only while connecting and for up to 10 seconds, a small UDP packet with the room code to the local network (as a broadcast and to the addresses of its own local network); the device that opened the room listens on ports 47330 to 47339 and answers only its own code and only private network addresses, with the room's port. These packets carry only the code and the port; none of this leaves the local network or reaches us. During the run, the two devices exchange only what is needed to play: the run state (positions, health and the like), control inputs, the game version name, the chosen guardian and her progress bonuses for the run (Sanctuary, Bond, Hōju and Omamori). This data travels over the local network without the game's own encryption, so play on a network you trust. There is no chat, username or account, and the other device does not keep your data: each device saves only the result and missions to its own progress. On Android, the mode asks for no new permission beyond internet and network state; on PC, Windows may ask you to allow the game network access the first time you open a room.

**Purchases (Android).** On Android, the one-time (non-consumable) purchases "Support the game", "Fūjin's Hourglass" (2x/3x speed, also available for in-game ryō), guardian unlocks (Kuroe, Kurogoromo and the stage guardians, who also join for free when their stage is cleared) and the "Night of the Fall" (Kuroe and Kurogoromo) and "Complete Order" (the 7 stage guardians, Kuroe, Kurogoromo and Fūjin's Hourglass) bundles are processed by Google
Play under Google's terms and privacy policy. We do not receive your name, email or payment data; the
game checks the purchases only on the device, with no server of our own, and stores on the device only
whether each one was made. To recover the purchases (for example, after reinstalling the game), use Options › Restore purchases. If a purchase is refunded through Google Play, the game removes only what came with it; anything you earned by playing (such as a guardian unlocked by clearing her stage or the Hourglass bought with ryō) or bought separately stays yours.

**PC edition (Steam).** The PC (Windows) edition is sold on Steam, is a paid game and already
includes everything that is sold separately on Android ("Support the game", "Fūjin's Hourglass" and
the guardians Kuroe and Kurogoromo; the stage guardians join when their stage is cleared, as on
Android). It has no ads: the Google Mobile Ads SDK and Google's consent form (UMP) are not part of
the game, no advertising ID is read or sent, and the optional rewards are given as gifts. There are
no in-game purchases and no Google Play Billing, and the game does not include the Steam SDK
(Steamworks): it sends no data to Steam, Google or us. The purchase, download and updates are
handled by Steam, operated by Valve Corporation, under the Steam Subscriber Agreement
(<https://store.steampowered.com/subscriber_agreement/>) and Valve's Privacy Policy
(<https://store.steampowered.com/privacy_agreement/>); Valve processes your Steam account and payment
data, and we do not receive your name, email or payment data. Progress, the suspended run, settings
and the local run log stay only on the computer, in the user data folder (on Windows,
`%APPDATA%\Godot\app_userdata\Hyakki`); the game does not upload this progress to the cloud.
Uninstalling the game through Steam may not delete this folder: to remove everything, use
Options › Erase progress or delete the folder. The game works normally offline; the network is used
only by the local co-op described above. The permissions, Android backup, ads and Google Play
purchases described above apply only to Android.

**Children.** The game is directed at people aged 13 and over and does not knowingly collect data
from children under 13. If you are a parent or guardian and believe a child sent us data, write to
the contact above.

**Security, retention and deletion.** We keep no data on our own servers, so there is nothing to
retain or delete on our side. Local data stays until you erase your progress or uninstall the app; a
copy in the Android backup stays in your Google Account and follows Google's backup rules and tools.
On PC, local data stays until you erase your progress or delete the game's data folder.
Data processed by Google follows Google's retention periods and tools (for example, resetting the
advertising ID and <https://myaccount.google.com>); your Steam account data follows Valve's rules
and tools.

**Your rights (GDPR and LGPD).** You may request confirmation of processing, access, correction,
deletion, portability and information about sharing, and withdraw consent at any time. Since we
receive no data, in most cases the answer will be that we hold no data about you; for data processed
by Google or Valve, we will point you to their tools. We reply within 15 days at the email above. You may
also lodge a complaint with your local data protection authority (in Brazil, the ANPD). On Android, the legal
basis for personalized ads is consent; for non-personalized ads and fraud prevention, legitimate
interest.

**Changes.** If this policy changes, the new version will be published at this address with an
updated date. Relevant changes, such as switching ad networks, will also be announced in the release notes.
