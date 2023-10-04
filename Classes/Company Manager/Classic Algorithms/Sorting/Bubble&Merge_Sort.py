class Sort:
    def __init__(self,list):
        self.list = list

    def merge(self):
        for index in range(0, len(self.list - 1), 2):   
            if self.list[index] < self.list[index + 1]:
                pass
                #Need to add temporary lists

    def bubble(self):
        len_list = len(self.list)
        count_sort = 0
        while True:
            for i in range(len_list - 1):
                if self.list[i] < self.list[i + 1]:
                    count_sort = count_sort + 1
                elif self.list[i + 1] < self.list[i]:
                    self.list[i], self.list[i+1] = self.list[i+1],self.list[i]
                else:
                    count_sort = count_sort + 1
            if count_sort == len_list - 1:
                return self.list
            count_sort = 0
    
    def print(self):
        print(self.list)

list = Sort([9,5,6,7,4,1,3,2])

Sort.print(list)
Sort.merge(list)
Sort.print(list)