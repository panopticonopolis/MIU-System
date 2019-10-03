# MIU-System
# A simple program that allows a user to build theorems in the MIU-System, as proposed in GEB, pp33-5.

def MIU(axiom):
    while True:
        print("\nAxiom is currently", axiom)
        choice = input("\nPlease enter rule number, 'r' to see the rules again, or ENTER to quit: ")
        if not choice:
            print('\nGoodbye!\n')
            break
        elif choice == 'r' or choice == 'R':
            rules()
        elif choice == '1': 
            if axiom[-1] == 'I':
                axiom += 'U'
            else:
                print("\nCan't apply rule 1 with axiom", axiom)
        elif choice == '2':
            axiom += axiom[1:]
        elif choice == '3':
            if 'III' in axiom:
                # print([axiom[i] for i in axiom if 'III' in axiom])
                l = []
                for i in range(len(axiom)):
                    if i < (len(axiom) - 2) and 'III' in axiom[i:i+3]:
                        l.append(i)
                print("\nYou can replace III --> U at these points:", l)
                x = int(input("Please enter a point: "))
                axiom = axiom[:x] + 'U' + axiom[x+3:]
            else:
                print("\nCan't apply rule 3 with axiom", axiom)
        elif choice == '4':
            if 'UU' in axiom:
                l = []
                for i in range(len(axiom)):
                    if i < (len(axiom) - 1) and 'UU' in axiom[i:i+2]:
                        l.append(i)
                print("\nYou can reduce UU --> U at these points:", l)
                x = int(input("Please enter a point: "))
                axiom = axiom[:x] + 'U' + axiom[x+2:]
            else:
                print("\nCan't apply rule 4 with axiom", axiom)
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
    print("\nWe begin with an axiom of '" + axiom + "'.")
    rules()
    MIU(axiom)

main()
