from dcard import Api

def main():
    api = Api()
    # get the popular forums from dcard
    popular_forums = api.get_popular_forums()

if __name__ == "__main__":
    main()

