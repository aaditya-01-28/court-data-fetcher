from app import create_app

app = create_app()

if __name__ == '__main__':
    # Note: debug=True is not for production
    app.run(debug=True, port=5001)