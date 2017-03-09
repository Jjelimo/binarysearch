class BinarySearch(list):

  def __init__(self, a, b): 
    self.a = length
    self.b = step
         
    for number in range(self.a):

      list.append(self, self.b)
      self.b +=step
      number +=1
  
    self.length = digit

  def search(self,digit):

    number_one = 0
    end_number = self.length-1
    found = False
    count = 0
    in_list = False
    try:
      index = self.index(digit)
      in_list = True
    except ValueError:
      index = -1
      in_list = False

    while first<=last and not found and in_list and digit != self[end_number]:
        mid_number = (first+last)//2
        mid_digit = self[mid_number]
        if mid_digit == digit:
            found = True
            count +=1
            index = mid_number
        else:
            if digit < mid_digit:
                last = mid_number - 1
                count +=1
            else:
                first = mid_number + 1
                count +=1
    
    
    return {"count": count, "index": index}