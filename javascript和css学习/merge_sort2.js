//为了使数组原地排序，构造splice方法的参数，对数组进行先删后增。
function merge(left,right){
    var result = [],
        l = left.length,
        r = right.length,
        il = 0,
        ir = 0;
    while(il < l && ir < r){
        if(left[il] <= right[ir]){
            result.push(left[il++]);
        }else{
            result.push(right[ir++]);
        }
    }
    return result.concat(left.slice(il)).concat(right.slice(ir));
}

function mergeSort(a){
    var n = a.length;
    if(n < 2){
        return a;
    }
    var mid = Math.floor(n/2),
        left = a.slice(0,mid),
        right = a.slice(mid);
    var params = merge(mergeSort(left),mergeSort(right));
    params.unshift(0,n);
    a.splice.apply(a,params)
    return a;
}