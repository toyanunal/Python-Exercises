###########################################################
# #
# <Name>, <StudentID> #
# #
# IS 545, Assignment 3 #
# #
###########################################################

from ctypes import c_byte


class Node: #toyan: yeni bir class eklemek uygun olmayabilir. crate classı node class gibi kullanabiliyorsun

    def __init__(self, data, nextNode=None):
        self.data = data
        self.nextNode = nextNode

    def getData(self):
        return self.data

    def getNextNode(self):
        return self.nextNode

    def setNextNode(self, val):
        self.nextNode = val


class Crate:
    """LIFO container for plates with varying thicknesses, implemented using a
ctypes array as underlying storage."""

    def __init__(self, capacity):
        if capacity > 99 or capacity < 9:
            raise Exception("Argument out of range!")
        self._occupied_thickness = 0
        self._capacity = capacity
        self._array = (capacity * c_byte)()
        self._count = 0

    def get_capacity(self):
        return self._capacity

    def is_empty(self):
        if self._count == 0:
            return True
        return False

    def get_remaining_space(self):
        return self._capacity - self._count

    def push(self, thickness):
        if self._occupied_thickness + thickness < self._capacity: #toyan: buranın küçük eşit olması gerekiyor
            self._array[self._count] = thickness
            self._count = self._count + 1
            self._occupied_thickness = self._occupied_thickness + thickness
        else:
            raise Exception("there is not enough capacity.")

    def pop(self):
        """removes topmost plate from the crate and returns its thickness"""
        if Crate.is_empty(self):
            raise Exception("pop from empty crate")
        else:
            self._count = self._count - 1
            temp = self._array[self._count]
            self._array[self._count] = 0  # şuraya tekrar bak
            self._occupied_thickness = self._occupied_thickness - temp
            return temp

    def __str__(self):
        # this part should not be modified
        return str.format("[{0}/{1}:", self._occupied_thickness, self._capacity) + ",".join(
            str(self._array[i]) for i in range(self._count)) + "]"


class CrateConveyor:
    """FIFO container for crates, implemented using singly linked list as
    underlying storage."""

    def __init__(self):
        self._head = None
        self._size = 0

    def feed(self, crate):
        """adds crate to the rear, only Crate objects expected"""
        if isinstance(crate, Crate):
            new_node = Node(crate, self._head)
            self._head = new_node
            self._size += 1
            return True
        raise Exception("parameter of type Crate expected")

    def pick_up(self):
        """removes and returns the crate at the front, returns None if empty"""
        temp = 0
        if self._head is None:
            return None
        if self._head.getNextNode() is None:
            temp = self._head
            self._head = None
            return temp.getData()
        second_last = self._head
        while second_last.getNextNode().getNextNode():
            second_last = second_last.getNextNode()
        temp = second_last.getNextNode()
        second_last.setNextNode(None)
        return temp.getData()

    def __iter__(self):
        list_of_crates = list()
        curr = self._head
        while curr:
            list_of_crates.append(curr.data)
            curr = curr.getNextNode()
        list_of_crates.reverse()
        return iter(list_of_crates)

    def __str__(self):
        # this part should not be modified
        L = []
        for crate in self:
            L.insert(0, str(crate))
        return "{" + "->".join(L) + "}"


class TransportSystem:
    def __init__(self, capacities):
        """capacities parameter is a list of integers corresponding to the empty
        crates, first item is at the front, last item is at the rear of the conveyor"""
        self.first_conveyor = CrateConveyor()
        self.second_conveyor = CrateConveyor()
        for item in capacities:
            self.first_conveyor.feed(Crate(int(item)))
    def add(self, thickness):
        """puts a plate to the source point of the transport system with the
        specified thickness.
        Returns True if successful, returns False if there is no crate available
        to put the plate """
        raise Exception("This part will be implemented by the student")

    def remove(self):
        """removes a plate from the destination point of the transport system.
        Returns 0 (zero) if there is no crate/plate at the destination point.
        If successful, returns thickness of the plate that was removed"""

        raise Exception("This part will be implemented by the student")

    def __str__(self):
        """String representation of the transport system in the following order.
        <Source Crate> <Source to Dest Conveyor> <Dest Crate> <Dest to Source
        Conveyor>
        Note that if there is no source or destination create, use []
        representation
        See the following examples:
        [] {} [] {[0/15:]->[0/10:]->[0/20:]->[0/9:]}
        [15/20:4,5,6] {} [3/9:1,2] {[0/15:]->[0/10:]}
        """
        raise Exception("This part will be implemented by the student")
