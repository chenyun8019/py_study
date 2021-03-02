class gloable_var:
    id="0"
    url4="1"
    request="2"
    run="3"
    header="4"
    requestData="5"
    yuqi="6"
    shiji="7"
    yilaiId="8"
    yilaiData="9"
    yilaiKey="10"

def get_id():
    return gloable_var.id
def get_url8():
    return gloable_var.url4
def get_request():
    return gloable_var.request
def get_run():
    return gloable_var.run
def get_header():
    return gloable_var.header
def get_requestdata():
    return gloable_var.requestData
def get_yuqi():
    return gloable_var.yuqi
def get_shiji():
    return gloable_var.shiji
def get_yilaiID():
    return gloable_var.yilaiId

def get_yilaiDATA():
    return gloable_var.yilaiData
def get_yilaiKEY():
    return gloable_var.yilaiKey
def header_value():
    header={
        "header":"12345"
    }

if __name__ == '__main__':
    ee=gloable_var()
    print (ee.shiji)