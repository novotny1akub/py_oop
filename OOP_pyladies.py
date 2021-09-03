# základní vlastnost objektů je to, že obsahují jak data (informace), tak chování – instrukce nebo metody, které s těmito daty pracují
# data každého objektu jsou specifická pro konkrétní objekt
# metody – bývají společné pro všechny objekty daného typu
# společné chování určuje typ (angl. type) neboli třída (angl. class) daného objektu
# třída je popis, jak se všechny objekty daného typu chovají
# „vlastní“ třídy mají funkčnost, kterou třídy jako str nedovolují: máš možnost si definovat vlastní atributy
# atributy se označují tak, že mezi hodnotu a jméno jejího atributu napíšeš tečku
# data se schovávají právě v atributech jednotlivých objektů
# každá metoda má přístup ke konkrétnímu objektu, na kterém pracuje přes argument self
# nově definovaná třída může dědit u jiné, již vytvořené
# odvozeným třídám se říká taky podtřídy (angl. subclasses) 
# opakem je nadtřída (angl. superclass)
# pokud nevyhovuje chování některé metody v nadtřídě, stačí dát metodu stejného jména do podtřídy
# podstatou polymorfismu je tedy metoda nebo metody, které mají všichni potomci definované se stejnou hlavičkou, ale jiným tělem (zvířata a jak mluví)

# třídy, metody, attributy
class Kotatko:
    def zamnoukej(self):
        print("Mňau!")
        
# zavoláním třídy Kotatko vytvářím objekt kotatko
kotatko = Kotatko() # kotatko = instance, Kotatko = class

kotatko.zamnoukej()

mourek = Kotatko()
mourek.jmeno = 'Mourek' # objektu morek přiřazuji atribut jmeno

micka = Kotatko()
micka.jmeno = 'Micka'

print(mourek.jmeno)

# parametr self
class Kotatko:
    # __init__ (constructor) se provede hned na začátku
    def __init__(self, jmeno): # __neco__ značí speciální metody (reserved method)
        self.jmeno = jmeno
    
    # __str__ je příklad speciální metody
    def __str__(self):
        return f'<Kotatko jmenem {self.jmeno}>'

    def zamnoukej(self):
        print(f"{self.jmeno}: Mňau!")

    def snez(self, jidlo):
        print(f"{self.jmeno}: Mňau mňau! {jidlo} mi chutná!")

mourek = Kotatko('Mourek')
print(mourek)


# dědičnost
class Zviratko:
    def __init__(self, jmeno):
        self.jmeno = jmeno

    def snez(self, jidlo):
        print(f"{self.jmeno}: {jidlo} mi chutná!")

# třída Kotatko dědí ze třídy Zviratko (angl. inherits from Zviratko)
# „je odvozená” ze třídy Zviratko/“rozšiřuje” (angl. extends)
# odvozeným třídám se říká taky podtřídy (angl. subclasses) 
# Zviratko je tu nadtřída (angl. superclass).
class Kotatko(Zviratko):
    def snez(self, jidlo):
        print(f"({self.jmeno} na {jidlo} chvíli fascinovaně kouká)")
        super().snez(jidlo)
        
class Stenatko(Zviratko):
    def zastekej(self):
        print(f"{self.jmeno}: Haf!")

# polymorfismus

