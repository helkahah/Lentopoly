def Execute(Actions):
    while True:
        DisplayActions = {}

        ActionCount = 1

        for Name, Function in Actions.items():
            print("[", ActionCount, "]", Name)
            DisplayActions[ActionCount] = Name
            ActionCount += 1

        SelectedAction = int(input())

        ActionFunction = Actions[DisplayActions[SelectedAction]]

        if ActionFunction == "Stop":
            break
        else:
            Actions[DisplayActions[SelectedAction]]()