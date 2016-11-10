import re, requests
def template(template_name, *args):
    text = open(template_name, 'r').read().replace('\n', '')
    text = text % args
    return text

def hashtag(text):
    hh = False
    ret_text = ""
    hs_text = ""
    for t in text:
        if t == '#':
            hh = True
        elif t == ' ' and hh == True:
            ret_text += template('hashtag.html', hs_text, hs_text)
            ret_text += ' '
            hs_text = ''
            hh = False
        elif hh == True:
            hs_text += t
        else:
            ret_text += t
    return ret_text

def at(text):
    hh = False
    ret_text = ""
    hs_text = ""
    for t in text:
        if t == '@':
            hh = True
        elif t == ' ' and hh == True:
            ret_text += template('at.html', hs_text, hs_text)
            ret_text += ' '
            hs_text = ''
            hh = False
        elif hh == True:
            hs_text += t
        else:
            ret_text += t
    return ret_text

def link_image(text, link=True, image=True):
    pat_url = re.compile(r'''(?x)((http|ftp|gopher|https)://(\w+[:.]?){2,}(/?|[^ \n\r"]+[\w/])(?=[\s\.,>)'"\]]))''')
    for url in re.findall(pat_url, text):
        path = url[3].rsplit('.',1)
        if image == True and len(path) > 1 and path[1] in ['png','jpg','jpeg','gif','ico']:
            text = text.replace(url[0], template('image.html', url[0], url[0]))
        elif link == True:
            text = text.replace(url[0], template('link.html', url[0], url[0].split('://',1)[1]))
    return text
    
def bio(text):
    return link_image(at(hashtag(text)), image=False)
    
def chirp(text):
    return link_image(at(hashtag(text)))
