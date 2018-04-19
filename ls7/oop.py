#camelcase:
#def ThisisFuncion():
#    pass

#snackcase
#def this_is_function():
#    pass


class A:
    attr_1 = 1
    attr_2 = "abc"


    def get_attr_1(self):
        return self.attr_1

    def return_all_values(self):
        result = '{}. {}'.format(self.attr_1, self.attr_2)
        return result


if __name__ == '__main__':
    a = A ()
    print(a.attr_1)
    a.get_attr_1()
    def2 = a.return_all_values()
    print(def2)
    a.attr_1 = 888
    a.get_attr_1()


    #LIFO(Last in First Out) and FIFO



