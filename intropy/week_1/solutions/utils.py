class Person:
    """ Example Person class. 
    
    Parameters
    ----------
    name : str
        Name of the person
    age : int/float
        Age of the person
    """
    def __init__(self, name, age):
        """ Initializes a Person object. """
        self.name = name
        self.age = age
        
    def introduce(self):
        """ Introduces the Person object. """
        print(f"Hi, I am {self.name}!")
        
    def is_older_than_30(self):
        """ Checks whether the person is older than 30. """
        older = self.age >= 30
        return older

    def increase_age(self, nr):
        """ Increases the age of the Person object by 'nr'.
        
        Parameters
        ----------
        nr : int
            Number to increase age with.
        """
        self.age = self.age + nr
