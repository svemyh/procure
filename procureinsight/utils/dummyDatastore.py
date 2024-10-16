# dummyDatastore.py

import random

class DummyDatastore:
    def __init__(self):
        pass

    def getAllCompanies(self):
        companies = [
            {"title": "Google", "tag": "Google", "description": "Google is a search engine, created by Larry Page and Sergey Brin."},
            {"title": "Meta", "tag": "Meta", "description": "Social media platform, created by Mark Zuckerberg."},
            {"title": "Palantir", "tag": "Palantir", "description": "Sell data analysis software to governments and corporations."},
            {"title": "Amazon", "tag": "Amazon", "description": "E-commerce and cloud computing company, created by Jeff Bezos."},
            {"title": "Microsoft", "tag": "Microsoft", "description": "Software company, created by Bill Gates and Paul Allen."},
            {"title": "Deutsche Bank", "tag": "Deutsche-Bank", "description": "Banking and financial services company."},
        ]
        return companies

    def getCompany(self, company_name):
        """
        Dummy data for company data. Used for testing.
        """
        company_data = {
            f"company_name": f"{company_name}",
            "description": f"{company_name} is a search engine, created by Larry Page and Sergey Brin.",
            "products": [
                {"title": f"{company_name} Adwords", "tag": "google-adwords", "description": "Large scale advertising platform."},
                {"title": f"{company_name} Search", "tag": "google-search", "description": "Search engine."},
                {"title": f"{company_name} Maps", "tag": "google-maps", "description": "Mapping software."},
                {"title": f"{company_name} Drive", "tag": "google-drive", "description": "Cloud storage."},
                {"title": f"{company_name} Cloud", "tag": "google-cloud", "description": "Cloud computing."},
                {"title": f"{company_name} Workspace", "tag": "google-workspace", "description": "Collaboration tools."},
                {"title": f"{company_name} Analytics", "tag": "google-analytics", "description": "Web analytics."},
                {"title": f"{company_name} Chrome", "tag": "google-chrome", "description": "Web browser."},
                {"title": f"{company_name} Pixel", "tag": "google-pixel", "description": "Smartphone."},
                {"title": f"{company_name} Nest", "tag": "google-nest", "description": "Smart home devices."},
                {"title": f"{company_name} Fi", "tag": "google-fi", "description": "Mobile phone service."},
                {"title": f"{company_name} Photos", "tag": "google-photos", "description": "Photo storage."},
            ],
        }
        return company_data

    def getProduct(self, product_name):
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

    @staticmethod
    def getProductStatic(self, product_name):
        """
        Get static dummy product data for testing.
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
                # ... (other static data entries)
            ]
        }

        return product_data
