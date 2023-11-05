from src.sheet_parser.sheet_parser import insert_sheet_into_db, parse_sheet
from src.server.server import create_app


def main() -> None:
    app = create_app()
    app.run(debug=True, host='0.0.0.0', port=4000)
    # insert_sheet_into_db(parse_sheet())       uncomment this when implemented


if __name__ == '__main__':
    main()
