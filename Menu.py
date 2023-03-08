def Space():
    for i in range(1,100):
        print()

def Prompt(Actions, *args):
    while True:
        DisplayActions = {}

        ActionCount = 1

        for Name, Function in Actions.items():
            print("[", ActionCount, "]", Name)
            DisplayActions[ActionCount] = Name
            ActionCount += 1


        Input = input()
        if not Input:
            break
        SelectedAction = int(Input)

        print(SelectedAction)

        ActionFunction = Actions[DisplayActions[SelectedAction]]

        if ActionFunction == "Stop":
            break
        else:
            Actions[DisplayActions[SelectedAction]](DisplayActions[SelectedAction], *args)