from dcard import Api
import json

def export_json(filename : str, file : dict) -> None:
    with open(f'./data/{filename}.json', "w", encoding="utf8") as outfile:
        json.dump(file, outfile, ensure_ascii=False)

def main():
    api = Api()

    popular_forums = api.get_popular_forums()
    sensity_forums = api.get_sensity_forums()

    api.close()

    # write data to the json file
    export_json("popular_forums",
                {"popular_forums" : popular_forums})

    export_json("sensity_forums",
                {"sensity_forums" : sensity_forums})

    print("Writed...")

if __name__ == "__main__":
    main()
