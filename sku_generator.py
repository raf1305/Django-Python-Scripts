SKU = ''
alphas = ['Q','W','E','R','T','Y','U','I','O','P','0','7','3','6','A','S','D','F','G','H','J','K','L','1','8','2','Z','X','C','V','B','N','M','4','5','9']
# alphas = ['A','B','C']
import datetime

def f(previous):
    if len(previous)==0:
        return str(datetime.now().year)[2:4]
    last = previous[-1]

    index = alphas.index(last)
    if index == len(alphas)-1:
        previous = f(previous[:-1])
        previous = previous+alphas[index]
        index = -1
    previous = previous[:-1] + alphas[index+1]
    return previous

def generate_item_sku():
    if EcomItem.objects.count() == 0:
        co = SKU+'QWERT'
    else:
        prev = EcomItem.objects.latest('id').sku
        if SKU not in prev:
            co = SKU+'QWERT'
        else:
            co = SKU+f(prev.replace(SKU,''))
    return co
