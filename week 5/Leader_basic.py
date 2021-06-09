def user_score(read_count, reply_count, new_post_count):
    read_count = (read_count)
    new_reply_count = 3*(reply_count)
    new_po_count = 5*(new_post_count)
    
    if(read_count+new_reply_count+new_po_count>50):
        return 'Leader'
    else:
        return 'Basic'