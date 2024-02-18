https://runestone.academy/ns/books/published/pythonds3/Introduction/ObjectOrientedProgramminginPythonDefiningClasses.html

#A child classs should always call the cosntructor of the parent class. 

class LogicGate:
    def __init__(self, lbl):
        self.label = lbl
        self.output = None

    def get_label(self):
        return self.label

    def get_output(self):
        self.output = self.perform_gate_logic()
        return self.output
    
class BinaryGate(LogicGate):
    def __init__(self, lbl):
        LogicGate.__init__(self, lbl)
        self.pin_a = None
        self.pin_b = None

    def get_pin_a(self):
        return int(input(f"Enter pin A input for gate \
            {self.get_label()}: "))

    def get_pin_b(self):
        return int(input(f"Enter pin B input for gate \
            {self.get_label()}: "))
    
class UnaryGate(LogicGate):
    def __init__(self, lbl):
        LogicGate.__init__(self, lbl)
        self.pin = None

    def get_pin(self):
        return int(input(f"Enter pin input for gate \
            {self.get_label()}: "))
    
class AndGate(BinaryGate):
    def __init__(self, lbl):
        super().__init__(lbl)

    def perform_gate_logic(self):
        a = self.get_pin_a()
        b = self.get_pin_b()
        if a == 1 and b == 1:
            return 1
        else:
            return 0
        
#ALL super() function does is call the parent class -> parent function  super().parentFunction(). 
 