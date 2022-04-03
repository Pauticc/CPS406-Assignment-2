class Club():
    
    def __init__(self):
        self.members = [] #list of all members of the club
        self.data = {} #dictionary of info for each member
        self.discounts = [] #list of members with a discount

    def add_member(self, name: str, number: str, paid: bool, address: str):
        """Create a dictionary with member names as keys to a list 
        containing their phone number, whether they paid or not, their 
        address, and attendance.
        """
        self.data[name] = [number, paid, address, 0]
        self.members.append(name)

    def add_attendance(self, member: str):
        "Incerement member's attendance by 1."
        self.data[member][3] += 1

    def sort_by_attendance(self):
        """Sort the list of members by attendance from highest to lowest."""
        for i in range(len(self.members) - 1):
            minimum = i
            for j in range( i + 1, len(self.members)):
                lst = self.members
                if(self.data[lst[j]][3] < self.data[lst[minimum]][3]):
                    minimum = j
            if(minimum != i):
                self.members[i], self.members[minimum] = self.members[minimum], self.members[i]
        self.members.reverse()
    
    def add_discount(self, member: str):
        "Add member to 10% discount list."
        self.discounts.append(member)



    