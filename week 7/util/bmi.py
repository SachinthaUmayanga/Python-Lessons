class BMI:

    def bmi_calculator(height:float,weight:float)->str:
        try:
            bmi = weight / (height/100)**2
        
            notification = ""
            if bmi <= 18.5:  
                notification = "Oops! You are underweight."
            elif bmi <= 24.9:  
                notification = "Awesome! You are healthy."
            elif bmi <= 29.9:  
                notification = "Eee! You are over weight." 
            else:  
                notification = "Seesh! You are obese."
            
            return notification
        
        except Exception as error:
            print("an error occorred",error)