# MIU-System
# A simple program that allows a user to build theorems in the MIU-System, as proposed in GEB, pp33-5.

def MIU(theorem):
    while True:
        print("\nTheorem is currently", theorem)
        choice = input("\nPlease enter rule number, 'r' to see the rules again, or ENTER to quit: ")
        if not choice:
            print('\nGoodbye!\n')
            break
        elif choice == 'r' or choice == 'R':
            rules()
        elif choice == '1': 
            if theorem[-1] == 'I':
                theorem += 'U'
            else:
                print("\nCan't apply rule 1 with theorem", theorem)
        elif choice == '2':
            theorem += theorem[1:]
        elif choice == '3':
            if 'III' in theorem:
                l = [i for i in range(len(theorem)) if i < (len(theorem) - 2) and 'III' in theorem[i:i+3]]
                print("\nYou can replace III --> U at these points:", l)
                x = int(input("Please enter a point: "))
                theorem = theorem[:x] + 'U' + theorem[x+3:]
            else:
                print("\nCan't apply rule 3 with theorem", theorem)
        elif choice == '4':
            if 'UU' in theorem:
                l = [i for i in range(len(theorem)) if i < (len(theorem) - 1) and 'UU' in theorem[i:i+2]]
                print("\nYou can reduce UU --> U at these points:", l)
                x = int(input("Please enter a point: "))
                theorem = theorem[:x] + 'U' + theorem[x+2:]
            else:
                print("\nCan't apply rule 4 with theorem", theorem)
        else:
            print("\nI'm sorry, I didn't understand. Please try again.")
    
def rules():
    print('\nThere are four operations possible within the MIU-System:')
    print("\t1) If the string has the last letter 'I' then 'U'' can be added")
    print("\t2) All characters following M can be doubled (eg, 'Mx' --> 'Mxx'")
    print("\t3) Any one sequence of 'III' can be replaced by 'U' (eg, 'MIII' --> 'MUI' or 'MIU'")
    print("\t4) Any one sequence of 'UU' can be reduced to 'U' (eg, 'MUUIUU' --> 'MUIUU' or 'MUUIU'")

def main():
    axiom = 'MI'

    print('\nWelcome to the MIU System')
    print("\nWe begin with an theorem of '" + axiom + "'.")
    rules()
    MIU(axiom)