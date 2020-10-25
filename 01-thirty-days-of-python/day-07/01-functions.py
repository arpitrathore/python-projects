
def my_print(txt):
    print(txt)

my_print("Hello World\n")

msg_template = """Hello {name},
Thank you for joining {website}. We are very
happy to have you with us.
"""

def format_msg(my_name="Arpit", my_website="arpitrathore.com"):
    my_msg = msg_template.format(name=my_name, website=my_website)
    return my_msg

print(format_msg())

"""
"{} {}".format("abc", 123)
"{1} {0}".format("abc", 123)
"{name} {number}".format(name="abc", number=123)
"{} {name} {number}".format("another", name="abc", number=123)
"""


def base_function(*args, **kwargs):
    print(args, kwargs)