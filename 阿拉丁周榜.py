# -*- coding: utf-8 -*-
# 尝试一下branch功能
"""
Created on Fri Jun 28 10:32:53 2019

@author: 31782
"""

# Read Response.txt


response = {"code":200,"msg":"\u83b7\u53d6\u6210\u529f","day":"2019\/07\/07","data":[{"id":"88691113","appkey":"346bd82b51d286add5d626eee02ff991","name":"\u5c0f\u5e74\u7cd5+","category":"\u5185\u5bb9\u8d44\u8baf","logo":"http:\/\/aldpicsh-1252823355.cossh.myqcloud.com\/caijicons\/6a6ec5e437d224944ce0aa13a0d99c9d.png","desc":"\u6b23\u8d4f\u7f51\u53cb\u4f73\u4f5c\uff0c\u5173\u6ce8\u6709\u6599\u7528\u6237\uff01\u7167\u7247\u8f6c\u6210\u914d\u4e50\u89c6\u9891\uff1a\u6a21\u677f\u7cbe\u7f8e\uff0c\u6548\u679c\u4e30\u5bcc\uff1b\u64cd\u4f5c\u6781\u7b80\uff0c\u8f7b\u677e\u521b\u4f5c\uff01","gzh_num":"3","read_count":"12.4\u4e07","aldzs":"10000","grow":"75","status":1,"ranks_variety":0,"category_ranks_variety":0},{"id":"88691116","appkey":"4bdab85127b5ef4b7b277a6fa23c93d8","name":"\u62fc\u591a\u591a","category":"\u7f51\u7edc\u8d2d\u7269","logo":"http:\/\/aldpicsh-1252823355.cossh.myqcloud.com\/caijicons\/2fc87e6acc084ad16693b9e82cd80677.png","desc":"\u62fc\u591a\u591a\uff0c\u591a\u5b9e\u60e0\uff0c\u591a\u4e50\u8da3\u3002","gzh_num":"5","read_count":"0.8\u4e07","aldzs":"9336","grow":"62","status":0,"ranks_variety":1,"category_ranks_variety":0},{"id":"88694341","appkey":"17d3cfdd71a4e7039d99833c62190f66","name":"\u540c\u7a0b\u827a\u9f99\u9152\u5e97\u673a\u7968\u706b\u8f66\u7968\u95e8\u7968","category":"\u65c5\u6e38","logo":"http:\/\/aldpicsh-1252823355.cossh.myqcloud.com\/caijicons\/9eeb6184b140749d0449d055e79ce981.png","desc":"\u540c\u7a0b\u65c5\u6e38\u5b98\u65b9\u5c0f\u7a0b\u5e8f\uff0c\u63d0\u4f9b\u98de\u673a\u7968\u3001\u706b\u8f66\u7968\u3001\u6c7d\u8f66\u7968\u3001\u9152\u5e97\u3001\u666f\u70b9\u95e8\u7968\u53ca\u8239\u7968\u9884\u8ba2\u670d\u52a1\uff0c\u54c1\u8d28\u65c5\u6e38\u8ba9\u60a8\u65c5\u884c\u9884\u5b9a\u66f4\u653e\u5fc3\u3002","gzh_num":"126","read_count":"35.3\u4e07","aldzs":"9334","grow":"35","status":0,"ranks_variety":-1,"category_ranks_variety":0},{"id":"87562401","appkey":"187c25e336d0cffa28e28bfc03014292","name":"\u795d\u798f\u5708\u5b50","category":"\u89c6\u9891","logo":"http:\/\/aldpicsh-1252823355.cossh.myqcloud.com\/ad_advertiser\/1551946677.jpg","desc":"\u4eca\u5929\u662f\u4e2a\u597d\u65e5\u5b50\uff0c\u5b9a\u5236\u6700\u597d\u795d\u798f\u9001\u7ed9\u4eb2\u4eba\uff0c\u670b\u53cb\uff0c\u7fa4\u53cb\uff01\u5728\u8fd9\u91cc\u60a8\u53ef\u4ee5\u66f4\u65b9\u4fbf\u7684\u5236\u4f5c\u548c\u6b23\u8d4f\u4f5c\u54c1\u3001\u7ed3\u4ea4\u66f4\u591a\u77e5\u97f3\u3002","gzh_num":"4","read_count":"0.3\u4e07","aldzs":"8819","grow":"644","status":1,"ranks_variety":1,"category_ranks_variety":0},{"id":"87550672","appkey":"22650289f0d081654a919a8161343bd6","name":"\u706b\u67f4\u4eba\u51b2\u7a81","category":"\u6e38\u620f","logo":"http:\/\/aldpicsh-1252823355.cossh.myqcloud.com\/caijicons\/b4bbcf0f97ee0b334677582d67d452db.png","desc":"\u4ece\u524d\u6709\u6839\u706b\u67f4\u6320\u4e86\u6320\u5934\uff0c\u7136\u540e\u5b83\u5c31\u7740\u4e86\uff01","gzh_num":0,"read_count":"0","aldzs":"8545","grow":"631","status":1,"ranks_variety":3,"category_ranks_variety":1},{"id":"88693149","appkey":"2e3665f38b5d746d33e2fb4fda440cf0","name":"\u7f8e\u56e2\u5916\u5356","category":"\u9910\u996e","logo":"http:\/\/aldpicsh-1252823355.cossh.myqcloud.com\/caijicons\/e696a1b81216f34d6a10f8f95eae37c5.png","desc":"\u7f8e\u56e2\u5916\u5356\uff0c\u9001\u5565\u90fd\u5feb\uff01\u9644\u8fd1\u7f8e\u98df\u3001\u65e9\u5348\u665a\u9910\u3001\u4e0b\u5348\u8336\u3001\u5bb5\u591c\u3001\u4e2d\u9910\u3001\u897f\u9910\u3001\u5bb6\u5e38\u83dc\u3001\u9c9c\u82b1\u86cb\u7cd5\u3001\u996e\u6599\u751c\u70b9\u3001\u751f\u9c9c\u8d85\u5e02\u3001\u6c34\u679c\u852c\u83dc\u3001\u4fbf\u6377\u652f\u4ed8\u300130\u5206\u949f\u9001\u8fbe","gzh_num":"11","read_count":"40.4\u4e07","aldzs":"8437","grow":"64","status":0,"ranks_variety":-2,"category_ranks_variety":0},{"id":"87545329","appkey":"cc03069b0ddbeb83d83996e648d64cd2","name":"\u60f3\u4f60\u76f8\u518c","category":"\u56fe\u7247\u6444\u5f71","logo":"http:\/\/aldpicsh-1252823355.cossh.myqcloud.com\/ad_advertiser\/1557749019.jpg","desc":"\u4e0a\u4f20\u60a8\u7684\u7167\u7247\uff0c\u8ba9\u8fdc\u65b9\u7684\u4ed6\uff0c\u6536\u5230\u60a8\u7684\u795d\u798f\u3002","gzh_num":"1","read_count":"0.7\u4e07","aldzs":"8433","grow":"587","status":1,"ranks_variety":2,"category_ranks_variety":0},{"id":"87563880","appkey":"0eacc8166b7fb7094bd068002696f547","name":"\u6d88\u706d\u75c5\u6bd2","category":"\u6e38\u620f","logo":"http:\/\/aldpicsh-1252823355.cossh.myqcloud.com\/caijicons\/afbd87deb79f3b77fd514f84b0ac3cf8.png","desc":"\u6d88\u706d\u75c5\u6bd2\uff0c\u8eb2\u907f\u75c5\u6bd2\uff0c\u5347\u7ea7\u6b66\u5668\uff0c\u6d88\u706d\u75c5\u6bd2\uff01","gzh_num":"4","read_count":"1.2\u4e07","aldzs":"8273","grow":"68","status":0,"ranks_variety":-3,"category_ranks_variety":-1},{"id":"87927245","appkey":"a90bb1a04c0e4b1edd31922b5a6c4c9a","name":"\u548c\u5e73\u7cbe\u82f1","category":"\u6e38\u620f","logo":"http:\/\/aldpicsh-1252823355.cossh.myqcloud.com\/ad_advertiser\/1562207216.jpg","desc":"\u52c7\u8005\u540c\u884c\uff0c\u548c\u5e73\u7cbe\u82f1\uff01\u5feb\u9080\u8bf7\u597d\u53cb\u6765\u300a\u548c\u5e73\u7cbe\u82f1\u300b\u4e00\u8d77\u5f00\u9ed1\u5427\uff01","gzh_num":"6","read_count":"<0.1\u4e07","aldzs":"8270","grow":"17","status":0,"ranks_variety":-2,"category_ranks_variety":-1},{"id":"88689931","appkey":"afc1b90d68e30bc113ee1a06af909829","name":"\u6b22\u4e50\u6597\u5730\u4e3b","category":"\u6e38\u620f","logo":"http:\/\/aldpicsh-1252823355.cossh.myqcloud.com\/caijicons\/954ceeac7811c4864cadfc15b4af53b3.png","desc":"\u56fd\u6c11\u7ecf\u5178\u68cb\u724c\u6e38\u620f\u8f7b\u88c5\u8715\u53d8\uff0c\u514d\u4e0b\u8f7d\u9a6c\u4e0a\u73a9\uff01 \u5728\u7ebf\u5339\u914d\u4e0e\u4eba\u6597\u4e50\uff0c\u6b8b\u5c40\u95ef\u5173\u667a\u80dcAI\uff0c\u5355\u673a\u5bf9\u6218\u8f7b\u677e\u4f11\u95f2\uff0c\u603b\u6709\u4e00\u6b3e\u662f\u4f60\u6240\u7231~","gzh_num":"2","read_count":"7.8\u4e07","aldzs":"8206","grow":"49","status":0,"ranks_variety":5,"category_ranks_variety":4}]}
data = response["data"]

'''
data是一个list，list中每一项是一个字典，每一个字典是一个app，字典中每一项是app的一个参数。
'''
def write_to_excel(name):  
    # Create excel workbook and spreadsheet
    import xlwt
    wkb = xlwt.Workbook()
    ws = wkb.add_sheet('总榜')
    
    # 写入数据到excel
    for j in range(0,len(data)): # 控制行，j表示第j个应用
        appJdic = data[j]
        i = 0
        for key in appJdic.keys(): # 控制列，i表示第i中属性 
            ws.write(j, i, appJdic[key])
            i = i + 1
    
    for k in range(0, 13):
        ws.write(j+1, k, list(data[0].keys())[k])

    wkb.save(name +'.xls')
    
if __name__ == '__main__':
    write_to_excel("ald")
