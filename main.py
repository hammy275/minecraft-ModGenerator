#Can someone remind me why I wrote code for Java in Python?
#Whatever

def getUserInput():
    type = str(raw_input('Item or Block? '))
    type=type.lower()
    material = ''
    if type != 'block' and type != 'item':
        print('Please enter valid input')
        getUserInput()
    if type == 'block':
        material = str(raw_input('Material for block: ')) #At some point I will add a sanity check here
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
        print("public static Block " + id + ";") #public static Block itemID;
    else:
        print('That moment when your sanity check doesn\'t work.')
        print('Leave a comment on the GitHub page that you got this error. Thanks!')
        return #I have no idea if these 3 lines actually work lol (will test later maybe)
    print("")
    print("Put the following code in preInit")
    print('')
    if type == 'item':
        print(id + " = new " + id + "().setCreativeTab(" + creativetab + ").setUnlocalizedName(" + "\"" + id + "\"" + ").setTextureName(" + "\"" + modid + ":" + id + "\"" + ");") #Comment on this code goes here
        print('GameRegistry.registerItem(' + id + ", " + id + ".getUnlocalizedName().substring(5));") #GameRegistry.registerItem(itemID, itemID.getUnlocalizedName().substring(5))
    elif type == 'block':
        print(id + " = new " + id + "(Material." + material + ").setCreativeTab(" + creativetab + ").setBlockName(" + "\"" + id + "\"" + ").setBlockTextureName(" + "\"" + modid + ":" + id + "\"" + ");") #Comment on this code goes here
        print('GameRegistry.registerBlock(' + id + ", " + id + ".getUnlocalizedName().substring(5));") #GameRegistry.registerItem(itemID, itemID.getUnlocalizedName().substring(5))
    else:
        print('Moo!')
        print('Please report this error and other previously recieved errors on the GitHub page.')
        return
    print('')
    print("Put the following in en_US.lang")
    print('')
    if type == 'item':
        print("item." + id + ".name=" + name) #item.itemID.name=itemName
    elif type == 'block':
        print("tile." + id + ".name=" + name) #tile.itemID.name=blockName
    else:
        print('Will 3 sanity errors save us?')
        print('Please report this error and other previously recieved errors on the GitHub page.')
        return
    print("")
    print("")
    print("Don\'t forget to make a class from your item id!") #Reminds user to create class for their item
    generateAgain = str(raw_input("Generate Again?! [Y/N]" )) #Prompts user if they want to generate another item
    generateAgain = generateAgain.lower()
    if generateAgain == "y":
        for i in range(6):
            print('')
        getUserInput()
    elif generateAgain == '':
        return
    #Apparently pressing ENTER at this prompt didn't call the else statement (hence this code)
    else:
        return
getUserInput() #Runs getUserInput (it gets User Input omg)

#I have the cleanest code that doesn't ever repeat /s
