try:
    v=input('enter a v: ')
    print(int(v)/len(v))
except ValueError:
    print('bad inp')
except ZeroDivisionError:
    print('v d i')
except TypeError:
    print('v v b i')
except:
    print('boo')