# Padrões de Design em Python

Este repositório contém exemplos de implementação de vários padrões de design em Python.

## Índice

1. Padrão Singleton
2. Padrão Factory
3. Padrão Observer
4. Padrão Decorator
5. Padrão Strategy
6. Padrão State
7. Padrão Template Method
8. Padrão Composite
9. Padrão Proxy
10. Padrão Flyweight

## Padrão Singleton

O padrão Singleton garante que uma classe tenha apenas uma instância e fornece um ponto de acesso global a ela. É útil quando exatamente um objeto é necessário para coordenar ações no sistema.

## Padrão Factory

O padrão Factory fornece uma maneira de encapsular as instâncias de tipos concretos em classes. O Factory pode ser útil quando um cliente não pode antecipar o tipo de objeto que precisa criar.

## Padrão Observer

O padrão Observer define uma dependência um-para-muitos entre objetos, de modo que quando um objeto muda de estado, todos os seus dependentes são notificados e atualizados automaticamente. É útil quando a mudança de estado de um objeto requer a mudança de outros objetos, e a quantidade de objetos é desconhecida.

## Padrão Decorator

O padrão Decorator anexa responsabilidades adicionais a um objeto dinamicamente. Os decoradores fornecem uma alternativa flexível à subclasse para estender a funcionalidade.

## Padrão Strategy

O padrão Strategy define uma família de algoritmos, encapsula cada um deles e os torna intercambiáveis. A estratégia permite que o algoritmo varie independentemente dos clientes que o utilizam.

## Padrão State

O padrão State permite que um objeto altere seu comportamento quando seu estado interno muda. O objeto parecerá ter mudado de classe.

## Padrão Template Method

O padrão Template Method define o esqueleto de um algoritmo em uma operação, adiando alguns passos para as subclasses. O Template Method permite que subclasses redefinam certos passos de um algoritmo sem alterar a estrutura do algoritmo.

## Padrão Composite

O padrão Composite compõe objetos em estruturas de árvore para representar hierarquias parte-todo. O Composite permite que os clientes tratem objetos individuais e composições de objetos de maneira uniforme.

## Padrão Proxy

O padrão Proxy fornece um substituto ou espaço reservado para outro objeto para controlar o acesso a ele. O uso do proxy pode ser simplesmente para encaminhamento para o objeto real, ou pode fornecer lógica adicional. Quando o objeto real é carregado na memória, o proxy pode lidar com sua criação e manutenção.

## Padrão Flyweight

O padrão Flyweight usa compartilhamento para suportar eficientemente grandes quantidades de objetos de granulação fina. Um objeto flyweight é um objeto compartilhado que pode ser usado em vários contextos simultaneamente. O objeto flyweight atua como um objeto independente em cada contexto - é indistinguível de uma instância do objeto.

