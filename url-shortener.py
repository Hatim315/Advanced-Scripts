import pyshorteners
m=input("Provide the url here:")
n=input("Provide the shortener(tinyurl/bitly):")
def short(m,n):
    
    if n=="tinyurl":
        k=pyshorteners.Shortener()
        return k.tinyurl.short(m)
    elif n=="bitly":
        k=pyshorteners.Shortener(api_key="052f1a710671006ac2c02447e3221ad6495f5422",user_id="jashan8999")
        return k.bitly.short(m)
   
    else:return "We don't support this shortener yet."
print(short(m,n))
#we can make our own url shortener using django and flask