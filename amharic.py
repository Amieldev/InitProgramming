# ቁጥር ወደ አማርኛ.

ones = ('', 'አንድ', 'ሁለት', 'ሶስት', 'አራት', 'አምስት', 'ስድስት', 'ሰባት', 'ስምንት', 'ዘጠኝ')

twos = ('አሥር', 'አስራ አንድ', 'አስራ ሁለት', 'አስራ ሶስት', 'አስራ አራት', 'አስራ አምስት', 'አስራ ስድስት', 'አስራ ሰባት', 'አስራ ስምንት', 'አስራ ዘጠኝ')

tens = ('ሀያ', 'ሰላሳ', 'አርባ', 'ሀምሳ', 'ስልሳ', 'ሰባ', 'ሰማንያ', 'ዘጠና', 'መቶ')

suffixes = ('', 'ሺህ', 'ሚሊየን', 'ቢሊየን')

def num2text(number, index):
    
    if number=='0':
        return 'ዜሮ'    
   
    length = len(number)
    
    if(length>3):
        return False
    number = number.zfill(3)
    words = ''
    hdigit = int(number[0])
    tdigit = int(number[1])
    odigit = int(number[2])
    
    words += '' if number[0] == '0' else ones[hdigit]
    words += ' መቶ ' if not words == '' else ''
    if(tdigit > 1):
        words += tens[tdigit - 2]
        words += ' '
        words += ones[odigit]
    
    elif(tdigit == 1):
        words += twos[(int(tdigit + odigit) % 10) - 1]
        
    elif(tdigit == 0):
        words += ones[odigit]

    if(words.endswith('ዜሮ')):
        words = words[:-len('ዜሮ')]
    else:
        words += ' '
     
    if(not len(words) == 0):    
        words += suffixes[index]
        
    return words;
    
def getTxt(number):
    length = len(str(number))
    
    if length>12:
        return 'ከ 12 በላይ አይችልም.'
    
    count = length // 3 if length % 3 == 0 else length // 3 + 1
    copy = count
    words = []
 
    for i in range(length - 1, -1, -3):
        words.append(num2text(str(number)[0 if i - 2 < 0 else i - 2 : i + 1], copy - count))
        count -= 1;

    final_words = ''
    for s in reversed(words):
        temp = s + ' '
        final_words += temp
    

    return final_words

number = int(input('ቁጥር አስገባ: '))

print('%d በፊደል: %s' %(number, getTxt(number)))