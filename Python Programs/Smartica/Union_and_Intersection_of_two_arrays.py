# Union and intersection of two arrays without using inbuilt functions

class UnionIntersection:
    def union(self, arr1, arr2):
        # Convert the arrays into set
        set1 = set(arr1)
        set2 = set(arr2)
        
        # Find the union of two sets without using inbuilt function
        union = list(set1)
        for i in set2:
            if i not in union:
                union.append(i)
        return union
    
    def intersection(self, arr1, arr2):
        # Convert the arrays into set
        set1 = set(arr1)
        set2 = set(arr2)
        
        # Find the intersection of two sets without using inbuilt function
        intersection = []
        for i in set1:
            if i in set2:
                intersection.append(i)
        return intersection
    
# Create object of the class
ui = UnionIntersection()

arr1 = [1, 2, 3, 4, 5]
arr2 = [1, 2, 3, 5]

# Call the method to find union of two arrays
print("Union of two arrays is", ui.union(arr1, arr2))