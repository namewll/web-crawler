CryptoJS=require("crypto-js")
function Md5(e){
    return CryptoJS.MD5(e).toString()
}
function l(t, e) {
    return t.toString().toUpperCase() > e.toString().toUpperCase() ? 1 : t.toString().toUpperCase() == e.toString().toUpperCase() ? 0 : -1
}
function s(e) {
    return Md5(e)
}
function u(t) {
    for (var e = Object.keys(t).sort(l), n = "", a = 0; a < e.length; a++)
        if (void 0 !== t[e[a]])
            if (t[e[a]] && t[e[a]]instanceof Object || t[e[a]]instanceof Array) {
                var i = JSON.stringify(t[e[a]]);
                n += e[a] + i
            } else
                n += e[a] + t[e[a]];
    return n
}
function d(t) {
    for (var e in t)
        "" !== t[e] && void 0 !== t[e] || delete t[e];
    var n = "B3978D054A72A7002063637CCDF6B2E5" + u(t);
    return s(n).toLocaleLowerCase()
}
e={
    "ts": 1770608498695,
    "pageNo": 1,
    "pageSize": 20,
    "total": 101,
    "KIND": "GCJS",
    "GGTYPE": "1",
    "timeType": "1",
    "BeginTime": "2026-02-09 00:00:00",
    "EndTime": "2026-02-09 11:41:38",
    "createTime": []
}
// console.log(d(e));


function b(t) {
    var e = CryptoJS.enc.Utf8.parse("EB444973714E4A40876CE66BE45D5930")
      , n = CryptoJS.enc.Utf8.parse("B5A8904209931867")
      , a = CryptoJS.AES.decrypt(t, e, {
        iv: n,
        mode: CryptoJS.mode.CBC,
        padding: CryptoJS.pad.Pkcs7
    });
    return a.toString(CryptoJS.enc.Utf8);
}
t="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"
console.log(b(t));







