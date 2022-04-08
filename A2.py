class Club():
    
    def __init__(self):
        self.members = [] #list of all members of the club
        self.data = {} #dictionary of info for each member
        self.discounts = [] #list of members with a discount
        self.payments = {} #number of practices paid and unpaid by members
        self.three_months = [] #list of members who have not skipped payments for 3 months
        self.revenue = 0
        self.cost = 0
        self.profit = 0

    def add_member(self, name: str, number: str, paid: bool, address: str):
        """Create a dictionary with member names as keys to a list 
        containing their phone number, whether they paid for the current
        practice or not, their address, and attendance.
        """
        self.data[name] = [number, paid, address, 0]
        self.members.append(name)
        self.payments[name] = [0, 0]

    def add_revenue(self, rev):
        """Increments club finances as income"""
        self.revenue += rev

    def add_expense(self, exp):
        """Decrements club finances as expenses"""
        self.cost += exp
    
    def log_profit(self):
        """Tracks club's profit"""
        self.profit = self.revenue - self.cost
    
    def add_attendance(self, member: str):
        """Incerement member's attendance by 1."""
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
    
    def add_discount_v1(self, member: str):
        """Add top 10 members based on attendance to 10% discount list."""
        self.sort_by_attendance()
        for i in range(10):
            self.discounts.append(self.members[i])

    def add_payment(self, member: str, paid: bool):
        """Increment the members amount of paid or unpaid practices depending on
        whether paid is true or false."""
        if paid is True:
            self.payments[member][0] += 1
        else:
            self.payments[member][1] += 1

    def sort_by_payments(self, paid: bool):
        """Sort the list of members by number of paid or unpaid payments 
        depending on whether paid is true or false."""
        if paid is True:
            for i in range(len(self.members) - 1):
                minimum = i
                for j in range( i + 1, len(self.members)):
                    lst = self.members
                    if(self.payments[lst[j]][0] < self.payments[lst[minimum]][0]):
                        minimum = j
                if(minimum != i):
                    self.members[i], self.members[minimum] = self.members[minimum], self.members[i]
            self.members.reverse()
        else:
            for i in range(len(self.members) - 1):
                minimum = i
                for j in range( i + 1, len(self.members)):
                    lst = self.members
                    if(self.payments[lst[j]][1] < self.payments[lst[minimum]][1]):
                        minimum = j
                if(minimum != i):
                    self.members[i], self.members[minimum] = self.members[minimum], self.members[i]
            self.members.reverse()
            
    def warning(self):
        """Return a list of members who missed at least one payment."""
        lst = []
        for member in self.payments:
            if self.payments[member][1] > 0:
                lst.append(member)
        return lst
    
    def append_three_months(self, member: str):
        """Add member to list of those who have not skipped payment 
        for three months."""
        self.three_months.append(member)
    
    def add_discount_v2(self):
        """Add members who have not skipped payments for 3 months"""
        for member in self.members:
            if member in self.three_months:
                self.discounts.append(member)

    