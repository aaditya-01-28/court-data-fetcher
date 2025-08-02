from flask import render_template, request, Blueprint
from .scraper import fetch_case_data
from .database import SessionLocal, log_query

main = Blueprint('main', __name__)

@main.route('/', methods=['GET'])
def index():
    """Renders the main input form."""
    return render_template('index.html')

@main.route('/search', methods=['POST'])
def search():
    """Handles form submission, calls the scraper, and displays results."""
    case_type = request.form.get('case_type')
    case_number = request.form.get('case_number')
    case_year = request.form.get('case_year')

    if not all([case_type, case_number, case_year]):
        return render_template('error.html', message="All fields are required.")

    # Fetch data
    result, raw_html = fetch_case_data(case_type, case_number, case_year)

    # Log the query to the database 
    db = SessionLocal()
    log_query(db, case_type, case_number, case_year, raw_html)

    # Handle results
    if 'error' in result:
        # Display user-friendly error message [cite: 7]
        return render_template('error.html', message=result['error'])
    
    # Render parsed details nicely [cite: 6]
    return render_template('results.html', data=result)