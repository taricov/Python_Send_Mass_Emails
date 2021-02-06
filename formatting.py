def my_print(txt):
    print(txt)

msg_template = """Hello {name},
Thank you for joining {website} we are very happy to have you with us. 
"""#.format(name='Hugo', website='xXx.com')

# print(msg_template)

def format_msg(my_name='Tek', my_website='GNR.net'):
    my_msg = msg_template.format(name=my_name, website=my_website)
    # print(my_msg)
    return my_msg
