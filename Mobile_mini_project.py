class Mobiles():
    def __init__(self):
        self.brands = {
            "iphone": {
                "name": "Apple",
                "os": "iOS 17",
                "variants": ["iphone 15", "iphone 15 plus", "iphone 15 pro"],
                "details": {
                    "iphone 15": {
                        "model": "iPhone 15",
                        "camera": "48MP Main",
                        "battery": "4500 mAh",
                        "display": "6.1 inch OLED",
                        "ram": "8GB",
                        "price": "$999.94"
                    },
                    "iphone 15 plus": {
                        "model": "iPhone 15 Plus",
                        "camera": "Dual 12MP",
                        "battery": "5000 mAh",
                        "display": "6.7 inch OLED",
                        "ram": "8GB",
                        "price": "$1099.94"
                    },
                    "iphone 15 pro": {
                        "model": "iPhone 15 Pro",
                        "camera": "Triple 48MP",
                        "battery": "5500 mAh",
                        "display": "6.1 inch OLED (ProMotion)",
                        "ram": "12GB",
                        "price": "$1299.94"
                    }
                }
            },
            "samsung": {
                "name": "Samsung",
                "os": "Android 14",
                "variants": ["samsung S21", "samsung S22", "samsung S23"],
                "details": {
                    "samsung S21": {
                        "model": "Galaxy S21",
                        "camera": "12MP Main",
                        "battery": "4000 mAh",
                        "display": "6.2 inch AMOLED",
                        "ram": "8GB",
                        "price": "$799.99"
                    },
                    "samsung S22": {
                        "model": "Galaxy S22",
                        "camera": "50MP Main",
                        "battery": "4500 mAh",
                        "display": "6.8 inch AMOLED",
                        "ram": "12GB",
                        "price": "$899.99"
                    },
                    "samsung S23": {
                        "model": "Galaxy S23",
                        "camera": "200MP Main",
                        "battery": "5000 mAh",
                        "display": "7.2 inch AMOLED",
                        "ram": "16GB",
                        "price": "$999.99"
                    }
                }
            }
        }

    def get_mobile(self):
        want_mobile = input("Do you want mobile ..........\n Please Enter Yes or No  ")

        if want_mobile.lower() == 'yes':
            brands = ["iphone", "samsung"]
            brand_choice = input("Which brand are you interested in: iphone or samsung ").lower()
            while brand_choice not in brands:
                print("Sorry, that brand is not available. Please try checking others.")
                brand_choice = input("Enter the brand Name: ").lower()
            return brand_choice
        else:
            print("See you next time.")

    def iphone_vari(self):
        iphones = ["iphone 15", "iphone 15 plus", "iphone 15 pro"]

        iph = input(f"Choose which variant you want {iphones}: ").lower()
        while iph not in iphones:
            print(f"Sorry, we don't have that model. We have only these: {iphones}")
            iph = input("Select from above list: ").lower()
        return iph

    def samsung_vari(self):
        samsung = ["samsung S21", "samsung S22", "samsung S23"]
        sam = input(f"Choose which variant you want {samsung}: ").lower()
        while sam not in [variant.lower() for variant in samsung]:
            print(f"Sorry, we don't have that model. We have only these: {samsung}")
            sam = input("Select from above list: ").lower()
        return sam

    def get_color(self):
        print("Which Color do you want: Black, Red, Blue?")
        col = input().lower()
        return col

    def get_storage(self):
        print("These are the storage capacity we have: 128, 256, 512GB\nYou can choose any of these.")
        store = int(input())
        return store

class Smart_phone(Mobiles):
    def ph(self):
        print("Welcome to Smart Communication World")
        brand_choice = self.get_mobile()
        if brand_choice == "iphone":
            variant = self.iphone_vari()
        elif brand_choice == "samsung":
            variant = self.samsung_vari()
        else:
            return None

        color = self.get_color()
        storage = self.get_storage()

        
        details = self.brands[brand_choice]["details"]

        
        variant_key = None
        for key in details.keys():
            if key.lower() == variant.lower():
                variant_key = key
                break

        if variant_key:
            brand_details = details[variant_key]
            phone_info = {
                "Brand": self.brands[brand_choice]["name"],
                "Model": f"{variant.title()} {brand_details['model']}",
                "OS": self.brands[brand_choice]["os"],
                "Variant": variant,
                "Color": color,
                "Storage": f"{storage}GB",
                "Camera": brand_details["camera"],
                "Battery": brand_details["battery"],
                "Display": brand_details["display"],
                "RAM": brand_details["ram"],
                "Price": brand_details["price"]
            }
            return phone_info
        else:
            print("Sorry, that variant is not available.")
            return None


c = Smart_phone()
phone_info = c.ph()
if phone_info:
    print(phone_info, end="\n")
else:
    print("You didn't choose a phone.")
