# Padrões de Design em Python

Este repositório contém exemplos de implementação de vários padrões de design em Python.

## Índice

### Padrões de Criação
1. Padrão Singleton
2. Padrão Factory
3. Padrão Prototype
4. Padrão Builder
5. Padrão Abstract Factory

### Padrões Estruturais
6. Padrão Adapter
7. Padrão Bridge
8. Padrão Composite
9. Padrão Decorator
10. Padrão Facade
11. Padrão Flyweight
12. Padrão Proxy

### Padrões Comportamentais
13. Padrão Chain of Responsibility
14. Padrão Command
15. Padrão Interpreter
16. Padrão Iterator
17. Padrão Mediator
18. Padrão Memento
19. Padrão Observer
20. Padrão State
21. Padrão Strategy
22. Padrão Template Method
23. Padrão Visitor

## Padrões de Criação

### Padrão Singleton

O padrão Singleton garante que uma classe tenha apenas uma instância e fornece um ponto de acesso global a ela. É útil quando exatamente um objeto é necessário para coordenar ações no sistema[^1^][1].

### Padrão Factory

O padrão Factory fornece uma maneira de encapsular as instâncias de tipos concretos em classes. O Factory pode ser útil quando um cliente não pode antecipar o tipo de objeto que precisa criar[^1^][1].

### Padrão Prototype

O padrão Prototype é usado quando a criação de um novo objeto é cara e consome recursos. Ele fornece uma maneira de copiar um objeto original, o protótipo, e reutilizá-lo para criar novos objetos[^1^][1].

### Padrão Builder

O padrão Builder é usado para construir um objeto complexo passo a passo. Ele separa a construção de um objeto complexo de sua representação, de modo que o mesmo processo de construção possa criar diferentes representações[^1^][1].

### Padrão Abstract Factory

O padrão Abstract Factory fornece uma interface para criar famílias de objetos relacionados ou dependentes sem especificar suas classes concretas. É útil quando um sistema deve ser independente de como seus produtos são criados, compostos e representados[^1^][1].


### Padrões Estruturais

### Padrão Adapter

O padrão Adapter converte a interface de uma classe em outra interface que os clientes esperam. O Adapter permite que classes trabalhem juntas, o que de outra forma não poderia devido a interfaces incompatíveis[^1^][1].

### Padrão Bridge

O padrão Bridge desacopla uma abstração de sua implementação, para que as duas possam variar independentemente[^1^][1].

### Padrão Composite

O padrão Composite compõe objetos em estruturas de árvore para representar hierarquias parte-todo. O Composite permite que os clientes tratem objetos individuais e composições de objetos de maneira uniforme[^1^][1].

### Padrão Decorator

O padrão Decorator anexa responsabilidades adicionais a um objeto dinamicamente. Os decoradores fornecem uma alternativa flexível à subclasse para estender a funcionalidade[^1^][1].

### Padrão Facade

O padrão Facade fornece uma interface unificada para um conjunto de interfaces em um subsistema. A fachada define uma interface de nível superior que facilita o uso do subsistema[^1^][1].

### Padrão Flyweight

O padrão Flyweight usa compartilhamento para suportar eficientemente grandes quantidades de objetos de granulação fina. Um objeto flyweight é um objeto compartilhado que pode ser usado em vários contextos simultaneamente[^1^][1].

### Padrão Proxy

O padrão Proxy fornece um substituto ou espaço reservado para outro objeto para controlar o acesso a ele. O uso do proxy pode ser simplesmente para encaminhamento para o objeto real, ou pode fornecer lógica adicional[^1^][1].
