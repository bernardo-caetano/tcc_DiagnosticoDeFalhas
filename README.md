Projeto de Graduação apresentado ao Curso de Engenharia Elétrica da Escola Politécnica, Universidade Federal do Rio de Janeiro, como parte dos requisitos necessários à obtenção do título de Engenheiro.
Aluno: Bernardo Caetano Fernandes de Araujo

O código consiste em uma análise de diagnosticabilidade utilizando o software DESLab desenvolvido pelo Laboratório de Controle e Automação da UFRJ. Esse software utiliza a linguagem de programação Python e portanto, toda a análise deve ser feita utilizando essa mesma linguagem. Além disso, o DESLab é baseado em autômatos para modelar sistemas a eventos discretos.

O tutorial do DESLab pode ser encontrado no endereço: http://www.repositorio.poli.ufrj.br/monografias/monopoli10011673.pdf
Tutorial para desenvolvedores com funções extras: http://www.repositorio.poli.ufrj.br/monografias/monopoli10025764.pdf

Nesse trabalho, são realizadas três abordagens distintas: (i) na primeira, todas as falhas são modeladas em um mesmo autômato e consideradas como um único evento; (ii) na segunda, assim como em Sampath et al. 1995, todas as falhas estão modeladas em um mesmo autômato, mas construindo um diagnosticador para cada falha, considerando as outras como eventos não observáveis comuns; (iii) cada autômato modela apenas uma única falha e é construído um diagnosticador para cada falha. Por fim, a função is_diagnosable nos retorna "true" para falhas que são diagnosticáveis e "false" para falhas não diagnosticáveis.