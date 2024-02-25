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
11. Padrão Command
12. Padrão Adapter
13. Padrão Facade
14. Padrão Bridge
15. Padrão Composite
16. Padrão Prototype
17. Padrão Builder
18. Padrão Mediator
19. Padrão Chain of Responsibility
20. Padrão Visitor
21. Padrão Interpreter
22. Padrão Iterator
23. Padrão Memento

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

## Padrão Command

O padrão Command encapsula uma solicitação como um objeto, permitindo que você parametrize clientes com filas, solicitações e operações. Ele também permite suportar operações que podem ser desfeitas.

## Padrão Adapter

O padrão Adapter converte a interface de uma classe em outra interface que os clientes esperam. O Adapter permite que classes trabalhem juntas, o que de outra forma não poderia devido a interfaces incompatíveis.

## Padrão Facade

O padrão Facade fornece uma interface unificada para um conjunto de interfaces em um subsistema. A fachada define uma interface de nível superior que facilita o uso do subsistema.

## Padrão Bridge

O padrão Bridge desacopla uma abstração de sua implementação, para que as duas possam variar independentemente.

## Padrão Composite

O padrão Composite compõe objetos em estruturas de árvore para representar hierarquias parte-todo. O Composite permite que os clientes tratem objetos individuais e composições de objetos de maneira uniforme.

## Padrão Prototype

O padrão Prototype é usado quando a criação de um novo objeto é cara e consome recursos. Ele fornece uma maneira de copiar um objeto original, o protótipo, e reutilizá-lo para criar novos objetos.

## Padrão Builder

O padrão Builder é usado para construir um objeto complexo passo a passo. Ele separa a construção de um objeto complexo de sua representação, de modo que o mesmo processo de construção possa criar diferentes representações.

## Padrão Mediator

O padrão Mediator define um objeto que encapsula como um conjunto de objetos interage. Ele promove o acoplamento fraco ao evitar que os objetos se refiram uns aos outros explicitamente, permitindo que você varie suas interações independentemente.

## Padrão Chain of Responsibility

O padrão Chain of Responsibility evita o acoplamento do remetente de uma solicitação ao seu receptor, dando a mais de um objeto a oportunidade de tratar a solicitação. Encadeia os objetos de recepção e passa a solicitação ao longo da cadeia até que um objeto a trate.

## Padrão Visitor

O padrão Visitor representa uma operação a ser executada nos elementos de uma estrutura de objeto. O Visitor permite que você defina uma nova operação sem alterar as classes dos elementos nos quais opera.

## Padrão Interpreter

O padrão Interpreter fornece uma maneira de avaliar a gramática ou expressão de linguagem. Este tipo de padrão vem sob o padrão comportamental.

## Padrão Iterator

O padrão Iterator é muito comumente usado em um conjunto de dados. Este padrão é usado para obter uma maneira de acessar os elementos de uma coleção de objetos de maneira sequencial sem precisar expor sua representação subjacente.

## Padrão Memento

O padrão Memento é usado quando queremos salvar o estado de um objeto para que possamos restaurá-lo mais tarde. O Memento é um objeto de valor que representa um instantâneo de um objeto.