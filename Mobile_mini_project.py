class Mobiles():
    def _init_(self):
        pass
    def get_mobile(self):
        want_mobile = input("Do you want mobile ..........\n Please Enter Yes or No  ")
        
        if want_mobile=='YES' or want_mobile=='yes':
            brands =["iphone","samsung"]
            brand_choice =input("Which brand are you interested in iphone or samsung").lower()
            while brand_choice not in brands :
                print("Sorry that brand is not available try checking others")
                brand_choice = input("Enter the brand Name ").lower()
            return brand_choice
        else:
            print("See u next time")
    
    def iphone_vari(self):
        iphones = ["iphone 15","iphone 15 plus","iphone 15 pro"]
        
        iph = input(f"Choose which varient you want {iphones}").lower()
        while iph not in iphones:
            print(f"sorry we don't have that model we have only this {iphones}")
            iph = input("Select from above list")
        return iph
        
    def samsung_vari(self):
        samsung = ["samsang S21","samsang S22","samsang S23"]
        sam = input(f"Choose which varient you want {samsung} ").lower()
        while sam not in samsung:
            print(f"sorry we don't have that model we have only this {samsung}")
            sam = input("Select from above list")
        return sam
    
    def get_color(self):
         print("Which Color you want Black, Red, Blue")
         col = input().lower()
         return col

    def get_storage(self):
        print("These are the storage capacity we have 128,256,512  \n you can choose any of these")
        store = int(input())
        return store


class Smart_phone(Mobiles):
    def ph(self):
        print("Welcome to Smart Communication World")
        brand_choice = self.get_mobile()
        if brand_choice =="iphone":
            variant = self.iphone_vari()
            color = self.get_color()
            storage = self.get_storage()
            return {
                "Model" : "Apple",
                "model": f"iPhone {variant}",
                "OS":"ios 17",
                "variant": variant,
                "color": color,
                "storage": storage,
                "camera": "48MP Main: 24 mm, ƒ/1.78 aperture, second‑generation sensor‑shift optical image stabilisation, 100% Focus Pixels, support for super‑high‑resolution photos (24MP and 48MP)",
                "battery": "4500 mAh",
                "display": "15.54 cm / 6.1″ (diagonal) all‑screen OLED display 2556x1179-pixel resolution at 460 ppi",
                "price": "$999.94",
                "launch_date": "September 2024",
                "version": "iOS 18",
                "charging_type": "MagSafe charging 15W, Lightning (USB-C may also be supported)",
                "ram": "8GB"
            }
        elif brand_choice =="samsung":
            variant = self.samsung_vari()
            color = self.get_color()
            storage = self.get_storage()
            return {
                "brand": "Samsung",
                "model":f"samsung {variant}",
                "variant": variant,
                "color": color,
                "storage": storage,
                "camera": "200-megapixel",
                "battery": "4855mAh",
                "display": "Dynamic AMOLED 2X, 120Hz, HDR10+, 1200 nits (HBM), 1750 nits (peak)",
                "price": "Rs 99,999",
                "launch_date": "February 2023",
                "version": "Android 14",
                "charging_type": "USB-C",
                "ram": "8/12GB"
                
            
}
    

        
   
    
c = Smart_phone()
phone_info = c.ph()
print(phone_info)