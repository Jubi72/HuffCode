from tree import * # Funktionsnamen ueberschneiden sich nicht, da selbst definiert

class HuffCode:
    
    def __init__ (self):
        """
        pre: None
        post: HuffCode initialized
        """
        self.__text     = None # Text, der eingelesen wird bei self.write
        self.__freqlist = None # Liste mit Haeufigkeiten
        self.__codeTree = None # Hauptbaum mit Haeufigkeiten pro Zeichen
        self.__bitSeq   = None # Zeichenfolge mit codierten Bits; Code für Datei
        

    def write (self, text, filename = "code.hfc"):
        """
        pre: text given
        post: write huffcode-compressed text into file called filename
              if no filename given file is called code.hfc
        """
        pass

    def __getFrequencies (self, string):
        """
        pre: string given
        post: returns list of type Tree with frequency for each character in string
        """
        pass

    def __getCodeTree (self, freqlist):
        """
        pre: frequencies as list of type Tree given
        post: returns Tree of frequencies
        """
        pass
    
    def __getDictionary (self, codeTree):
        """
        pre: code Tree given
        post: return encode dictionary for bit sequences
        """
        pass

    def __getBitSeq (self, string, dictionary):
        """
        pre: user's string and encode dictionary given
        post: returns bit sequence to write into file
        """
        pass

    def __writeFile (self, bitSeq, codeTree, filename):
        """
        pre:  bit sequence bitSeq given
              filename is same as in self.write
              codeTree is same as in self.__getBitSeq
        post: write file called filename using bit sequence
        """
        pass
