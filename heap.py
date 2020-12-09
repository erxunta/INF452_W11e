class EmptyHeapException(Exception):
    def __init__(self, msg):
        self._msg = msg
    def __str__(self):
        return self._msg
    


# helper functions

   

def left(index):
    '''Return index's left child index.
    '''
    return index * 2 + 1


def right(index):
    '''Return index's left child index.
    '''
    return index * 2 + 2
    
    
def parent(index):
    '''Return index's parent index.'''
    
    return (index - 1) // 2


class MinHeap:
    
    def __init__(self, L=None):
        '''Create a new MinHeap.
        This method is complete.'''
        
        if not L:        
            self._data = []
        else:
            self._data = L
            self._min_heapify()

        
    def __len__(self):
        '''Return the length of the MinHeap.
        This method is complete.'''
        
        return len(self._data)
    

    def __str__(self):
        '''Return a string representation of the heap.
        This method is complete.'''
        
        return str(self._data)
    
    
    def insert(self, v):
        '''Insert v in self. Maintain heap property.'''
        
        self._data.append(v)
        #swap the last node with the adding value v
        #using variable last_node to store the value 
        if len(self._data) != 1:
            self._percolate_up()
            
            
    
    
    def extract_min(self):
        '''Remove minimal value in self. Restore heap property.
        Raise EmptyHeapException if heap is empty.'''
        
       
        if len(self._data) == 0:
            raise EmptyHeapException("This is empty.")
        if len(self._data) == 0:
            self._data.pop(0)
        
        
        self._min_heapify()
        return self._data.pop(0)
        
                
                
        
        
        
        
    
    
    def _percolate_up(self):
        '''Restore heap property of self after 
        adding new item'''
        
        index = len(self._data)-1
      
       
        
        while index != 0:
            if self._data[parent(index)] > self._data[index]:
                #swap the smaller value with its parent
                #using variable node to store the parent value 
                node = self._data[parent(index)]
               
                self._data[parent(index)] = self._data[index]
               
                self._data[index] = node
             
            index = parent(index)
        
          
       
        
        
    
    
    def _percolate_down(self, i):
        ''' Restore heap property of subtree 
        rooted at index i.
        '''
        
        # while larger than at least one child
        # swap with smaller child and repeat
        index = i
        left_c = left(i)
        right_c = right(i)
        
        if left_c < len(self._data) and self._data[index] > self._data[left_c]:
            index = left_c
        
        if right_c < len(self._data) and self._data[index] > self._data[right_c]:
            index = right_c
        
        if index != i:
            node = self._data[i]
            self._data[i] = self._data[index]
            self._data[index] = node
            self._percolate_down(index)
                        
        
            
            
        
    
    
    def _min_heapify(self):
        '''Turn unordered list into min-heap.'''
        
        # for each node in the first half of the list
        # percolate down
        for i in range(len(self._data) // 2, -1, -1):
            self._percolate_down(i)

    