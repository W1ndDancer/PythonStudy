
import Complex
import Rational
import view

def getResult():
    answer = ''
    choice = view.getChoice()
    view.init(choice)
    while choice in range(1,4):
        if choice == 1:
            x = Complex.getX()
            y = Complex.getY()
            operation = Complex.getOperation()
            Complex.initComplex(x,y,operation)
            if y == 0 and operation == '/':
                result = 'Division by zero!'
            else:
                result = (Complex.Calculator(x, y, operation))
            view.showResultC1(x,y,operation,result)
            answer = input('One more operation?(print y for yes or n for no) --> ')
            while answer not in ['y','n']:
                answer = input('One more operation?(print y for yes or n for no) --> ')
            if answer == 'y':
                choice = view.getChoice
                getResult()
            else:
                view.showResultC4()
                break
        elif choice == 2:
            x = Rational.getX()
            Rational.initRational(x)
            conv = Rational.Convert(x)
            opCount = Rational.FindOperAmount(x)
            Rational.CalcPRO(conv, opCount)
            view.showResultC2(x, conv)
            answer = input('One more operation?(print y for yes or n for no) --> ')
            while answer not in ['y','n']:
                answer = input('One more operation?(print y for yes or n for no) --> ')
            if answer == 'y':
                choice = view.getChoice
                getResult()
            else:
                view.showResultC4()
                break
        elif choice == 3:
            view.showResultC3()
            answer = input('One more operation?(print y for yes or n for no) --> ')
            while answer not in ['y','n']:
                answer = input('One more operation?(print y for yes or n for no) --> ')
            if answer == 'y':
                choice = view.getChoice
                getResult()
            else:
                view.showResultC4()
                break
    else:
        if choice == 4:
            view.showResultC4()