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
        if len(freqlist) < 2: # make sure merging is only done when there are
                              # at least 2 elements in freqlist
            return freqlist[0]
        
        t = Tree(freqlist[0].frequency + freqlist[1].frequency)
            # add frequencies of 1st and 2nd element, the char is None
        t.left = freqlist[0]
        t.right = freqlist[1]
        freqlist.remove(freqlist[0]) # remove merged elements from freqlist
        freqlist.remove(freqlist[0])
        
        # insert new tree into freqlist
        if len(freqlist) == 0: # true, if we just merged the last 2 elements
                               # we had to merge
            return t
        else:
            for el in freqlist:
                if el.frequency > t.frequency:
                    freqlist.insert(freqlist.index(el), t)
                    break
            if not t in freqlist:
                freqlist.append(t)

        # we have finished merging the first two elements of freqlist and
        # inserting it again, so now we go into recursion
        return self.__getCodeTree(freqlist)
    
    def __getDictionary (self, codeTree, binCode = ""):
        """
        pre: code Tree given
        post: return encode dictionary for bit sequences
        """
        if(codeTree.left == None or codeTree.right == None):
            return {codeTree.char:binCode}
        codeDict = (self.__getDictionary(codeTree.left, binCode+"0"))
        codeDict.update(self.__getDictionary(codeTree.right, binCode+"1"))
        return codeDict
        
    def _bitsToString(self, bits):
        """
        pre: sring of bits given
        post: returns the string of these Bits
        """
        string = ""
        lastBits = 0
        for i in range(len(bits)//8):
            string += chr(int(bits[i*8:(i+1)*8], 2))
            lastBits = (i+1)*8
        if(bits[lastBits:] != ''):
            string += chr(int(bits[lastBits:]+ ("0"*((8-len(bits))%8)), 2))
        return string

    def __getBitSeq (self, string, dictionary):
        """
        pre: user's string and encode dictionary given
        post: returns bit sequence to write into file
        """
        encodedDictionary = ""
        for char in dictionary:
            encodedDictionary += char
            print(bin(ord(char)))
            print(dictionary[char])
            print("Anzahl Bytes:",'{0:05b}'.format((len(dictionary[char])+7)//8), '{0:03b}'.format((8-len(dictionary[char]))%8))
            
            encodedDictionary += self._bitsToString('{0:05b}'.format((len(dictionary[char])+7)//8) \
                                                  + '{0:03b}'.format((8-len(dictionary[char]))%8))
            encodedDictionary += self._bitsToString(dictionary[char] + "0"*((8-len(dictionary[char]))%8))
        
        encodedText = ""
        for char in string:
            encodedText += dictionary[char]
            print(encodedText)
            
        encodedDictionary += self._bitsToString("0"*(8+5) + '{0:03b}'.format(len(encodedText)%8))
        encodedText = self._bitsToString(encodedText)
        return encodedDictionary + encodedText

    def __writeFile (self, bitSeq, codeTree, filename):
        """
        pre:  bit sequence bitSeq given
              filename is same as in self.write
              codeTree is same as in self.__getBitSeq
        post: write file called filename using bit sequence
        """
        pass
