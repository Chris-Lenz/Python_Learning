def guest_list(guests):
        for guest in guests:
                (name, age, job) = guest
                print("{} is {} years old and works as a {}".format(name, age, job))

guest_list([('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")])
