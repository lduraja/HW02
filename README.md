[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/EJ61cHeV)
# Domácí úkol č. 2
> **Upravujte pouze soubor `assignment_2_1.py` a v něm pouze nahraďte `...` podle zadání!**

Vaším úkolem je určit, zda-li je vybraná část zadaného textového řetězce palindrom či nikoliv 
(viz [Wikipedia](https://cs.wikipedia.org/wiki/Palindrom)). 
Vstupem bude tedy textový řetězec a indexy začátku a konce palindromu, který budete analyzovat.
Požadovaným výstupem je buď hodnota `True` nebo `False`, uložená do proměnné `is_palindrome`.

Jakým způsobem postupovat? Pokud máte nápad, pusťte se do toho vlastními silami. 
V opačném případě můžete použít naši nápovědu:
* Nejprve je potřeba pomocí řezání vybrat tu část z textového řetězce `my_string`, kterou chcete analyzovat. 
  Indexy začátku a konce jsou v proměnných `start` a `end`.
* V dalším kroku je dobré upravit ty znaky v řetězci, které by Vám mohli při hodnocení působit potíže. 
  Typicky jsou to mezery, diakritika, velké a malé znaky či interpunkce. Odstranění mezer jsme už nachystali 
  a diakritiku slibujeme, že u testování nepoužijeme. Korekce velikosti znaků a odstranění interpunkce na konci vět
  je na Vás.
* Dále využijte toho, že se znaky u palindromu "zrcadlí" kolem prostředního prvku. Zjistěte proto obecnou pozici 
  prostředního prvku pro libovolně dlouhý řetězec. **Pozor na to, že index musí být celé číslo**!
* A teď přijde ten nejtěžší krok. Řetězec je potřeba vhodně rozdělit na dvě poloviny (dva podřetězce). Pokud v jedné 
  z těchto polovin změníte pořadí znaků (např. od posledního po první), stačí Vám oba podřetězce porovnat pomocí 
  vhodného logického operátoru a požadovaný výsledek je na světě!
  **Pozn.**: Úlohu lze vyřešit i bez rozdělení na podřetězce. My si ale chceme protrénovat řezání a indexaci řetězců
  a proto půjdeme tou těžší cestou :) 

> **Malý chyták**: Pozor na to, aby Váš program fungoval pro řetězce se sudým i lichým počtem znaků. 
> Protože jsme ještě neprobírali cykly a podmínky, které by nám usnadnily práci, je třeba trochu experimentovat
> s nastavením indexů při řezání řetězce (Zkuste prohodit pořadí některých operací, např. výřez podřetězce a inverzi 
> prvků, nebo využít operátor modulo).
