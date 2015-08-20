# http://www.amazon.com/Drive-Medical-Rollator-Removable-Support/product-reviews/B005S1CHKC/ref=cm_cr_pr_btm_link_163?ie=UTF8&showViewpoints=1&sortBy=recent&reviewerType=all_reviews&formatType=all_formats&filterByStar=all_stars&pageNumber=163

import time
import re
from retrieveurl import graburlcontent

alexa = "http://www.alexa.com/siteinfo/"
sites = ["mynewplace.com", 'apartmentfinder.com', 'apartmentguide.com', 'forrent.com', 'zillow.com', 'trulia.com', 'apartmentlist.com', 'apartments.com']


####################### Setting the Stage (methods) #######################


def grab_us_rank(pagetext):
    usrank = re.findall('alt=\'United States Flag\'><strong class="metrics-data\salign-vmiddle">\s([\d,]+)', pagetext)
    return usrank

def grab_global_rank(pagetext):
    global_rank = re.findall('<!-- Alexa web traffic metrics are available via our API at http://aws.amazon.com/awis -->\s([\d,]+)', pagetext)
    return global_rank



####################### Execution part #######################
print('Website\tLocal Rank\tGlobal Rank')
for i in sites:
    try:
        page_contents = graburlcontent(alexa + i)
        #print(page_contents)
        usrank = grab_us_rank(page_contents)
        global_rank = grab_global_rank(page_contents)
        
        print(i, '\t', usrank[0], '\t', global_rank[0])
        time.sleep(4)
        
       
        """
        reviewer_names = grab_reviewer_name(page_contents)
        star_ratings = grab_star_rating(page_contents)[2:]
        reviews = grab_reviews(page_contents)
        
        x = 0
        for i in range(x, len(reviews)):
            print('Name: ', reviewer_names[x].replace('&amp;','and'), '\n')
            print('Stars they gave to the product: ', star_ratings[x], '\n')
            print('Review: ', reviews[x].replace('<br /><br />',' '),'\n')
            print('\n'*2)
            
            x += 1
        """    
            

    except:
        print("can't print for some reason, check the control flow in zipsx")
        continue

        print('\n')
        

        
