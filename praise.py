def yell(text):
    text = text.upper()
    number_of_characters = len(text)
    result = text + "!" * (number_of_characters // 4)
    print(result)    

yell ("you are doing great")
yell ("dont forget to ask for help")
yell ("dont repeat yourself, keep things DRY")
