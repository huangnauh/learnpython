//也可以使用闭包来实现就地排序
function mergeSort(a){
    var n = a.length;
    if(n <= 1){
        return;
    }
    var mid = Math.floor(n/2);
    function merge(left,right){
        var l = left.length;
        var r = right.length;
        var i=0,j=0,k=0;
        while(i<l && j<r){
            if(left[i] <= right[j]) {
                a[k++] = left[i++];
            }else{
                a[k++] = right[j++];
            }
        }
        while(i<l){
            a[k++] = left[i++];
        }
        while(j<r){
            a[k++] = right[j++];
        }
    }
    var left = a.slice(0,mid);
    var right = a.slice(mid,n);
    mergeSort(left);
    mergeSort(right);
    merge(left,right);
}