def getUserInput():
    id = str(raw_input('Enter Item ID: ')) #Asks user for item id
    name = str(raw_input('Enter Item Name: ')) #Asks user for item name
    creativetab = str(raw_input('Enter Creative Tab: ')) #Asks user for what creative tab they want the item in
    modid = str(raw_input('Enter Mod ID: ')) #Asks user for the mod id
    output(id, name, creativetab, modid)

def output(id, name, creativetab, modid):
    print("Put the following in your class:")
    print("")
    print("public static Item " + id + ";") #public static Item itemID;
    print("")
    print("Put the following code in preInit")
    print('')
    print(id + " = new " + id + "().setCreativeTab(" + creativetab + ").setUnlocalizedName(" + "\"" + id + "\"" + ").setTextureName(" + "\"" + modid + ":" + id + "\"" + ");") #Comment on this code goes here
    print('GameRegistry.registerItem(' + "\"" + id + "\"" + ", " + id + ".getUnlocalizedName().substring(5));") #GameRegistry.registerItem(itemID, itemID.getUnlocalizedName().substring(5))
    print('')
    print("Put the following in en_US.lang")
    print('')
    print("item." + id + ".name=" + name) #item.itemID.name=itemName
    print("")
    print("")
    print("Don\'t forget to make a class from your item id!") #Reminds user to create class for their item
    generateAgain = str(raw_input("Generate Again?! [Y/N]" )) #Prompts user if they want to generate another item
    generateAgain = generateAgain.lower()
    if generateAgain == "y":
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        getUserInput()
    else:
        return
getUserInput() #Runs getUserInput (it gets User Input omg)
