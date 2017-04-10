#!/usr/bin/python

def get_batches(text):

    seq_length = 5

    batch_size = 3

    seq_x, seq_y, batch_x, batch_y, batches = [], [], [], [], []
        
    for i in range(0, len(text)):
        seq_x.extend([text[i:i+seq_length]])
        seq_y.extend([text[i:i+seq_length]])
        for ii in range (0, len(seq_x)):
            batch_x.extend(seq_x[ii:ii+batch_size])
            batch_y.extend(seq_y[ii:ii+batch_size])
            for iii in batch_x, batch_y in range(0, len(batch_x)):
                batch = [batch_x, batch_y]
                batches.extend(batch)
    yield np.ndarray(batches)
    
print get_batches("For its April Fools prank this year Google unveiled apps for your cats and dogs for both iOS and Android giving the internet to our furry friends After countless cute photos and memes of puppies and kittens its only fair we let them browse through it too Welcome to the internet cats and dogs please dont dig through my Twitter history Are you Feeling Meow The search engine giant has built a reputation out of April Fools Day tricking visitors each year Last years Drop the Mic joke backfired when it got rid of a feature that people actually use on Gmail As part of its long-standing April 1 tradition the company has also hinted at Pokemon Go two years before it actually came out declared an end to YouTube and announced the Google Nose wearable")
