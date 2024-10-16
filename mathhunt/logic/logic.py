def multiplicity_n(arg: int) -> bool:

    if not isinstance(arg, int):
        raise TypeError("[fastmath] : [logic] : Input error! Arguments must be an integer")
    
    else:
        if arg >= 0:
            return True
        else:
            return False

def multiplicity_z(arg: int) -> bool:

    if not isinstance(arg, int):
        raise TypeError("[fastmath] : [logic] : Input error! Arguments must be an integer")
    
    else:
        return True

def multiplicity_q(arg: float) -> bool:

    if not isinstance(arg, float):
        raise TypeError("[fastmath] : [logic] : Input error! Arguments must be an integer")
    
    else:
        return True

def multiplicity_e(arg: float) -> bool:

    if not isinstance(arg, float):
        raise TypeError("[fastmath] : [logic] : Input error! Arguments must be an integer")
    
    else:
        if (arg % 2) == 0:
            return True
        else:
            return False

def multiplicity_o(arg: float) -> bool:

    if not isinstance(arg, float):
        raise TypeError("[fastmath] : [logic] : Input error! Arguments must be an integer")
    
    else:
        if (arg % 2) != 0:
            return True
        else:
            return False

def conjunction(arg: bool, kwarg: bool) -> bool:

    if not isinstance(arg, bool) or not isinstance(kwarg, bool):
        raise TypeError("[fastmath] : [logic] : Input error! Arguments must be boolean")

    else:
        if arg == True and kwarg == True:
            return True
        if arg == False and kwarg == False:
            return False
        if arg != kwarg:
            return False

def disjunction(arg: bool, kwarg: bool) -> bool:

    if not isinstance(arg, bool) or not isinstance(kwarg, bool):
        raise TypeError("[fastmath] : [logic] : Input error! Arguments must be boolean")

    else:
        if arg == True or kwarg == True:
            return True
        else:
            return False

def negation(arg: bool) -> bool:

    if not isinstance(arg, bool) :
        raise TypeError("[fastmath] : [logic] : Input error! Argument must be boolean")

    else:
        if arg == False:
            return True

def implication(arg: bool, kwarg: bool) -> bool:

    if not isinstance(arg, bool) or not isinstance(kwarg, bool):
        raise TypeError("[fastmath] : [logic] : Input error! Arguments must be boolean")

    else:
        if arg == False or kwarg == True:
            return True
        else:
            return False

def equivalence(arg: bool, kwarg: bool) -> bool:

    if not isinstance(arg, bool) or not isinstance(kwarg, bool):
        raise TypeError("[fastmath] : [logic] : Input error! Arguments must be boolean")

    else:
        if arg == kwarg:
            return True
        else:
            return False