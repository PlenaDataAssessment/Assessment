import collections as c


class Prompt:
    def __init__(self):
        self.string = input("Please enter a string: ")
        self.checkInput()
        self.rephrase()

    def checkInput(self):
        """
        check the validity of the input.
        :return:  None
        """
        while not isinstance(self.string, str):
            self.string = input("The input must be string,please re-enter: ")
        while not self.string.isalpha():
            self.string = input("The input should only contain characters and not empty, please re-enter: ")

    def rephrase(self):
        """
        find and display the first non repeated character, then reorder the input
        (upper and lower case would be considered the same character)
        :return: None
        """
        length = len(self.string)
        if length == 1:
            print(self.string)
            return

        lowerString = self.string.lower()        # convert the upper case into lower case
        counter = c.Counter(lowerString)         # use Counter() to get occurrence of every character

        order = c.defaultdict(list)            # initiate a dictionary to store the index of every number of occurrence
        search = True                          # boolean to indicate if we need keep searching the first character
        ans = ''                               # initiate the reordered input

        for index, char in enumerate(self.string):
            if search and counter[char.lower()] == 1:
                print(char)
                search = False
            order[counter[char.lower()]].append(index)

        for key in sorted(order):
            for index in order[key]:
                ans += self.string[index]
        print(ans)


if __name__ == '__main__':
    p = Prompt()
