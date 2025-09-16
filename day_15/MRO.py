#method resolution order - MRO
class Top:

    def m_top(self):
        print("Top class (YAY)")

class Middle(Top):

    def m_middle(self):
        print("Middle class (Alright)")

class Bottom(Top, Middle):

    def m_bottom(self):
        print("Bottom class (Boooooooo)")


bottom = Bottom()

bottom.m_top()
bottom.m_middle()
bottom.m_bottom()