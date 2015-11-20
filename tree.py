# -*- coding: utf-8 -*-
class Tree:
    
    def __init__ (self, freq, char = None):
        """
        pre:  frequency must be given
        post: Tree is made with frequency freq and character char
              if no char given, char is None (should appear in any root)
        """
        self.frequency = freq # Haeufigkeit
        self.char      = char # Zeichen, für das die Haeufigkeit gilt
        self.left      = None # linker Unterbaum
        self.right     = None # rechter Unterbaum
