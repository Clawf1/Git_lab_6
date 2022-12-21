def simple_calculator(string):
    try:
        return eval(string, {}, {})
    except:
        return 'ERR'


def main():
    equation = input()
    while equation:
        print(simple_calculator(equation))
        equation = input()


if __name__ == '__main__':
    main()
