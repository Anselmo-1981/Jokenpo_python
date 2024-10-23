<h2>Jogo do Jokenpô ou Pedra, Papel e Tesoura</h2>
<p>A criação desse programa tem como objetivo treinar a escrita de código usando <strong><i>funções</i></strong> e <strong><i>módulos</i></strong>.
O primeiro módulo <strong><i>' jokenpo_game_main.py '</i></strong> é o programa principal que importa o módulo auxiliar <strong><i>' jokenpo_game_modulo_checa_opcao.py '</i></strong>, 
este contendo as funções <strong><i>' def modulo_checa_opcao() '</i></strong> e <strong><i>' def comparador() '</i></strong> responsáveis por 
todos os testes condicionais do programa.</p>
<p>Outro aspecto interessante é o uso do método <strong><i>' choice() '</i></strong> importado da biblioteca <strong><i>' random '</i></strong>. O método permite a escolha 'randômica' ou 
'aleatória' de um elemento a partir de uma estrutura de dados como uma lista(<strong><i>list</i></strong>) ou tupla(<strong><i>tuple</i></strong>).</p>
<p>Para o uso correto do programa, o jogador deverá seguir as instruções que serão apresentadas na tela e utilizar somente os números 1, 2 e 3 para interagir com o programa. Ao 
  digitar qualquer outro número, o sistema contará 1 ponto a favor do computador. Caracteres alfabéticos (<strong><i>letras</i></strong>), também não devem ser utilizadas, pois 
terão como saída <strong><i>' ValueError: invalid literal for int() with base 10: '</i></strong>.</p>
<h3>COMO O JOGO FUNCIONA</h3>
<ul>
  <li>Pedra empata com pedra;</li>
  <li>Pedra ganha de tesoura;</li>
  <li>Pedra perde para papel;</li>
  <li>Tesoura empata com tesoura;</li>
  <li>Tesoura ganha de papel;</li>
  <li>Tesoura perde para pedra;</li>
  <li>Papel empata com papel;</li>
  <li>Papel perde para tesoura;</li>
  <li>Papel ganha de pedra.</li>
</ul>
<p>Divirta-se!</p>
