#Can someone remind me why I wrote code for Java in Python?
#Whatever

def getUserInput():
    type = str(raw_input('Item or Block? '))
    type=type.lower()
    material = ''
    if type == 'block':
        material = str(raw_input('Material for block: '))
    id = str(raw_input('Enter Item ID: ')) #Asks user for item id
    name = str(raw_input('Enter Item Name: ')) #Asks user for item name
    creativetab = str(raw_input('Enter Creative Tab: ')) #Asks user for what creative tab they want the item in
    modid = str(raw_input('Enter Mod ID: ')) #Asks user for the mod id
    output(id, name, creativetab, modid, type, material)

def output(id, name, creativetab, modid, type, material):
    print("Put the following in your class:")
    print("")
    if type == 'item':
        print("public static Item " + id + ";") #public static Item itemID;
    elif type == 'block':
        print("public static Block " + id + ";") #public static Block itemID
    else:
        print(type + " isn\'t a valid type.")
        getUserInput()
    print("")
    print("Put the following code in preInit")
    print('')
    if type == 'item':
        print(id + " = new " + id + "().setCreativeTab(" + creativetab + ").setUnlocalizedName(" + "\"" + id + "\"" + ").setTextureName(" + "\"" + modid + ":" + id + "\"" + ");") #Comment on this code goes here
        print('GameRegistry.registerItem(' + id + ", " + id + ".getUnlocalizedName().substring(5));") #GameRegistry.registerItem(itemID, itemID.getUnlocalizedName().substring(5))
    elif type == 'block':
        print(id + " = new " + id + "(Material." + material + ").setCreativeTab(" + creativetab + ").setBlockName(" + "\"" + id + "\"" + ").setBlockTextureName(" + "\"" + modid + ":" + id + "\"" + ");") #Comment on this code goes here
        print('GameRegistry.registerBlock(' + id + ", " + id + ".getUnlocalizedName().substring(5));") #GameRegistry.registerItem(itemID, itemID.getUnlocalizedName().substring(5))
    print('')
    print("Put the following in en_US.lang")
    print('')
    if type == 'item':
        print("item." + id + ".name=" + name) #item.itemID.name=itemName
    elif type == 'block':
        print("tile." + id + ".name=" + name)
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
