def index():
    with open('Work/templates/index.html') as template:
        return template.read()


def blog():
    with open('Work/templates/blog.html') as template:
        return template.read()
