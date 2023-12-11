def url_to_id(url):
    '''The function url_to_id aims to convert an url into a tweet id
    The parameters used are 
    :param url: this param represents the twitter url of a tweet and is of type string

    url_to_id returns the tweet id and is of type int'''
    i = 1
    res = ""
    try:
        # if we encounter a '/' we return the id as an int
        while url[(-1)*i] != "/":
            res = url[(-1)*i] + res
            i += 1
        return int(res)
    except:
        # the URL isn't valid
        return None
