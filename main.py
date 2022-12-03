# TODO: Finish handling self posts and likes
# TODO: Recognize non-reacted posts
# TODO: Link post to poster
# TODO: Make Table

# Table Columns
# - User
# - Total Likes
# - Link to Meme?
# - Date?

from bs4 import BeautifulSoup
from emoji import UNICODE_EMOJI
import re

from the_boys import the_boys

print("-- List of Usernames to Look for --")
print(the_boys)
print()

def is_emoji(s):
    return s in UNICODE_EMOJI['en']

with open('chat.html', 'r', encoding="utf-8") as f:
    contents = f.read()
    
soup = BeautifulSoup(contents, 'html.parser')

chat_box = soup.select_one('div._ab5z._ab5_')

for chat in chat_box.div.children:
    txt = chat.get_text()
    image = chat.find('img', {'class': '_ac71'})
    image2 = chat.find('img',{'style': 'height: 236px;'})
    reaction = chat.find('div', {'class': '_acfk _acfl _acfm'})
    my_image = chat.find('img',{'class': '_ab8w  _ab94 _ab99 _ab9f _ab9m _ab9p _abcm'})
    my_reaction = chat.find('div', {'class': '_acfk _acfl'})
    
    has_image = False
    user_name = False
    total_likes = 0
    
    if image or my_image or image2:
        has_image = True
    
    username = chat.find('div', {'class': '_aacl _aacn _aacu _aacy _aada'})
    if username:
        print()
        print(username.get_text())
        
    username_forward = chat.find('div', {'class':'_aacl _aacn _aacu _aacy _aad6'})
    if username_forward:
        print()
        print(username_forward.get_text())
    
    me = chat.find('div',{'class':'_acd2 _acd3'})
    
    if me:
        print()
        print('jlcalvano')
    
    profile_picture_classes = "x6umtig x1b1mbwd xaqea5y xav7gou xk390pu x5yr21d xpdipgo xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x11njtxf xh8yej3"
    
    if reaction:
        reaction_txt = reaction.get_text()
        num_profile_pictures = reaction.find_all('img', {'class': profile_picture_classes})
        plus_sign = re.findall(r'^.*\+ (\d)$', reaction_txt)
        
        if plus_sign:
           total_likes = int(len(num_profile_pictures)) + int(plus_sign[0])
         
        if not plus_sign:
           just_number = re.findall(r'^.*(\d)$', reaction_txt)
           if just_number:
            total_likes = int(just_number[0])
           else:
            total_likes = len(num_profile_pictures)
        print('--- ' + repr(txt)," Total Likes: ", total_likes)
    
    if has_image and not reaction:
        print('--- ' + repr(txt)," Total Likes: ", total_likes)
    
    if my_reaction:
        print("my reaction!")
           
           
        