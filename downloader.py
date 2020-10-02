import urllib.request

def reporthook(blocknum, blocksize, totalsize):
    readsofar = blocknum * blocksize
    # Fix for progressbar with random length
    if readsofar > totalsize:
        readsofar = totalsize
    percent = int((readsofar * 50 / totalsize))
    r_size = totalsize / 1024**2
    d_size = readsofar / 1024**2
    pgbar = '[{}{}] '.format('█' * percent, ' ' * (50 - percent)) + '[{0:.2f}/{1:.2f} MB]'.format(d_size, r_size)
    print('\r>>>>', pgbar, end='\r')

def download(url, output_path):
    opener = urllib.request.URLopener()
    opener.addheader('User-Agent', 'Mozilla/5.0')
    opener.retrieve(url, filename=output_path, reporthook=reporthook)
    print()