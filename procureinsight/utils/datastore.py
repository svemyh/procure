# datastore.py

import firebase_admin
from firebase_admin import credentials, firestore

PATH_TO_SERVICE_ACCOUNT = './firebase-service-account.json'

class Datastore:
    def __init__(self, service_account_path=PATH_TO_SERVICE_ACCOUNT):
        # Initialize Firebase app if not already initialized
        if not firebase_admin._apps:
            cred = credentials.Certificate(service_account_path)
            firebase_admin.initialize_app(cred)
        self.db = firestore.client()

    @staticmethod
    def isUnsafePattern(company_name):
        """
        Checks for SQL injection and similar vulnerabilities in the company_name parameter.
        """
        # Implement actual pattern checking logic here
        # For now, it returns False as a placeholder
        return False

    def getAllCompanies(self):
        """Fetches all companies from Firestore."""
        companies = []
        try:
            docs = self.db.collection("companies").stream()
            for doc in docs:
                companies.append(doc.to_dict())
        except Exception as e:
            print(f"Error fetching companies: {e}")
        return companies

    def getCompany(self, company_name):
        """
        Retrieves company data from Firestore. Returns None if company does not exist.
        """
        if self.isUnsafePattern(company_name):
            print("Unsafe pattern detected in company name.")
            return None

        try:
            doc = self.db.collection("companies").document(company_name).get()
            if doc.exists:
                return doc.to_dict()
            else:
                print(f"Company '{company_name}' does not exist.")
                return None
        except Exception as e:
            print(f"Error fetching company data: {e}")
            return None

    def getProduct(self, product_name):
        """
        Retrieves product data from Firestore. Returns None if product does not exist.
        """
        if self.isUnsafePattern(product_name):
            print("Unsafe pattern detected in product name.")
            return None

        try:
            doc = self.db.collection("products").document(product_name).get()
            if doc.exists:
                return doc.to_dict()
            else:
                print(f"Product '{product_name}' does not exist.")
                return None
        except Exception as e:
            print(f"Error fetching product data: {e}")
            return None
