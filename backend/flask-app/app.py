###
# Main application interface
###

from src import create_app
from src.read_csv import get_data


def main():
     data = get_data()  
    # create the app object
     app = create_app()
     app.run(debug=True, host='0.0.0.0', port=4000)


if __name__ == '__main__':
    # debug mode for hot reloading)
    # this app will be bound to port 4000
    main()
