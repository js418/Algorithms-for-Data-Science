# 590D Algorithm for Data Science
# Jie Song, Buqin Wang, Swetal Bhatt
# Homework 2
# min-heap calss for Question 2_b

class MinHeap(object):

    def __init__(self, item= None,value=0):
        # store the items ans their counters in two lists
        self.heap_item =[]     
        self.heap_value = []
        self.heap_size = 0

    # if the coming item is in the heap, we need to replace it 
    def replace_item(self,item,value):
        index = self.find_item(item)
        if index == -1:  #not in the heap, no replacement
            return False
        else:
            self.heap_item[index] = item
            self.heap_value[index] = value
            leftchildren_index = index*2 + 1
            rightchildren_index = index*2 + 2
            self.bubble_down(index)
            return True

    # insert item to the heap                   
    def insert(self, item, value):
        self.heap_size += 1
        self.heap_item.append(item)
        self.heap_value.append(value)
        index = self.heap_size -1
        if index >0:
            self.bubble_up(index)

    def bubble_up(self,index):
        if index==0:
            return
        parent_index = (index-1) // 2
        if self.heap_value[parent_index] > self.heap_value[index]:
            temp_value = self.heap_value[parent_index]
            self.heap_value[parent_index] = self.heap_value[index]
            self.heap_value[index] = temp_value

            temp_item = self.heap_item[parent_index]
            self.heap_item[parent_index] = self.heap_item[index]
            self.heap_item[index] = temp_item
            
            self.bubble_up(parent_index)


    def bubble_down(self,index):
        leftchildren_index = index*2 + 1
        rightchildren_index = index*2 + 2
        if leftchildren_index >= self.heap_size:
            return
        else:
            min_index = index
            if self.heap_value[leftchildren_index] < self.heap_value[index]:
                min_index = leftchildren_index
            if (rightchildren_index < self.heap_size) and (self.heap_value[rightchildren_index ] < self.heap_value[min_index]):
                min_index = rightchildren_index
            if min_index != index:
                temp_value = self.heap_value[index]
                self.heap_value[index] = self.heap_value[min_index]
                self.heap_value[min_index] = temp_value
                
                temp_item = self.heap_item[index]
                self.heap_item[index] = self.heap_item[min_index]
                self.heap_item[min_index] = temp_item

                self.bubble_down(min_index)
        

    # check if the item in the heap
    def find_item(self,item):
        if item in self.heap_item:
            return self.heap_item.index(item)
        else:
            return -1

    def get_items(self):
        print self.heap_item

    def get_values(self):
        print self.heap_value

    def get_list(self):
        a_list = []
        for i in range(self.heap_size):
            t = (self.heap_item[i],self.heap_value[i])
            a_list.append(t)
        return a_list
            


    
                
            
        

    
        
            
        
