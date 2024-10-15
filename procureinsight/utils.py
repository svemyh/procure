import random
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use a service account.
cred = credentials.Certificate('./firebase-service-account.json')
app = firebase_admin.initialize_app(cred)
db = firestore.client()

class datastore:
    def isUnsafePattern(company_name):
        """
        Checks for SQL injection and similar vulnerabilites in the company_name parameter.
        """
        return False
    
    def getCompaniesDummy():
        companies = [
            {"title": "Google", "tag":"Google", "description": "Google is a search engine, created by Larry Page and Sergey Brin."},
            {"title": "Meta", "tag":"Meta", "description": "Social media platform, created by Mark Zuckerberg."},
            {"title": "Palantir", "tag":"Palantir", "description": "Sell data analysis software to governments and corporations."},
            {"title": "Amazon", "tag":"Amazon", "description": "E-commerce and cloud computing company, created by Jeff Bezos."},
            {"title": "Microsoft", "tag":"Microsoft", "description": "Software company, created by Bill Gates and Paul Allen."},
            {"title": "Deutsche Bank", "tag":"Deutsche-Bank", "description": "Banking and financial services company."},
        ]
        return companies
    
    def getAllCompanies():
        """Data fetched from Firestore"""

        # Get all docs in collection:
        companies = []
        docs = db.collection("companies").stream()
        for doc in docs:
            companies.append(doc.to_dict())

        return companies


    def getCompanyDataDummy(company_name):
        """
        Dummy data for company data. Used for testing.
        """
        company_data = {
            "company_name": "Google",
            "description": "Google is a search engine, created by Larry Page and Sergey Brin.",
            "products": [
                {"title": "Google Adwords", "tag":"google-adwords", "description": "Large scale advertising platform."},
                {"title": "Google Search", "tag":"google-search", "description": "Search engine."},
                {"title": "Google Maps", "tag":"google-maps", "description": "Mapping software."},
                {"title": "Google Drive", "tag":"google-drive", "description": "Cloud storage."},
                {"title": "Google Cloud", "tag":"google-cloud", "description": "Cloud computing."},
                {"title": "Google Workspace", "tag":"google-workspace", "description": "Collaboration tools."},
                {"title": "Google Analytics", "tag":"google-analytics", "description": "Web analytics."},
                {"title": "Google Chrome", "tag":"google-chrome", "description": "Web browser."},
                {"title": "Google Pixel", "tag":"google-pixel", "description": "Smartphone."},
                {"title": "Google Nest", "tag":"google-nest", "description": "Smart home devices."},
                {"title": "Google Fi", "tag":"google-fi", "description": "Mobile phone service."},
                {"title": "Google Photos", "tag":"google-photos", "description": "Photo storage."},
            ],
        }
        return company_data


    def getCompanyData(company_name):
        """
        Get company data from database. Returns None if company does not exist.
        """
        return None
    

    def get_product_data_dummy(product_name):
        """
        Dummy data for company data used for testing B2B procurement costs for a product.
        :param product_name: Name of the product (e.g., Jira)
        :return: A dictionary with detailed cost breakdown for different company sizes.
        """
        company_sizes = ["Small Business", "Medium Business", "Large Enterprise"]
        years = [2021, 2022, 2023, 2024]
        
        # Generating dummy data for each company size and each year
        cost_data = []
        for size in company_sizes:
            company_data = {
                "company_size": size,
                "top_line_price": {
                    "dollar_value": round(random.uniform(1000, 50000), 2),
                    "payment_timing": random.choice(["Annual", "Monthly", "Quarterly"]),
                    "financing": random.choice(["Upfront", "Installments", "Subscription"]),
                },
                "implementation_costs": {
                    "integration": round(random.uniform(500, 10000), 2),
                    "training": round(random.uniform(1000, 15000), 2),
                    "consulting": round(random.uniform(1000, 20000), 2),
                },
                "hosting_costs": {
                    "servers": round(random.uniform(1000, 20000), 2),
                    "sla": random.choice(["Standard", "Premium", "Enterprise"]),
                    "cloud_compute": round(random.uniform(500, 15000), 2),
                },
            }
            cost_data.append(company_data)

        product_data = {
            "product_name": product_name,
            "description": f"{product_name} is a tool designed to help teams organize and collaborate more effectively.",
            "cost_breakdown": cost_data,
        }

        print(product_data)
        
        return product_data
    
    def get_product_data_dummy_static(product_name):
        """
        Get product data from database. Returns None if product does not exist.
        """
        product_data = {
            "product_name": "Jira",
            "description": "Jira is a project management tool designed to help teams organize and track work.",
            "cost_breakdown": [
                {
                "year": 2021,
                "company_size": "Small Business",
                "top_line_price": {
                    "dollar_value": 21895.74,
                    "payment_timing": "Monthly",
                    "financing": "Upfront"
                },
                "implementation_costs": {
                    "integration": 7569.99,
                    "training": 5584.07,
                    "consulting": 17074.38
                },
                "hosting_costs": {
                    "servers": 7161.8,
                    "sla": "Standard",
                    "cloud_compute": 2736.54
                }
                },
                {
                "year": 2022,
                "company_size": "Small Business",
                "top_line_price": {
                    "dollar_value": 20099.38,
                    "payment_timing": "Annual",
                    "financing": "Upfront"
                },
                "implementation_costs": {
                    "integration": 6650.94,
                    "training": 1296.36,
                    "consulting": 10898.02
                },
                "hosting_costs": {
                    "servers": 12313.18,
                    "sla": "Enterprise",
                    "cloud_compute": 2109.08
                }
                },
                {
                "year": 2023,
                "company_size": "Small Business",
                "top_line_price": {
                    "dollar_value": 23339.1,
                    "payment_timing": "Monthly",
                    "financing": "Subscription"
                },
                "implementation_costs": {
                    "integration": 4873.83,
                    "training": 9480.48,
                    "consulting": 14705.82
                },
                "hosting_costs": {
                    "servers": 8925.31,
                    "sla": "Standard",
                    "cloud_compute": 13900.83
                }
                },
                {
                "year": 2024,
                "company_size": "Small Business",
                "top_line_price": {
                    "dollar_value": 40692.66,
                    "payment_timing": "Monthly",
                    "financing": "Subscription"
                },
                "implementation_costs": {
                    "integration": 4776.87,
                    "training": 3561.14,
                    "consulting": 15767.52
                },
                "hosting_costs": {
                    "servers": 14465.5,
                    "sla": "Premium",
                    "cloud_compute": 3838.27
                }
                },
                {
                "year": 2021,
                "company_size": "Medium Business",
                "top_line_price": {
                    "dollar_value": 21782.74,
                    "payment_timing": "Monthly",
                    "financing": "Subscription"
                },
                "implementation_costs": {
                    "integration": 9985.3,
                    "training": 9598.0,
                    "consulting": 17917.65
                },
                "hosting_costs": {
                    "servers": 13406.63,
                    "sla": "Standard",
                    "cloud_compute": 10531.03
                }
                },
                {
                "year": 2022,
                "company_size": "Medium Business",
                "top_line_price": {
                    "dollar_value": 44377.63,
                    "payment_timing": "Quarterly",
                    "financing": "Subscription"
                },
                "implementation_costs": {
                    "integration": 8839.18,
                    "training": 12751.84,
                    "consulting": 7024.16
                },
                "hosting_costs": {
                    "servers": 6521.03,
                    "sla": "Enterprise",
                    "cloud_compute": 676.61
                }
                },
                {
                "year": 2023,
                "company_size": "Medium Business",
                "top_line_price": {
                    "dollar_value": 20852.42,
                    "payment_timing": "Monthly",
                    "financing": "Upfront"
                },
                "implementation_costs": {
                    "integration": 2197.82,
                    "training": 11874.66,
                    "consulting": 16055.2
                },
                "hosting_costs": {
                    "servers": 16248.02,
                    "sla": "Standard",
                    "cloud_compute": 2184.59
                }
                },
                {
                "year": 2024,
                "company_size": "Medium Business",
                "top_line_price": {
                    "dollar_value": 42431.1,
                    "payment_timing": "Quarterly",
                    "financing": "Upfront"
                },
                "implementation_costs": {
                    "integration": 7813.46,
                    "training": 13105.6,
                    "consulting": 2059.93
                },
                "hosting_costs": {
                    "servers": 8005.46,
                    "sla": "Enterprise",
                    "cloud_compute": 13149.5
                }
                },
                {
                "year": 2021,
                "company_size": "Large Enterprise",
                "top_line_price": {
                    "dollar_value": 22750.11,
                    "payment_timing": "Annual",
                    "financing": "Installments"
                },
                "implementation_costs": {
                    "integration": 1996.47,
                    "training": 5911.44,
                    "consulting": 9467.81
                },
                "hosting_costs": {
                    "servers": 2215.16,
                    "sla": "Premium",
                    "cloud_compute": 3719.36
                }
                },
                {
                "year": 2022,
                "company_size": "Large Enterprise",
                "top_line_price": {
                    "dollar_value": 35099.81,
                    "payment_timing": "Monthly",
                    "financing": "Installments"
                },
                "implementation_costs": {
                    "integration": 9632.8,
                    "training": 3350.72,
                    "consulting": 19355.16
                },
                "hosting_costs": {
                    "servers": 4812.67,
                    "sla": "Premium",
                    "cloud_compute": 11277.1
                }
                },
                {
                "year": 2023,
                "company_size": "Large Enterprise",
                "top_line_price": {
                    "dollar_value": 1461.15,
                    "payment_timing": "Monthly",
                    "financing": "Installments"
                },
                "implementation_costs": {
                    "integration": 5449.92,
                    "training": 4291.49,
                    "consulting": 15429.32
                },
                "hosting_costs": {
                    "servers": 11741.58,
                    "sla": "Enterprise",
                    "cloud_compute": 12559.67
                }
                },
                {
                "year": 2024,
                "company_size": "Large Enterprise",
                "top_line_price": {
                    "dollar_value": 29295.67,
                    "payment_timing": "Annual",
                    "financing": "Installments"
                },
                "implementation_costs": {
                    "integration": 1780.89,
                    "training": 5219.66,
                    "consulting": 14750.9
                },
                "hosting_costs": {
                    "servers": 9209.12,
                    "sla": "Premium",
                    "cloud_compute": 10105.14
                }
                }
            ]
            }

        return product_data