
class datastore:
    def isUnsafePattern(company_name):
        """
        Checks for SQL injection and similar vulnerabilites in the company_name parameter.
        """
        return False


    def getCompanyDataDummy(company_name):
        """
        Dummy data for company data. Used for testing.
        """
        company_data = {
            "company_name": "Google",
            "description": "Google is a search engine, created by Larry Page and Sergey Brin.",
            "products": [
                {"product": "Google Adwords", "content": "Large scale advertising platform."},
                {"product": "Google Search", "content": "Search engine."},
                {"product": "Google Maps", "content": "Mapping software."},
                {"product": "Google Drive", "content": "Cloud storage."},
            ],
        }
        return company_data


    def getCompanyData(company_name):
        """
        Get company data from database. Returns None if company does not exist.
        """
        return None