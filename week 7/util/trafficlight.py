class Traffic_Light:

    def simulator(color: str) -> str:
        try:
            output=""
            color_dic = {
                "red": "stop",
                "yello": "ready",
                "green": "go"
            }
            output = [value for key, value in color_dic.items() if key == color]
    
        except Exception as error:
            print("an error occord",error)

        else:
            print("noerror")

        finally:
            return output