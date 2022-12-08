from dcard import Api
import json

def main():
    api = Api()

    # get the popular forums from dcard
    popular_forums = api.get_popular_forums()
    # write data to the json file
    export_json("popular_forums",
                {"popular_forums": popular_forums})


def export_json(filename : str, file : dict) -> None:
    with open(f'./data/{filename}.json', "w", encoding="utf8") as outfile:
        json.dump(file, outfile, ensure_ascii=False)


if __name__ == "__main__":
    main()
