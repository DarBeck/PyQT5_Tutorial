import time

class AttManger:

    emps = ("John Doe", "Michael Black")

    @staticmethod
    def check_name(name):
        return name in AttManger.emps

    def logger(clock_time):
        def inner(name):
            if AttManger.check_name(name):
                record = clock_time(name)
                with open("log_file.txt", "a") as file:
                    file.write(record + "\n")
        return inner

    @logger
    def clock_in(user):
        clock_time = time.strftime("%I:%M:%S%p")
        return "User: %s || Clock In: %s" % (user, clock_time)

    @logger
    def clock_out(user):
        clock_time = time.strftime("%I:%M:%S%p")
        return "User: %s || Clock Out: %s" % (user, clock_time)

AttManger.clock_in("Lora Gills")