function main(data1){
    cryptoJS=require("crypto-js")
    var paramPublicKey = "MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCvxXa98E1uWXnBzXkS2yHUfnBM6n3PCwLdfIox03T91joBvjtoDqiQ5x3tTOfpHs3LtiqMMEafls6b0YWtgB1dse1W5m+FpeusVkCOkQxB4SZDH6tuerIknnmB/Hsq5wgEkIvO5Pff9biig6AyoAkdWpSek/1/B7zYIepYY0lxKQIDAQAB";
    JSEncrypt=require("jsencrypt")
    var encrypt = new JSEncrypt;
    encrypt.setPublicKey(paramPublicKey);
    function getUuid() {
        var s = [];
        var hexDigits = "0123456789abcdef";
        for (var i = 0; i < 32; i++) {
            s[i] = hexDigits.substr(Math.floor(Math.random() * 16), 1)
        }
        s[14] = "4";
        s[19] = hexDigits.substr(s[19] & 3 | 8, 1);
        s[8] = s[13] = s[18] = s[23];
        var uuid = s.join("");
        return uuid
    }

    function dataTojson(data) {
        var arr = [];
        var res = {};
        arr = data.split("&");
        for (var i = 0; i < arr.length; i++) {
            if (arr[i].indexOf("=") != -1) {
                var str = arr[i].split("=");
                if (str.length == 2) {
                    res[str[0]] = str[1]
                } else {
                    res[str[0]] = ""
                }
            } else {
                res[arr[i]] = ""
            }
        }
        return res
    }
    function sort_ASCII(obj) {
        var arr = new Array;
        var num = 0;
        for (var i in obj) {
            arr[num] = i;
            num++
        }
        var sortArr = arr.sort();
        var sortObj = {};
        for (var i in sortArr) {
            sortObj[sortArr[i]] = obj[sortArr[i]]
        }
        return sortObj
    }
    function Md5(text){
        return cryptoJS.MD5(text).toString()
    }
    var b64map = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/";
    var b64pad = "=";
    function hex2b64(h) {
        var i;
        var c;
        var ret = "";
        for (i = 0; i + 3 <= h.length; i += 3) {
            c = parseInt(h.substring(i, i + 3), 16);
            ret += b64map.charAt(c >> 6) + b64map.charAt(c & 63)
        }
        if (i + 1 == h.length) {
            c = parseInt(h.substring(i, i + 1), 16);
            ret += b64map.charAt(c << 2)
        } else if (i + 2 == h.length) {
            c = parseInt(h.substring(i, i + 2), 16);
            ret += b64map.charAt(c >> 2) + b64map.charAt((c & 3) << 4)
        }
        while ((ret.length & 3) > 0) {
            ret += b64pad
        }
        return ret
    }
    encrypt.encryptLong = function(text) {
        var _this = this.getKey();
        var maxLength = (this.getKey().n.bitLength() + 7 >> 3) - 11;
        try {
            var ct_1 = "";
            if (text.length > maxLength) {
                var lt = text.match(/.{1,117}/g);
                lt.forEach(function(entry) {
                    var t1 = _this.encrypt(entry);
                    ct_1 += t1
                });
                return hex2b64(ct_1)
            }
            var t = this.getKey().encrypt(text);
            var y = hex2b64(t);
            return y
        } catch (ex) {
            console.log(ex);
            return false
        }
    }

    timestamp = Date.parse(new Date)
    requestId=getUuid()
    data_param=JSON.stringify(sort_ASCII(dataTojson(data1 || "{}")))
    sign=Md5(data_param + requestId + timestamp)
    data=encrypt.encryptLong(data_param)


    return [requestId,sign,timestamp,data];
}
