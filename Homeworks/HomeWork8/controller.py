
import view
import creator
import log


def GetResult():
    answer = ''
    choice = view.getChoice()
    view.init(choice)
    view.init(choice)
    while choice in range(1,3):
        if choice == 1:
            n = creator.CreateNewNames()
            s = creator.CreateNewSurnames()
            b = creator.CreateNewBirthdays()
            t = creator.CreateNewTelephones()
            a = creator.CreateNewAdresses()
            log.SaveFile(n,s,b,t,a)
            view.newDB()
            view.PrintInfo(n,s,b,t,a)
            choice = view.getChoice()
        elif choice == 2:
            n = log.LoadFileN()
            s = log.LoadFileS()
            b = log.LoadFileB()
            t = log.LoadFileT()
            a = log.LoadFileA()
            view.PrintInfo(n,s,b,t,a)
            choice = view.getChoice()
        elif choice == 3:
            view.Quit()
            break

