def main():
    # request user for input
    name = input("Enter a fruit: ")
    
    fruits = {
        'banana': '50kgcals',
        'orange': '25kgcals',
        'mango' : '75kgcals',
        'apple': '60kgcals',     
    }
    try:
        if not fruits[name]:
            pass
    except KeyError:
            pass  
    else:
        print(fruits[name])
    
    
    
        
  


main()