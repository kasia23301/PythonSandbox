import requests

if __name__ == "__main__":
    r = requests.get('https://parking-finder-spring.herokuapp.com/api/v1/parking/public/nearToLocation')