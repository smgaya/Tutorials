import matplotlib.pyplot as plt

blog_1 = "I am so awesome"
blog_2 = "Cars are cool"
blog_3 = "Awww look at my hamster"

site_title = "My Blog"


def blog_posts_args(title, *args):
    print(title)
    for post in args:
        print(post)

blog_posts_args(site_title,
                blog_1,
                blog_2,
                blog_3)


def blog_posts_kwargs(title, **kwargs):
    print(title)
    for p_title, post in kwargs.items():
        print(p_title, post)

blog_posts_kwargs(site_title,
                  blog_1='I am so awesome',
                  blog_2='Cars are cool',
                  blog_3='Aww look at my hamster')


def graph_function(x, y):
    print("Function that graphs {} and {}".format(str(x), str(y)))
    plt.plot(x, y)
    plt.show()

x1 = [1, 2, 3, 4]
y1 = [2, 3, 1, 2]

graph_me = [x1, y1]
graph_function(*graph_me)
